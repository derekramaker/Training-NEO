# UAT Test Plan Template

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** plan, run and record user acceptance testing (UAT) so the business can decide on evidence whether a change is fit to go live. It covers custom tool changes, reports, interfaces and the e2open UAT cycles.
- **Who uses it:** the BSA as UAT lead or tester; business testers; the checker (Senior or Manager), who reviews test cases and evidence; the developer, tool owner or vendor, who fixes defects; the business owner, who signs.
- **When:** write the test cases as soon as the requirements are signed, not after the build. Taught in M4 in W7. Used for the first tool change in W8 (with `docs/templates/bsa/06-change-request.md`) and for e2open UAT once the build is ready (M10; [COMPANY: e2open UAT dates from the project plan]).

## How to fill this in

Text in [square brackets] is a prompt: replace it. [COMPANY: ...] is a company-specific value.

1. Start from the acceptance criteria in the requirements (`docs/templates/bsa/02-requirements.md`) or the Jira stories (`docs/templates/bsa/07-jira-epic-story.md`). Each Must needs at least one test case. Add negative and boundary cases.
2. Write the expected result before you run the test, with exact values. Work out duty by hand or with the shared Tariff-Impact Model, which computes duty only. Work out fees, freight and full landed cost by hand, using the rules in [COMPANY: name of std-cost tool]. "Works correctly" is not an expected result.
3. List the test data each case needs (items, countries, dates, entries) and prepare it in the test environment. Never test in production. Supplier cost and margin data stays in access-controlled test locations.
4. Have the checker review the test cases before execution. This is an entry criterion.
5. Run the cases. Record what actually happened, in words and values, and save evidence named [Test case ID]_[YYYY-MM-DD]_[initials].
6. When a case fails, log a defect the same day and link it to the case. After the fix, retest the case and re-run related cases (regression).
7. When the exit criteria are met, write the summary and get sign-off.

## Template

### 1. Document control

| Field | Entry |
|---|---|
| Test plan title and version | [Name, v0.1] |
| Change under test | [Jira epic or story; change request ID] |
| Build or version under test | [Build ID, file version, e2open release] |
| Test environment | [COMPANY: test environment or e2open sandbox] |
| UAT lead | [Name] |
| Checker | [Senior or Manager] |
| Business owner | [COMPANY: role] |

### 2. Scope

- **In scope:** [requirement IDs, features, interfaces, countries, item sets]
- **Out of scope:** [what is not tested, and why]
- **Test data:** [source, refresh date, who prepares it, how sensitive data is protected]
- **Assumptions:** [for example: development and system testing are complete; the broker test file can be produced in test]

### 3. Entry criteria (all must be true before testing starts)

- [ ] Requirements or stories are signed off, with acceptance criteria.
- [ ] The build is in the test environment, with release notes listing what changed.
- [ ] The developer, tool owner or vendor has finished their own testing and shared the results.
- [ ] Test data is loaded and reconciled (`docs/templates/bsa/04-data-mapping-spec.md`, Part 7).
- [ ] Testers have test-environment access (least privilege; no shared logins).
- [ ] Test cases have expected results and are reviewed by the checker.
- [ ] Known defects are listed, so testers don't re-log them.

### 4. Exit criteria (all must be true to recommend go-live)

- [ ] 100% of Must test cases are executed; [COMPANY: target, for example 95%] of all cases pass.
- [ ] No open Critical or High defects.
- [ ] Every open Medium or Low defect has a workaround, an owner and a fix date, agreed by the business owner.
- [ ] Data reconciliation passed for the final test load.
- [ ] Regression cases for interfaces (broker feeds, Oracle loads) passed.
- [ ] Evidence for every executed case is saved and linked.
- [ ] Sign-off is recorded.

### 5. Roles

| Role | Name | Responsibilities |
|---|---|---|
| UAT lead | [BSA] | Plan, test data, schedule, daily status, defect triage, summary |
| Tester | [Business users and BSAs] | Run cases, record actual results and evidence, log defects |
| Checker | [Senior or Manager] | Review cases before execution and evidence before sign-off |
| Developer, tool owner or vendor | [Name] | Fix defects; deploy fixed builds with notes |
| Data owner | [COMPANY: role] | Confirm test data and reconciliation |
| Business owner | [COMPANY: role] | Decide go or no-go; sign off |

### 6. Schedule

| Activity | Start | End | Owner |
|---|---|---|---|
| Test cases written and reviewed | [ ] | [ ] | [ ] |
| Test data ready | [ ] | [ ] | [ ] |
| Execution cycle 1 | [ ] | [ ] | [ ] |
| Fixes and retest | [ ] | [ ] | [ ] |
| Sign-off | [ ] | [ ] | [ ] |

### 7. Test scenarios

| Scenario ID | Scenario | Requirement IDs | Priority | Tester |
|---|---|---|---|---|
| [TS-01] | [Business situation to prove] | [FR IDs] | [Must, Should, Could] | [Name] |

