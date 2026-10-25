---
name: focus
description: >
  Simulated focus group in one pass. Ten everyday users and ten decision-makers
  (investors and funders, gatekeepers, operators, strategists, one domain expert)
  each react to the product described in the current conversation in their own
  voice, then one joint synthesis: scoreboard, consensus, deal-breakers, a ranked
  list of changes and the conflicts between the market and the money. Worldwide
  market by default; other markets are plug-in files. Use when the user types
  /focus, asks for a focus group, a panel or persona review, "what would users
  or investors say about this", or wants to pressure-test a concept, pitch,
  landing page, pricing or positioning. `/focus lite` is a 3 + 3 quick check.
argument-hint: "[lite] [market]"
---

# Focus: the street and the boardroom in one room

You run a focus group of twenty fictional people inside a single response. Ten
are ordinary people who might meet the product in their real lives (Panel A).
Ten are people who can fund it, distribute it or kill it with one decision
(Panel B). Each of them reacts in their own voice. Then you step out of the room
and write one synthesis that counts, names and ranks.

This skill does not visit the product. It works from what the conversation
says the product is. When there is a live build and you want each persona to be
a separate agent that actually opens it, use **focus-swarm** instead.

## 0. Read the room before you cast it

Read the whole conversation and infer, without asking: the product, its
audience, business model, domain, stage, geography and price or access model.
Ask a question only when the product itself is unclear (for example the
conversation names two different products). For anything else, make the
assumption, state it in one line at the top, and go.

If there is no product at all in the conversation, say so in one sentence and
ask for a description, a link or a pitch. Do not invent one.

## 1. Arguments

| Argument | Effect |
|---|---|
| *(none)* | 10 + 10 personas, full synthesis, `world` market |
| `lite` | 3 + 3 personas, short reviews, synthesis = top 5 changes only |
| `<market>` | load `references/markets/<market>.md` instead of `world.md` |

Arguments combine in any order: `/focus lite`, `/focus lite world`.

## 2. Market

The market decides where the personas live, what they pay with, which
institutions and platforms sit on Panel B, which rules apply and which
competitors count as the benchmark.

1. An explicit market argument wins. Load `references/markets/<market>.md`.
   If no such file exists, say so in one line and fall back to `world`.
2. Otherwise use `references/markets/world.md`.
3. Each market file has a **Detect** section. If the conversation clearly
   matches another installed market file (for example a product sold only in
   one country), mention that market in the first line as an option, but run
   `world` unless the user asked for it.

New markets are added by dropping a file into `references/markets/` that
follows `references/markets/TEMPLATE.md`. Nothing else needs to change.

## 3. Panel A: the 99% (10 everyday people)

Specific named humans with messy lives, not archetypes.

- Age across the realistic range, roughly balanced gender, education from
  school dropout to PhD, income from student to comfortable, urban and rural,
  locals and migrants, as set by the market file.
- Tech literacy from "asks a nephew to install apps" to "builds side projects".
- Relationship to the product: first-timer, returning, reluctant (dragged in by
  a partner or a boss), accidental, switched from a competitor.
- At least one skeptic of the whole category and one wildcard from outside the
  target audience.

Persona header: `### A1. Name, age, job or situation, city`, then
**Background** (2 to 3 sentences that shape the reaction) and **Why they
matter** (1 sentence).

Review, in their own voice and register:
- **First 10 seconds:** what they see, feel and do.
- **Works for them:** 2 bullets.
- **Doesn't work:** 2 bullets, each with the consequence in their life.
- **Wish:** 1 bullet.
- **Would they use, buy, attend or recommend it?** YES / NO / MAYBE, plus
  what would flip a MAYBE.

## 4. Panel B: the 1% (10 decision-makers)

People who can write the cheque, open the door or close it with one call. They
have seen hundreds of pitches and they pattern-match fast.

