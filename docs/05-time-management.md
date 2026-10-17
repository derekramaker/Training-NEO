# Time Management for New BSAs

Last updated: 2026-10-17 · Owner: BSA Manager

- **Purpose:** a working method for planning a week, handling intake and interruptions, protecting learning time, and saying "not by then" without damaging trust. Includes copy-paste templates and three practice scenarios.
- **Who uses it:** both hires every day, and the Manager in the Monday confirm and Friday 1:1. Part of module M0.
- **When:** read it on Day 1 (Mon 10/19, 15:00-15:45). The Wed 10/21 ways-of-working session puts it into practice. Re-read the scenarios before Week 6, when the first exports backlog items arrive.

## Why this matters here

About 5-8 of your 40 hours a week are guided by the Manager or the Senior (about 9-10 in W1-W2, about 5 in W10-W13). The other 32-35 are yours to plan: self-study, shadowing, documentation and, later, real work. Both trainers have small, fixed budgets (Manager 8 h a week across both of you, Senior about 4.5 h), so a badly timed question or a missed review slot costs more than it would on a bigger team.

The work also has hard dates you don't control: tariff effective dates, the Finance cost cycle, broker cut-offs, the e2open kickoff (expected W12). The habits below are about seeing those dates early and saying clearly what will and will not be done.

## The rhythm at a glance

| When | Ritual | Time | Output |
|---|---|---|---|
| Every morning | Anki review, then write the daily top-3 | 15 min + 5 min | Reviews done; top-3 in the daily plan |
| Tue-Fri 08:15 | Stand-up with the other hire (no trainer) | 10 min | Top-3 and blockers shared; blockers sent to the Manager in Teams |
| Every day | Two focus blocks | 2 x 90 min | Named self-study or work item moved forward |
| Every day, 16:45 | Daily wrap | 15 min | Question log updated; notes tidied; tomorrow's top-3 drafted |
| Once a week (from W3: Wed 15:00; none in W5, W6, W9, W10, W11) | Senior office hours | 30 min | Batched questions answered; answers turned into cards or notes |
| Friday morning (holiday Fridays: the last working day) | Friday self-report and next week's plan | 60 min, due 11:30 | Self-report (format below) and weekly plan sent to the Manager, copy to the Senior |
| Friday 13:00 (Hire A) or 13:45 (Hire B); holiday Fridays: the last working day | 1:1 with the Manager | 45 min (30 min in W5, W6, W9-W11, W13) | Plan agreed; actions noted (`docs/03-check-ins-and-scorecards.md`) |
| Monday 08:15 | Monday confirm with the Manager | 15 min | Plan confirmed or adjusted for anything new |

Holiday Fridays: when Friday is not a working day (W6 Fri 11/27, assumed off; W10 Fri 12/25; W11 Fri 1/1), the self-report, the 1:1s and the teach-back (W10 only) move to the last working day of that week ([COMPANY: confirm holiday calendar]). In W6 that is Wed 11/25, with the 1:1s at 15:00 (Hire A) and 15:30 (Hire B). The rule is in the standard week, Section 5 of `docs/01-30-60-90-plan.md`.

## Weekly planning ritual

### Friday plan (30 of the 60 minutes on Friday morning)

1. Open next week's page in `docs/02-weeks-1-2-schedule.md` (W1-W2). From W3, open the week's row in Section 3 of `docs/01-30-60-90-plan.md` and the standard week in its Section 5, plus that week's self-study list and Knowledge Topics rows. Copy the fixed commitments into your weekly plan: sessions, 1:1, office hours, shadows, deadlines.
2. Check Jira and Planner for anything due next week or already late.
3. Pick **three outcomes** for the week. An outcome is finished, reviewed and posted, not "work on X". Good: "Exercise 4 posted and reviewed". Not good: "Analytics".
4. Put every self-study block and work item into a time slot. Each one names a file and an output.
5. Capacity check: add up the planned hours. Leave **15% unplanned** (about 6 hours of a 40-hour week) for interruptions, reviews that come back with changes, and things you didn't know about.
6. Book every review you need now. If an item needs maker-checker review on Thursday, put the 30-minute review request on the reviewer's calendar on Friday, not on Thursday afternoon.
7. Write down the learning/doing split you planned (see the phase table below).

