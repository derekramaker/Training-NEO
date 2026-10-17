# Business Systems Analysis Primer

Last updated: 2026-10-17 · Owner: BSA Manager

- **Purpose:** the foundation for M4 (BSA fundamentals and craft). It explains the discipline behind the team's BSA templates: what a business systems analyst does here, the BABOK knowledge areas and core concepts, stakeholders, elicitation, requirements (types, quality, user stories, acceptance criteria, MoSCoW, traceability), analysis and modeling, and solution evaluation. The templates in `docs/templates/bsa/` say what to fill in; this primer says why, and how to do it well. One fictional tariff action on KIT-100 runs through it (Part 10).
- **Who uses it:** Hire A and Hire B for self-study (about 3.25 hours in W2–W3, taken from the existing self-study budget). The Manager uses it in the W2 session "M4 intake and Jira stories" (Wed 10/28, 13:00) and the W3 session "M4 intake and requirements". Trainers can cite sections in review comments (for example "BSA primer 5.2").
- **When:** Parts 1–3 in W2; Parts 4–6, the Part 10 worked example and the self-check in W3; Parts 7–9 as short reads in W4 and W8 (study plan below), with short re-reads before later M4 sessions.

## How to use this primer

| Session | When | Parts | Focused time | Output |
|---|---|---|---|---|
| 1 | W2, before the Wed 10/28 13:00 M4 session | 1 and 2 | 0.75 h | 3 Anki cards; one paragraph: "what does a BSA do on this team?" |
| 2 | W2, after the session, with your shadow write-up | 3 | 0.5 h | Stakeholder list (3.5) for the item you shadowed |
| 3 | W3, before the "M4 intake and requirements" session | 4 and 5 | 1.0 h | Two questions for the session, in your question log |
| 4 | W3, after the Wed 11/4 scoping with the Senior | 6, with Part 10 as your model | 0.75 h | Stakeholder list and elicitation plan (3.5, 4.6) on the Jira issue for your W3 intake by Fri 11/6; one decision table or 5 Whys for an item in your track |
| 5 | W3, end of week | Self-check questions 1–16 (Part 11) | 0.25 h | Answers in OneNote; open questions in your question log |
| Short reads | W4–W11, inside that week's existing self-study | W4: Parts 8 and 9, and 6.1 again (process mapping). W7: 5.6 and 6.1 (data mapping and UAT basics). W8: Part 7 and question 17 (with the change request's post-implementation check, 06 Section 12), and 5.7. Your first closeout: Part 7 again. W9–W11: Parts 4 and 6 (e2open as-is interviews) | 10–15 min each | Notes added to your earlier answers |

**Your W3 intake** is the intake record (`docs/templates/bsa/01-intake-request.md`) for your small real analysis, scoped with the Senior on Wed 11/4. Its stakeholder list and elicitation plan are a day-30 Should criterion for both hires (`docs/01-30-60-90-plan.md` Section 4).

Tailoring:

- **Hire A (Research):** most of your work starts outside the company, with a notice. Spend extra time on 4.5 (working with the Senior as expert) and 6.2 (decision tables for scope, stacking and exclusions). Your A30-9 stakeholder map covers every group you meet in W3–W4; start each work item's stakeholder list (3.5) from it. If you script, the candidate query in Part 10 is a good first saved query: run it in the team database with your personal login, on loaded extracts, and never run unreviewed code against a production system (`docs/primers/data-platform-primer.md` Part 1).
- **Hire B (Standard Cost):** the business context in Part 1 is a refresher, so skim it and spend the time on 5.6 (traceability) and 6.1, and read Part 7 in W3 instead of W8. Finance will ask you to prove that a cost change does what was agreed.

Rules: [COMPANY: ...] marks a company fact the Manager confirms. Quotations marked "BABOK" are from BABOK Guide v3 (IIBA, 2015). KIT-100, PART-A, PART-B, PART-C, Country X and Action X-1 are fictional. Terms are in the Glossary tab of the trackers workbook.

## 1. What a business systems analyst does on this team

### 1.1 Need, change, data

A business systems analyst (BSA) turns a business need into a system change and makes sure the data behind it is right. Almost every piece of our work has these three layers:

| Layer | Question the BSA answers | Example from our work |
|---|---|---|
| Business need | What problem or opportunity, for whom, by when? | Pricing must know before the effective date which items a new duty covers |
| System change | What must change in which system, tool, file or process? | A checked brief and model; effective-dated rate rows in [COMPANY: name of std-cost tool]; broker data, if a classification changes |
| Data | Which data proves it, and is it right? | HTS numbers as text, origin, effective dates, entry lines, cost elements |

Stop at layer 1 and you write wishes. Start at layer 2 and you build the wrong thing. Skip layer 3 and the change fails silently.

### 1.2 The two tracks as BSA work

- **Research (Hire A)** analyses an external change (a tariff or regulatory action) and turns it into a scope determination, the WHAT, in a Tariff-Impact Brief (`docs/templates/domain/tariff-impact-brief.md`): elicitation from sources and experts, analysis of scope rules, and requirements for everyone downstream.
- **Standard Cost (Hire B)** turns Research's determination and cost data into the $ and an Oracle cost update with Finance: data analysis, requirements for cost inputs, reconciliation, and checking that the update did what Finance agreed.
- **Both** own one custom tool by day 60 (M6) and will be core BSAs on the e2open project (M10): as-is documentation, data mapping, UAT (user acceptance testing). The boundary rule holds everywhere: Research owns the WHAT, Standard Cost owns the $ and never decides scope (`docs/01-30-60-90-plan.md` Section 1).

### 1.3 The translator

