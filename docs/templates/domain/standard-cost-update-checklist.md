# Standard Cost Update Checklist

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** run one periodic standard cost update for duty and landed-cost inputs, end to end, with the same steps and evidence every time: plan with Finance, collect inputs, calculate, validate, maker-checker review and Finance approval, load to Oracle, verify, communicate, archive. It is also the control record: a cycle without this completed checklist did not happen properly.
- **Who uses it:** Hire B (Standard Cost) as maker. The Manager as checker (the Senior checks duty-rate and classification questions). [COMPANY: Finance cost accounting contact] plans the calendar and approves before any Oracle load. Hire A (Research) supplies tariff actions through checked Tariff-Impact Briefs.
- **When:** every cost cycle ([COMPANY: cycle frequency]) and every interim tariff-driven update. Training use: walkthrough in W5, dry run on a copy for B60-2 (W7 to W8), a live cycle, full parallel run or interim update as maker for B90-1 (W12 to W13). Module M5C. Hire B: the cost data is the part to push hardest; the business context is a refresher for you.

## How to use this checklist

1. Copy this page for each cycle into [COMPANY: cost cycle folder] and name it `SCU_[cycle ID]_checklist`. Create one Jira epic per cycle.
2. **T** is the Oracle cost update date: the day the new standards take effect. Timings are in working days relative to T (T-10 = 10 working days before).
3. Tick each item when done and add the evidence link next to it. An item without evidence is not done.
4. The maker never approves their own work. The checker and Finance sign before anything loads to Oracle production. This continues after day 90.
5. Do not run a live cycle in W6, W10 or W11 without named trainer and Finance coverage (`docs/01-30-60-90-plan.md`, risk register).

### Company settings (fill once, review yearly)

| Setting | Value |
|---|---|
| Cycle frequency and next cycle dates | [COMPANY: for example annual full update plus interim duty updates] |
| Oracle product | [COMPANY: Oracle EBS or Fusion] |
| Where pending costs are held before the update | [COMPANY: EBS pending cost type name, or Fusion cost scenario naming rule] |
| Cost elements and sub-elements for landed cost | [COMPANY: for example material plus material overhead sub-elements for freight, duty, brokerage] |
| Load method | [COMPANY: cost interface, file-based import, Web ADI, custom tool] |
| Who loads, who runs the update | [COMPANY: roles; segregation of duties confirmed with Finance] |
| Variance review thresholds | [COMPANY: % change per unit] and [COMPANY: $ annual impact per item] |
| Materiality threshold | [COMPANY: materiality threshold] (same value as in `docs/01-30-60-90-plan.md`) |
| FX rate for costing | [COMPANY: Finance costing rate source and date rule] |
| Tariff action policy | [COMPANY: which actions go into the standard: effective on or before the cost-effective date only, or also announced actions] |
| Finance approver | [COMPANY: role] |
| Evidence archive and retention | [COMPANY: folder] and [COMPANY: retention period] |

## Landed-cost components

| Component | Typical source | Per-unit basis | Watch-outs |
|---|---|---|---|
| Purchase price | Oracle PO or contract price | Price per Oracle primary unit of measure | Currency and FX date; price unit vs stocking unit |
| International freight and insurance | [COMPANY: freight rate file or contracts] | Allocated by weight, volume or value ([COMPANY: rule]) | Allocation basis drives the result; keep it the same between cycles unless agreed |
| Duty (base rate) | Rate by HTS, import country and origin from [COMPANY: duty rate table or tool] | Duty base x rate | US duty base is the customs value, which excludes international freight and insurance when identified separately. Mexico's valor en aduana includes freight and insurance to the point of entry. Canada uses value for duty. See `docs/primers/customs-trade-compliance-primer.md` |
| Additional duties and surtaxes | Checked Tariff-Impact Briefs (`docs/templates/domain/tariff-impact-brief.md`) | Duty base x additional rate, stacked as the brief says | Only checked brief versions; effective dates vs the cost-effective date |
| Preference (USMCA) | Classification master plus certification on file | Preferential rate only where the claim is supported | A "qualifying" flag without a current certification is a data error |
| Customs fees | US: MPF on formal entries (ad valorem with a per-entry minimum and maximum); HMF on ocean shipments. Other countries: [COMPANY: fees in use] | Allocated per unit using average entry size ([COMPANY: rule]) | Amounts change (the MPF minimum and maximum are adjusted each US fiscal year): use `docs/primers/current-tariff-landscape.md` and record the date |
| Brokerage | Broker invoices ([COMPANY: source]) | Fee per entry divided by average units per entry | Extra lines for new Chapter 99 numbers can change fees |
| Inland freight and other | [COMPANY: sources] | [COMPANY: rule] | [COMPANY: components in scope] |
| Recoverable taxes | Canada GST and Mexico IVA on imports | Normally not a cost when recoverable | Confirm treatment with Finance; never add them by default |

