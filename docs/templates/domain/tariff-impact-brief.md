# Tariff-Impact Brief Template

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** the Research handoff for one tariff or regulatory action. It states the WHAT: the action, its legal basis, timing, scope (HTS, origins, products, exclusions, stacking), rates, our interpretation with a confidence level, and which of our items it covers. Every claim cites a primary source. It contains no dollar figures: Standard Cost turns it into $ in the shared Tariff-Impact Model (`docs/templates/domain/tariff-impact-model-guide.md`).
- **Who uses it:** Hire A (Research) as maker. The Senior (legal scope and interpretation) or the Manager as checker. Hire B (Standard Cost) as the receiver. The Manager approves any business communication built on it.
- **When:** for every new or changed action that may touch our items in the US, Canada or Mexico. Outline by W4 (A30-6), full brief for a real recent action in W7 (A60-1), live as maker from W12 (A90-1). Module M5R. For time-sensitive actions, the urgency rule in `docs/01-30-60-90-plan.md` ("Live tariff actions during training") decides who is maker.

## How to fill this in

Text in [square brackets] is a prompt: replace it. [COMPANY: ...] is a company-specific value.

1. **Primary sources only.** Every fact in the brief carries a source ID (S1, S2, ...) from Part 4. Primary sources are the legal instrument (Federal Register notice, proclamation, executive order, Canada Gazette order, DOF decree), the official tariff schedule (HTSUS, Canada Customs Tariff, TIGIE) and the customs agency's implementing guidance (CBP CSMS, CBSA Customs Notice). News, law-firm alerts and broker newsletters are leads: use them to find the primary source, never as the source.
2. **Quote, then interpret.** For timing, scope, exclusions and stacking, paste the exact words first. Write your interpretation underneath, separately, with a confidence level (Part 8).
3. **No legal advice, and who contacts the broker.** The BSA records "our working interpretation". Anything rated Medium or Low that changes which items are in scope, the rate or the date goes, through the Senior (or the Manager), to the licensed customs broker or trade counsel before release. Before the day-60 review you never contact a customs broker, agente aduanal or trade counsel yourself: send the question to the Senior. After the day-60 review, with the Senior's agreement, you may email the broker with the Senior copied. Trade counsel is always contacted through the Senior or the Manager ([COMPANY: whether Manager approval is needed before contacting trade counsel]). Record who confirmed what, when and how.
4. **No dollars.** Item counts are fine. Landed cost, margin and $ impact belong to Standard Cost. A brief with $ figures is sent back (boundary rule, `docs/01-30-60-90-plan.md`).
5. **One brief per action and importing country.** A US action and a Canadian countermeasure are two briefs, even when they are linked.
6. **Versions.** v0.x while drafting. v1.0 is the first checked release. Any change after release is v1.1, v1.2 and so on, logged in Part 13, re-checked, and re-sent to Standard Cost. The model's Action tab names the brief version it was built from.
7. **Where it lives.** Save in [COMPANY: briefs folder] as `TIB_[Action ID]_v[n].docx` (or the OneNote page), and link it on the Jira story. Do not email copies.
8. **Never write current rates or dates from memory.** Take them from the sources on the day you write, and record the date you checked. For the current landscape, see `docs/primers/current-tariff-landscape.md`.

### The 60-minute first pass (do this before you write anything)

1. Find the legal instrument and its annexes. US: Federal Register (and the proclamation or executive order). Canada: the Department of Finance announcement, then the order in the Canada Gazette, Part II. Mexico: the decree or resolution in the DOF.
2. Find the implementing guidance. US: the CBP CSMS message (Chapter 99 numbers, filing order, in-transit claims). Canada: the CBSA Customs Notice. Mexico: ask the Senior to get the agente aduanal's view of how they will apply it ([COMPANY: agente aduanal contact]).
3. Read the timing clause and copy it word for word.
4. Get the HTS list as text (download the annex or copy from the HTSUS Chapter 99 page). Never retype a list of HTS numbers by hand.
5. Read the exclusions, the exemptions and any stacking or "does not apply" clauses.
6. Run the candidate-item query (Part 9) and count the matches.
7. Write down every question. Log the Jira story and tell the Manager the effective date and the candidate count.

## Reference: legal authority categories

Categories only. Whether any action under these authorities is in force today is a current-status question: check `docs/primers/current-tariff-landscape.md` and the sources.

