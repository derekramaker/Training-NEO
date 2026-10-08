# Intake Request and Triage Template

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** capture every incoming work request the same way, score it, route it to the right place (quick answer, Jira story, Jira epic, or decline), and send the requester a clear reply. It is the front door for all BSA work.
- **Who uses it:** both hires for every request they receive; the Manager to confirm priorities and declines; the Senior when a request lands in exports, reporting or drawback.
- **When:** the same working day a request arrives, before any work starts. First practice: Wed 10/21 (ways-of-working session). From then on, every request. Module M4.

## How to fill this in

Text in [square brackets] is a prompt: replace it with your answer. [COMPANY: ...] marks a company-specific value the Manager fills in once in the company copy; if one is still blank, ask.

1. Log the request before you start work. Paste the requester's own words into Part A. Do not paraphrase them away.
2. Fill every Part A field (about 10 minutes). If you don't know a value, write "Unknown, asked [person] on [date]". Never leave a field blank and never guess.
3. Score Part B using the definitions in the table, not gut feel. Write one line of reasoning per score (about 5 minutes).
4. Apply the routing rule in Part C. The first rule that matches wins.
5. Check the boundary rule. Research owns the WHAT (which action, which items, which rates and dates). Standard Cost owns the $ (cost and margin impact, the Oracle cost update, variance). A request that needs both becomes two linked issues.
6. Reply using Part D: acknowledge the same working day; confirm the route, scope and date within 1 working day.
7. In days 1 to 60, the Manager confirms every P1 or P2 priority and every decline before you send it. Until then, say "I'll confirm by [time]".

Where the answers go: Part A and Part B go into the Jira issue ([COMPANY: Jira project key and intake fields]). For a quick answer, keep one line in your daily notes. The priority definitions match `docs/05-time-management.md`.

## Part A: Request form

| Field | What to enter | Example of a good entry |
|---|---|---|
| Jira key | Created when you log it; "none" for a quick answer | [COMPANY: project key]-142 |
| Title | Track: verb + object + scope, under 80 characters | Research: scope new US duty on steel fasteners from Country X |
| Requester | Name, team, role | [COMPANY: Purchasing category manager] |
| Date and channel received | Date, time, and how (email, Teams, meeting) | Tue, 09:40, email |
| Request in their words | Paste the message or your verbatim notes | "Which of our items are hit and what does it do to our cost?" |
| Decision it supports | What the requester will decide or do with the answer | Re-price the fastener line at Friday's pricing meeting |
| Needed by, and why that date | The date and the driver: regulatory effective date, broker cut-off, Finance cost cycle, meeting, customer | Fri 10:00, pricing meeting. Duty effective 8 working days out |
| Scope | Countries (US, CA, MX), items or item families, HTS codes, suppliers, origin countries, cost period, entry date range | US imports; HTS heading 7318; origin Country X; active items only |
| Data and sources needed | Systems, reports, files, external sources; whether you can access them | Federal Register notice; HTSUS Chapter 99; AS400 classification master (inquiry); warehouse import history |
| Systems that could change | AS400 trade system, Oracle, SQL Server or warehouse, Power BI, a custom tool, a broker feed, e2open. "None" if read-only | None (read-only analysis) |
| Track | Research, Standard Cost, Exports, Reporting, Tools, e2open, Other | Research and Standard Cost (split) |
| Deliverable | Answer, Tariff-Impact Brief, model, analysis, report, tool change, data fix | Brief plus $ impact in the shared Tariff-Impact Model |
| Downstream users | Who or what consumes the result: broker, Finance, pricing, Oracle, a report | Pricing; Finance (next cost update); brokers (if any classification changes) |
| Maker and checker | Who does the work; who gives the documented second-person review | Maker: Hire A. Checker: Senior |
| First size estimate | Under 15 min, under 1 day, 1 to 5 days, more than 5 days | 1 to 5 days per track |
| Related items | Linked Jira issues, prior briefs, earlier requests | [COMPANY: project key]-118 (earlier action on the same heading) |
| Sensitivity | Supplier pricing, margin, legal question, personal data. Say how you will restrict sharing | Margin data: share only with the requester and Finance |

## Part B: Triage scoring

Score Value, Urgency and Risk from 1 to 3. Effort is sized separately: it decides the route in Part C, not the priority.