## Cycle calendar

| Phase | Maker | Checker or approver | Timing | Output |
|---|---|---|---|---|
| 1 Plan with Finance | Hire B | Finance; Manager | T-30 to T-25 | Agreed date, scope, freeze date, thresholds |
| 2 Collect inputs | Hire B (tariff actions: Hire A) | Manager | T-25 to T-15 | Frozen input pack |
| 3 Calculate | Hire B | none yet | T-15 to T-12 | Cost file v0.x |
| 4 Validate | Hire B | none yet | T-12 to T-10 | Exception list, all explained |
| 5 Review and approve | Hire B submits | Manager (checker); Finance (approver) | T-10 to T-5 | Approved cost file v1.0, sign-offs |
| 6 Load and update in Oracle | [COMPANY: who loads] | Finance; Hire B verifies | T-3 to T | Pending costs loaded, simulation approved, update run |
| 7 Post-load verification | Hire B | Manager | T to T+1 | 100% tie-out |
| 8 Communicate | Hire B drafts | Manager approves | T+1 to T+2 | Finance and business notes sent |
| 9 Archive evidence | Hire B | Manager | By T+5 | Complete evidence folder; Jira closed |

## Phase 1: Plan the cycle with Finance (T-30 to T-25)

- [ ] Agree T, the cost-effective date and the period with [COMPANY: Finance cost accounting contact]. Put T on the team calendar and the Jira epic.
- [ ] Agree the scope: full update (all items) or partial (new items, and items with duty, tariff, freight or price changes).
- [ ] Agree the input freeze date (default T-15). Later changes wait for the next cycle unless Finance and the Manager approve.
- [ ] With Hire A, list every Tariff-Impact Brief released or expected before T. Apply [COMPANY: tariff action policy] to decide which ones go in.
- [ ] Confirm the variance thresholds and the materiality threshold for this cycle.
- [ ] Confirm who loads the file and who runs the update, and that the maker of the cost file cannot approve it ([COMPANY: Oracle roles and segregation of duties]).
- [ ] Book time: checker review (Manager, about 1.5 h between T-10 and T-7), Finance approval (T-6 to T-5), load window. In EBS, Oracle recommends running the update at the start of the accounting period, before transactions start for the new period. In Fusion, the cost scenario's effective date controls when new costs apply.
- [ ] Check holidays and absences for T-10 to T+2 and name a backup for each role.
- [ ] Create the cycle folder and Jira epic; copy this checklist.

## Phase 2: Collect inputs (T-25 to T-15)

- [ ] Item and cost extract from [COMPANY: Oracle cost extract or warehouse cost tables]: item, organization, primary unit of measure, current standard cost by cost element, on-hand and in-transit quantity, annual usage or forecast. Record the run date and time.
- [ ] Classification and origin from [COMPANY: AS400 trade master or warehouse table]: HTS (as text), country of origin, import country, USMCA status and certification expiry.
- [ ] Base duty rates by HTS and import country from [COMPANY: duty rate table or tool], with the date of the tariff schedule they come from.
- [ ] Additional duties: one line per Tariff-Impact Brief used (brief ID, version, checker, effective date). Rates come from the brief, never from news or email.
- [ ] Freight rates and allocation basis from [COMPANY: freight source]; any change in basis agreed with Finance.
- [ ] Brokerage fees and average units per entry from [COMPANY: broker invoice data].
- [ ] Customs fees (MPF, HMF, others) from `docs/primers/current-tariff-landscape.md`, with the date checked.
- [ ] Other landed-cost factors: [COMPANY: inland freight, handling, others].
- [ ] FX rates per [COMPANY: Finance costing rate rule], with the rate date.
- [ ] Freeze: save the input pack as read-only with every extract timestamp; post the link on the Jira epic.

## Phase 3: Calculate (T-15 to T-12)

- [ ] Build landed cost per item, component by component, in [COMPANY: name of std-cost tool or workbook].
- [ ] Duty = duty base x (base rate + additional rates), combined exactly as each brief's stacking section says. Use the duty base rules for each import country.
- [ ] Convert every component to the Oracle primary unit of measure.
- [ ] Map each component to its Oracle cost element and sub-element ([COMPANY: mapping]).
- [ ] For tariff-driven items, take the per-unit change from the checked Tariff-Impact Model (`docs/templates/domain/tariff-impact-model-guide.md`) and make sure the cost file gives the same answer.
- [ ] No typed-over formulas. Every manual override goes on an override log: item, old value, new value, reason, approver.
- [ ] Save as v0.x; keep earlier versions.

