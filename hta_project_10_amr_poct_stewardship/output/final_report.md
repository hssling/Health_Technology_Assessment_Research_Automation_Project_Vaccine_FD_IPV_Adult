# HTA Automation Report – hta_project_10_amr_poct_stewardship

**Generated:** 2025-11-02 15:20:02

## 1. Protocol (parsed)
# HTA Protocol: Antimicrobial Stewardship and Point-of-Care Testing vs Empirical Antibiotic Use at Primary Care Level in India

## 1. Background
India faces one of the highest rates of antibiotic consumption and antimicrobial resistance (AMR) globally. A key driver is empirical antibiotic prescribing for febrile and respiratory illnesses at primary and secondary levels without diagnostic confirmation. Point-of-care tests (POCT) such as C-reactive protein (CRP), procalcitonin (PCT), or rapid bacterial/viral panels, when integrated with antimicrobial stewardship (AMS) training, can potentially reduce inappropriate antibiotic use.

This HTA evaluates whether introducing POCT + AMS is cost-effective compared to current empirical antibiotic practices in primary care settings, and estimates the programmatic budget impact.

## 2. Objectives
- **Primary:** Evaluate cost-effectiveness (cost per antibiotic prescription avoided; cost per AMR infection averted) of POCT + AMS versus empirical antibiotics.
- **Secondary:** Estimate budget impact for NHM/state health systems and identify thresholds where POCT + AMS is cost-saving.

## 3. PICO
- **Population:** Patients with acute febrile or respiratory illness attending PHC/CHC outpatient clinics.
- **Intervention:** POCT (CRP or equivalent) + AMS training and feedback.
- **Comparator:** Current practice (empirical antibiotic use without diagnostics).
- **Outcomes:** Reduction in antibiotic use, AMR infections averted, cost per case managed, cost per QALY gained.
- **Perspective:** Health system; secondary societal.
- **Time horizon:** 1 year (base case); 5 years (for AMR progression).
- **Discounting:** 3%.

## 4. Methods
- Decision tree linking infection etiology, test accuracy, antibiotic use, and outcomes.
- Costs:
  - POCT device and consumable per test.
  - AMS training and supervision.
  - Antibiotic and complication treatment costs.
- Effectiveness:
  - Reduction in antibiotic prescribing rate.
  - Reduced AMR infection probability over time.

## 5. Sensitivity / Scenario Analysis
- One-way: test cost, baseline antibiotic overuse rate, adherence to test results, AMR prevalence.
- Scenario: CRP-only vs multiplex POCT, urban vs rural clinics, public vs private.

## 6. Budget Impact
- Inputs: annual PHC outpatient load, suspected infections, test coverage, cost/test, antibiotic cost savings.
- Outputs: incremental program cost, antibiotics saved, net system cost change.

## 7. Outputs
1. Search strategy
2. Data extraction sheet
3. Python model
4. BIA CSV
5. Draft manuscript


## 2. Search Strategy
PubMed search:
(("point-of-care testing"[Mesh] OR "rapid diagnostic tests" OR CRP OR procalcitonin OR PCT OR "rapid viral tests")
AND ("antimicrobial stewardship" OR "antibiotic use" OR "antimicrobial resistance")
AND (India OR LMIC)
AND (cost OR "cost-effectiveness" OR "health technology assessment" OR HTA OR "economic evaluation"))
AND ("2005/01/01"[Date - Publication] : "3000"[Date - Publication])

Grey literature:
- ICMR AMR policy papers
- WHO GLASS India reports
- NHM operational guidelines


## 3. Model Output (stdout)
```
Empirical – antibiotics used: 700.0 AMR cases: 50.0 cost: 1320000.0
POCT+AMS – antibiotics used: 400.0 AMR cases: 35.0 cost: 1135000.0
Incremental cost: -185000.0
Antibiotics avoided: 300.0
AMR infections averted: 15.0
ICER (INR per antibiotic avoided): -616.6666666666666
ICER (INR per AMR infection averted): -12333.333333333334

```

## 4. Draft Manuscript (template)
# Draft Manuscript – Antimicrobial Stewardship and Point-of-Care Testing at Primary Care Level in India

## Title
Cost-Effectiveness of Point-of-Care Testing Combined with Antimicrobial Stewardship Compared to Empirical Antibiotic Use in Primary Care Settings in India: A Health Technology Assessment

## Abstract
...

## Sections
1. Introduction – AMR burden, inappropriate antibiotic use, policy context
2. Methods – model comparing empirical vs POCT + AMS
3. Results – reduction in antibiotic use and AMR infections; ICERs
4. Discussion – feasibility, diagnostics supply chain, training needs
5. Conclusion – policy implications for ICMR-AMR and NHM


## 5. Orchestrator Log
```
=== Processing project: hta_project_10_amr_poct_stewardship ===
Protocol: loaded.
Search strings: loaded.
Literature search: starting...
Literature search: completed, extracted 5 data points.
Data processing: starting...
Data processing: completed, filled 5 rows.
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

Model: executed 04_amr_poct_model.py
Model stdout:
Empirical – antibiotics used: 700.0 AMR cases: 50.0 cost: 1320000.0
POCT+AMS – antibiotics used: 400.0 AMR cases: 35.0 cost: 1135000.0
Incremental cost: -185000.0
Antibiotics avoided: 300.0
AMR infections averted: 15.0
ICER (INR per antibiotic avoided): -616.6666666666666
ICER (INR per AMR infection averted): -12333.333333333334

Manuscript generation: starting...
Manuscript generation: completed.
```