| Group | They speak in | They need from you | You need from them |
|---|---|---|---|
| Trade compliance (the Senior; brokers and counsel only through the Senior) | Legal text, HTS, origin, entries | Precise questions, item lists, evidence | Interpretation, confirmation, sources |
| Finance ([COMPANY: Finance cost accounting contact]) | Cost elements, periods, GL (general ledger) accounts, tolerances | Inputs that tie out; explained variances | Costing policy, calendar, sign-off |
| Business users (Purchasing, Pricing, Logistics) | Items, suppliers, prices, dates | Answers on time, in their words | The decision behind the request; volumes |
| IT and vendors (AS400 support, Power Platform admins, e2open) | Systems, fields, environments, tickets | Testable requirements; data maps | Feasibility, build, environments, fixes |

### 1.4 What a BSA is not

- **Not the lawyer.** You record "our working interpretation"; legal questions go through the Senior.
- **Not your own checker.** Every release gets a documented second-person review (maker-checker), after day 90 too.
- **Not the administrator.** Schema changes in the team database go through the Senior. Tool changes go through a change request (`docs/templates/bsa/06-change-request.md`), and there is no production write before the day-60 review.
- **Not the broker's contact, before day 60.** Questions for a customs broker, agente aduanal or trade counsel go through the Senior (or the Manager).

## 2. The discipline in one page

### 2.1 BABOK and the six knowledge areas

The reference for business analysis is the BABOK Guide (A Guide to the Business Analysis Body of Knowledge) from the International Institute of Business Analysis (IIBA). BABOK Guide v3 (2015) is still the current edition as of Oct 2026; IIBA also publishes a free, shorter Business Analysis Standard (v2.0, 2025) that summarizes it (check https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/). BABOK v3 has 6 knowledge areas, 30 tasks and 50 techniques. The knowledge areas "are not meant to imply a sequence": on a live tariff action you work in several at once.

| Knowledge area (BABOK v3) | What it means here | Our templates and tools | First taught |
|---|---|---|---|
| Business Analysis Planning and Monitoring | Plan the work: who to involve, how to triage, who checks | 01 Parts A–C; Jira epic (07); stakeholder list and elicitation plan (3.5, 4.6) | W2–W3 |
| Elicitation and Collaboration | Get information from people and documents, confirm it, keep people informed | 03 Part 3 (interviews); shadowing notes (`docs/03-check-ins-and-scorecards.md` Section 4); 01 Part D | W2 onward |
| Requirements Life Cycle Management | Trace, maintain, prioritize and approve requirements; manage changes | 02 change log and sign-off; MoSCoW; change request (06) | W3, W8 |
| Strategy Analysis | Understand the current state, define the future state, assess risks | 02 Section 1 (problem statement); as-is and to-be (03); e2open as-is (M10) | W4, W9–W13 |
| Requirements Analysis and Design Definition | Specify and model requirements; verify and validate them; define design options | Requirements (02); stories and acceptance criteria (07); data mapping (04); decision tables | W3, W7 |
| Solution Evaluation | Measure whether the solution delivers value; recommend actions | UAT evidence (05); post-implementation check (06 Section 12); closeout (08); SOP KPIs | W7–W8, W13 |

Numbers 01 to 08 are the templates `docs/templates/bsa/01-intake-request.md` to `docs/templates/bsa/08-project-closeout.md`.

Keep two BABOK words apart. **Verify** checks that requirements "meet quality standards and are usable for the purpose they serve". **Validate** checks that they "align to the business requirements and support the delivery of needed value". A requirement can be perfectly written (verified) and still be the wrong one (not validated).

### 2.2 The six core concepts

BABOK's Business Analysis Core Concept Model (BACCM) has six concepts. None is primary; each is defined by the others. Use them as a 2-minute check on every intake: a concept you cannot name is your first elicitation question.

| Concept | BABOK v3 definition | Example: fictional Action X-1 and KIT-100 |
|---|---|---|
| Change | "The act of transformation in response to a need." | Adding Action X-1 to our brief, model, rate table and, if needed, broker data |
| Need | "A problem or opportunity to be addressed." | Know before the effective date which items Action X-1 covers, so duty deposits, prices and standard costs are right |
| Solution | "A specific way of satisfying one or more needs in a context." | A checked brief, the shared Tariff-Impact Model and effective-dated rate rows |
| Stakeholder | "A group or individual with a relationship to the change, the need, or the solution." | Purchasing, Pricing, Finance, the Standard Cost BSA, the Senior, the broker (through the Senior) |
| Value | "The worth, importance, or usefulness of something to a stakeholder within a context." | A pricing decision made on time on the right item list; no surprise PPV (purchase price variance) next period |
| Context | "The circumstances that influence, are influenced by, and provide understanding of the change." | The effective date, CBP guidance, the AS400 being replaced by e2open, the boundary rule |

**How this applies to our work:** for Research the need is usually dated by someone else (the effective date); for Standard Cost the context includes Finance's cost calendar; for owned tools and e2open it includes what e2open will replace (`docs/templates/bsa/02-requirements.md` Section 3).

## 3. Stakeholders

### 3.1 Identify

