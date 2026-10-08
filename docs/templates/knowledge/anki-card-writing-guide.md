# Anki Card-Writing Guide

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** how to write flashcards that actually stick, how to tag them so they line up with the training modules, how to run the 15-minute daily routine, and how to keep company-specific cards in a separate deck that never leaves company systems.
- **Who uses it:** Hire A and Hire B, every day. The Senior or the Manager spot-checks 10 cards at each milestone and expects zero factual errors. Anyone who edits the team deck's source files (`data/anki/*.csv`, maintained by the Manager) follows it too.
- **When:** from Day 1 (Mon 10/19: import BSA-Onboarding.apkg from the onboarding folder, first reviews). First 5 own cards on Wed 10/21; at least 15 by the end of W2. Targets for the cards you write (company-specific plus your own generic cards; the team deck does not count): 20 by day 30, 50 by day 60, 80 by day 90 (`docs/01-30-60-90-plan.md`). Write 2 or more cards after every Senior session, shadowing session and teach-back.

## Two decks, two purposes

| Deck | What is in it | Where it comes from | May it leave company systems? |
|---|---|---|---|
| Team deck: "BSA Onboarding" (3 sub-decks) | Industry and regulatory knowledge, BSA craft and data skills. Nothing company-specific | BSA-Onboarding.apkg in the onboarding folder, built by the Manager. You study it; you do not edit it | Yes: it contains no company data. But Anki syncs whole profiles, so the sync rules below still apply |
| Your own deck, for example "BSA Company Internal" | Every card you write: company systems, tables, tools, process steps, roles and rules of thumb (tag `company`), plus your own cards on general topics such as regulations, craft and data (tag `own`) | Written by you as you learn; company cards shared through [COMPANY: SharePoint or OneNote location] | No, unless [COMPANY: policy confirms] |

If a card names a company system object, tool, report, team, person, threshold, customer, supplier or item, it is company-specific: tag it `company`.

**Which cards count.** The targets above, the W2 check (15 cards) and the milestone spot checks count only the cards you write: `company` plus `own`. Cards in the team deck do not count, because you did not write them. Keep all your own cards in your own deck, never inside the team deck, so that importing a new team-deck version never touches them. In the Friday self-report, write "cards: N company, M own".

## Principles

1. **Atomic: one fact per card.** If the back has "and" joining two facts, make two cards.
2. **Question on the front.** A real question you could be asked at work, with enough context to have one right answer. Put the country first when rules differ: "US: ...", "CA: ...", "MX: ...".
3. **Short back: 40 words or fewer.** The answer first, then at most one line of why or source.
4. **Basic or cloze?** Use basic (front and back) for "why", "who", "where to find" and definitions. Use cloze (fill in the blank) for a fixed phrase, a short sequence or one term inside a sentence. Never cloze more than one idea per card number.
5. **Avoid volatile facts.** Tariff rates, fee amounts, thresholds, the current status of an action and system names change. Prefer a card on where to find the current value. If you must keep a fact that can change, tag the card `dated`, cite the source, and end the back with the month you checked it, for example "(as of Oct 2026)". The team deck uses the same convention. Update or delete the card when the fact changes.
6. **Cite a source** in the Source field: primer section, regulation, SOP ID, brief ID, OneNote page. A card you cannot source is a question for the question log, not a card.
7. **Your own words,** not copied paragraphs. Writing the card is half the learning.
8. **No lists longer than 3.** Break them up or use cloze, one card per item. Exception: the team deck keeps a few fixed lists from a legal text or standard (for example the nine USMCA certification data elements or the five ECCN product groups) as numbered lists; every card you write follows rule 8.
9. **No yes or no questions.** Ask for the thing itself.
10. **Fix or suspend bad cards.** A card you keep failing is badly written more often than it is hard. Rewrite it.

## Good and bad examples from our domain