Copilot Chat may turn your notes into a first draft of the plan or rank your question batch (`docs/primers/copilot-chat-guide.md` 4.10). You still choose the three outcomes, the hours and the reviews, and you do the capacity check yourself.

### Monday confirm (15 minutes with the Manager)

- Walk through the three outcomes and the fixed commitments.
- Name anything that changed since Friday: a new request, a tariff notice, a cancelled session.
- Leave with one of two answers: "plan confirmed" or "plan changed: X drops, Y is added". Update Planner straight away.

## Daily top-3

- Write the top-3 before opening email. At least one is a learning item and, from W3, at least one is a doing item.
- Size each item to what fits in a focus block or two. "Finish the US/CA/MX comparison table" fits; "learn Mexico customs" does not.
- At the 16:45 wrap, mark each item done, moved (and to when), or dropped (and who agreed). Two days in a row with the same unfinished top-3 item is a signal: raise it with the Manager in Teams, or at the Monday confirm or 1:1.

## Intake triage: where work goes

Rule of thumb: **if someone else is waiting for it, or it will need a review, it goes in Jira.**

| What comes in | Where it lives | Rule |
|---|---|---|
| A work request from a stakeholder (research question, cost question, data pull, report, tool fix or enhancement) | Jira | Log it before you start, using the fields in `docs/templates/bsa/01-intake-request.md`. Reply to the requester with the issue key |
| Your graded documentation deliverables (tool docs, SOPs, as-is docs) | Jira, as stories under your onboarding epic | So the review is traceable |
| Learning tasks, reading, teach-back prep, access follow-ups | Planner ("BSA Onboarding" plan) | One task per item with a due date; the Manager can see it |
| A quick factual question you can answer in under 15 minutes, with nothing produced | Email or Teams reply | Answer it. If it grows, log it in Jira and reply with the key |
| A decision or approval that arrives by email or Teams | Jira comment, with the message linked or pasted | Email is not the record |
| A question you have for someone else | Question log (OneNote) | Batch it; ask at office hours or the 1:1 unless it passes the "ask now" test |
| A new tariff or regulatory action | Jira (Research), and tell the Manager within 30 minutes | See scenario 1 |
| A change to a tool, data or system | Jira plus a change request (`docs/templates/bsa/06-change-request.md`) | Never without change control. No production write access before day 60: changes to your owned tool are drafted and tested in a test copy until the day-60 review |

### How to log a request (about 10 minutes)

1. Capture the request in the requester's own words. Paste the email or message.
2. Fill in the intake fields: requester, date received, the decision it supports, due date and **why** that date, scope (countries, items, HTS, cost period), data needed, track (Research, Standard Cost, Exports, Reporting, Tools), reviewer for maker-checker, first size estimate.
3. Check the boundary rule. If it asks "what is the tariff action and which items does it cover?", that is Research (the WHAT). If it asks "what does it do to cost or margin?", that is Standard Cost (the $). Many requests need both: split them into two linked issues.
4. Set a priority (table below) or ask the Manager to.
5. Reply within the same working day: "Logged as [KEY]. I'll confirm a date by [time]." Then confirm the date.

### Priority

| Priority | Meaning | Examples | Who sets it in days 1-60 |
|---|---|---|---|
| P1 | Legal or effective-date driven, or wrong data could reach a broker, Finance or a system today | A tariff action effective in days; a classification error found on items shipping this week | The Manager. Tell them at once |
| P2 | A dated business need this week | Finance needs a cost answer for a pricing meeting; a cost-cycle input is due | Manager confirms; the Senior can stand in if the Manager is out |
| P3 | Improvement, backlog, learning-related | A tool doc, a report tweak, a data cleanup idea | You propose; the Manager agrees in the Monday confirm |