Start from the intake record: Part A of `docs/templates/bsa/01-intake-request.md` already names the requester, downstream users, systems that could change, and the maker and checker. Then ask: who decides with the answer, and who pays if it is wrong? Who owns the data you will use or change ([COMPANY: data owners])? Who receives the output (a broker, Finance, Oracle, a report's users)? Who checks it and who approves release? And ask the requester: "Who else should I talk to?" The company's list of stakeholder groups is [COMPANY: stakeholder list].

### 3.2 Analyse: influence and interest

BABOK technique 10.43, "Stakeholder List, Map, or Personas", covers a stakeholder list, a stakeholder matrix, an onion diagram, a RACI matrix (3.3) and personas. A **stakeholder matrix** plots each stakeholder's influence against their interest; positions change over time, so redo it when the work changes. An **onion diagram** shows how close each group is to the solution, from people who use it directly out to people outside the company. **Personas** describe a typical user group.

| Influence and interest | Typical stakeholder here | How to engage |
|---|---|---|
| High influence, high interest | Pricing lead on a tariff action; Finance on a cost update | Involve early; agree the problem and success measures; review drafts; sign-off |
| High influence, lower interest | [COMPANY: trade compliance lead]; an IT system owner | Short, decision-ready updates; consult on anything in their area |
| Lower influence, high interest | Buyers; the users of a tool | Keep informed; ask for real examples and help with testing |
| Lower influence, lower interest | Teams that only read a report | General communication when something changes |

### 3.3 RACI for a tariff action

R = does the work; A = accountable (exactly one per row); C = consulted (two-way); I = informed (one-way). This is the default for a new tariff action; adjust it per action.

| Activity | Research BSA | Standard Cost BSA | Senior | Manager | Requester |
|---|---|---|---|---|---|
| Log, score and route the intake | R | I | I | A | C |
| Determine scope, rates and dates (the brief) | R | I | C | A | C |
| Check the brief before release | C | I | R | A | n/a |
| Model the $ on the checked brief | C | R | I | A | C |
| Draft the business communication (the Manager approves it before it goes out) | R | R | I | A | I |

The Senior is consulted on scope, not just informed, because the checker's questions change the brief. The Standard Cost BSA is only informed on scope because Standard Cost never decides it. The checker is never the maker.

### 3.4 Keep them informed

Acknowledge every request the same working day, and confirm scope, date, maker and checker within 1 working day (01 Part D, replies D1 and D2). Agree the update rhythm with high-interest stakeholders at intake ("next update: Wednesday 16:00") and keep it, even when the news is "no change"; say early when a date is at risk, with the new date and the reason. Put status where people look: the Jira issue first, then email or Teams with the Jira key in the subject. Tell users before and after any tool change (06 Section 11). Send supplier prices and margins only to people who need them (01 Part A, Sensitivity).

### 3.5 Your stakeholder list

Attach this to the Jira issue for your W3 intake. If the work grows into an epic, it becomes the stakeholder table in `docs/templates/bsa/02-requirements.md` Section 4.

| Stakeholder (name or [COMPANY: role]) | Role in this work | Influence and interest | What they need | How engaged | Contact rule |
|---|---|---|---|---|---|
| [Requester] | [Requester, user, data owner, checker, receiver] | [High, High] | [Decision and date] | [Interview, review, informed by email] | [Direct; or through the Senior] |

Done when every row says how the person is engaged, one person is accountable for the outcome, and every external party (broker, agente aduanal, counsel) has the contact rule "through the Senior" (before your day-60 review).

**How this applies to our work:** Research stakeholders change with each action (different item families and buyers), so build the list fresh at intake. For Standard Cost, Finance is high influence and high interest in every cycle. For an owned tool, the users and downstream receivers are the impact rows in 06 Section 4. For e2open, add the project team, the vendor and the data owners; the list feeds the as-is header (03 Part 1).

## 4. Elicitation

Elicitation means drawing out information from people and sources, then confirming you understood it. BABOK's Elicitation and Collaboration tasks start with preparing for elicitation, conducting it, and confirming the results (section 4.2 of this primer).

### 4.1 Techniques and when to use them

| Technique (BABOK v3 no.) | Use it when | Example here | Watch out for |
|---|---|---|---|
| Interviews (10.25) | You need one person's knowledge, decision or process | Requester at intake; doer and checker for an as-is map | Interviewing only the manager, not the person who does the work |
| Observation (10.31), also called job shadowing | People skip steps when they describe their work | Shadowing a research item or a cost load | Changing what you watch; save questions for pause points |
| Document Analysis (10.18) | The answer exists in writing | Federal Register notice, CBP CSMS (Cargo Systems Messaging Service) message, SOP, tool code, Jira history | Old documents; SOPs that differ from practice |
| Workshops (10.50) | Several groups must agree | e2open to-be steps with Research, Standard Cost and Finance | No agenda, no decision owner |
| Focus Groups (10.21) | You want ideas and attitudes from a group | Tool users on what a report should show | Treating opinions as requirements |
| Survey or Questionnaire (10.45) | Many people, short factual answers | Which reports each team uses, and how often | Leading wording; low response |
| Prototyping (10.36) | People react better than they describe | A mock-up of a Power BI page or an export layout | The prototype taken as the finished build |
| Brainstorming (10.5) | You need many options quickly | Possible causes of a recurring data break (6.3) | Judging ideas too early |

### 4.2 Prepare, conduct, confirm

| Step | What to do |
|---|---|
| Prepare | Write the session goal in one sentence and what you will produce. Read what exists first (intake, Jira history, SOP, tool doc, the notice). Pick the people: the requester for the decision; the doer and the checker for the process. Draft 5 to 8 questions and ask them to bring a real example (the file, the screen, last month's report). |
| Conduct | Open with the purpose and how you will use the notes. Walk through the last real instance, not the theory, and ask for numbers. Close with "Who else should I talk to?" and a playback date. For process interviews, use the question set and interview habits in 03 Part 3. |
| Confirm | Write up within 24 hours and send a recap (4.4). Play back maps and requirements to the person who gave them, correct them, then record "Validated by" with name and date. Turn reusable answers into an SOP line, glossary entry or Anki card within 2 working days. |

### 4.3 Asking good questions

| Type | Use it to | Example |
|---|---|---|
| Open | Start a topic and let them talk | "What happens when a new tariff notice reaches you?" |
| Probing | Get under a vague answer | "You said 'usually'. When does it not go that way? What was the last exception?" |
| Show me | See what really happens | "Show me the file you used last time and where that number came from." |
| Numbers | Size the problem | "How many times a month? How long each time?" |
| Closed | Confirm a fact at the end | "So the checker is always the Senior, never the Manager?" |

Avoid leading questions. They put your answer in the other person's mouth, and people agree to be polite.

| Leading (avoid) | Neutral (use) |
|---|---|
| "You check the HTS list against the annex, right?" | "How do you check the HTS list before it goes out?" |
| "Wouldn't it be better if the tool stored effective dates?" | "How do you find the rate that applied last quarter?" |
| "The broker always uses our code, doesn't it?" | "How do you know which code the broker filed?" |

### 4.4 Confirm in writing

After every session that produced a fact, a decision or a requirement, send a short recap and paste it on the Jira issue. Silence is not agreement for anything that changes scope, a rate, a date or a cost: get a reply.

> Subject: [Jira key]: notes from our call on [date]
>
> Thanks for your time. What I understood: [3 to 5 bullets: facts, numbers, decisions]. Open questions: [list, with who answers each]. Next step: [what I will do, by when]. Please correct anything I got wrong by [date].

### 4.5 Working with experts

- **The Senior** (customs, trade compliance, data and analytics) is your main expert and checker. Batch non-urgent questions for office hours or the next session, and say what you already tried (`docs/03-check-ins-and-scorecards.md` Section 2).
- **Brokers, the agente aduanal and trade counsel:** before the day-60 review you never contact them yourself. Write the question (item, source, what you think and why) and give it to the Senior (or the Manager). After day 60, with the Senior's agreement, you may email the broker with the Senior copied.
- **Finance** ([COMPANY: Finance cost accounting contact]): ask for the policy behind a number, not just the number; confirm tolerances in writing.
- **IT and vendors** (AS400 support, Power Platform admins, e2open consultants from W12): ask how it works and what would change it. Vendor claims are marketing until confirmed in writing (`docs/primers/trade-systems-gtm-e2open-primer.md` Section 5.2).
- **Copilot Chat** (M11) can help draft a question list or a recap, within [COMPANY: AI acceptable-use policy] (`docs/primers/copilot-chat-guide.md`). It is not an expert: never cite it as the source of a regulatory fact, an HTS number or a rate.

### 4.6 Your elicitation plan

Attach this to the Jira issue for your W3 intake, next to the stakeholder list (3.5).

| Who | What you need to learn | Technique | When | How you will confirm it |
|---|---|---|---|---|
| [Requester] | [The decision, the date, the scope] | [Interview, 30 min] | [Date] | [Recap email; reply received] |
| [Doer or data owner] | [Where the data lives; how it is checked] | [Observation; document analysis] | [Date] | [Playback] |

**How this applies to our work:** in Research, document analysis of primary sources is your main technique, and the Senior confirms interpretation. In Standard Cost, observe a real cost cycle with Finance before you write any requirement for it. For an owned tool, interview the knowledge holder, then observe a run; the tool doc is your confirmed result. For e2open, interview the doer and the checker for your as-is document (A90-2, B90-2), and expect workshops from W12.

## 5. Requirements

### 5.1 Four types

BABOK v3 sorts requirements into four types. Writing them separately stops anyone from designing a solution before the need is agreed.

| Type | BABOK v3 meaning | Example (fictional Action X-1) |
|---|---|---|
| Business | "Statements of goals, objectives, and outcomes that describe why a change has been initiated." | Before the effective date, the business knows which active items Action X-1 covers |
| Stakeholder | "The needs of stakeholders that must be met to achieve the business requirements." | The Purchasing category manager needs the in-scope item list, with the reason for each item, 2 working days before the pricing meeting |
| Solution, functional | "A capability that a solution must have in terms of the behaviour and information the solution will manage." | The candidate query shall return every active item whose US HTS number begins with an annex prefix and whose origin is Country X |
| Solution, non-functional | Conditions under which the solution must remain effective, or qualities it must have; usually measurable | The candidate query shall return its result in under 2 minutes on the full active-item extract |
| Transition | What is needed to move from the current state to the future state; temporary | Before e2open cutover, classification history for active items is migrated and reconciled to the AS400 counts (04 Part 7) |

A **business rule** is not a requirement. A rule holds whatever the system. For example, BR-01 in the 02 example: a US import is dutiable at the rate in effect at the time of entry (or withdrawal from warehouse for consumption), unless the action itself says otherwise. A requirement says what the system does about it. Keep rules in 02 Section 6, each with a source and an owner: Research for scope, rates and dates; Finance for costing policy.

### 5.2 Quality: weak and strong

The nine characteristics below are the ones commonly listed from BABOK v3 task 7.2 (Verify Requirements). Use them as your own check before any review.

| Characteristic | Weak | Strong |
|---|---|---|
| Atomic | "The tool shall store rates and email the broker." | Two requirements, one behavior each |
| Complete | "Show the duty." | "Show duty per unit before and after the action for each in-scope item." |
| Consistent | One requirement uses the PO date; BR-01 says the entry date | Both use the date of entry (or of withdrawal from warehouse for consumption) |
| Concise | Three sentences of background inside the requirement | Background in the problem statement; one sentence here |
| Feasible | "Update rates automatically from every government source." | "Load rates from a checked brief." Content feeds: Won't (this time) |
| Unambiguous | "Recent entries" | "Entries dated 2026-07-01 to 2026-09-30" |
| Testable | "The report should be fast." | "The report refreshes in under 5 minutes for 12 months of entries." |
| Prioritized | No priority | A MoSCoW priority on every row (5.5) |
| Understandable | "Apply X99 logic to SPI-flagged rows." | Plain words; any term defined in the glossary |

The one-sentence form from `docs/templates/bsa/02-requirements.md`: "The [tool, report or process] shall [behavior] [condition]." If it contains "and", it is probably two requirements.

### 5.3 User stories and INVEST

A user story states a need from the user's side: "As a [role], I want [deliverable or capability], so that [decision or benefit]." The team's story template and definition of ready are in `docs/templates/bsa/07-jira-epic-story.md`. Check each story against INVEST (Bill Wake, 2003):

| Letter | Meaning | Check on our stories |
|---|---|---|
| I, Independent | Can be delivered on its own (mostly) | WHAT and $ are separate, linked stories; the Research story blocks the Standard Cost story |
| N, Negotiable | A starting point for a conversation, not a contract | Scope in and scope out agreed with the requester |
| V, Valuable | Matters to someone who cares about the result | The "so that" names a decision |
| E, Estimable | Can be sized well enough to plan | Inputs and sources are named and accessible |
| S, Small | Hours to days of work | 5 working days or less, or split it |
| T, Testable | "Given any inputs, we can agree on the expected system behavior and/or outputs." | Given/When/Then acceptance criteria with real data |

### 5.4 Acceptance criteria: Given/When/Then

Given/When/Then was proposed by Dan North and Chris Matts in 2004 as part of behaviour-driven development, and it is the pattern of the Gherkin language (cucumber.io). **Given** puts things in a known starting state, **When** is the action or event, **Then** is an outcome someone can observe. Each criterion gets an ID (AC1, AC2). The rules in 07: one behavior per criterion; concrete data (an item, an HTS number, a date, a value); at least one edge case where dates or validation are involved; never "works correctly" or "as expected". 07 has weak and strong examples ("A bad example, rewritten"). An effective-date edge case looks like this: "AC2 Given an entry dated the day before the effective date, when duty is calculated, then the additional duty is not applied."

For Mexico-based stakeholders, Gherkin keywords exist in Spanish: Dado, Cuando, Entonces.

### 5.5 MoSCoW

MoSCoW comes from DSDM, an agile project framework published by the Agile Business Consortium. It ranks requirements inside one change or release. The meaning and test for each priority are in the MoSCoW table of `docs/templates/bsa/02-requirements.md`. DSDM adds two points worth remembering: together, the Must Haves are the Minimum Usable SubseT (test: if one is not delivered, would we cancel or refuse to go live?), and "Won't Have this time" is written down so the item is not quietly reintroduced. Could Haves are the first to drop when the date is at risk.

DSDM's guidance is that Musts take no more than about 60% of the effort and Coulds about 20%, which leaves contingency. If everything is a Must, nothing is. Do not mix up the team's three schemes: P1, P2 and P3 rank requests (`docs/05-time-management.md`); MoSCoW ranks requirements within one change; PP1, PP2 are pain-point IDs in a process map (03).

### 5.6 Traceability

BABOK task 5.1, Trace Requirements, exists "to ensure that requirements and designs at different levels are aligned to one another, and to manage the effects of change to one level on related requirements." In practice you keep a traceability matrix: a table linking each requirement back to its source and forward to its story, test and release (columns: requirement, source, story and AC, test case, result, release; a filled row is in Part 10). Trace both ways. Backward finds requirements nobody asked for; forward finds requirements nobody built or tested. Keep it in the requirements document or on the Jira epic. For a small change, the story's acceptance criteria plus the change request's test table (06 Section 6) are the trace. UAT cases start from the acceptance criteria (`docs/templates/bsa/05-uat-test-plan.md`).

### 5.7 When requirements change

Requirements change: a notice is amended, Finance changes a policy, a test exposes a misunderstanding. Handle every change the same way:

1. Log it on the Jira issue with its source: who, when, why.
2. Use the trace matrix to find what it touches: other requirements, stories, tests, data maps, the tool doc.
3. Assess the impact with the requester and re-apply MoSCoW; something may move to Won't this time.
4. After version 1.0, record it in the change log and get it re-approved (02 Sections 13 and 14).
5. A change to a tool, a configuration or production data goes through a change request (06), made and tested in a test copy. You have no production write access before the day-60 review: whoever holds production rights today implements the approved change.
6. Tell everyone who received the earlier version. Research: an amended action means a new brief version, re-checked and re-sent to Standard Cost.

**How this applies to our work:** the Research brief is a requirements document for everyone downstream, and every WHAT claim needs a primary source, just as every requirement needs a source. In Standard Cost, Finance's costing rules are business rules, and your cost input file has acceptance criteria (row counts and totals tie out). For an owned tool, the W8 change request is a small requirements-to-test loop: write the acceptance criteria before you change the test copy. On e2open, the project will trace to-be requirements to UAT cases, so build the habit now.

## 6. Analysis and modeling

### 6.1 Process models and data maps

- **Process models** (`docs/templates/bsa/03-process-map-as-is-to-be.md`): the SIPOC (suppliers, inputs, process, outputs, customers) fixes where the process starts and ends; the step table is the source of truth; the swimlane is drawn from the table. Give every control an ID (C1) and every pain point an ID (PP1), with evidence. Map what really happens, workarounds included, before you design the to-be. For the system view, use `docs/primers/trade-systems-gtm-e2open-primer.md` Section 7.
- **Data maps** (`docs/templates/bsa/04-data-mapping-spec.md`): field by field, how data moves from a source to a target, with the transform rule, the quality rule, the value cross-reference and the reconciliation. Profile the source before you map it, because real values beat field names. HTS numbers are text, the right length per country, with leading zeros kept.

### 6.2 Decision tables

A decision table (BABOK 10.17, Decision Modelling) shows how a decision is made: each row is a rule, each column a condition, and when all of a rule's conditions are true, its outcome applies. Use one whenever scope, stacking or exclusion logic has more than two conditions. It makes gaps and overlaps visible, and each row becomes a test case. Example for fictional Action X-1; the rules are invented, and a real action's rules come from its notice and the checked brief:

| Rule | HTS on the annex? | Origin Country X? | Entered on or after the effective date? | On the exclusion list? | Action X-1 duty applies? |
|---|---|---|---|---|---|
| R1 | Yes | Yes | Yes | No | Yes |
| R2 | Yes | Yes | Yes | Yes | No |
| R3 | Yes | Yes | No | Any | No |
| R4 | Yes | No | Any | Any | No |
| R5 | No | Any | Any | Any | No; list borderline items (such as a kit containing an annex part) for the Senior |

Check every decision table for completeness (each combination of inputs falls under exactly one rule) and for conflicts (two rules giving different outcomes for the same inputs). Whether a new duty adds to other duties (stacking) is a separate decision with its own table, owned by Research.

### 6.3 Root cause analysis for ad-hoc investigations

The BABOK glossary defines a root cause as "the cause of a problem having no deeper cause, usually one of several possible causes" (technique 10.40, Root Cause Analysis). Use **5 Whys** (keep asking "why?" until you reach a cause you can act on; five is typical, not a rule) and the **fishbone diagram** (also called an Ishikawa or cause-and-effect diagram, named after Kaoru Ishikawa): list possible causes by category (BABOK's example categories are people, processes, tools and policies), then run 5 Whys on the likely branches. Verify each cause with data before you call it the root cause.

Fictional example of the A60-3 type: duty paid on an entry line for PART-A is higher than expected.

1. Why? The broker filed PART-A under a different HTS number from our master.
2. Why? The broker's product file still had the old number.
3. Why? The classification changed in the AS400 after that night's broker file had run, and the shipment was entered the next morning.
4. Why did nobody catch it? Nothing checks that a classification change has reached each broker file.
5. Why? The control was never designed: the SOP says "update the broker" with no evidence step.

The root cause is a missing control, not a person's mistake. Recommend a control with evidence (03 Part 5) and give the finding to the Senior; any correction of a past entry is filed by the broker on [COMPANY: trade compliance lead]'s decision.

**How this applies to our work:** Research uses decision tables for scope, stacking and exclusions and root cause for ad-hoc investigations (A60-3). Standard Cost uses 5 Whys on the top PPV drivers (B60-3) and a data map for cost inputs (B90-3). An owned tool's process model and data sources go in its tool doc (`docs/templates/knowledge/tool-doc.md`). For e2open, the as-is document and data map are your day-90 evidence (A90-2, A90-3, B90-2, B90-3).

## 7. Solution evaluation

### 7.1 Did it deliver value?

In BABOK, Solution Evaluation means measuring how a solution performs, analysing the measures, and recommending actions to increase its value. A change that passed UAT can still fail here: the brief went out on time but Pricing could not use the item list; the tool works but users kept their own spreadsheet. When a measure misses its target, ask where the limit is: in the solution (a defect, a missing feature, a slow run) or around it (no time to use it, unclear ownership, a policy, missing training). Recommend the smallest action that closes the gap, as a Jira issue with an owner. Before e2open, keep fixes small and say whether e2open will replace them (02 Section 3).

### 7.2 Measures

Set measures before you build, in 02 Section 2 (objective, measure, baseline, target, how and when measured). Once the process has an SOP, use its KPIs (`docs/templates/knowledge/process-sop.md` Section 10). You practise KPI design in Exercise 9 of `docs/analytics/practice-exercises.md` (W7).

| Kind | Example | Source |
|---|---|---|
| Timeliness | Checked brief released before the date the requester needed it | Jira dates |
| Quality | Material errors found after release (target 0) | 30-day look-back; closeouts |
| Control | Releases with a documented checker sign-off (target 100%) | Jira comments; sign-off blocks |
| Efficiency | Hours per action or per cost cycle, before and after | Self-reports; Jira |
| Adoption | Users running the new version, not their own copy | Tool run log; ask the users |

### 7.3 The closeout

Write a closeout (`docs/templates/bsa/08-project-closeout.md`) within 5 working days of the last child issue: objectives against results with data, deliverables and their new owners, controls evidence, documentation updated, open items with owners, and lessons learned as Keep, Stop and Start. A closeout that only says "delivered" is not an evaluation.

**How this applies to our work:** Research runs a 30-day look-back for material errors after release. Standard Cost ties out the post-load reconciliation with Finance. An owned tool gets a post-implementation check after its first production run (06 Section 12). On e2open, parallel-run comparisons and UAT evidence decide go-live (05, scenario TS-09).

## 8. Where analytics fits

BSAs use data at every step, not only in reports. Profiling **finds** the problem (unmatched entry lines, blank origins, 9-digit HTS numbers). Counts **size** it: "2 of the last 5 actions were logged late" beats "often", and counts, hours and $ ranges set priority (01 Part B). A query **tests** a requirement against reality before you write "all active items have an origin". Reconciliations and tie-outs **prove** the result (04 Part 7; `docs/templates/domain/standard-cost-update-checklist.md`).

Where to go next:

- The M3 practice pack, Exercises 1–8 (`docs/analytics/practice-exercises.md`, W1–W4), then the analytics depth Exercises 9–11 in the same file (W7–W9): KPI design, a Power BI star-schema model with DAX measures, and basic statistics for variance work. The answer key is trainer-only.
- Where the team's data lives and the safe-use rules (your personal login for all interactive work, Oracle EBS read-only, loads only into [COMPANY: sandbox or staging schema in the team database], no schema changes): `docs/primers/data-platform-primer.md`.
- How a requirement becomes a tested, released change (environments, test levels, release and rollback): `docs/primers/sdlc-primer.md`, in W5–W6.

## 9. Growing as a BSA

### 9.1 IIBA certifications (as of Oct 2026)

| Certification | Experience required | Exam | Typical audience (IIBA) |
|---|---|---|---|
| ECBA | None | 50 questions, 75 minutes, online remote proctored (the format for English exams since 21 July 2025) | Entry level and career changers |
| CCBA | 3,750 hours of BA work in the last 7 years; 21 professional development hours in the last 4 years; 2 references | 130 questions, 180 minutes | About 2–3 years of experience |
| CBAP | 7,500 hours in the last 10 years; 35 professional development hours in the last 4 years; 2 references | 120 questions, 210 minutes | 5 or more years of experience |

Check the current rules at https://www.iiba.org/business-analysis-certifications/ before planning anything. Fees change and are not printed here: see https://www.iiba.org/business-analysis-certifications/certification-fees/ (as of Oct 2026). Certification is optional and is not part of this program's criteria. [COMPANY: confirm whether certification fees are sponsored].

### 9.2 Reading list and habits

| What | Why | Where |
|---|---|---|
| BABOK Guide v3 (IIBA, 2015) | The full reference: knowledge areas, tasks and 50 techniques | https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/ |
| The Business Analysis Standard v2.0 (IIBA, 2025) | Free, about 60 pages; the short version | https://www.iiba.org/business-analysis-blogs/the-updated-business-analysis-standard-your-foundation-for-success/ |
| Bill Wake's INVEST article (2003) | Where INVEST comes from | https://xp123.com/invest-in-good-stories-and-smart-tasks/ |
| User Stories Applied (Mike Cohn, 2004) | The classic book on user stories | Book |
| MoSCoW prioritisation (Agile Business Consortium) | The DSDM definitions | https://www.agilebusiness.org/dsdm-project-framework/moscow-prioritisation.html |
| Gherkin reference (Cucumber) | Given/When/Then keywords and rules | https://cucumber.io/docs/gherkin/reference/ |
| Fishbone diagram (ASQ) | Cause-and-effect diagrams with 5 Whys | https://asq.org/quality-resources/fishbone |

Habits that build the skill: after every elicitation session, send the recap, update the question log and write 2 Anki cards; teach one BA technique at a Friday teach-back before day 60 (`docs/templates/knowledge/teach-back.md`); keep a pre-check list built from the checker's findings on your work, and read it before every submission.

## 10. Worked example: a Research intake for Action X-1 on KIT-100

Everything here is fictional: Action X-1, Country X, KIT-100, PART-A to PART-C and the timing. It shows the method end to end, not a real notice.

**The request.** On a Monday in W3 or later, [COMPANY: Purchasing category manager] emails: "Heard there's a new US duty on Country X parts. Does it hit KIT-100? Pricing meets in three weeks." A Federal Register notice published that morning adds an additional duty on goods of listed 8-digit HTSUS subheadings from Country X, for goods entered (or withdrawn from warehouse) for consumption on or after 12:01 a.m. eastern time, 20 business days later. With more than 15 business days' lead time, Hire A is maker on the normal cycle and the Senior is checker (`docs/01-30-60-90-plan.md` Section 7). KIT-100 is imported as one item under its own HTS number, which is not on the annex. PART-A, one of its components, is also imported on its own as a spare, and its subheading is on the annex.

**Stakeholders (Part 3).**

| Stakeholder | Role | Influence and interest | How engaged |
|---|---|---|---|
| [COMPANY: Purchasing category manager] | Requester | High, High | Interview at intake; D2 reply; recap |
| [COMPANY: Pricing lead] | Decides prices on the result | High, High | Informed at each update; receives the communication |
| Hire B (Standard Cost) | Receives the checked brief for the $ | Medium, High | Informed; linked story, blocked by the Research story |
| Senior | Checker; expert on borderline items | High, High | Consulted on KIT-100; checks the brief |
| Manager | Accountable; approves release | High, High | Confirms priority; approves the communication before it goes out |
| Customs broker | Files the entries | Low, Medium | Only through the Senior, and only if a classification changes |

**Two interview questions (Part 4).**

1. To the requester (open, about the decision): "Walk me through the decision you will make with this answer. Which items, by what date, and what happens if an item is missing from the list?"
2. To [COMPANY: item data owner] or the Manager, with the extract open (show me): "Show me KIT-100 and PART-A in the classification master: the US HTS number, the origin, when each was set, and where the rationale is kept."

**Requirements of different types, with MoSCoW (Parts 5.1 and 5.5).** The three Musts are the minimum usable subset; FR-3 is written down so it is not lost. (BUS- is used for business requirements here because BR- IDs belong to business rules in 02.)

| ID | Type | Requirement | MoSCoW | Source |
|---|---|---|---|---|
| BUS-1 | Business | Before the effective date, the business knows which active items Action X-1 covers, with the legal basis for each | Must | Requester email; the notice |
| SR-1 | Stakeholder | The Purchasing category manager receives the in-scope item list, with the scope reason for each item and borderline items flagged, 2 working days before the pricing meeting | Must | Intake interview |
| FR-1 | Solution, functional | The candidate query shall return every active item whose US HTS number, compared as 10-digit text, begins with an annex prefix and whose origin is Country X | Must | Notice annex; PP3 in the 03 example |
| FR-2 | Solution, functional | The candidate query shall list every kit whose bill of materials contains a candidate item, as borderline items for the Senior | Should | Senior; workaround is a manual kit list ([COMPANY: where kit structures live]) |
| FR-3 | Solution, functional | The annex list shall load automatically from the Federal Register | Won't (this time) | Deferred to e2open |

A first version of the candidate query. Table names are examples, not real objects: `stg.` stands for [COMPANY: sandbox or staging schema in the team database], where the AS400 item extract and the annex list are loaded. It reads only those copies, never a production system.

```sql
-- Candidate items for Action X-1 (fictional). Compare HTS as text:
-- both columns hold digits only (no dots), with leading zeros kept.
SELECT DISTINCT i.item_no, i.hts_us, i.origin_country
FROM stg.item_extract AS i          -- (example name)
JOIN stg.annex_prefix AS a          -- (example name)
  ON i.hts_us LIKE a.prefix + '%'
WHERE i.item_status = 'ACTIVE'
  AND i.origin_country = 'XX';      -- Country X (fictional code)
```

**The story (Parts 5.3 and 5.4),** in the format of `docs/templates/bsa/07-jira-epic-story.md`. The timing and stacking criteria of 07 Example 1 also apply; they are left out here to keep the example short.

```text
STORY: Research: Tariff-Impact Brief for Action X-1 (fictional) on Country X goods
As the Purchasing category manager and the Standard Cost BSA, I want a checked brief
stating which of our items Action X-1 covers, at what rate and from when, so that
pricing and the $ impact can be decided before the pricing meeting.
Context: Federal Register notice [citation], published [date]. Intake [key].
Scope in: US imports; annex subheadings; origin Country X; active items.
Scope out: Canada and Mexico; $ impact (Standard Cost story, blocked by this one).
Inputs and sources: the notice and annex; item extract dated [date] in the staging
schema; the Senior on borderline items.
Acceptance criteria:
AC1 Given the item extract dated [date] and the annex prefixes, when the candidate
    query runs, then every active item whose HTS (as text) begins with a prefix and
    whose origin is Country X is listed exactly once, PART-A included.
AC2 Given KIT-100 contains PART-A but its own HTS number is not on the annex, when the
    brief is complete, then KIT-100 is listed as borderline with a one-line note and
    the Senior's decision.
AC3 Given the boundary rule, when the brief is reviewed, then it contains no $ figures.
AC4 Given the checker review, when the story moves to Done, then the Senior's comment
    records name, date, brief version and findings, all closed.
Maker / Checker: Hire A / Senior
Due: [date] because the pricing meeting is on [date] and SR-1 needs the list 2 working
days before it.
Deliverable location: [COMPANY: briefs folder]
Ready checked by: [Name, date]
```

**The test it traces to (Part 5.6).** Before the query result is used, Hire A runs it on a small test file and saves the evidence for the Senior. The trace row links the requirement to the test and the release.

| ID | Steps | Expected | Actual | Pass/Fail |
|---|---|---|---|---|
| TC-01 | Pre: test rows PART-A (annex prefix, origin Country X); PART-B (annex prefix, origin Country Y); PART-C (annex prefix starting with 0, origin Country X); KIT-100 (not on the annex). 1. Run the candidate query. | PART-A and PART-C returned once each, with 10-digit HTS numbers; PART-B and KIT-100 not returned | [Values; evidence file TC-01_[date]_HA] | [Pass, Fail] |

| Requirement | Source | Story and AC | Test case | Result | Release |
|---|---|---|---|---|---|
| FR-1 | Notice annex; PP3 | Research story, AC1 | TC-01 | [Pass, date, evidence file] | Brief v1.0, [date] |

**Afterwards (Part 7).** The closeout records whether the checked brief went out before the pricing meeting, the Senior's findings, and the 30-day look-back (target: no material errors). The Standard Cost story takes the $ from brief v1.0.

## 11. Self-check questions

| No. | Question | Where to check |
|---|---|---|
| 1 | Describe one piece of your track's work as need, system change and data. | 1.1 |
| 2 | Name the six BABOK knowledge areas and one team template for each. | 2.1 |
| 3 | What is the difference between verifying and validating a requirement? | 2.1 |
| 4 | Name the six BACCM core concepts and give a trade example of each. | 2.2 |
| 5 | Place the stakeholders of your W3 intake on an influence and interest grid. Who needs close engagement? | 3.2, 3.5 |
| 6 | In the tariff-action RACI, why is the Standard Cost BSA only informed on scope? | 3.3 |
| 7 | When would you use observation instead of an interview? Give an example from your track. | 4.1 |
| 8 | Rewrite "You check the annex, right?" as a neutral question. | 4.3 |
| 9 | A broker's answer would settle a scope question. What do you do before day 60? | 4.5 |
| 10 | Give one example of each of the four requirement types for a standard cost update. | 5.1 |
| 11 | Rewrite "the report should be fast" as a testable requirement. | 5.2 |
| 12 | Write a Given/When/Then criterion that includes an effective-date edge case. | 5.4 |
| 13 | What is the difference between MoSCoW, P1–P3 and PP1? | 5.5 |
| 14 | A notice is amended after your brief was released. Which steps follow, in order? | 5.7 |
| 15 | Build a decision table for an action with an exclusion list. How do you check it is complete? | 6.2 |
| 16 | Run 5 Whys on a recent data error in your track. Is the root cause a person or a control? | 6.3 |
| 17 | Name three measures that show a released change delivered value. | 7.2 |
