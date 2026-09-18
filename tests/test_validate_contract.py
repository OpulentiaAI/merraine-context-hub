"""Contract tests for the graph checks.

Two halves:
  - negative tests: a deliberately broken hub MUST produce the named error
  - positive tests: a correct hub MUST stay clean

The negative half is the point. A validator nobody has watched fail is a
validator nobody should trust.
"""
from __future__ import annotations

import unittest

from tests.support import HubCase


class FrontmatterRules(HubCase):
    def test_missing_frontmatter_is_an_error(self):
        self.declare_type("gtm.thing")
        self.write("signals/bare.md", "# no frontmatter at all\n")
        self.assert_error_contains("no frontmatter")

    def test_unknown_type_is_an_error(self):
        self.instance("signals/mystery.md", "gtm.does_not_exist")
        self.assert_error_contains("unknown type")

    def test_frontmatter_without_type_is_an_error(self):
        self.write("signals/typeless.md", "---\ntldr: x\n---\n\n# Body\n")
        self.assert_error_contains("frontmatter has no `type`")

    def test_missing_tldr_is_an_error(self):
        self.declare_type("gtm.thing")
        self.write("signals/notldr.md", (
            "---\ntype: gtm.thing\nstatus: active\nowner: x\nupdated: 2026-09-18\n"
            "surface: jeremy\nprovenance: p\n---\n\n# Body\n"
        ))
        self.assert_error_contains("no tldr")

    def test_a_clean_instance_passes(self):
        self.declare_type("gtm.thing")
        self.instance("signals/good.md", "gtm.thing")
        self.assertEqual(self.errors(), [])


class LinkRules(HubCase):
    def test_dangling_wikilink_is_an_error(self):
        self.declare_type("gtm.thing")
        self.instance("signals/linky.md", "gtm.thing", body="\n# Body\n\nSee [[nowhere]].\n")
        self.assert_error_contains("dangling link [[nowhere]]")

    def test_resolvable_wikilink_is_fine(self):
        self.declare_type("gtm.thing")
        self.instance("signals/target.md", "gtm.thing")
        self.instance("signals/source.md", "gtm.thing", body="\n# Body\n\nSee [[target]].\n")
        self.assertEqual(self.errors(), [])


class SendSafetyRules(HubCase):
    def test_send_ready_yes_is_an_error(self):
        self.declare_type("gtm.message")
        self.instance("signals/draft.md", "gtm.message", extra="sendReady: yes\n")
        self.assert_error_contains("sendReady is yes")

    def test_send_ready_no_is_clean(self):
        self.declare_type("gtm.message")
        self.instance("signals/draft.md", "gtm.message", extra="sendReady: no\n")
        self.assertEqual(self.errors(), [])


class AutomationRules(HubCase):
    def prompt(self, extra: str = "enabled: no\nfirstOpenChecked: no\ncostCeilingUsd: 1\n",
               caution: bool = True) -> str:
        tail = "CAUTION: never send.\n" if caution else "do the thing.\n"
        return (
            "---\n"
            "type: gtm.automation\n"
            "tldr: t\nstatus: active\nowner: x\nupdated: 2026-09-18\n"
            "surface: jeremy\nprovenance: p\n"
            "slug: t\n"
            f"{extra}"
            "---\n\n# Overview\n\n# Prompt\n\n```text\n"
            f"{tail}"
            "```\n\n# Forbidden Actions\n"
        )

    def setUp(self):
        super().setUp()
        self.declare_type("gtm.automation")

    def test_enabled_without_first_open_is_an_error(self):
        self.write("automations/a.md", self.prompt("enabled: yes\nfirstOpenChecked: no\ncostCeilingUsd: 1\n"))
        self.assert_error_contains("enabled without a checked first open")

    def test_enabled_with_first_open_checked_is_allowed(self):
        self.write("automations/a.md", self.prompt("enabled: yes\nfirstOpenChecked: yes\ncostCeilingUsd: 1\n"))
        self.assert_no_error_containing("enabled without a checked first open")

    def test_prompt_without_caution_is_an_error(self):
        self.write("automations/a.md", self.prompt(caution=False))
        self.assert_error_contains("no CAUTION line")

    def test_missing_prompt_block_is_an_error(self):
        self.write("automations/a.md", (
            "---\ntype: gtm.automation\ntldr: t\nstatus: active\nowner: x\n"
            "updated: 2026-09-18\nsurface: jeremy\nprovenance: p\nslug: t\n"
            "enabled: no\nfirstOpenChecked: no\ncostCeilingUsd: 1\n---\n\n# Overview\n"
        ))
        self.assert_error_contains("no fenced Prompt block")

    def test_negative_cost_ceiling_is_an_error(self):
        self.write("automations/a.md", self.prompt("enabled: no\nfirstOpenChecked: no\ncostCeilingUsd: -1\n"))
        self.assert_error_contains("costCeilingUsd must be a non-negative number")

    def test_missing_cost_ceiling_warns(self):
        self.write("automations/a.md", self.prompt("enabled: no\nfirstOpenChecked: no\n"))
        self.assertTrue(any("no costCeilingUsd" in w for w in self.warnings()))


class SurfaceRules(HubCase):
    def test_operator_marker_on_product_surface_is_an_error(self):
        self.declare_type("gtm.thing")
        self.instance("signals/leak.md", "gtm.thing", extra="surface: operator\n")
        self.assert_error_contains("operator file must live under ops/")

    def test_forbidden_phrase_on_product_surface_is_an_error(self):
        self.declare_type("gtm.thing")
        self.instance("signals/leak.md", "gtm.thing", body="\n# Body\n\nCONVEX_DEPLOY here.\n")
        self.assert_error_contains("product surface contains")


