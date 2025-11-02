"""AMR / POCT + AMS vs empirical antibiotic use – decision model"""

patients = 1000
baseline_antibiotic_rate = 0.7
post_poct_rate = 0.4
test_cost = 200
training_cost_per_patient = 20
antibiotic_cost = 100
complication_cost = 800

amr_infection_rate_base = 0.05
amr_infection_rate_poct = 0.035
amr_treatment_cost = 25000

def strategy_empirical():
    ab_users = patients * baseline_antibiotic_rate
    amr_cases = patients * amr_infection_rate_base
    cost = (
        ab_users * antibiotic_cost +
        amr_cases * amr_treatment_cost
    )
    return ab_users, amr_cases, cost

def strategy_poct():
    ab_users = patients * post_poct_rate
    amr_cases = patients * amr_infection_rate_poct
    cost = (
        patients * (test_cost + training_cost_per_patient) +
        ab_users * antibiotic_cost +
        amr_cases * amr_treatment_cost
    )
    return ab_users, amr_cases, cost

if __name__ == "__main__":
    ab_u, amr_u, cost_u = strategy_empirical()
    ab_i, amr_i, cost_i = strategy_poct()

    incr_cost = cost_i - cost_u
    ab_avoided = ab_u - ab_i
    amr_averted = amr_u - amr_i

    icer_ab_avoid = incr_cost / ab_avoided if ab_avoided > 0 else None
    icer_amr_avert = incr_cost / amr_averted if amr_averted > 0 else None

    print("Empirical – antibiotics used:", ab_u, "AMR cases:", amr_u, "cost:", cost_u)
    print("POCT+AMS – antibiotics used:", ab_i, "AMR cases:", amr_i, "cost:", cost_i)
    print("Incremental cost:", incr_cost)
    print("Antibiotics avoided:", ab_avoided)
    print("AMR infections averted:", amr_averted)
    print("ICER (INR per antibiotic avoided):", icer_ab_avoid)
    print("ICER (INR per AMR infection averted):", icer_amr_avert)