## Phase 4: Validate (T-12 to T-10)

- [ ] Completeness: rows in the cost file = items in scope. No item in scope is missing; no item outside scope is included.
- [ ] Zero and blank costs: none unless intended and explained. In EBS, an item with no pending cost defined is skipped by the update, and an item with a pending cost of zero is updated to zero.
- [ ] Hand check: recompute 5 items from the source data, including one per import country.
- [ ] Threshold review: every item over [COMPANY: % threshold] change per unit, or over [COMPANY: $ threshold] annual impact (change per unit x annual quantity), has a driver: purchase price, duty rate, tariff action, freight, FX, unit of measure, or data correction.
- [ ] Top movers: the top 20 items by annual $ impact and the top 20 by % change are explained in one line each.
- [ ] Reasonableness: duty as % of landed cost by origin and product category, compared with the last cycle. Investigate any group that moved more than [COMPANY: tolerance] without a known tariff action.
- [ ] Red flags: an item whose HTS carries an additional duty in a checked brief but shows no additional duty; a preferential rate without a current certification; duty on an item that is duty-free; a cost change on an item with no input change.
- [ ] Inventory revaluation estimate: sum of (new standard minus current standard) x on-hand and in-transit quantity, by organization. Finance needs this before approving.
- [ ] Tie the tariff-driven items to the Tariff-Impact Model totals.
- [ ] Exception list complete: every flag above is either fixed or explained.

## Phase 5: Maker-checker review and Finance approval (T-10 to T-5)

- [ ] Maker sends the review pack: this checklist, input pack, cost file candidate, exception list, top movers, override log, revaluation estimate, list of briefs used.
- [ ] Checker (Manager; Senior for duty-rate or classification questions) traces 10 items to source, including 5 top movers and at least one item per import country.
- [ ] Checker confirms every brief used is a checked version and its rates and dates match the cost file.
- [ ] Checker reviews the threshold explanations, override log and formula integrity.
- [ ] Findings logged on Jira, fixed by the maker, re-checked. Checker records name, date, version reviewed and findings.
- [ ] Finance approval: [COMPANY: Finance approver] approves the cost changes and the revaluation estimate in writing, before any load.
- [ ] Lock the approved file (read-only, version in the file name). Any later change is a new version with a new review and approval.

## Phase 6: Load to Oracle and run the update (T-3 to T)

Method: [COMPANY: load method]. Product: [COMPANY: Oracle EBS or Fusion]. Steps differ by product and release, so follow [COMPANY: Oracle cost update work instruction] where it differs.

- [ ] Load the approved file into [COMPANY: pending cost type (EBS) or cost scenario (Fusion)], never straight into the live standard.
- [ ] Check the load log: rows loaded = rows in the approved file; rejects are zero or fixed and re-checked.
- [ ] Simulate before updating. EBS: run Report Pending Adjustments, which produces the inventory, intransit and WIP standard cost adjustment reports without posting. Fusion: compare the scenario's standard costs with the current published costs (and the inventory impact view, where your release has it).
- [ ] Compare the simulated revaluation with the Phase 4 estimate. Explain any difference; Finance confirms.
- [ ] Run the update at the agreed time. EBS: Update Standard Costs from the pending cost type to Frozen. Fusion: run the update or publish step for the cost scenario with the agreed effective date. Done by [COMPANY: who runs the update], with Finance informed.
- [ ] Save the update output and adjustment reports to the cycle folder.
- [ ] Know the correction path before you start: in Fusion a published scenario cannot be unpublished once its costs are used in transactions (an Undo Cost Update task exists for unintended updates); in EBS a correction normally means another cost update. Agree the path with Finance in advance.

## Phase 7: Post-load verification (T to T+1)

- [ ] 100% compare by query: Oracle's new standard costs against the approved file, by item, organization and cost element. Zero unexplained differences. Do not rely on sampling.
- [ ] Items outside the scope did not change (compare before and after snapshots).
- [ ] The posted adjustment total equals the simulated total, or the difference is explained.
- [ ] Spot-check 5 items on the Oracle cost screens, including the top mover.
- [ ] Rate tables in [COMPANY: name of std-cost tool] carry the new rates with the right effective dates; old rows end-dated.
- [ ] Watch the first receipts after T (T+5 to T+10): PPV on the top movers should be close to zero unless the price, duty or freight on the receipt differs from the new standard. Explain any surprises.

## Phase 8: Communicate (T+1 to T+2)