| Bad card | Problem | Better card |
|---|---|---|
| Front: "USMCA" / Back: a paragraph on the agreement | Not a question; many facts; too long | Front: "USMCA: what are the two main kinds of requirement a product-specific rule of origin can set?" / Back: "A tariff classification change (tariff shift) and a regional value content (RVC) percentage, alone or combined." |
| Front: "What is the Section 301 rate on our items?" / Back: "25%" | Volatile, company-specific, no date or source | Team deck: "US: where do you confirm the additional duty on an HTS number today?" / "The HTSUS Chapter 99 heading and its notes, the latest Federal Register notice and CBP CSMS guidance; record the date checked." |
| Front: "True or false: the PO date decides the US duty rate." | Yes or no question | Front: "US: which date decides the duty rate on an import?" / Back: "The entry date, or the date of withdrawal from warehouse for consumption; not the PO, ship or receipt date, unless the action says otherwise (19 CFR 141.69)." |
| Front: "Protest?" / Back: "180 days" | No context; the answer has no meaning on its own | Front: "US: how long does an importer have to protest a CBP liquidation decision?" / Back: "180 days from the date of liquidation (19 U.S.C. 1514)." |
| Front: "List all landed-cost components." | A long list on one card | Cloze: "Landed cost = purchase price + {{c1::international freight and insurance}} + {{c2::duty}} + {{c3::customs fees and brokerage}} + inland freight." |
| Front: "Explain IMMEX, Anexo 24 and Anexo 30." | Three topics on one card | Front: "Mexico IMMEX: what is Anexo 24?" / Back: "The automated inventory control system that tracks temporarily imported goods until they are exported or change customs regime." |
| Front: "Who owns tariffs?" | Vague; several right answers | Front: "Tariff action: who owns the $ impact on item cost, Research or Standard Cost?" / Back: "Standard Cost. Research owns the WHAT (scope, HTS, origins, rates, dates, sources) in the Tariff-Impact Brief." |
| Front: "SQL HTS" / Back: "text" | Cryptic both ways | Front: "Why compare HTS codes as text, not numbers?" / Back: "Numbers drop leading zeros, so chapter 01 to 09 codes stop matching (0303... becomes 303...)." |

Company-deck examples (fill in on company systems only):

- Front: "Which table holds our item classification master?" / Back: "[COMPANY: table]. Key: item number + import country." / Source: "[COMPANY: OneNote page]".
- Front: "Standard Cost: who approves a cost update before it loads to Oracle?" / Back: "[COMPANY: Finance approver role], after the checker's sign-off." / Source: "SOP-STC-01 step [n]".
- Front: "How often does [COMPANY: tool name] run, and who receives its output?" / Back: "[Schedule]; [recipient]. (as of [Mon YYYY])" / Source: "Tool doc T-[nn]" / Tags: `M6::Tools company dated`.

## Tag convention

Tags let both hires and the trainers filter cards by module. The team deck uses the same convention.

- **First tag: the module ID, then the topic, joined by two colons.** Examples: `M1::USMCA`, `M1::Classification::GRI`, `M1::Valuation`, `M2::e2open`, `M3::SQL`, `M4::UAT`, `M5R::Sources`, `M5C::PPV`, `M6::Tools`, `M7::Exports`, `M9::Drawback`. Module IDs are the ones in `docs/01-30-60-90-plan.md` (M0 to M10).
- Anki shows tags with `::` as a tree in the Browse window, so you can click `M1` to see every M1 card.
- **Extra tags:** a country (`US`, `CA`, `MX`) where useful; `dated` on any card whose fact can change (its back ends "(as of Mon YYYY)"; review these monthly); and on every card you write, either `company` (company-specific) or `own` (your own generic card).
- Tags are separated by spaces, so a tag never contains a space. Use a hyphen inside a topic: `M5C::Landed-cost`.
- Keep topic names short and reuse existing ones. Check the tag tree before you invent a new topic.

## Daily routine (15 minutes)

| When | What | Time |
|---|---|---|
| Every morning, first thing | Review all due cards in both decks. Reviews before new cards | 15 min |
| During the day | Note card candidates in OneNote as you learn (last 5 minutes of each study block) | 1 to 2 min each |
| 16:45 daily wrap | Turn the day's card candidates and answered questions into cards | Inside the wrap |
| Friday, 10 minutes | Search `tag:leech` and `tag:dated`; rewrite or retire those cards; count the cards you wrote (`tag:company`, `tag:own`) for the Friday self-report | 10 min |

