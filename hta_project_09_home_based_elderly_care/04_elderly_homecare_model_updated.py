"""Home-based elderly care vs usual facility-based care – simple annual model"""

elderly_population = 1000

# placeholder inputs (to be overwritten from extraction sheet)
homecare_cost_month = 1800     # INR
hospitalization_rate_usual = 0.35
hospitalization_rate_home = 0.22
inpatient_cost = 18000
opd_cost_usual = 2500
opd_cost_home = 1500

utility_home = 0.75
utility_post_hosp = 0.6
mortality_rate = 0.05

def strategy_usual():
    hosp_events = elderly_population * hospitalization_rate_usual
    cost = (
        elderly_population * opd_cost_usual +
        hosp_events * inpatient_cost
    )
    qaly = (
        elderly_population * (utility_home - (hospitalization_rate_usual * 0.1))  # small disutility
    )
    return hosp_events, cost, qaly

def strategy_homecare():
    hosp_events = elderly_population * hospitalization_rate_home
    cost = (
        elderly_population * opd_cost_home +
        elderly_population * homecare_cost_month * 12 +
        hosp_events * inpatient_cost
    )
    qaly = (
        elderly_population * utility_home  # better stability
    )
    return hosp_events, cost, qaly

if __name__ == "__main__":
    h_u, c_u, q_u = strategy_usual()
    h_h, c_h, q_h = strategy_homecare()

    incr_cost = c_h - c_u
    hosp_averted = h_u - h_h
    incr_qaly = q_h - q_u

    icer_per_hosp = incr_cost / hosp_averted if hosp_averted > 0 else None
    icer_per_qaly = incr_cost / incr_qaly if incr_qaly > 0 else None

    print("Usual care – hospitalizations:", h_u, "cost:", c_u, "QALY-like:", q_u)
    print("Home care – hospitalizations:", h_h, "cost:", c_h, "QALY-like:", q_h)
    print("Incremental cost:", incr_cost)
    print("Hospitalizations averted:", hosp_averted)
    print("Incremental QALYs:", incr_qaly)
    print("ICER (INR per hospitalization averted):", icer_per_hosp)
    print("ICER (INR per QALY gained):", icer_per_qaly)