class CoverageRules(HubCase):
    """One extraction is not coverage — the guardrail is enforced, not just documented."""

    def test_connected_source_without_manifest_row_is_an_error(self):
        self.declare_type("gtm.source-manifest", parents="thing::au-base-types",
                          fields="  sourceId: String\n  state: String\n"
                                 "  doesNotCover: String[+]\n  lastObservedAt: Date\n  blockerNote: String")
        self.connector("spear")
        self.write("entities/source-manifest.md", (
            "---\ntype: gtm.source-manifest\ntldr: t\nstatus: active\nowner: x\n"
            "updated: 2026-09-18\nsurface: jeremy\nprovenance: p\n---\n\n"
            "# Manifest\n\nsources:\n"
            "  - sourceId: notion\n"
            "    state: pending\n"
            "    doesNotCover: mailbox\n"
        ))
        self.assert_error_contains("has no source-manifest row")

    def test_connected_sources_without_any_manifest_warn_once(self):
        self.connector("spear")
        self.connector("notion")
        warns = [w for w in self.warnings() if "no source-manifest" in w]
        self.assertEqual(len(warns), 1, f"expected exactly one coverage warning, got {warns}")

    def test_manifest_row_missing_does_not_cover_is_an_error(self):
        self.connector("spear")
        self.write("entities/source-manifest.md", (
            "---\ntype: gtm.source-manifest\ntldr: t\nstatus: active\nowner: x\n"
            "updated: 2026-09-18\nsurface: jeremy\nprovenance: p\n---\n\n"
            "sources:\n  - sourceId: spear\n    state: pending\n"
        ))
        self.assert_error_contains("doesNotCover is required")

    def test_extracted_row_requires_last_observed_at(self):
        self.connector("spear")
        self.write("entities/source-manifest.md", (
            "---\ntype: gtm.source-manifest\ntldr: t\nstatus: active\nowner: x\n"
            "updated: 2026-09-18\nsurface: jeremy\nprovenance: p\n---\n\n"
            "sources:\n  - sourceId: spear\n    state: extracted\n    doesNotCover: mailbox\n"
        ))
        self.assert_error_contains("extracted` requires lastObservedAt")

    def test_unavailable_row_requires_a_blocker_note(self):
        self.connector("gmail")
        self.write("entities/source-manifest.md", (
            "---\ntype: gtm.source-manifest\ntldr: t\nstatus: active\nowner: x\n"
            "updated: 2026-09-18\nsurface: jeremy\nprovenance: p\n---\n\n"
            "sources:\n  - sourceId: gmail\n    state: unavailable\n    doesNotCover: mail\n"
        ))
        self.assert_error_contains("requires a blockerNote")


class ExtractionRunRules(HubCase):
    """Exercised against the real gtm.extraction-run declaration."""

    def run_doc(self, extra: str) -> None:
        base = ("sourceId: s\nscope: full\nobservedAt: 2026-09-18\nproduced: [rows]\n"
                "recordCount: 1\nfileCount: 1\ncompleteness: COMPLETE\ntruncated: no\n"
                "outcome: ok\nprivacy: private\n")
        self.instance("extractions/r.md", "gtm.extraction-run", extra=base + extra)

    def test_partial_without_gap_or_blocker_is_an_error(self):
        self.run_doc("outcome: partial\n")
        self.assert_error_contains("requires `missing` or `blockerNote`")

    def test_partial_with_missing_is_clean(self):
        self.run_doc("outcome: partial\nmissing: [dms]\n")
        self.assert_no_error_containing("requires `missing`")

    def test_artifact_ref_without_hash_is_an_error(self):
        self.run_doc("artifactRef: a.zip\n")
        self.assert_error_contains("artifactRef without artifactSha256")

    def test_delta_without_continuing_from_is_an_error(self):
        self.run_doc("scope: delta\n")
        self.assert_error_contains("delta run requires continuingFrom")

    def test_ok_run_is_clean(self):
        self.run_doc("artifactRef: a.zip\nartifactSha256: deadbeef\n")
        self.assertEqual(self.errors(), [])

    def test_truncated_read_is_representable(self):
        self.run_doc("truncated: yes\nerrors: [large-output truncation lost rows]\n")
        self.assertEqual(self.errors(), [])


class ExperimentRules(HubCase):
    """Exercised against the real gtm.experiment declaration."""

    BASE = ("unit: replies\nhypothesis: h\nmeasure: rate\nthreshold: 3\ndirection: at_least\n"
            "preconditions: [approval]\n")

    def experiment(self, extra: str) -> None:
        self.instance("research/e.md", "gtm.experiment", extra=self.BASE + extra)

    def test_supported_without_value_is_an_error(self):
        self.experiment("state: supported\n")
        self.assert_error_contains("requires observedValue and sampleSize")

    def test_insufficient_must_not_carry_a_value(self):
        self.experiment("state: insufficient\nobservedValue: 0\n")
        self.assert_error_contains("must not carry an observedValue")

    def test_supported_with_value_and_sample_is_clean(self):
        self.experiment("state: supported\nobservedValue: 3\nsampleSize: 20\n")
        self.assertEqual(self.errors(), [])

    def test_insufficient_alone_is_clean(self):
        self.experiment("state: insufficient\n")
        self.assertEqual(self.errors(), [])

    def test_run_experiment_carries_no_promotion(self):
        # Promotion is a human decision. An automation must never set it.
        self.experiment("state: running\n")
        self.assert_no_error_containing("promotedBy")


if __name__ == "__main__":
    unittest.main()