In days 1-60, never accept a P1 or P2 deadline on your own. Say "I'll confirm by [time]" and check with the Manager first.

## Timeboxing self-study

- Every self-study block in the schedule names a file and an output. Start by skimming the headings for 5 minutes and writing the one question you want the block to answer.
- Work in 45-50 minute sprints. Use the last 5-10 minutes of each one to write three lines in OneNote: what I learned, what is unclear (goes into the question log), card candidates (go into Anki).
- **Stuck rule:** after 15 minutes stuck on one point, log it in the question log with what you tried, and move on to the next part.
- **Stop rule:** when the block ends, stop. Write a "next step" note so you can restart quickly. You may borrow up to 15 minutes from the next block, never more. Anything unfinished goes on the Friday self-report.
- One primer section per block. Reading a whole primer in one sitting doesn't stick; the Anki cards and teach-backs do.
- Anki comes first each morning and takes 15 minutes. Skipping two days doubles the backlog; protect it.

## Interruptions, the question log and office hours

The question log saves trainer time. A batched question with "tried so far" filled in usually takes 2 minutes to answer. The same question asked cold in chat, mid-task, costs both people 15.

### The "ask now" test

Ask straight away (Teams message or a walk over) if **any** of these is true. Otherwise put it in the question log.

1. Wrong data could go to a broker, Finance, a customer or a system today.
2. A dated deliverable (effective date, cost cycle, deadline) is blocked and nothing else on your plan can move forward.
3. You've noticed a possible security, access or compliance problem.
4. You've been stuck for more than 45 minutes on something that blocks today's top-3, and the primers and official sources didn't help.

### Who to ask

| Topic | First stop | Then |
|---|---|---|
| Customs and trade compliance, classification, USMCA, IMMEX | The primers, then official sources (cbp.gov, ecfr.gov, cbsa-asfc.gc.ca, dof.gob.mx, ustr.gov) | Senior office hours |
| SQL Server, the data warehouse, Power BI, analytics method | The exercise text, then Microsoft Learn | Senior office hours |
| The AS400 trade system, custom tools, process, priorities, people | OneNote tool docs and SOPs (as they get written) | Manager (Teams, Monday confirm or 1:1) |
| Oracle cost data and the cost calendar | [COMPANY: Finance cost accountant] (Hire B) | Manager |
| How the business works (purchasing, logistics, sales) | [COMPANY: business contacts] | Manager |
| Access and IT | An [COMPANY: IT service desk] ticket | Manager, if it blocks a needed-by date |
| What a broker filed, or why | The broker portal or packet, if you have access | The Senior (or the Manager), who decides whether to ask the broker |

Brokers, agentes aduanales and trade counsel: before the day-60 review, you never contact them directly. The question goes to the Senior (or the Manager). After day 60, with the Senior's agreement, you may email the broker with the Senior copied.

### Senior office hours

- Fixed 30-minute slots: in W1-W2 they are in `docs/02-weeks-1-2-schedule.md`; from W3, one slot a week, Wed 15:00-15:30, in the standard week in Section 5 of `docs/01-30-60-90-plan.md` (none in W5, W6, W9, W10 and W11; in those weeks bring non-urgent questions to the recap block of the next Senior session or to your 1:1).
- Send your batch by 12:00 on the day: at most 5 questions each, ranked, every one with "tried so far" filled in.
- Both hires come together, and you each hear the other's answers.
- After the session, turn every answer into an Anki card, a glossary entry, or a line in a tool doc or SOP. Mark it in the question log's last column.

## WIP limits

- **W1-W5:** at most **1 real-work item** and **2 documentation items** (tool inventory, SOP draft) in progress. Learning tasks in Planner are not limited, but each has a due date this week.
- **W6-W13:** at most **3 items in progress**: one primary-process item (brief, model, PPV, cost input file, then your live cycle), one transition item (exports, then reporting), and one owned-tool, e2open or documentation item. Run them one after another inside each slot: for example, Hire A's model handoff, then the ad-hoc investigation; exports item 2 before the reporting item.
- Items waiting for a review, data or access go to the Waiting or Blocked bucket and don't count toward the limit.
- "Done" means reviewed and posted. "I sent it" is not done.
- Give a waiting or blocked item the reason, who it's waiting on, and the date. Check it daily and escalate to the Manager after 2 working days.
- Want to start something new while at the limit? Finish or park one first, and tell the Manager which in Teams.