- [ ] Finance: revaluation by organization, adjustment report reference, exceptions, anything deferred to the next cycle.
- [ ] Pricing and Purchasing: top movers, tariff-driven changes with margin effect (from the Tariff-Impact Model), effective date, known limits.
- [ ] Note that PPV is now measured against the new standards, and which items will show variance for known reasons (for example in-transit goods still entering at the old duty rate).
- [ ] The Manager approves any message to the business before it is sent.
- [ ] Team: SOP updates, new Anki cards (`docs/templates/knowledge/anki-card-writing-guide.md`), lessons learned.

## Phase 9: Archive evidence (by T+5)

- [ ] The cycle folder holds: this completed checklist; input pack with extract timestamps; briefs used (with versions); approved cost file; exception and override logs; checker sign-off; Finance approval; load log; simulation and update reports; post-load compare; communications sent.
- [ ] The Jira epic links the folder; every story is Done; follow-ups are new issues.
- [ ] Retention follows [COMPANY: records retention schedule].
- [ ] For a cycle with problems, write a closeout (`docs/templates/bsa/08-project-closeout.md`).

## RACI

R = does the work, A = accountable (one per row), C = consulted, I = informed. Adjust the Oracle columns once [COMPANY: who loads and runs the update] is confirmed.

| Activity | Std Cost BSA (Hire B) | Checker (Manager or Senior) | Finance cost accounting | Research BSA (Hire A) | Oracle or IT support |
|---|---|---|---|---|---|
| Plan calendar and scope | R | C | A | I | C |
| Tariff-Impact Briefs for actions in the cycle | I | A (Senior checks) | I | R | none |
| Collect and freeze inputs | R | A | C | C | C |
| Calculate and validate | R | A | I | C | none |
| Maker-checker review | C | R and A | I | C | none |
| Approve cost changes and revaluation | C | C | R and A | none | I |
| Load pending costs and simulate | C (verifies) | I | A | none | R |
| Run the cost update | C | I | R and A | none | C |
| Post-load verification | R | A | C | none | C |
| Communicate to Finance and the business | R | A | C | I | none |
| Archive evidence | R | A | I | none | none |

## Common errors and how to catch them

| Error | How it shows up | How to catch it |
|---|---|---|
| Duty applied to the wrong base (for example US duty on a value that includes international freight) | Duty a few percent too high on every item from one lane | Hand-check 5 items per import country against the duty base rules |
| Supplier or ship-from country used instead of country of origin | Wrong additional duties for whole supplier groups | Compare origin in the cost file with the classification master for every item covered by a brief |
| Additional duty missing or double-counted | Duty % of landed cost jumps or fails to move after an action | Tie tariff-driven items to the Tariff-Impact Model; check each brief's stacking result for 3 items |
| Rate used before its effective date, or after it ends | Standard includes a duty the receipts do not pay yet (or still pay) | Brief dates vs the cost-effective date, applied through [COMPANY: tariff action policy] |
| HTS leading zero lost in Excel (chapters 01 to 09) | Items do not match the rate table; duty shows as zero | Keep HTS as text; count matched vs unmatched rows; length check of 10 digits |
| Unit of measure mismatch | Cost per unit off by a pack size (x12, x100) | Top movers by %; compare price unit with Oracle primary unit |
| Wrong FX rate or date | Every item from one currency moves the same % | Reasonableness by currency; FX rate and date recorded in the input pack |
| USMCA rate without a current certification | Duty too low; compliance exposure | Join preference claims to certification expiry dates |
| Freight allocation basis changed silently | All items on a lane move with no rate change | Compare allocation basis with last cycle's input pack |
| Zero or blank pending cost | Item updated to zero, or skipped and left at the old cost | Zero and blank check in Phase 4; load log row count |
| Late input change after the freeze | File no longer matches what the checker reviewed | Read-only approved file; version in the file name; post-load 100% compare |
| Update run mid-period or in the wrong organization or cost type | Unexpected revaluation; costs on the wrong items | Simulation reviewed and Finance-approved before the update; run only in the agreed window |
| Recoverable taxes (GST, IVA) added to cost | Landed cost too high for Canada or Mexico items | Component list reviewed with Finance once a year |
| Typed numbers over formulas in the workbook | Totals do not change when inputs change | Checker spot-checks formulas; override log required |

## Quality checklist before you ask for Finance approval

- [ ] Every phase 1 to 5 item is ticked, with evidence links.
- [ ] Input pack frozen, with timestamps; briefs listed with versions.
- [ ] Hand check of 5 items passed; top movers and threshold items explained.
- [ ] Revaluation estimate prepared by organization.
- [ ] Checker sign-off recorded on Jira with name, date, version and findings, all closed.
- [ ] The file Finance will approve is the exact version that will be loaded.
