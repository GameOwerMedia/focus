# Market: <code>

Copy this file to `references/markets/<code>.md` (lower case, for example
`de.md`, `us.md`, `jp.md`) and fill every section. The skill loads it when the
user runs `/focus <code>`. Keep the seven section headings exactly as they are;
the test suite checks for them.

Write in English even when the output language is not English: the file is an
instruction to the model, and the **Language and style** section tells it what
to write in.

## Detect

The signals that a conversation belongs to this market: language of the
product or copy, top-level domain, currency, cities or venues, local funders,
partners or clients named in the conversation. Also say when *not* to pick it
(for example a local team building for a global audience).

## Language and style

- Output language and register (formal or informal address, if the language has
  both).
- Currency and how prices are written.
- Punctuation or style rules that make the output read as native.

## Panel A

- How to spread the ten everyday people geographically: big cities, mid-size
  towns, rural areas, regions that differ in income or culture.
- Who must be in the room: at least one person from a small town or the
  countryside, at least one migrant or foreigner living in the country.
- Everyday context to draw on: payment habits, delivery and marketplaces,
  social platforms, commuting, housing, family obligations.

## Panel B

Public organisations that can fill each seat, grouped as in `SKILL.md`. These
are illustrative examples; personas stay fictional.

- **The Money:** local VC firms and angel networks, public development banks
  and innovation agencies, grant programmes, culture and film funds, corporate
  sponsors.
- **The Gatekeepers:** national media, trade press, platforms and retailers,
  festivals and venues, influential communities.
- **The Operators, Strategic Minds and Domain Expert:** comparable local
  companies, local offices of consultancies and law firms, sector bankers.

## Rules and regulators

Data protection authority, consumer protection, competition, broadcasting,
collecting societies, tax and social security reality, public procurement,
sector regulators. Only the ones a product in this market is likely to meet.

## Benchmarks

Which competitors count first: local ones, then the global products people in
this market already use.

## Labels

- Panel A verdicts in the output language (equivalents of YES / NO / MAYBE).
- Panel B verdicts in the output language (equivalents of FUND / CONDITIONAL /
  PASS).
- Translated section headings, if the output language is not English.