| Category | Legal basis and instrument | Published in | Scope and rate patterns to look for |
|---|---|---|---|
| Section 232 (US) | Trade Expansion Act of 1962, national security. Presidential proclamation after a Commerce investigation | Federal Register; HTSUS Chapter 99; CBP CSMS | Product lists by HTS, often including "derivative" products; processes that add products later; special origin or content reporting (for example melt-and-pour country for steel) |
| Section 301 (US) | Trade Act of 1974, unfair foreign practices. USTR determination and notice of action | Federal Register (USTR); HTSUS Chapter 99 | HTS lists in annexes (often 8-digit); product exclusions written as narrative descriptions narrower than the HTS line, often with expiry dates |
| Section 201 (US) | Trade Act of 1974, safeguards after a USITC finding. Presidential proclamation | Federal Register; HTSUS Chapter 99 | Tariff-rate quotas, rates that step down over time, country exemptions |
| Section 122 (US) | Trade Act of 1974, balance of payments. Proclamation | Federal Register; HTSUS Chapter 99; CBP CSMS | Statute caps it at 15% ad valorem for up to 150 days unless Congress extends it; broad coverage with listed exceptions |
| Section 338 (US) | Tariff Act of 1930, countries that discriminate against US commerce. Proclamation | Federal Register; HTSUS Chapter 99; CBP CSMS | Statute caps new or additional duties at 50% ad valorem; country-specific product lists |
| IEEPA (US) | International Emergency Economic Powers Act. Executive order declaring a national emergency | Federal Register; HTSUS Chapter 99; CBP CSMS | Country-wide duties, carve-outs (for example USMCA-qualifying goods), interaction rules with other actions. The Supreme Court held on 2026-02-20 (Learning Resources, Inc. v. Trump) that IEEPA does not authorize tariffs. Use this category for past entries only (refunds, audits); status and refunds: US-1 in `docs/primers/current-tariff-landscape.md` |
| AD/CVD (US, CA, MX) | US: Tariff Act of 1930, Title VII (Commerce and USITC). Canada: Special Import Measures Act (CBSA and CITT). Mexico: cuotas compensatorias (Secretaría de Economía) | US: Federal Register and CBP AD/CVD messages. Canada: CBSA SIMA notices. Mexico: DOF | The written scope description decides coverage; HTS numbers are listed for convenience. Rates depend on producer and exporter. USMCA preference does not remove AD/CVD |
| Canada surtax order | Customs Tariff, section 53 (Governor in Council order on Finance's recommendation) | Canada Gazette, Part II; CBSA Customs Notice; Finance Canada announcement | Schedules of tariff items; surtax as % of value for duty; origin defined in the order; in-transit and other exclusions; relief sometimes through a separate remission order |
| Mexican decree (DOF) | Decree modifying the Tarifa of the LIGIE (TIGIE), or other decrees and agreements | Diario Oficial de la Federación (DOF) | Lists of fracciones arancelarias (8 digits) and NICO; whether trade-agreement (preferential) rates still apply; entry into force in the transitory articles; effects on IMMEX and PROSEC operations (the Senior asks the agente aduanal) |

### Timing language, decoded

| Wording or situation | What it means for us | What to check |
|---|---|---|
| "Entered for consumption, or withdrawn from warehouse for consumption, on or after 12:01 a.m. eastern time on [date]" (US) | The entry date and time decides the rate, not the PO, ship or receipt date. Rates in effect at the time of entry apply, and goods in a bonded warehouse take the rate at withdrawal (19 CFR 141.69) | Daylight or standard time; whether the broker will hold or speed up entries near the cutoff (an operational decision for the Manager, not Research) |
| In-transit provision (US pattern: goods loaded on the final mode of transit before the effective date and entered before a later date are not covered) | Some goods already on the water keep the old rate if both conditions are met | Both dates; how CBP wants the claim filed (check the CSMS guidance, for example a specific Chapter 99 number); whether the broker can prove the loading date |
| Canada surtax orders: goods imported from the date the order comes into force | The order's coming-into-force and application provisions decide; quote them | Whether goods in transit on that day are excluded (some 2025 surtax orders excluded them); the CBSA Customs Notice on how to account for it |
| Mexican decree "entra en vigor" in the transitory articles (often the day after publication) | The decree's own transitory articles decide when it starts | Which date fixes the rate on a pedimento: under Ley Aduanera article 56 this is generally the arrival date (sea: anchoring or berthing; land: crossing the border; air: arrival at the first Mexican airport). Confirm with the agente aduanal, through the Senior |
| End dates, sunsets, step changes, quotas | Rates can change again on a known date or when a quota fills | Put every date in Part 5; Standard Cost needs them for the cost period |
| AD/CVD | Cash deposits at entry; the final duty can be set years later in an administrative review | Producer and exporter on our entries; flag to the Senior |

## Reference: source documents

| Source | Country | What it gives you | Link |
|---|---|---|---|
| Federal Register | US | Legal text of notices, proclamations and executive orders, with annexes | https://www.federalregister.gov/ |
| HTSUS (USITC) | US | Chapter 99 headings and their U.S. notes; base rates; earlier editions and revisions | https://hts.usitc.gov/ |
| CBP CSMS messages | US | CBP filing guidance: Chapter 99 numbers, reporting order, in-transit claims, effective time in ACE | https://www.cbp.gov/trade/automated/cargo-systems-messaging-service (archive: https://www.cbp.gov/document/guidance/csms-archive) |
| USTR | US | Section 301 notices and exclusion lists | https://ustr.gov/ |
| Commerce, Enforcement and Compliance | US | AD/CVD orders and scope rulings | https://www.trade.gov/ |
| Canada Gazette, Part II | CA | Surtax and other orders made under the Customs Tariff | https://gazette.gc.ca/ |
| CBSA Customs Notices | CA | How CBSA applies an order; dates and accounting instructions | https://www.cbsa-asfc.gc.ca/publications/cn-ad/menu-eng.html |
| CBSA Customs Tariff | CA | Departmental consolidation of the Customs Tariff (pick the current year's edition) | https://www.cbsa-asfc.gc.ca/trade-commerce/tariff-tarif/2026/menu-eng.html |
| Diario Oficial de la Federación | MX | Decrees modifying the TIGIE; AD/CVD resolutions | https://www.dof.gob.mx/ |
| Secretaría de Economía | MX | Trade measures, IMMEX and PROSEC information | https://www.gob.mx/se |
| Our broker or agente aduanal | All | How they will file it; confirmation of our interpretation. Contact through the Senior (How to fill this in, item 3) | [COMPANY: broker contacts per country] |

## Template

### Part 1: Header

| Field | Entry |
|---|---|
| Action name | [Plain-language name: country, product, measure] |
| Action ID | [TA-country-year-nn, for example TA-US-2027-03. Same ID in the model file name and on its Action tab. The Jira label is tariff-action-[short id] (`docs/templates/bsa/07-jira-epic-story.md`): record it here] |
| Brief ID and version | [TIB-Action ID v0.1] |
| Importing country | [US, CA or MX] |
| Status | [Draft, In check, Released v1.0, Superseded] |
| Maker / checker | [Hire A] / [Senior or Manager] |
| Jira | [Story key; linked Standard Cost story key] |
| Date received / due | [Date and time] / [Date and time, and why] |
| Date sources last checked | [Date and time] |

### Part 2: Summary (5 lines, no $)

[1. What: the measure in one sentence. 2. Who: origins and products. 3. From when, and until when. 4. Rate and how it combines with existing duties. 5. Our exposure: number of candidate and in-scope items, and the open questions that could change that.]

### Part 3: Legal authority

| Field | Entry |
|---|---|
| Category | [Section 232, Section 301, Section 201, Section 122, Section 338, IEEPA, AD/CVD, Canada surtax order, Mexican decree (DOF), other] |
| Instrument | [Proclamation, executive order, notice of action, order, decree; number and date] |
| Issuing authority | [President, USTR, Commerce, Governor in Council, Secretaría de Economía, ...] |
| Related earlier actions | [Earlier actions on the same goods, with their brief IDs] |

### Part 4: Source documents

| ID | Document | Date published | Link or location | What it is used for |
|---|---|---|---|---|
| S1 | [Federal Register notice 91 FR [page], or Canada Gazette SOR/[year-number], or DOF decree of [date]] | [Date] | [URL] | [Legal text, annexes] |
| S2 | [CBP CSMS #[number], or CBSA Customs Notice [number]] | [Date] | [URL] | [Filing guidance] |
| S3 | [HTSUS Chapter 99 heading 9903.[xx.xx] and U.S. note] | [Revision] | [URL] | [Heading text and rate] |
| S4 | [Broker or counsel confirmation] | [Date] | [COMPANY: where emails are filed] | [Confirmation of Part 8 items] |

### Part 5: Timing

| Field | Entry | Source |
|---|---|---|
| Effective date and time | [Date, time, time zone] | [S#] |
| Basis (quote the words) | ["entered for consumption, or withdrawn from warehouse for consumption, on or after ..." / "imported into Canada on or after ..." / decree transitory article] | [S#] |
| In-transit provision | [Quote; both dates; how it is claimed] | [S#] |
| End date, sunset or review date | [Date, or "none stated"] | [S#] |
| Step changes or quotas | [Dates and triggers, or "none"] | [S#] |
| Retroactivity or refunds | [Any retroactive date or refund mechanism, or "none"] | [S#] |
| Exclusion or inclusion request process | [Who may request; docket or portal; deadline; expected decision time; or "none"] | [S#] |

### Part 6: Scope

#### 6.1 HTS and Chapter 99 headings

| Chapter 99 heading (or tariff item, or fracción) | What it covers | Covered HTS numbers or list | Source | Notes |
|---|---|---|---|---|
| [9903.xx.xx] | [Heading text] | [Annex list, attached as a text file; number of lines] | [S#] | [Digit level of the list: 4, 6, 8 or 10] |

#### 6.2 Countries of origin

| Country | Covered? | Origin rule used | Source |
|---|---|---|---|
| [Country] | [Yes, No] | [Normal non-preferential origin, or the action's own rule, for example melt-and-pour, or CUSMA marking rules in a Canadian order] | [S#] |

Origin is the country of origin in our classification master ([COMPANY: AS400 field or table]), not the supplier's country or the ship-from country. Flag any item where those differ.

#### 6.3 Product scope language

[Paste the scope paragraph word for word. Then write in one or two sentences what it adds to, or removes from, the HTS list. If the scope is a written description (as in AD/CVD), the description decides and the HTS list is only a guide.]

#### 6.4 Exclusions and exemptions

| Exclusion or exemption | Type | How we identify affected items | Evidence needed at entry | Source |
|---|---|---|---|---|
| [Text] | [HTS line, product description, end use, certificate, quota, date-limited] | [Query, item attribute, or item-by-item review] | [Certificate, declaration, special Chapter 99 number] | [S#] |

#### 6.5 USMCA-qualifying treatment

| Question | Answer | Source |
|---|---|---|
| Does the action exempt or reduce the duty for goods that qualify for USMCA (CUSMA, T-MEC) preference? | [Yes, exempt; Partial (state how: a lower rate, or duty on the non-US content only); No; Not applicable (no USMCA-party origin in scope)]. Model: Action B18 = Y, PARTIAL, N or N/A; Partial also needs its own Part 7 line | [S#] |
| If yes, what must be on the entry, and what evidence must we hold? | [Preference claim on the entry line; certification of origin on file] | [S#] |
| Which of our items rely on it, and is their certification current? | [Count; ask [COMPANY: USMCA certification owner]] | [Query] |

#### 6.6 Stacking and interaction with other actions

| Other measure on the same goods | Interaction | Filing (Chapter 99 numbers, order) | Source |
|---|---|---|---|
| [Base rate, other Chapter 99 duties, AD/CVD, surtax] | [Adds to it; this action does not apply when the other applies; the other no longer applies when this one does (non-stacking); replaces it; reduced] | [Numbers in the order CBP's guidance gives] | [S#] |

When this action switches off another duty on some of our items, list those items and the rate removed (Part 9 item list). They go on the model's Action tab as determinations with a displaced rate, or on a rate line when every item on that line pays the other duty at the same rate. When this action does not apply because another one does, those items are OUT determinations.

#### 6.7 De minimis and low-value shipments

[Does the action apply to shipments that would otherwise enter duty-free under a low-value or de minimis rule (US: Section 321)? US de minimis treatment changed repeatedly in 2025; check the current status in `docs/primers/current-tariff-landscape.md`. State whether any of our import flows use low-value entries ([COMPANY: confirm]).]

#### 6.8 Drawback eligibility

[Quote what the action says about drawback. Some actions have expressly barred drawback of their duties; others leave normal drawback rules in place. If the action is silent, write "silent" and send it to the Senior, who owns US duty drawback (M9).]

#### 6.9 Other provisions

[Tariff-rate quotas; foreign-trade zone provisions (FTZ is not used by us: [COMPANY: confirm]); Chapter 98 provisions; IMMEX, Anexo 24 and PROSEC effects in Mexico; anything else that affects which entries pay the duty.]

### Part 7: Rates

| Line | Applies to | Rate and type | Base the rate applies to | Adds to or replaces | Source |
|---|---|---|---|---|---|
| [R1] | [Chapter 99 heading or list (6.1); the origins, if the rate differs by origin; USMCA-qualifying goods or not, if it differs] | [25% ad valorem; or specific, per kg] | [US: the customs value (transaction value, excluding international freight and insurance), or the part of it the action names, for example the value of the metal content or the non-US content, and where that value comes from. Canada: value for duty. Mexico: valor en aduana] | [Adds to the base rate; replaces earlier rate of x%; switches off [other measure] at y%] | [S#] |

How the lines go into the model (Action tab, `docs/templates/domain/tariff-impact-model-guide.md`):

- **One rate for every in-scope item:** R1 goes in B15, its base (full or part) in B20.
- **More than one rate:** the line that covers most items goes in B15. Every other line becomes a rate line, keyed by rate group (the 6.1 heading, entered next to each of its HTS prefixes), origin and USMCA status. A line for excluded goods ("no additional duty") is an exclusion (6.4), not a rate line.
- **Which line wins:** when two lines could apply to the same item, the model uses the most specific one (origin, then USMCA status, then rate group). If the instrument sets a different order, say so here and give the item-level answer, so the model can carry an extra line.
- **Part of the value:** write which part and the source of each item's share. Standard Cost enters the shares on Items; the checker traces them. Research states the rule; Standard Cost does the arithmetic.

### Part 8: Interpretation, confidence and confirmation

Confidence: **High** = the text says it expressly and the agency guidance agrees. **Medium** = a reasonable reading with no contradicting source, not yet confirmed. **Low** = ambiguous or sources conflict. Medium items that change scope, rate or date need broker or counsel confirmation before release, sent through the Senior (How to fill this in, item 3). A brief with an open Low item can only be released as "provisional", with the Manager's approval and the Low items stated in the summary.

| Q | Question | Our working interpretation | Confidence | Confirmed with (who, date, how) | Source |
|---|---|---|---|---|---|
| [Q1] | [Specific question] | [Interpretation in one or two sentences] | [H, M, L] | [Broker [COMPANY], date, email filed at [location]; or "not yet"] | [S#] |

### Part 9: Affected items (extract method)

| Step | Entry |
|---|---|
| Source and extract time | [COMPANY: classification master table or AS400 extract], run [date and time] |
| Filters | [Import country; active items ([COMPANY: active status rule]); origins in Part 6.2] |
| Matching rule | [HTS stored and compared as text; prefix match at the digit level of the annex (for example the first 8 digits); exclusions applied after the match] |
| Saved query | [COMPANY: code repository path], version [n] |
| Counts | [Candidates n; in scope n; out n (by reason); borderline n] |
| Borderline review | [List of items whose description doesn't clearly fit; reviewed by the Senior on [date]] |
| Item list delivered | [Location of the item list and determinations; Action tab of model version [n]] |

Candidate-item query pattern (adjust the table and column names to [COMPANY: warehouse schema]):

```sql
-- Load the annex list as text first: one row per HTS prefix, digits only.
-- CREATE TABLE #scope (prefix VARCHAR(10));  INSERT ... from the annex text file
SELECT c.item_number, c.import_country, c.hts_code, c.country_of_origin, s.prefix
FROM [COMPANY: classification table] AS c
JOIN #scope AS s
  ON REPLACE(c.hts_code, '.', '') LIKE s.prefix + '%'   -- text match keeps leading zeros
WHERE c.import_country = 'US'
  AND c.country_of_origin IN ('[origin codes]')
  AND c.item_status = '[COMPANY: active status]';
```

### Part 10: Open questions

| # | Question | Asked to | Date asked | Needed by | Status and answer |
|---|---|---|---|---|---|
| [OQ1] | [Question; what changes if the answer is different] | [Senior, Purchasing; a broker or counsel only through the Senior] | [Date] | [Date] | [Open, Answered: answer and source] |

### Part 11: Handoff to Standard Cost

| What is delivered | Entry |
|---|---|
| Brief version | [v1.0, released date and time] |
| Model | [Action tab filled and checked in model file [name] v[n]] |
| Item list | [In-scope items with determinations and reasons; location] |
| Dates Standard Cost needs | [Effective date, in-transit end date, end or step dates] |
| Open questions that could change the $ | [OQ numbers and what would change] |
| Needed by | [Date and time, and the business reason (pricing meeting, cost cycle)] |
| Handoff call | [15 minutes, date; Standard Cost confirms on Jira that the inputs are understood] |

### Part 12: Maker-checker sign-off

| Role | Name | Version | Date and time | Result and findings |
|---|---|---|---|---|
| Maker | [Hire A] | [v] | [ ] | [Self-check complete (checklist below)] |
| Checker | [Senior or Manager] | [v] | [ ] | [Approved; Approved with changes (list); Returned (list)] |
| Release approval for business communication | [Manager] | [v] | [ ] | [Approved to send] |

When the checker approves with changes, the checker confirms the changes in the released version and records that version here. The checker also records name, date, version and findings on the Jira story.

### Part 13: Change log

| Version | Date | Change | By | Checked by |
|---|---|---|---|---|
| [v0.1] | [ ] | [First draft] | [ ] | [n/a] |

## Filled example (FICTIONAL)

**This action is FICTIONAL.** Country X, the notice, the Chapter 99 heading 9903.XX.01, the CSMS message and all dates below are invented to show the method. Do not use any of it as fact. It continues the hypothetical "Country X steel fasteners" example used in `docs/templates/bsa/01-intake-request.md`, `docs/templates/bsa/07-jira-epic-story.md` and `docs/templates/bsa/08-project-closeout.md`. The 14 SAMPLE rows in Tariff-Impact-Model-Template.xlsx (in the onboarding folder) apply the same rules to a small synthetic item set. One difference to notice: the brief's aerospace bolt (Q2) is IN because certificates come with only some of its shipments, while the model's SAMPLE-005 is OUT because its supplier certifies every shipment.

### Header and summary

| Field | Entry |
|---|---|
| Action name | FICTIONAL: US additional duty on iron or steel fasteners (heading 7318) from Country X |
| Action ID | TA-US-FIC-01 (Jira label tariff-action-cx7318) |
| Brief ID and version | TIB-TA-US-FIC-01 v1.0 |
| Importing country | US |
| Status | Released v1.0, Thu 2027-02-18 11:30 |
| Maker / checker | Hire A / Senior |
| Date received / due | Tue 2027-02-16 09:40 / Thu 2027-02-18 12:00 (pricing meets Fri; duty applies in 8 working days) |
| Date sources last checked | Thu 2027-02-18 10:15 |

Summary: (1) A FICTIONAL Section 301 action adds a 25% ad valorem duty on goods of HTS heading 7318 from Country X. (2) Origin Country X only; all of heading 7318 except the Annex II exclusions. (3) Goods entered on or after 12:01 a.m. EST Mon 2027-03-01; no end date; goods already in transit get relief until 2027-04-30 if conditions are met. (4) Adds to the column 1 General rate. It switches off the FICTIONAL 9903.YY.01 duty (an earlier 10% on listed goods of Country X) on the goods it covers (S1 clause 4); 3 of our in-scope items pay 9903.YY.01 today (Q5). (5) 140 candidate items; 138 in scope after the Senior's review; 1 open question on how to claim the in-transit relief.

### Legal authority and sources

| Field | Entry |
|---|---|
| Category | Section 301 of the Trade Act of 1974 (FICTIONAL instance; no such action exists) |
| Instrument | FICTIONAL USTR notice of action, 92 FR 00000, published 2027-02-16 |
| Issuing authority | USTR |
| Related earlier actions | None on heading 7318 from Country X |

| ID | Document | Date published | Link or location | What it is used for |
|---|---|---|---|---|
| S1 | FICTIONAL USTR notice of action 92 FR 00000, with Annex I (covered) and Annex II (excluded) | 2027-02-16 | [federalregister.gov link] | Legal text, timing, scope, rate |
| S2 | FICTIONAL CBP CSMS #00000000 | 2027-02-17 | [cbp.gov CSMS link] | Filing: 9903.XX.01 and 9903.XX.02, reporting order, stacking |
| S3 | FICTIONAL HTSUS heading 9903.XX.01 and U.S. note 99 | Revision [n] | [hts.usitc.gov link] | Heading text and rate |
| S4 | Email from [COMPANY: US broker] confirming Q2 and Q3 (Hire A's question, sent with the Senior copied) | 2027-02-17 | [COMPANY: email archive] | Confirmation |

### Timing

| Field | Entry | Source |
|---|---|---|
| Effective date and time | 12:01 a.m. eastern standard time, Mon 2027-03-01 | S1 |
| Basis (quote) | "...products of Country X that are entered for consumption, or withdrawn from warehouse for consumption, on or after 12:01 a.m. eastern standard time on March 1, 2027" | S1 |
| In-transit provision | "...does not apply to products loaded onto a vessel at the port of loading and in transit on the final mode of transit before 12:01 a.m. eastern standard time on March 1, 2027, and entered for consumption before 12:01 a.m. eastern daylight time on April 30, 2027." Claimed under 9903.XX.03 (S2) | S1, S2 |
| End date | None stated | S1 |
| Step changes or quotas | None | S1 |
| Retroactivity or refunds | None | S1 |
| Exclusion or inclusion request process | None in the notice | S1 |

### Scope

| Chapter 99 heading | What it covers | Covered HTS numbers or list | Source | Notes |
|---|---|---|---|---|
| 9903.XX.01 | Products of Country X listed in Annex I: additional 25% | Annex I: heading 7318 (1 line) | S1, S3 | 4-digit list: every 7318 number is covered unless in Annex II |
| 9903.XX.02 | Products of Country X listed in Annex II: no additional duty | Annex II: (1) subheading 7318.24 (cotters and cotter pins); (2) "fasteners certified for use in civil aircraft and accompanied by a certificate of conformity" | S1, S2 | Exclusion (2) is a product description, not an HTS line |
| 9903.XX.03 | In-transit products | Same as Annex I | S2 | Claim conditions in Timing |

| Country | Covered? | Origin rule used | Source |
|---|---|---|---|
| Country X | Yes | Normal non-preferential origin (no special rule in the notice) | S1 |
| All others | No | n/a | S1 |

| Exclusion or exemption | Type | How we identify affected items | Evidence needed at entry | Source |
|---|---|---|---|---|
| 7318.24 cotters and cotter pins | HTS line | Query: HTS starts 731824 | None beyond classification; filed under 9903.XX.02 | S1, S2 |
| Civil-aircraft fasteners with certificate | Product description and certificate | Item-by-item: aerospace item attribute [COMPANY: attribute] plus Purchasing check | Certificate of conformity with each entry | S1, S2 |

| Topic | Entry | Source |
|---|---|---|
| USMCA | Not applicable: Country X is not a USMCA party; goods of Canada and Mexico are not covered. Routing Country X goods through Mexico does not change their origin unless they are substantially transformed there (flag any such supply chain to the Senior) | S1 |
| Stacking | Adds to the column 1 General rate. S1 clause 4: goods that pay 9903.XX.01 no longer pay the FICTIONAL 9903.YY.01 (10%). 3 of our items pay 9903.YY.01 today (Q5): they go on the Action tab as determinations with 10% displaced. S2: apart from 9903.YY.01, no other additional duty applies to these goods. Report 9903.XX.01 before the Chapter 73 number | S1, S2 |
| De minimis | S2: applies regardless of value. Our imports from Country X are formal entries ([COMPANY: confirm]) | S2 |
| Drawback | S1 is silent; S2 says normal drawback rules apply. Sent to the Senior 2027-02-17 | S2 |

### Rates

| Line | Applies to | Rate and type | Base the rate applies to | Adds to or replaces | Source |
|---|---|---|---|---|---|
| R1 | 9903.XX.01 | 25% ad valorem | Customs value of the Chapter 73 good (full value) | Adds to the column 1 General rate; switches off 9903.YY.01 (10%) on covered goods | S1, S3 |
| R2 | 9903.XX.02 (excluded) | No additional duty | n/a | n/a | S1 |

### Interpretation and confirmation

| Q | Question | Our working interpretation | Confidence | Confirmed with (who, date, how) | Source |
|---|---|---|---|---|---|
| Q1 | Are plated or coated screws of 7318.15 covered? | Yes. Plating does not change the heading, and Annex I covers all of 7318 | High | Not needed | S1 |
| Q2 | Our aerospace bolt (1 item) has certificates for some shipments only. In or out? | In scope unless a certificate accompanies the entry. Purchasing confirmed on 2027-02-17 that the supplier does not issue them for our orders, so the item is IN | Medium before, High after | [COMPANY: US broker], 2027-02-17, email (S4) | S1, S2, S4 |
| Q3 | 6 items have descriptions that may belong outside 7318 (brackets, hooks). Are they covered? | Covered only if correctly classified in 7318. The Senior reviewed all 6: 2 belong in another heading and go through change requests before the effective date; 4 stay in 7318 | Medium before, High after | Senior 2027-02-17; [COMPANY: US broker] (S4) | S3 |
| Q4 | How do we claim the in-transit relief? | File 9903.XX.03 with proof of the loading date. CBP said further guidance will follow | Medium | Open: OQ1 | S2 |
| Q5 | Which of our items pay 9903.YY.01 today, and does clause 4 remove it from all of them? | 3 items, found from the last 12 months of entry lines and the 9903.YY.01 list. Clause 4 removes it from any good that pays 9903.XX.01, so all 3 drop it | High | Not needed | S1 |

### Affected items and open questions

| Step | Entry |
|---|---|
| Source and extract time | [COMPANY: classification master], run 2027-02-16 14:00 |
| Filters | Import country US; active items; origin Country X |
| Matching rule | HTS digits as text, prefix 7318; Annex II applied after the match |
| Counts | 140 candidates. 0 in 7318.24. 2 out after the Senior's classification review (Q3). 138 in scope, including the aerospace bolt (Q2) |
| Borderline review | 6 items reviewed by the Senior on 2027-02-17 (Q3) |
| Item list delivered | Action tab of TIM_TA-US-FIC-01_US_v1.0; item list with determinations (including the 3 items with 9903.YY.01 displaced) in [COMPANY: briefs folder] |

| # | Question | Asked to | Date asked | Needed by | Status and answer |
|---|---|---|---|---|---|
| OQ1 | Exact filing and proof requirements for in-transit goods (9903.XX.03). Affects goods on the water on 2027-03-01 only, not the item list | [COMPANY: US broker]; watch CBP CSMS | 2027-02-17 | 2027-02-26 | Open. Hire A checks CSMS daily until answered |

### Handoff and sign-off

Handoff: brief v1.0 and the checked Action tab released Thu 2027-02-18 11:30. Standard Cost needs the effective date (2027-03-01) and the in-transit end date (2027-04-30) for in-transit stock; OQ1 does not change the item list. The 15-minute handoff call was held Thu 13:00, and Hire B confirmed on the Jira story.

| Role | Name | Version | Date and time | Result and findings |
|---|---|---|---|---|
| Maker | Hire A | v0.3 | 2027-02-18 09:00 | Self-check complete |
| Checker | Senior | v0.3 | 2027-02-18 10:45 | Approved with changes: stacking wording now quotes S1 and S2 instead of paraphrasing them. Closed in v1.0; Senior confirmed v1.0 at 11:20 |
| Release approval | Manager | v1.0 | 2027-02-19 08:35 | Approved to send with the Standard Cost $ summary |

## Quality checklist (maker, before you send for checking)

- [ ] Every fact has a source ID, and every source is primary (or an identified broker or counsel confirmation).
- [ ] Timing, scope, exclusion and stacking wording is quoted, not paraphrased.
- [ ] Effective date, time, time zone and basis are stated; the in-transit provision is stated or "none".
- [ ] The HTS list came from the source as text and was not retyped; its digit level is stated.
- [ ] Origin rule stated; origins checked against our classification master, not supplier addresses.
- [ ] Each exclusion says how we find affected items and what evidence the entry needs.
- [ ] USMCA, stacking, de minimis and drawback each have an answer or "not applicable", with a source.
- [ ] Each Part 7 line says which goods it applies to and its base (full value or a named part); every duty the action switches off is listed by item.
- [ ] Every Medium or Low interpretation that changes scope, rate or date is confirmed or listed as an open question; broker and counsel questions went through the Senior.
- [ ] Item counts add up (candidates = in scope + out + borderline), and the query is saved.
- [ ] No $ figures anywhere in the brief.
- [ ] The Action tab of the model matches this version, line for line.
- [ ] Version and change log updated; Jira story linked.

## Checker checklist (Senior or Manager)

- [ ] Open each source and compare the brief to it line by line: HTS list, origins, rate, effective date and time, exclusions, in-transit terms.
- [ ] Re-run the candidate count, or check the saved query's logic and filters.
- [ ] Challenge every High rating once: "Where does the text say that?"
- [ ] Confirm the stacking result for at least 3 items that carry other duties.
- [ ] Check the boundary: no $; nothing on cost or pricing decisions.
- [ ] Record name, date, version and findings on the Jira story and in Part 12.