Starter trade scenarios. Keep the ones that apply and add the rest from the requirements.

| Scenario ID | Scenario | What it proves | Priority | Typical tester |
|---|---|---|---|---|
| TS-01 | A classification change flows to the broker feed | An approved HTS change reaches the right broker file, for the right country, once, from the right date; nothing else changes | Must | Research BSA |
| TS-02 | USMCA qualification result | The system's qualification result and origin criterion match a hand-worked result; missing or expired certifications block the claim | Must | Research BSA |
| TS-03 | Landed-cost and duty calculation matches expected | Duty per unit matches the Tariff-Impact Model (duty only); fees and full landed cost per unit match a hand calculation using [COMPANY: name of std-cost tool] rules, within tolerance | Must | Standard Cost BSA |
| TS-04 | Tariff effective-date handling | The rate is chosen by the date of entry (or withdrawal from warehouse for consumption), with correct behavior on both sides of the effective date and for any in-transit terms | Must | Research and Standard Cost BSAs |
| TS-05 | Stacking and exclusions | Additional duties combine (or don't) exactly as the Tariff-Impact Brief says; excluded items get no additional duty | Must | Research BSA |
| TS-06 | Duty base by country | The duty base follows each country's rule: the US and Canada generally leave international freight out of the duty base, Mexico includes freight and insurance to the point of entry (details in `docs/primers/customs-trade-compliance-primer.md`) | Must | Standard Cost BSA |
| TS-07 | Incomplete item blocked | A new item without a classification for a country is not sent to that country's broker feed, and someone is alerted | Should | Research BSA |
| TS-08 | Maker-checker in the system | A user cannot approve their own classification or rate change | Must | UAT lead |
| TS-09 | Legacy vs e2open parallel comparison | For the same period and inputs, e2open's broker feed and duty results equal the AS400 outputs (or the custom tool's, where the AS400 does not calculate them), or each difference is explained by an approved change or a cleansing log entry (`docs/templates/bsa/04-data-mapping-spec.md`, Part 6) | Must | Research and Standard Cost BSAs |

### 8. Test cases

Put preconditions and test data at the start of Steps. Expected results use exact values.

| ID | Steps | Expected | Actual | Pass/Fail |
|---|---|---|---|---|
| [TC-01] | Pre: [state and data]. 1. [Action]. 2. [Action]. | [Exact observable result] | [What happened, with values; evidence file name] | [Pass, Fail, Blocked] |

### 9. Defect log

| ID | Severity | Description | Status | Owner |
|---|---|---|---|---|
| [D-01] | [Critical, High, Medium, Low] | [Test case; steps; expected vs actual; evidence] | [New, Triaged, In fix, Ready for retest, Closed, Deferred] | [Name] |

| Severity | Definition | Trade example | Expected response |
|---|---|---|---|
| Critical | Wrong compliance or financial data would reach a broker, Finance, Oracle or a filing; or testing is blocked with no workaround | Broker feed sends the old HTS number after an approved change | Stop; fix before any further testing of the area |
| High | A Must requirement fails; any workaround is manual or risky | Rate chosen by PO date instead of entry date | Fix before go-live, or written risk acceptance by the business owner and the Manager |
| Medium | A Should requirement fails, or a Must fails with a safe workaround | Qualification screen hides the certification end date, but the report shows it | Fix date agreed before go-live |
| Low | Cosmetic; no effect on data or decisions | Column label misspelled | Backlog |

A defect is Deferred only with the business owner's written approval and a linked Jira issue.

### 10. Evidence rules

- Save evidence in [COMPANY: UAT evidence folder], named [Test case ID]_[YYYY-MM-DD]_[initials].
- Screenshots show the record key, the values tested and the system date or time.
- Keep output files (broker feed files, cost files) exactly as produced; do not edit them.
- Write the actual result in words and values, even on a pass ("Duty $2,750.00, as expected"), not just "as expected".
- Retain evidence per [COMPANY: records retention policy].

### 11. Summary and sign-off

| Measure | Count |
|---|---|
| Test cases planned | [n] |
| Passed | [n] |
| Failed | [n] |
| Blocked or not run | [n] |
| Open defects: Critical, High, Medium, Low | [n, n, n, n] |
| Recommendation | [Go, Go with conditions, No go] |

| Role | Name | Decision | Date | Conditions |
|---|---|---|---|---|
| Business owner | [ ] | [Go, Go with conditions, No go] | [ ] | [ ] |
| UAT lead | [ ] | [Exit criteria met: Yes or No] | [ ] | [ ] |
| Checker | [ ] | [Evidence reviewed] | [ ] | [ ] |
| Data owner | [ ] | [Reconciliation accepted] | [ ] | [ ] |
| Manager | [ ] | [ ] | [ ] | [ ] |

## Filled example (illustrative)

e2open GTM UAT cycle 1: classification, USMCA and duty. All items, rates and dates are hypothetical test values; real expected results come from the current tariff schedules and a checked Tariff-Impact Brief on the test date.

