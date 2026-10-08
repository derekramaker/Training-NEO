# Training-NEO: BSA New-Hire Onboarding Program

A 90-day onboarding program for two early-career Business Systems Analysts (BSAs) on an international trade
systems team (US / Canada / Mexico imports). Start date: **Monday, October 19, 2026**.

- **Hire A: Research track.** Owns tariff/regulatory change research, tariff modeling and ad-hoc investigations.
- **Hire B: Standard Cost track.** Owns duty/landed-cost inputs, the standard cost update cycle, tariff impact on cost, and PPV analysis.
- **Trainers:** BSA Manager (8 h/week) and a Senior BSA (4 to 5 h/week).

| Milestone | Date | The bar |
|---|---|---|
| Day 30 | Wed Nov 18, 2026 | Understands customs & trade compliance fundamentals and trade systems/GTM; has done real data analytics |
| Day 60 | Fri Dec 18, 2026 | Confident in own track; owns one custom tool; learning exports |
| Day 90 | Fri Jan 15, 2027 | Runs own process end to end with maker-checker sign-off; e2open as-is doc + data map done |

## Manager: do these before Oct 19

1. **Submit system access requests now.** Provisioning often takes 1 to 2 weeks. See `docs/04-access-request-checklist.md`.
2. Read `docs/00-program-on-a-page.md`, then the full plan `docs/01-30-60-90-plan.md` and the day-by-day `docs/02-weeks-1-2-schedule.md`.
3. Create the team **onboarding folder** on SharePoint/Teams and copy everything in `dist/` into it **except `dist/trainer-only/`**.
   The hires never read this repo; every hire-facing page refers to "the onboarding folder".
4. Set up the OneNote notebook (structure below) and paste in the Word files from `dist/docs/`.
5. Keep one shared copy of `BSA-Onboarding-Trackers.xlsx` in the onboarding folder and link it from OneNote.
6. Put `dist/trainer-only/answer-key.docx` somewhere only you and the Senior can open. The hires get it after their day-30 review.
7. Block the Senior's training time (4 to 5 h/week) on their calendar for weeks 1 to 13.
8. Have both hires install Anki and import `BSA-Onboarding.apkg` from the onboarding folder on day 1.
9. Fill the `[COMPANY: ...]` placeholders in the company copy (see "Generic-only policy" below).

## What's in `dist/` (ready to use)

| File | What it is | How to use it |
|---|---|---|
| `BSA-Onboarding-Handbook.docx` | Program on a page, plan, weeks 1 and 2 schedule, check-ins, access checklist, time management in one file | Print or read end to end |
| `docs/*.docx` | One Word file per page (plan, schedule, primers, templates) | Open in Word, select all, paste into a OneNote page |
| `BSA-Onboarding-Trackers.xlsx` | Skills tracker, knowledge tracker (one tab per hire), dashboard, tool inventory, glossary | Keep one shared copy; review in weekly 1:1s |
| `BSA-Onboarding.apkg` | Anki deck in 3 sub-decks (customs/classification/USMCA; programs/exports/cost; BSA craft/data) | Anki: File > Import. 15 minutes a day |
| `anki/BSA-Onboarding-cards.csv` | The same cards as a CSV | For Quizlet, Excel self-quiz, or review |
| `Tariff-Impact-Model-Template.xlsx` | Shared Research + Standard Cost tariff model (live formulas) | Copy per tariff action; see `docs/templates/domain/tariff-impact-model-guide.md` |
| `Practice-Data.xlsx`, `practice-data/*.csv` | Synthetic import data for the analytics exercises | Use with the practice exercises page |
| `trainer-only/answer-key.docx` | Answer key for the analytics exercises | **Manager and Senior only.** Not in the onboarding folder or the hires' OneNote sections until after day 30 |

## Suggested OneNote notebook structure

| Section | Pages |
|---|---|
| 00 Start Here | Program on a page, 30/60/90 plan, weeks 1 and 2 schedule, link to the trackers workbook |
| 01 Check-ins | 1:1 notes (one page per week per hire), milestone scorecards, Friday self-reports |
| 02 Primers | Customs & trade compliance, trade systems/GTM/e2open, current tariff landscape |
| 03 Templates | BSA project templates, Tariff-Impact Brief, standard cost checklist, knowledge templates |
| 04 Tool Docs | One page per custom tool, written by the hires (from `docs/templates/knowledge/tool-doc.md`) |
| 05 Process SOPs | Research SOP, Standard Cost SOP, Exports and Reporting SOPs as they transition |
| 06 Question Log | Running question log per hire (template in `docs/05-time-management.md`) |
| 07 Analytics | Practice exercises and the hires' findings memos. The answer key stays out of the notebook until after day 30 |

**Pasting tip:** open the `.docx` in Word, Ctrl+A, Ctrl+C, then paste into a blank OneNote page. Tables and checkboxes stay
editable. *Insert > File Printout* gives a read-only image instead. Link to the trackers workbook rather than embedding it,
because an embedded spreadsheet is a separate copy that won't stay in sync.

## Source layout

| Path | Contents |
|---|---|
| `docs/` | All program pages as Markdown (source of the Word files) |
| `docs/primers/` | Self-study primers for the core topics and the dated tariff landscape |
| `docs/templates/bsa/` | Intake, requirements, process map, data mapping, UAT, change request, Jira, closeout |
| `docs/templates/domain/` | Tariff-Impact Brief, standard cost update checklist, tariff model guide |
| `docs/templates/knowledge/` | Tool doc, process SOP, teach-back, Anki card-writing guide |
| `docs/analytics/` | Practice exercises and answer key |
| `data/trackers/` | Skills, knowledge topics and glossary (source of the trackers workbook) |
| `data/anki/` | Flashcards as CSV (source of the Anki deck) |
| `build/` | `build.py` turns the sources into `dist/`; `make_tariff_model.py` builds the tariff model |

## Rebuilding after edits

```
pip install python-docx openpyxl genanki pandas
python3 build/build.py
```

Requires `pandoc`. Card IDs are stable, so re-importing an updated `.apkg` updates existing cards instead of duplicating them.

## Generic-only policy

This repo holds templates and industry-level content only. Anything internal (tool names, report names, brokers,
Oracle configuration, people, internal policies) is a `[COMPANY: ...]` placeholder that gets filled in on company
systems, not here. Vendor platform names (Oracle, AS400, e2open, Power BI, Jira, OneNote) do appear; remove them if
your policy requires.

Regulatory content is training material, not legal advice. `docs/primers/current-tariff-landscape.md` is a dated
snapshot that goes stale. The Research track hire keeps it current. Confirm interpretations with your licensed
customs broker or trade counsel.