- **The Money (2 to 3):** investors or funders that fit the domain and stage.
- **The Gatekeepers (2):** whoever decides whether it reaches an audience:
  editors, platform and store teams, festival or conference programmers,
  analysts, buyers.
- **The Operators (2 to 3):** CMO, CTO or CPO, COO, General Counsel of a
  comparable company.
- **The Strategic Minds (1 to 2):** consultancy partner, head of strategy,
  sector banker, board member.
- **The Domain Expert (1):** someone who has already done exactly this at the
  top of the category.
- **At least 3 of the 10 are skeptical or hostile.** An all-friendly boardroom
  is a casting error.

Persona header: `### B1. Name, age, title, organisation`, then
**Background**, **Their question** (the one question they ask after a
30-second look) and **Disposition** (interested, neutral, skeptical, hostile).

Review, corporate and dense:
- **30-second scan:** where their eyes go first.
- **Gets their attention:** 2 bullets.
- **Concerns:** 2 bullets, framed as a risk or as a pattern they have seen fail.
- **Needs to see to say yes:** concrete and measurable.
- **Verdict:** FUND / CONDITIONAL / PASS, with the exact conditions.
  ("Fund" means back it with whatever this person controls: money, a
  slot, a listing, a contract.)

## 5. Joint synthesis

1. **Scoreboard:** Panel A YES / MAYBE / NO counts, Panel B FUND /
   CONDITIONAL / PASS counts, one paragraph on the temperature of the room.
2. **Consensus:** what 3 or more people agree on, positive and negative, with
   names from both panels.
3. **Deal-breakers:** what would make more than half of either panel walk out.
4. **High-impact changes, ranked 1 to 8:** each with
   "Fixes it for: A3 (reason), B7 (reason), ...", **Effort** (low / medium /
   high) and **Impact**. Rank by doors unlocked across both panels, not by how
   happy it makes people who were already friendly.
5. **Where the money disagrees with the market:** conflicts between Panel B
   and Panel A, said plainly, with the side you would follow and why.
6. **Fault lines:** where age, gender, region, income or background split
   Panel A.
7. **Wildcard insight** (from the Panel A outsider) and **Power move** (one
   non-obvious positioning shift for Panel B; not a feature).
8. **Blind spots:** 1 to 3 patterns nobody named that only show when all
   twenty reviews are read together.
9. **Market note:** one or two lines on what would change in another market,
   only when the product plausibly crosses that line.

## 6. Rules that hold everywhere

- **Fictional people, real context.** Every persona is invented. Panel B
  personas may sit at a real, public organisation type or a named public
  organisation from the market file, but they are fictional composites, never a
  real employee, and nothing they say is attributed to a real person. Start the
  output with the line: *All personas are fictional. Their reactions are a
  simulation, not research data.*
- **No invented facts.** Never invent statistics, market sizes, prices of
  competitors, grant amounts, deadlines or quotes. Name a real institution,
  fund or platform only when it genuinely fits the domain; otherwise describe
  the role ("a seed fund that backs consumer subscription apps").
- **No comfort.** If 7 of 10 would bounce, say 7 and name them. The ranked list
  is worthless if the reviews were softened first.
- **Voices stay distinct.** A 19-year-old courier, a procurement lead and a
  retired teacher do not sound alike. Flattening them into one polite reviewer
  is the failure mode this skill exists to avoid.
- **Contradictions survive.** Do not average a real split into a mild middle.
  Name both sides.
- **Language:** write in the language set by the market file (English for
  `world`). Personas may drop words of their own language where natural.

## 7. Output shape

```
Market: world (reason in a few words). Size: 10 + 10. Assumptions: ...
All personas are fictional. Their reactions are a simulation, not research data.

## Panel A: the 99%
### A1. ...
...
## Panel B: the 1%
### B1. ...
...
## Synthesis
### 1. Scoreboard
...
```

In `lite` mode keep the same headings with A1 to A3 and B1 to B3, and replace
the synthesis with the scoreboard plus the top 5 changes.
