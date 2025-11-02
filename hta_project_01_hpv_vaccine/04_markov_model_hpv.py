"""Markov model for HPV vaccination HTA – India
Run inside VS Code / Cline. Replace TODOs with real data extracted from literature.
"""

import numpy as np
import pandas as pd

# STATES
states = ["Susceptible", "HPV_infected", "CIN1", "CIN23", "Cervical_Cancer", "Death"]
n_states = len(states)
cycles = 70  # lifetime horizon (years)
discount_rate = 0.03

# TODO: fill from extraction sheet
annual_transition = {
    ("Susceptible", "HPV_infected"): 0.02,
    ("HPV_infected", "CIN1"): 0.03,
    ("CIN1", "CIN23"): 0.05,
    ("CIN23", "Cervical_Cancer"): 0.02,
}

# baseline mortality (all-cause) – to be filled from SRS life tables
baseline_mortality = 0.01

# vaccine effect – relative risk reduction on infection
vaccine_rr = 0.3   # 70% protection → RR = 0.3

def build_transition_matrix(vaccinated: bool):
    P = np.zeros((n_states, n_states))
    for i, s in enumerate(states):
        P[i, i] = 1.0  # start with stay
    # infection
    inf_rate = annual_transition[("Susceptible", "HPV_infected")]
    if vaccinated:
        inf_rate = inf_rate * vaccine_rr
    P[0, 0] = 1 - inf_rate - baseline_mortality
    P[0, 1] = inf_rate
    P[0, 5] = baseline_mortality

    # HPV_infected → CIN1
    rate = annual_transition[("HPV_infected", "CIN1")]
    P[1, 1] = 1 - rate - baseline_mortality
    P[1, 2] = rate
    P[1, 5] = baseline_mortality

    # CIN1 → CIN23
    rate = annual_transition[("CIN1", "CIN23")]
    P[2, 2] = 1 - rate - baseline_mortality
    P[2, 3] = rate
    P[2, 5] = baseline_mortality

    # CIN23 → Cancer
    rate = annual_transition[("CIN23", "Cervical_Cancer")]
    P[3, 3] = 1 - rate - baseline_mortality
    P[3, 4] = rate
    P[3, 5] = baseline_mortality

    # Cancer
    cancer_mort = 0.15  # annual cancer mortality – to refine
    P[4, 4] = 1 - cancer_mort - baseline_mortality
    P[4, 5] = cancer_mort + baseline_mortality

    # Death – absorbing
    P[5, 5] = 1.0
    return P

def run_markov(vaccinated: bool, cohort_size: int = 100000):
    P = build_transition_matrix(vaccinated)
    cohort = np.zeros((cycles, n_states))
    cohort[0, 0] = cohort_size
    for t in range(1, cycles):
        cohort[t, :] = cohort[t-1, :].dot(P)
    return cohort

def discount(value, t, r=discount_rate):
    return value / ((1 + r) ** t)

# COSTS (placeholders)
cost_vaccine_per_person = 800  # INR, 2 doses @ 400 each
annual_cost_cancer = 120000
annual_cost_cin = 5000

def compute_costs_and_qalys(vaccinated: bool):
    cohort = run_markov(vaccinated)
    total_cost = 0
    total_qaly = 0
    for t in range(cycles):
        pop = cohort[t, :]
        # costs
        cost = 0
        if t == 0 and vaccinated:
            cost += cost_vaccine_per_person * pop.sum() / pop.sum()  # pay once per person
        cost += pop[2] * annual_cost_cin
        cost += pop[4] * annual_cost_cancer
        # QALYs
        qaly = (
            pop[0] * 1.0 +      # healthy
            pop[1] * 0.95 +
            pop[2] * 0.9 +
            pop[3] * 0.85 +
            pop[4] * 0.6
        )
        total_cost += discount(cost, t)
        total_qaly += discount(qaly, t)
    return total_cost, total_qaly

if __name__ == "__main__":
    cost_vacc, qaly_vacc = compute_costs_and_qalys(True)
    cost_novacc, qaly_novacc = compute_costs_and_qalys(False)

    incr_cost = cost_vacc - cost_novacc
    incr_qaly = qaly_vacc - qaly_novacc
    icer = incr_cost / incr_qaly if incr_qaly != 0 else None

    print("Cost (vacc):", cost_vacc)
    print("Cost (no vacc):", cost_novacc)
    print("QALY (vacc):", qaly_vacc)
    print("QALY (no vacc):", qaly_novacc)
    print("ICER (INR per QALY):", icer)
