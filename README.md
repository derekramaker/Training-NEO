# Training-NEO: BSA New-Hire Onboarding Program

Last updated: 2026-10-17 · Owner: BSA Manager

A 90-day onboarding program for two early-career Business Systems Analysts (BSAs) on an international trade
systems team (US / Canada / Mexico imports). Start date: **Monday, October 19, 2026**.

- **Hire A: Research track.** Owns tariff/regulatory change research, tariff modeling and ad-hoc investigations.
- **Hire B: Standard Cost track.** Owns duty/landed-cost inputs, the standard cost update cycle, tariff impact on cost, and PPV analysis.
- **Trainers:** BSA Manager (8 h/week) and a Senior BSA (4 to 5 h/week).

| Milestone | Date | The bar |
|---|---|---|
| Day 30 | Wed Nov 18, 2026 | Understands customs & trade compliance fundamentals and trade systems/GTM; has done real data analytics; uses the team's data platform safely |
| Day 60 | Fri Dec 18, 2026 | Confident in own track; owns one custom tool; learning exports |
| Day 90 | Fri Jan 15, 2027 | Runs own process end to end with maker-checker sign-off; e2open as-is doc + data map done |

## Manager: do these before Oct 19

1. **Decide the service-account model before access requests go out** (`[COMPANY: confirm the service-account model before access requests go out]`). The recommended model is in Part 3 of `docs/primers/data-platform-primer.md`; the hires get no access to the service account.
2. **Submit system access requests now.** Provisioning often takes 1 to 2 weeks. See `docs/04-access-request-checklist.md`, including the sandbox grant in AR-07, AR-22 Copilot Chat, AR-23 DBeaver and AR-24 Remote Desktop.
3. **Confirm with `[COMPANY: ERP security]` that the DBeaver Oracle EBS account is read-only** at the database (AR-23), before either hire's first EBS query.
4. **Confirm the AI-use policy and Copilot Chat:** what `[COMPANY: AI acceptable-use policy]` allows, and that Microsoft 365 Copilot Chat is enabled for the hires' work accounts (AR-22; `docs/primers/copilot-chat-guide.md` 1.6).
5. **Fill in the data platform map on company systems, with the Senior** (`docs/templates/knowledge/data-platform-map.md`; at least Sections 1, 3 and 6 before the Senior's data landscape tour on Thu Oct 22). Real server, database, account and workspace names go only in `[COMPANY: location of the filled data platform map]`, never in this repo.
6. Read the short summary `docs/00-program-at-a-glance.md`, then the full plan `docs/01-30-60-90-plan.md` and the day-by-day `docs/02-weeks-1-2-schedule.md`.
7. Create the team **onboarding folder** on SharePoint/Teams and copy everything in `dist/` into it **except `dist/trainer-only/`**.
   The hires never read this repo; every hire-facing page refers to "the onboarding folder".
8. Set up the OneNote notebook (structure below) and paste in the Word files from `dist/docs/`.
9. Keep one shared copy of `BSA-Onboarding-Trackers.xlsx` in the onboarding folder and link it from OneNote.
10. Put `dist/trainer-only/answer-key.docx` somewhere only you and the Senior can open. After the day-30 review you decide whether to share it, without its Exercise 9 to 11 sections, which stay trainer-only (with the data generator) until the day-60 review.
11. Block the Senior's training time (4 to 5 h/week) on their calendar for weeks 1 to 13.
12. Have both hires install Anki and import `BSA-Onboarding.apkg` from the onboarding folder on day 1.
13. Fill the `[COMPANY: ...]` placeholders in the company copy (see "Generic-only policy" below).

## What's in `dist/` (ready to use)

| File | What it is | How to use it |
|---|---|---|
| `BSA-Onboarding-Handbook.docx` | Program at a glance, plan, weeks 1 and 2 schedule, check-ins, access checklist, time management in one file | Print or read end to end |
| `docs/*.docx` | One Word file per page: plan, schedule, primers (including the BSA fundamentals, SDLC, Copilot Chat and data platform primers), templates (including the Copilot prompt library and the data platform map) and the analytics exercises | Open in Word, select all, paste into a OneNote page. The platform map is filled in on company systems only |
| `BSA-Onboarding-Trackers.xlsx` | Skills tracker, knowledge tracker (one tab per hire), dashboard, tool inventory, glossary | Keep one shared copy; review in weekly 1:1s |
| `BSA-Onboarding.apkg` | Anki deck: Units 01–07 in teaching order (topic groups, diagrams, fill-in-the-diagram and worked-example cards) plus a suspended Reference unit | Anki: File > Import, then the one-time setup in the card-writing guide. 15 minutes a day |
| `anki/BSA-Onboarding-cards.csv` | The same cards as a CSV | For Quizlet, Excel self-quiz, or review |
| `Tariff-Impact-Model-Template.xlsx` | Shared Research + Standard Cost tariff model (live formulas) | Copy per tariff action; see `docs/templates/domain/tariff-impact-model-guide.md` |
| `Practice-Data.xlsx`, `practice-data/*.csv` | Synthetic import data for the analytics exercises | Use with the practice exercises page |
| `videos/*.mp4` (+ `.vtt`, poster, script) | Four short narrated explainers: how an import entry works (US, Canada, Mexico); how trade data flows (with e2open); the Research to Standard Cost handoff; USMCA origin with a bill of materials | Upload each MP4 to Microsoft Stream with its `.vtt` captions file and poster; put the links in the `[COMPANY: Stream link]` slots in the customs and trade systems primers, the Tariff-Impact Brief template and the model guide |
| `trainer-only/answer-key.docx` | Answer key for the analytics exercises (1 to 11) | **Manager and Senior only.** Not in the onboarding folder or the hires' OneNote sections; the Manager may share it after day 30, without the Exercise 9 to 11 sections until after day 60 |

## Suggested OneNote notebook structure

| Section | Pages |
|---|---|
| 00 Start Here | Program at a glance, 30/60/90 plan, weeks 1 and 2 schedule, link to the trackers workbook |
| 01 Check-ins | 1:1 notes (one page per week per hire), milestone scorecards, Friday self-reports |
| 02 Primers | Customs & trade compliance, trade systems/GTM/e2open, current tariff landscape, BSA fundamentals, SDLC, Copilot Chat guide, data platform |
| 03 Templates | BSA project templates, Tariff-Impact Brief, standard cost checklist, knowledge templates. The live team Copilot prompt library is a page in `[COMPANY: team OneNote section for the prompt library]` |
| 04 Tool Docs | One page per custom tool, written by the hires (from `docs/templates/knowledge/tool-doc.md`) |
| 05 Process SOPs | Research SOP, Standard Cost SOP, Exports and Reporting SOPs as they transition |
| 06 Question Log | Running question log per hire (template in `docs/05-time-management.md`) |
| 07 Analytics | Practice exercises 1 to 11 and the hires' findings memos and lab notes. The answer key stays out of the notebook (its Exercise 9 to 11 sections until after day 60) |

**Pasting tip:** open the `.docx` in Word, Ctrl+A, Ctrl+C, then paste into a blank OneNote page. Tables and checkboxes stay
editable. *Insert > File Printout* gives a read-only image instead. Link to the trackers workbook rather than embedding it,
because an embedded spreadsheet is a separate copy that won't stay in sync.

## Source layout

| Path | Contents |
|---|---|
| `docs/` | All program pages as Markdown (source of the Word files) |
| `docs/primers/` | Self-study primers for the core topics, the dated tariff landscape, BSA fundamentals (`business-systems-analysis-primer.md`), SDLC (`sdlc-primer.md`), Copilot Chat (`copilot-chat-guide.md`) and the data platform (`data-platform-primer.md`) |
| `docs/templates/bsa/` | Intake, requirements, process map, data mapping, UAT, change request, Jira, closeout |
| `docs/templates/domain/` | Tariff-Impact Brief, standard cost update checklist, tariff model guide |
| `docs/templates/knowledge/` | Tool doc, process SOP, teach-back, Anki card-writing guide, Copilot prompt library (`copilot-prompt-library.md`), data platform map (`data-platform-map.md`, filled in on company systems only) |
| `docs/analytics/` | Practice exercises (1 to 11) and answer key (trainer-only) |
| `data/trackers/` | Skills, knowledge topics and glossary (source of the trackers workbook) |
| `data/anki/` | Flashcards as CSV (source of the Anki deck) |
| `build/` | `build.py` turns the sources into `dist/`; `make_tariff_model.py` builds the tariff model |
| `video/` | Training video sources (narration script, scenes) and the engine; `python3 video/build_video.py <id>` renders to `dist/videos/` (see `video/README.md`) |

## Rebuilding after edits

```
pip install python-docx openpyxl genanki pandas
python3 build/build.py
```

Requires `pandoc`. Each card's ID comes from its deck and front text, so re-importing an updated `.apkg` updates cards whose front is unchanged and keeps their review history. Rewording a front creates a new card; suspend or delete the old one in Anki.

## Generic-only policy

This repo holds templates and industry-level content only. Anything internal (tool names, report names, brokers,
Oracle configuration, people, internal policies) is a `[COMPANY: ...]` placeholder that gets filled in on company
systems, not here. Vendor platform names (Oracle, AS400, e2open, Power BI, Jira, OneNote) do appear; remove them if
your policy requires.

Regulatory content is training material, not legal advice. `docs/primers/current-tariff-landscape.md` is a dated
snapshot that goes stale. The Research track hire keeps it current. Confirm interpretations with your licensed
customs broker or trade counsel.