## Estimating and saying "not by then"

### Estimating

1. Break the work into steps of half a day or less.
2. Estimate each step in hours. Add **review time** (maker-checker) and the **reviewer's lead time**: when can they actually look at it?
3. For a task you've never done, double your first number. This is a team rule of thumb for W1-W8, not a law; your own estimate-vs-actual history replaces it.
4. Give a date with a confidence level and the main risk: "Thursday noon, fairly confident. The risk is whether the AS400 extract has origin for all items."
5. Midpoint check: when half the time is gone and less than half the work is done, tell the requester and the Manager now, not at the deadline.
6. Record the estimate and the actual in Jira (or in the Friday self-report if time tracking isn't on [COMPANY]). Look at the pattern in a 1:1 once a month.

### Saying "not by then"

Five steps: **acknowledge, say what is possible, say what the full ask needs, offer options, confirm.** Never: a silent miss, "I'll try", or unreviewed numbers presented as final.

Scripts you can adapt:

- "Research can have the item list for the affected HTS codes to you by 16:00 today. The reviewed cost impact needs a second-person check, so the earliest is 10:00 tomorrow. Which helps you more for your meeting?"
- "To hit Wednesday, I'd have to pause the exports backlog item that's due Thursday. That's the Manager's call; I'll confirm by 14:00."
- "Our team rule is that a tariff model gets a documented review before it goes to the business. I've booked the review for 15:30, so you'll have it by 16:30."
- "I'm new to this report and don't want to guess at a date. I'll do the first step now and give you a firm date by end of day."

In days 1-60, any P1 or P2 date you can't meet, and any trade-off between two requesters, goes to the Manager. You don't choose between stakeholders alone.

## Focus blocks

- Two 90-minute focus blocks a day: one in the morning and one in the afternoon. Put them in your calendar as "Focus: [module or Jira key]".
- During a block: email closed, notifications off, Teams set to Do not disturb, with priority access for the Manager and the Senior if [COMPANY: Teams policy] allows it.
- Check messages at the end of each block. That way nobody waits more than about 90 minutes for you, which is fine for everything that doesn't pass the "ask now" test.
- Trainer sessions and shadows are not focus blocks. Schedule focus blocks around them, not over them.

## Meeting hygiene

- **Before:** know the purpose and your role (decide, inform, learn, take notes). Do the pre-read. Bring your top questions from the question log. If you didn't do the pre-read, say so at the start.
- **During:** one OneNote page per meeting with three headings: Decisions, Actions (owner and due date), Open questions.
- **After:** actions go into Jira or Planner within the hour. If you organized the meeting, send a five-line recap the same day: purpose, decisions, actions, open questions, next meeting.
- **When you run one:** put an agenda in the invite, default to 25 or 50 minutes, and end by reading the actions back.
- **Declining:** in W1-W4, check with the Manager before declining a stakeholder meeting. When you're optional, ask for the notes instead of attending.

## Learning vs doing, by phase

**Learning** = trainer sessions, primers, Anki, practice exercises, shadowing, teach-back prep.
**Doing** = real Jira work items (low-risk, reviewed), graded documentation (tool docs, SOPs, company-specific Anki cards, as-is docs, data maps), the tool inventory, exports and reporting backlog items, running your process with maker-checker sign-off.

| Phase | Weeks and dates | Target learning / doing | Of a 40-hour week | What "doing" looks like |
|---|---|---|---|---|
| Foundations | W1-W5, 10/19-11/20 | about 70 / 30 | 28 h / 10 h | Shadow write-ups, tool inventory, first small real analysis, first cards and SOP draft |
| Building | W6-W9, 11/23-12/18 | about 50 / 50 | 20 h / 18 h | Your own tool's doc and test-copy change, reviewed track items, exports backlog items |
| Owning | W10-W13, 12/21-1/15 | about 40 / 60 | 14 h / 24 h | Running your process cycle with maker-checker, e2open as-is doc, data map and kickoff, reporting backlog items |

Notes:

- The hours match the 40-hour table in Section 2 of `docs/01-30-60-90-plan.md`; about 2 h a week of admin is in neither column.
- W1-W2 run closer to 85/15, because almost everything is new. That is expected; W3-W4 make up the difference.
- W6 is about 3 working days (Thanksgiving) and W10-W11 are at about 50% capacity. Keep the same ratio on the reduced hours, and plan those weeks on the Friday before.
- Measure roughly: estimate your learning and doing hours to the nearest hour in the Friday self-report. If you are more than 15 points off the target two weeks in a row, raise it in the 1:1.

## Friday self-report

Use the 5 prompts in Section 5 of `docs/03-check-ins-and-scorecards.md`; there is no other format. Post it on your OneNote page "Weekly plans and self-reports" by 11:30 on Friday (on a holiday Friday, the last working day of the week) and send the link to the Manager, copy to the Senior. It drives the 1:1, so keep it short and honest. Prompt 1 is where your learning/doing hours go.

Copilot Chat may draft it from your own notes (the prompt in `docs/primers/copilot-chat-guide.md` 4.10), but you own the self-report: every line is true, the hours and the 0-4 ratings are yours (Copilot never rates your skills), the links work, and it says honestly what slipped. Copilot only drafts. Log the use in your Copilot use log.

## Templates (copy and paste)

### Weekly plan

| Field | Your entry |
|---|---|
| Week (W_, dates) | |
| Phase target (learning / doing) | |
| Outcome 1 (finished = reviewed and posted) | |
| Outcome 2 | |
| Outcome 3 | |
| Fixed commitments (sessions, 1:1, office hours, shadows, deadlines) | |
| Reviews booked (what, who, when) | |
| Risks, and what I need from the Manager or Senior | |
| Planned hours, out of available hours (leave 15% unplanned) | |

| # | Item (Jira or Planner key, or file) | Learn or Do | Est. h | Reviewer and due | Done? |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |

### Daily plan

| Item | Today |
|---|---|
| Date | |
| Top 1 | |
| Top 2 | |
| Top 3 | |
| Focus block 1 (time and item) | |
| Focus block 2 (time and item) | |
| Sessions, shadows, meetings | |
| Anki done? | |
| End of day: done | |
| End of day: moved (to when) or dropped (who agreed) | |
| Tomorrow's first task | |

### Question log

Your own page in OneNote section 06 Question Log. This is the only question-log format; `docs/03-check-ins-and-scorecards.md` Section 2 has the rules.

| Date | Question | Tried so far | Who to ask | Answer and source | Turned into |
|---|---|---|---|---|---|
| 10/20 | Example (M1): Is MPF charged on the entered value of every line, or once per entry? | Read the US duties section of the customs primer; searched cbp.gov | Senior | (fill in after office hours) | Card drafted |
| | | | | | |
| | | | | | |

The example question is there to show the format; the answer comes from the Senior, not from this page.

### Self-assessment (every fourth Friday, and before the day-30, 60 and 90 reviews)

Rate each habit 0-3: 0 = not doing it yet, 1 = sometimes, 2 = most days, 3 = every time without reminders. (The 0-4 proficiency scale is for skills, not habits.)

| Habit | Rating (0-3) | Evidence this period | One change next period |
|---|---|---|---|
| Weekly plan on Friday, confirmed on Monday | | | |
| Daily top-3 and 16:45 wrap | | | |
| Every request logged in Jira before starting | | | |
| Question log used; "ask now" test applied | | | |
| WIP limit respected | | | |
| Estimates given with date, confidence and risk; midpoint check done | | | |
| "Not by then" said early, with options | | | |
| Two focus blocks protected most days | | | |
| Reviews booked ahead (maker-checker) | | | |
| Learning/doing split close to the phase target | | | |

## Scenarios

Read each one and write down what you would do before you read the suggested handling. Discuss one in the Week 2 Friday 1:1.

### Scenario 1: an urgent tariff announcement mid-week

It is Tuesday 10:30 in Week 7. A new tariff action is published (for example a Federal Register notice under Section 232 or Section 301), effective for goods entered for consumption on or after 12:01 a.m. Eastern on Friday of next week: 7 business days away. CBP follows up with a CSMS message on how to report it. Hire A's plan for the rest of the week was the A60-1 brief on a recent action and an exports item. Hire B's plan was the PPV analysis.

Who is maker depends on the urgency rule in Section 7 of `docs/01-30-60-90-plan.md`. With 5-15 business days, the hire is maker, with a 15-minute daily checkpoint, and the checker reviews each draft on the same business day it is submitted; nothing is released before that review. If the effective date were fewer than 5 business days away (or the action were business-critical), the Senior would be maker for the WHAT and the Manager for the $, each checking the other. You would shadow, draft a parallel practice brief or model for review afterward, and write after-action notes within 2 working days. In W1-W2 the trainer is always maker.

Suggested handling, Hire A (Research owns the WHAT):

1. **First 15 minutes:** log a Jira Research item with the source link and the effective date. Message the Manager: "New [authority] action effective [date], 7 business days out, logged as [KEY]. I propose a 2-hour scoping pass and a draft Tariff-Impact Brief by Thursday 12:00, with a daily 15-minute checkpoint with the Senior. OK to pause the recent-action brief and use this one as my A60-1 evidence?"
2. **Re-plan:** the recent-action brief goes back to To Do (one primary-process item at a time); the exports item stays in its slot. Update the daily and weekly plans. Tell the Manager what slips.
3. **Book the review now:** put a 30-minute maker-checker slot with the Senior on Thursday at 15:00 on the calendar before you start writing.
4. **Scoping pass (2-hour timebox):** read the legal text itself (proclamation or notice, with its annex), not news summaries. Capture: authority, covered HTS codes, countries, rate, effective date and time, entry or in-transit provisions, stacking with other duties, exclusions, and how CBP says to report it. Mark each point "confirmed in source", "interpretation" or "open".
5. **Match:** using read-only data, pull the items with those HTS codes and origins from [COMPANY: AS400 trade item extract]. Count the affected items and flag any whose classification you're not sure of. This item list is Research's determination.
6. **Draft the brief** in `docs/templates/domain/tariff-impact-brief.md`, marked "DRAFT - not reviewed". Interpretation questions on stacking or scope pass the "ask now" test: take them to the Senior (or the Manager), who decides whether to ask [COMPANY: broker or trade counsel]. You don't contact them yourself.
7. **Release** only after the documented review. Then hand off to Standard Cost through the shared Tariff-Impact Model (`docs/templates/domain/tariff-impact-model-guide.md`).
8. **Friday:** the self-report shows the learning hours lost and when you'll make them up.

Suggested handling, Hire B (Standard Cost owns the $): park the PPV analysis (back to To Do; one primary-process item at a time) and tell the Manager. While the brief is in review, set up the model's cost baseline (customs value, volume, current duty, standard cost, sell price) for Research's draft item list. Label everything "pending brief [KEY]". Don't add or drop items yourself, and don't release any $ impact until the brief is reviewed and your own numbers have had their own maker-checker review. If the action changes the cost cycle prep, tell the Manager the same day.

What not to do: build on figures from a news article; let Research estimate cost impact (that's the $) or let Standard Cost decide scope (that's the WHAT); skip the review "because it's urgent"; stay late without telling anyone.

### Scenario 2: Finance wants a cost answer by end of day

It is Thursday 14:00. [COMPANY: Finance contact] messages Hire B: "What's the cost impact of the new duty on [product family]? Need it by EOD for a pricing meeting tomorrow at 9."

Suggested handling:

1. **Tell the Manager within 15 minutes.** A same-day P1 or P2 date is the Manager's call in days 1-60. If the duty takes effect in fewer than 5 business days, the Manager is maker for the $ and the Senior checks; you shadow, build a parallel practice model that is reviewed afterwards, and write after-action notes within 2 working days. Otherwise you are maker and steps 2-6 apply; with 5-15 business days to go, the checker reviews your numbers on the same business day you submit them.
2. **Clarify** (a call is faster than email): what decision is it for? Which items? Standard cost, landed cost or margin? Which tariff assumption, and is there a reviewed Tariff-Impact Brief? What format: one number or an item list? Does "EOD" mean 17:00 or "before 9 tomorrow"?
3. **Log it in Jira** and link the brief, if one exists. If there is no reviewed brief, the WHAT isn't settled: ask Research (Hire A or [COMPANY: current Research process runner]) where it stands, and tell Finance the answer depends on it.
4. **Estimate honestly.** For example: 40 items in the model takes about 2 hours, plus a 30-minute review. Ask the Manager or Senior for a review slot before 16:30.
5. **Reply with the options the Manager agreed**, for example: "By 17:00 I can give you a reviewed impact on standard cost for the 40 items, using the rate in brief [KEY]. A margin view by customer needs pricing data I don't have; earliest is Monday." If there's no reviewer today: "Today I can send the in-scope item list from Research's reviewed brief [KEY]. The reviewed $ impact will be with you by 08:30 tomorrow, before your meeting." If there is no reviewed brief, say the scope isn't settled yet.
6. **When you send it,** state the assumptions, the data date, the reviewer, and what isn't included.

What not to do: send unreviewed numbers "just as a rough idea" (they get forwarded and become the number); change Oracle standard costs outside the cycle (that's Finance's decision, under change control); answer questions about the tariff's legal scope yourself.

### Scenario 3: the Senior is heads-down on a drawback deadline

It is Monday in Week 4. The Senior posts: "Heads-down on drawback claims until Friday; office hours cancelled this week." Between them, the hires have 8 open questions, and 2 of them block the classification worksheet that is due Wednesday 11/11.

Suggested handling:

1. **Don't ping.** Acknowledge once: "Understood, good luck. We'll send one batched list for after Friday."
2. **Triage the question log.** Label each question B (blocks a dated deliverable this week), N (needed this week) or L (later).
3. **Try once more:** spend up to 15 more minutes on each B and N question in the primers and the official sources (HTSUS and its notes on hts.usitc.gov, CROSS rulings on rulings.cbp.gov, the Canada Customs Tariff on cbsa-asfc.gc.ca, TIGIE changes in the DOF), and update "tried so far". Each hire checks the other's log; the answer may already be there.
4. **Re-route:** process, system and priority questions go to the Manager. A blocking customs-interpretation question goes to the Manager too, who decides whether to wait, ask [COMPANY: broker], or move the due date.
5. **Re-plan:** move work that doesn't need the Senior to this week (analytics, tool inventory, SOP drafting, Anki). Tell the Manager if the Wednesday date moves.
6. **Send one consolidated message,** timed for after the deadline: at most 5 questions, ranked, each with "tried so far". Propose a 20-minute slot.
7. **Use it as M9 exposure:** ask the Manager (not the Senior, this week) whether there is a low-risk drawback task to observe after the deadline. Drawback stays with the Senior; you're there to learn how it works.

What not to do: wait silently until Friday; guess at a customs interpretation and build on it; ask the same question in three channels; ask the Senior "just one quick thing" during the deadline.

## Check yourself (end of Week 2)

- [ ] I have a weekly plan for W3 with three outcomes and booked reviews.
- [ ] My question log has at least 10 entries, and most have "tried so far" filled in.
- [ ] Everything anyone asked me to do is in Jira or Planner.
- [ ] I can say, without looking, the four "ask now" conditions and who to ask about what.
- [ ] I have written down what I would do in each of the three scenarios.
