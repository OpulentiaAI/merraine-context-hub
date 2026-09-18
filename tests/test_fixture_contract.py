"""Fixture-driven tests.

Worker A's fixtures declare, in their own frontmatter, the error each bad case
must produce:

    expectError: "<substring of the validator error>"

These tests honour that contract. Every `fixtures/bad/*.md` is dropped into a
scanned directory of a temp hub — alongside the good fixtures so its wikilinks
resolve — and the validator must produce the named error. A bad fixture that
passes validation is a fixture that is not testing anything.

Good fixtures get the mirror treatment: each must validate cleanly.
"""
from __future__ import annotations

import pathlib
import shutil
import tempfile
import unittest

from tests.support import REPO, VALIDATE

GOOD_DIR = REPO / "fixtures" / "good"
BAD_DIR = REPO / "fixtures" / "bad"
EXPECT_ERROR = "expectError:"


def bad_cases() -> list[pathlib.Path]:
    if not BAD_DIR.is_dir():
        return []
    return sorted(BAD_DIR.glob("*.md"))


def good_cases() -> list[pathlib.Path]:
    if not GOOD_DIR.is_dir():
        return []
    return sorted(GOOD_DIR.glob("*.md"))


class FixtureContract(unittest.TestCase):
    """Consume worker A's fixture contract directly, rather than restating it."""

    def build_hub(self) -> pathlib.Path:
        root = pathlib.Path(tempfile.mkdtemp(prefix="hub-fixtures-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        # The real type declarations: these fixtures must be checked against the
        # actual ontology, not a copy that can drift.
        shutil.copytree(REPO / "type", root / "type")
        for d in ("signals", "research", "entities"):
            (root / d).mkdir(parents=True, exist_ok=True)
        # Good fixtures live in a scanned directory so bad-case wikilinks resolve.
        shutil.copytree(GOOD_DIR, root / "fixtures" / "good")
        return root

    @unittest.skipIf(not good_cases(), "no good fixtures yet")
    def test_good_fixtures_validate_cleanly(self):
        root = self.build_hub()
        result = VALIDATE.run_checks(hub=root)
        rel_errors = [e for e in result.errors if "fixtures/good" in e]
        self.assertEqual(rel_errors, [], f"good fixtures must be clean; got {rel_errors}")

    @unittest.skipIf(not bad_cases(), "no bad fixtures yet")
    def test_every_bad_fixture_declares_an_expectation(self):
        for path in bad_cases():
            text = path.read_text(encoding="utf-8")
            self.assertIn(
                EXPECT_ERROR, text,
                f"{path.name} is in fixtures/bad but declares no expectError",
            )

    @unittest.skipIf(not bad_cases(), "no bad fixtures yet")
    def test_bad_fixtures_produce_their_expected_error(self):
        failures = []
        for path in bad_cases():
            text = path.read_text(encoding="utf-8")
            expected = ""
            for line in text.splitlines():
                if line.startswith(EXPECT_ERROR):
                    expected = line.split(":", 1)[1].strip().strip('"').strip("'")
                    break
            if not expected:
                continue
            root = self.build_hub()
            shutil.copy(path, root / "signals" / path.name)
            result = VALIDATE.run_checks(hub=root)
            if not any(expected in e for e in result.errors):
                failures.append(f"{path.name}: expected an error containing {expected!r}; got {result.errors}")
        self.assertEqual(failures, [], "\n".join(failures))


class CoverageGuardrail(unittest.TestCase):
    """The completeness rule must stay loud even without a manifest.

    A Jev evaluation of this design put its adoptability at 0.77 and its
    ability to prevent a silently deleted manifest at 0.70, so the warning is
    test-enforced rather than left to a reviewer to notice.
    """

    def test_repo_warns_when_connected_sources_lack_a_manifest(self):
        result = VALIDATE.run_checks(hub=REPO)
        connectors = list((REPO / "entities" / "connectors").glob("*.md"))
        connected = [
            p for p in connectors
            if VALIDATE.scalar(VALIDATE.parse_frontmatter(p.read_text(encoding="utf-8")).get("connected", "")) == "yes"
        ]
        manifests = list((REPO / "entities").glob("*source-manifest*.md"))
        if connected and not manifests:
            self.assertTrue(
                any("no source-manifest" in w for w in result.warnings),
                "connected sources exist with no manifest — the coverage warning must fire",
            )

    def test_repo_build_is_clean(self):
        result = VALIDATE.run_checks(hub=REPO)
        self.assertEqual(result.errors, [], f"repository must validate clean; got {result.errors}")


class Baseline(unittest.TestCase):
    """The regression floor: the checks pass on the real tree."""

    def test_expected_types_present(self):
        types = VALIDATE.load_types(REPO)
        for name in ("gtm.source-manifest", "gtm.extraction-run", "gtm.experiment",
                     "gtm.warm-path", "gtm.search-run", "gtm.award"):
            self.assertIn(name, types, f"{name} must be declared")

    def test_manifest_type_separates_authorization_from_reach(self):
        body = (REPO / "type" / "gtm.source-manifest.type.yaml").read_text(encoding="utf-8")
        self.assertIn("authorization:", body)
        self.assertIn("reach:", body)
        self.assertIn("past-use", body,
                      "registry state is not permission; past use must be representable")
        self.assertIn("datasetOwner:", body,
                      "different people's datasets must stay separable")


if __name__ == "__main__":
    unittest.main()
