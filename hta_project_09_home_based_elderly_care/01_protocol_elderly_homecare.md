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
