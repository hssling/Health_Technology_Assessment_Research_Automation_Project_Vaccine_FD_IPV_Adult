# HTA Automation Report – hta_project_09_home_based_elderly_care

**Generated:** 2025-11-02 15:19:43

## 1. Protocol (parsed)
# HTA Protocol: Home-Based Elderly Care Packages vs Institutional/Facility-Based Care under Ayushman Bharat / State Schemes in India

## 1. Background
India is experiencing rapid population ageing, with a growing proportion of people ≥60 years living with multimorbidity (HTN, DM, CKD, COPD, dementia, stroke sequelae) and functional limitations. Current public financing (PM-JAY and state health schemes) is mainly geared toward **acute inpatient episodes** rather than **long-term, home-based, or palliative care**. Families therefore bear substantial out-of-pocket expenditure, informal care burden, and productivity loss. Several states and large hospital groups are piloting **home-health / hospital-at-home / elder-care packages** which provide periodic nurse/physio/doctor visits, basic diagnostics, teleconsults, and medicine delivery at home.

There is a policy question: *Is it more cost-effective for the health system to finance structured, home-based geriatric care packages — which may reduce hospitalizations — than to continue paying only for episodic facility-based care?* This HTA aims to answer that.

## 2. Objectives
**Primary objective:**
- To compare the cost-effectiveness of (a) structured home-based elderly care packages vs (b) usual, primarily facility-based care (OPD + episodic hospitalization) for older adults with ≥1 chronic NCD.

**Secondary objectives:**
- To estimate the budget impact of including home-based elderly care in PM-JAY / state schemes.
- To identify subgroups in whom home care is likely to be cost-saving (bed-bound, post-stroke, advanced COPD/CHF).
- To analyze the effect on caregiver time and catastrophic health expenditure.

## 3. PICO
- **Population:** Adults ≥60 years, enrolled/eligible under PM-JAY/state schemes, with at least one chronic condition or functional limitation.
- **Intervention:** Home-based elderly care package (nurse visit 1–4x/month, teleconsult, basic labs, medicines refill, rehab/physio, emergency escalation).
- **Comparator:** Usual care — OPD visits + unplanned hospital admissions + private/home nurse paid OOP.
- **Outcomes:** Hospitalizations averted, emergency visits averted, QALYs gained (better function, fewer complications), caregiver hours saved, total health system cost.
- **Perspective:** Health system / payer; secondary societal (include caregiver time).
- **Time horizon:** 1 year (base case) and 3–5 years (sensitivity).
- **Discounting:** 3% for >1 year.

## 4. Methods
- Model: annual decision tree / simple Markov with 3 states:
  1. At home – stable
  2. Hospitalized / acute episode
  3. Death
- Transition probabilities differ for home-care vs usual care (home care assumed to reduce hospitalizations).
- Costs:
  - Home-care package monthly cost (HR, travel, telemedicine, consumables)
  - Usual care OPD cost
  - Hospitalization cost for acute event
  - Informal care hours (societal analysis)
- Outcomes:
  - QALYs using utility weights: stable at home (0.7–0.8), post-hospitalization (0.6), institutionalized (0.5)
  - Cost per hospitalization averted
  - Cost per QALY gained

## 5. Sensitivity / Scenario Analysis
- One-way: home-visit frequency, nurse salary, hospital cost, hospitalization risk reduction.
- Scenario: urban vs rural, with different travel costs.
- Scenario: high-risk group only (bed-bound / stroke / dementia).

## 6. Budget Impact
- Inputs: number of elderly enrolled in scheme, % eligible, package cost/year, expected reduction in inpatient spending.
- Output: net budget change for scheme in 1 and 5 years.

## 7. Outputs
1. Search strategy
2. Data extraction sheet
3. Python model
4. BIA CSV
5. Draft manuscript/policy brief


## 2. Search Strategy
PubMed search:
(("home care services"[Mesh] OR "home-based care" OR "hospital at home" OR "community geriatric care" OR "home health nursing")
AND (elderly OR older adults OR geriatric)
AND (India OR "South Asia" OR LMIC)
AND (cost OR "cost-effectiveness" OR "economic evaluation" OR HTA OR "budget impact"))
OR
(("long-term care" OR "institutional care" OR "nursing home")
AND (India)
AND (cost OR financing OR PM-JAY OR "health insurance"))

Grey literature:
- NPHCE (National Programme for Health Care of the Elderly) guidelines
- PM-JAY / NHA documents on long-term care / packages
- State pilot projects on home health / geriatric outreach


## 3. Model Output (stdout)
```
Usual care – hospitalizations: 350.0 cost: 8800000.0 QALY-like: 715.0
Home care – hospitalizations: 220.0 cost: 27060000.0 QALY-like: 750.0
Incremental cost: 18260000.0
Hospitalizations averted: 130.0
Incremental QALYs: 35.0
ICER (INR per hospitalization averted): 140461.53846153847
ICER (INR per QALY gained): 521714.28571428574

```

## 4. Draft Manuscript (template)
# Draft Manuscript – Home-Based Elderly Care vs Facility-Based Care in India

## Title
Cost-Effectiveness of Structured Home-Based Elderly Care Packages Compared with Usual Facility-Based Care under Indian Public Financing Schemes: A Health Technology Assessment

## Abstract
...

## Sections
1. Introduction – ageing, NPHCE, PM-JAY gap for long-term care
2. Methods – decision/Markov model, inputs, costs
3. Results – hospitalizations averted, ICER
4. Discussion – feasibility, HR requirements, urban/rural differences
5. Conclusion – policy options


## 5. Orchestrator Log
```
=== Processing project: hta_project_09_home_based_elderly_care ===
Protocol: loaded.
Search strings: loaded.
Literature search: starting...
Literature search: completed, extracted 14 data points.
Data processing: starting...
Data processing: completed, filled 14 rows.
R: executed.
R stderr:
â”€â”€ Attaching core tidyverse packages â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ tidyverse 2.0.0 â”€â”€
âœ” dplyr     1.1.4     âœ” readr     2.1.5
âœ” forcats   1.0.0     âœ” stringr   1.5.2
âœ” ggplot2   4.0.0     âœ” tibble    3.3.0
âœ” lubridate 1.9.4     âœ” tidyr     1.3.1
âœ” purrr     1.1.0     
â”€â”€ Conflicts â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ tidyverse_conflicts() â”€â”€
âœ– dplyr::filter() masks stats::filter()
âœ– dplyr::lag()    masks stats::lag()
â„¹ Use the conflicted package (<http://conflicted.r-lib.org/>) to force all conflicts to become errors

Model: executed 04_elderly_homecare_model.py
Model stdout:
Usual care – hospitalizations: 350.0 cost: 8800000.0 QALY-like: 715.0
Home care – hospitalizations: 220.0 cost: 27060000.0 QALY-like: 750.0
Incremental cost: 18260000.0
Hospitalizations averted: 130.0
Incremental QALYs: 35.0
ICER (INR per hospitalization averted): 140461.53846153847
ICER (INR per QALY gained): 521714.28571428574

Manuscript generation: starting...
Manuscript generation: completed.
```