### Test cases

| ID | Steps | Expected | Actual | Pass/Fail |
|---|---|---|---|---|
| TC-01 (TS-01) | Pre: test item A is classified in US subheading 7318.16 (nuts); 10-digit numbers taken from the current HTSUS. 1. As maker, change the US classification to subheading 7318.15 (other screws and bolts), effective today. 2. As checker, approve. 3. Run the US broker feed job in test. 4. Open the feed file and search for item A. | Item A appears once, for US only, with the new 10-digit number and today's effective date. No row with the old number. Feed row count equals the previous run. CA and MX classifications unchanged. Change log shows maker, checker and timestamps. | As expected. Row count 13,744 both runs. Evidence: TC-01_[date]_HA.png and the feed file | Pass |
| TC-02 (TS-02) | Pre: test item B is produced in Mexico from one non-originating material that meets the product-specific rule used for this test; supplier certification on file, blanket period 12 months, current. 1. Run USMCA qualification for item B. 2. Compare with Research's hand-worked result. | Result: Qualifies, origin criterion B (non-originating materials that satisfy the product-specific rule). Qualification valid no later than the certification's blanket-period end date. | Qualifies, criterion B; validity end matches the certification | Pass |
| TC-03 (TS-03) | Pre: US import of item C, 1,000 units, entered value $10,000.00, international freight $800.00. Hypothetical rates: base 2.5%, plus an additional 25% that the brief says stacks. 1. Run the landed-cost calculation for item C. 2. Compare duty with the Tariff-Impact Model, and landed cost with the hand calculation. | Duty $2,750.00 (entered value x 27.5%), that is $2.75 per unit, equal to the model's duty per unit after the action. Freight is not in the US duty base. Landed cost per unit (entered value + freight + duty + MPF, and HMF if it is an ocean shipment, at the current rates in `docs/primers/current-tariff-landscape.md`, + [COMPANY: other components agreed with Finance]) equals the hand calculation within $0.01. | Duty $2,750.00 ($2.75 per unit, equal to the model); landed cost per unit matches the hand calculation to $0.00 | Pass |
| TC-04 (TS-06) | Pre: Mexico import of item D, invoice $10,000.00, freight to the border $800.00, insurance $50.00; hypothetical IGI rate 10%. 1. Run the duty calculation. | Customs value $10,850.00 (Mexico includes freight and insurance to the point of entry); IGI $1,085.00. Other Mexican charges follow [COMPANY: landed-cost rules agreed with Finance and the agente aduanal]. | Customs value $10,850.00; IGI $1,085.00 | Pass |
| TC-05 (TS-04) | Pre: hypothetical action effective for goods entered for consumption on or after 12:01 a.m. eastern time on 2027-03-01. Item C entry 1 dated 2027-02-28, entry 2 dated 2027-03-01, both from POs dated 2027-01-15. 1. Run duty for both entries. | Entry 1: base 2.5% only. Entry 2: 27.5%. The PO date has no effect. | Both entries got 2.5%: the rate was chosen by PO date | Fail: D-01 |
| TC-06 (TS-08) | 1. As maker, change a duty rate. 2. Try to approve the same change with the same user. | Approval is refused with a message; the change stays pending | Refused; change pending | Pass |

More effective-date cases to add when they apply: a warehouse withdrawal for consumption on or after the effective date (the rate in effect at withdrawal applies); goods covered by an in-transit provision in the action; an action with an end date; and, if the system stores times in UTC, an entry late in the evening eastern time on the day before the effective date.

### Defect log

| ID | Severity | Description | Status | Owner |
|---|---|---|---|---|
| D-01 | High | TC-05: the rate is selected by PO date, not entry date. Expected 27.5% for entry 2, got 2.5%. Evidence TC-05_[date]_HB.xlsx | In fix | [COMPANY: e2open configuration lead] |
| D-02 | Medium | TC-02: the qualification screen does not show the certification end date; the qualification report does (workaround) | Triaged; fix date [date] | [COMPANY: e2open configuration lead] |

Status: Not ready to exit. D-01 is High and still open; TC-05 must be retested after the fix, with TC-03 re-run as regression.

## Quality checklist before you send

- [ ] Every Must requirement or acceptance criterion has at least one test case, linked by ID.
- [ ] Negative and boundary cases are included (effective-date edges, missing data, the maker trying to approve their own change).
- [ ] Expected results have exact values, worked out before execution and checked against the model or brief.
- [ ] Rates and dates in expected results come from a checked Tariff-Impact Brief, not from memory.
- [ ] Test data is in the test environment; no testing in production; sensitive data is protected.
- [ ] Entry criteria were met, and the checker reviewed the cases before execution.
- [ ] Actual results are written in words and values, with evidence saved under the naming rule.
- [ ] Each failure has a defect with a severity using the definitions above, linked to its case.
- [ ] Fixed defects were retested, with regression on related cases.
- [ ] The exit criteria are checked one by one, and sign-off is recorded with any conditions.