Settings that keep it at 15 minutes: in the deck options for the team deck, set new cards per day to about 10. If reviews take more than 20 minutes for 3 days in a row, cut new cards to 5 until it settles. Anki tags a card `leech` after 8 lapses by default and, if the deck's leech action is set to suspend, also suspends it. Find leeches with the search `tag:leech` and rewrite them.

## Adding your own cards in a separate deck

1. **Create the deck:** on the Decks screen, click Create Deck and name it "BSA Company Internal" (or [COMPANY: agreed deck name]). Keep it a top-level deck, not inside "BSA Onboarding", so that importing a new version of the team deck never touches it.
2. **Create the note type once:** Tools > Manage Note Types > Add > "Clone: BSA Onboarding Basic". Name it "BSA Company Basic". It keeps the Front, Back and Source fields. For cloze cards, use Anki's built-in "Cloze" note type.
3. **Add cards:** click Add, pick the note type and your own deck, fill Front, Back and Source, and add tags (for example `M5C::PPV company`, or `M1::Valuation own` for a generic card).
4. **Keep sensitive data out of cards entirely:** no passwords, personal data, customer or supplier names with prices, margins or anything [COMPANY: data classification policy] marks confidential. A card can say where to find a value without containing it.
5. **Peer check:** once a week, swap 5 new cards with the other hire and check each other's facts. The Manager's milestone spot check counts errors.

## Caution: AnkiWeb sync

- AnkiWeb sync uploads your whole collection to AnkiWeb, a cloud service run by the makers of Anki, under a personal account. That is outside company systems.
- Anki syncs the whole collection, not chosen decks. If your own deck is in the same profile as anything you sync, your own deck goes to AnkiWeb too.
- **Rule:** do not sync any Anki profile that contains company-specific cards unless [COMPANY: policy confirms] that AnkiWeb is approved for this data. Do not install your own deck on a personal phone or tablet. `docs/04-access-request-checklist.md` (AR-21) sets AnkiWeb sync to off for company-specific cards unless IT approves.
- If you want to study the generic team deck on your phone, ask the Manager first. The only safe set-up is a second Anki profile (File > Switch Profile) that holds the team deck only and is the only profile linked to your AnkiWeb account. Never link two profiles to the same AnkiWeb account: the Anki manual warns this loses data.

## Sharing company cards through OneNote or SharePoint

Share through company systems, never through AnkiWeb or personal email.

1. **Team card list (preferred).** Keep one shared workbook at [COMPANY: SharePoint location] with the columns front, back, tags and source (as in BSA-Onboarding-cards.csv in the onboarding folder, without its deck column), plus author, reviewed by and date reviewed. Add your cards there weekly; the reviewer fills the review columns. Link it from the OneNote page "Anki company deck".
2. **Import into Anki:** save the reviewed rows as CSV (UTF-8). In Anki: File > Import, choose the CSV, set the note type to "BSA Company Basic" and the deck to "BSA Company Internal", map the columns to Front, Back, Tags and Source, then Import.
3. **Or share a deck package:** File > Export, choose "Anki Deck Package (.apkg)", select only your own deck, and untick "Include scheduling information" so others get fresh cards. Save it to [COMPANY: SharePoint folder] and link it from OneNote. Others import it with File > Import.
4. **For review in OneNote or Excel:** File > Export > "Notes in Plain Text (.txt)" for your own deck, then open it in Excel.
5. When a fact changes, fix it in the shared workbook first, then in Anki, and tell the other hire.

## Quality checklist for each card

- [ ] One fact; the question has one right answer.
- [ ] Country or context on the front where rules differ.
- [ ] Back is 40 words or fewer, answer first.
- [ ] Source field filled.
- [ ] No volatile fact, or the card is tagged `dated` and the back ends "(as of Mon YYYY)".
- [ ] Module tag first (`M1::...`), plus `company` if it is company-specific or `own` if it is a generic card I wrote.
- [ ] My cards are in my own deck only, never in the team deck, with no confidential data.
