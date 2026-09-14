---
type: hub.skill
name: drafting-outreach
description: "Write an opener, sequence, or any message to a prospect for Merraine. Use whenever copy is being drafted, reviewed, or approved. Triggers: draft an email, write an opener, sequence, outreach copy, congratulations note, follow-up."
triggers: [draft, opener, outreach, copy, email, sequence, message]
readWhen: "Before writing any text intended for a human outside Merraine"
doNotUseFor: ["Sending", "Internal notes", "Anything addressed to Jeremy Sanchez himself"]
---

# Drafting outreach

1. Ground it. Every opener quotes a cited `gtm.observation` in its first sentence.
   No observation, no draft.
2. Match the man, not a persona. Use the voice profile from
   [[email-communications-extraction]] once it exists. Until then use the voice
   fields in [[merraine-icp]].
3. Cap it. 80 words for a signal opener, 60 for a congratulations note.
4. One question. One CTA.
5. Close with permission to pass — "no pressure if it's not for you." Reported to
   move compliance from 10% to 47% across 42 studies.
6. Run [[slop-patterns]]. Two trips means rewrite.
7. `sendReady: no`. Always. It flips only when a human types the confirm word.

Never write to Jeremy Sanchez. Outbound to him is Jeremy Alston's, and his reply
draft is already sitting unsent in Outlook.