| Factor | 1 = Low | 2 = Medium | 3 = High |
|---|---|---|---|
| Value | Nice to have; helps one person; no decision depends on it | Improves a recurring task or a team decision; affects some items or a report people use | Drives a pricing, cost, sourcing or compliance decision; affects many items, entries or more than [COMPANY: $ threshold] |
| Urgency | No date, or the date is more than 30 days out | Dated business need in 5 to 30 working days (meeting, Finance cycle input, report deadline) | Regulatory effective date, broker cut-off or Finance cut-off inside 10 working days, or the data is wrong in production now |
| Compliance or financial risk (if we get it wrong) | Internal only; no effect on filings, costs or reports | Could feed a future cost, report or broker data set; caught by a later review | Could cause a wrong customs declaration (classification, value, origin claim), a misstated standard cost or margin, or penalty exposure |
| Effort (size, for routing) | Under 1 day | 1 to 5 working days | More than 5 working days, or several people or tracks |

### Priority from the scores

- **P1** if any of these is true: Urgency 3 and Risk 3; wrong data is reaching a broker, Finance or a system now; a regulatory effective date falls inside 10 working days and our items may be in scope. Tell the Manager at once (within 30 minutes for a new tariff action).
- **P2** if Value + Urgency + Risk is 7 or more, or Urgency is 3.
- **P3** for everything else.
- Tie-break inside the same priority: earlier hard date first, then higher Risk, then smaller Effort.

### Scoring record (paste into the Jira issue)

| Factor | Score | One-line reason |
|---|---|---|
| Value | [1-3] | [Why] |
| Urgency | [1-3] | [The date and its driver] |
| Risk | [1-3] | [What goes wrong, and for whom, if the answer is wrong] |
| Effort | [1-3] | [Size and who is involved] |
| Priority | [P1, P2, P3] | [Rule that applied; who confirmed and when] |

## Part C: Routing rule

Check the rules in order. The first one that matches is the route.

| Order | If this is true | Route | What you create |
|---|---|---|---|
| 1 | It is out of the team's scope or someone else's job: a legal opinion (trade counsel, through the Manager); a filing or correction the broker makes (the broker files, we supply data, the Manager decides on contacting the broker); IT access or hardware (service desk); FTZ (not in scope). Or it duplicates an open issue. Or Value 1, Risk 1 and no date | Decline (redirect, link the duplicate, or park in the backlog) | No new issue, or a parked issue with [COMPANY: parked label]. Manager confirms in days 1 to 60 |
| 2 | Under 15 minutes, nothing is produced, no data or system changes, no review needed, and the answer is already documented or readable in a system you have access to | Quick answer | Reply directly; one line in your daily notes. If it grows past 15 minutes, log a story |
| 3 | More than 5 working days; or more than one deliverable or track (for example WHAT and $); or two or more stakeholder groups must sign off; or a production tool or system change with data migration or an interface (broker feed, Oracle load) | Epic | Jira epic with child stories (`docs/templates/bsa/07-jira-epic-story.md`). New capability: add requirements (`docs/templates/bsa/02-requirements.md`) |
| 4 | Anything else | Story (Bug if something is broken) | Jira story or bug with Given/When/Then acceptance criteria (`docs/templates/bsa/07-jira-epic-story.md`) |

Two standing rules apply on top of the route:

- **Any change to a tool, configuration or production data** needs a change request (`docs/templates/bsa/06-change-request.md`), whatever its size.
- **A new tariff or regulatory action that may cover our items** is always at least a Research story (WHAT, using `docs/templates/domain/tariff-impact-brief.md`). If anyone needs the cost or margin effect, it becomes an epic with a linked Standard Cost story ($, in the shared Tariff-Impact Model). The Research story blocks the Standard Cost story.

## Part D: What to send back to the requester

Copy the message that fits and replace the prompts. Send it from email or Teams, and paste a copy into the Jira issue.

### D1. Acknowledgement (same working day)

> Subject: [Jira key]: [short title]
>
> Hi [name], thanks. I've logged this as [Jira key]. I'll confirm the scope and a delivery date by [day, time]. If there is a hard date behind this (a tariff effective date, a Finance cut-off, a meeting), please tell me now.

### D2. Triage result (within 1 working day)

> Here is what I understood: [one sentence in plain words].
>
> Scope: [countries, items, HTS, period]. Not included: [what is out of scope].
>
> You will get: [deliverable] by [date], prepared by [maker] and reviewed by [checker].
>
> I need from you: [data, examples or a decision] by [date].
>
> Priority: [P1, P2 or P3] because [reason]. Next update: [date].

### D3. Quick answer

> [The answer]. Source: [system, report or document, and its date]. If you plan to use this for a filing, a cost update or a customer commitment, tell me and I'll log it so it gets a second-person review.

### D4. Decline or redirect

> We are not taking this one on because [reason: outside our scope, owned by another team, or lower value than the current P1 and P2 work]. [Team or contact] handles this: [how to reach them]. [If parked: "I've parked it as [Jira key] and we'll look at it again on [date]."]

Rules for every reply:

- In days 1 to 60, never commit a P1 or P2 date, and never decline, without the Manager's confirmation.
- Never give a legal interpretation as a quick answer. Interpretation goes through a Research story with a checker.
- Respect the boundary: Research replies do not state $ impacts; Standard Cost replies do not reinterpret legal scope.

## Filled example

The action below is hypothetical. It shows the method, not a real notice.

On a Tuesday at 09:40, [COMPANY: Purchasing category manager] emails: "Saw news of a new US tariff on steel fasteners from Country X starting next week. Which of our items are hit and what does it do to our cost? Pricing meets Friday." A Federal Register notice published that morning adds a new HTSUS Chapter 99 heading with an additional ad valorem duty on certain goods of HTS heading 7318 (screws, bolts, nuts and similar articles of iron or steel) from Country X. It applies to goods entered for consumption, or withdrawn from warehouse for consumption, on or after 12:01 a.m. eastern time, 8 working days out.

### Scoring record

| Factor | Score | One-line reason |
|---|---|---|
| Value | 3 | Drives a pricing decision across a product line; about 140 active items in heading 7318 |
| Urgency | 3 | Effective date in 8 working days; pricing meeting Friday |
| Risk | 3 | Wrong item scope means wrong duty deposits and a wrong cost and margin basis |
| Effort | 3 | Two tracks (WHAT and $), more than 5 days in total |
| Priority | P1 | Urgency 3 and Risk 3. Manager confirmed at 10:05 |

### Route

Epic: "Tariff action: Country X steel fasteners (hypothetical)". Child stories:

1. Research: Tariff-Impact Brief (legal scope, in-scope HTS and items, rate, effective date, stacking with other duties, sources). Maker Hire A, checker Senior. Due Thursday 12:00.
2. Standard Cost: landed-cost and margin impact for in-scope items in the shared Tariff-Impact Model. Maker Hire B, checker Manager. Blocked by story 1. Due Friday 08:00.
3. Research: confirm the classification of 6 borderline items (heading 7318 vs other headings). Maker Hire A, checker Senior. Any classification change gets its own change request because it changes broker data.

### D2 reply as sent (10:20)

> Here is what I understood: you need to know which of our items the new US duty on Country X fasteners covers, and what it does to landed cost and margin, before Friday's pricing meeting.
>
> Scope: US imports of HTS heading 7318 from Country X, active items. Not included: Canada and Mexico (no matching action announced), customer price recommendations.
>
> You will get: the checked item list with the legal basis by Thursday 12:00 (Hire A, reviewed by the Senior) and the cost and margin impact by Friday 08:00 (Hire B, reviewed by the Manager).
>
> I need from you: the volume forecast for the next two quarters by Wednesday 12:00.
>
> Priority: P1 because the duty takes effect in 8 working days. Next update: Wednesday 16:00.

### Routing practice: five more requests

| Request | V / U / R / Effort | Priority | Route | Why |
|---|---|---|---|---|
| "Why did the standard cost of item [COMPANY: item] rise 12% this period?" (pricing review in 2 weeks) | 2 / 2 / 2 / 2 | P3 | Story (Standard Cost) | One analysis, one maker, under 5 days |
| "What's the Canadian classification of item [COMPANY: item]?" | 1 / 1 / 1 / 1 | P3 | Quick answer | Readable in the classification master in 5 minutes; nothing produced |
| "The [COMPANY: tool closest to Research] export file drops the leading zero on chapter 01 to 09 HTS codes" | 3 / 3 / 3 / 1 | P1 | Bug plus change request | Wrong data reaching brokers now |
| "Please file a correction on last month's entry [entry number]" | 2 / 2 / 3 / 1 | n/a | Decline (redirect) | The broker files corrections. Log the finding; the Manager decides on contacting the broker |
| "Replace the AS400 classification screens with e2open" | 3 / 2 / 3 / 3 | P2 | Epic (part of the e2open project, M10) | Multi-track system change; goes to the project backlog |

## Quality checklist before you send

- [ ] Logged the same working day, before any work started.
- [ ] The requester's own words are pasted in, not just my summary.
- [ ] "Needed by" has a reason; regulatory effective dates and cut-offs are checked against the source, not taken from the email.
- [ ] Scope names countries, items or HTS, and the period. Out-of-scope is written down.
- [ ] Each score has a one-line reason using the table definitions.
- [ ] Priority follows the rule; P1 or P2 confirmed by the Manager (days 1 to 60).
- [ ] Route follows Part C; a WHAT and $ request is split into two linked issues.
- [ ] A change request is opened if any tool, configuration or production data will change.
- [ ] Maker and checker are named, and they are different people.
- [ ] The reply states the deliverable, date, maker, checker and what I need from the requester.
- [ ] No legal interpretation in a quick answer; no $ in a Research reply; no reinterpretation of scope in a Standard Cost reply.
- [ ] Sensitive data (supplier prices, margins) goes only to people who need it.
