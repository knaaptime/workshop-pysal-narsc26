#### 1

results = {}

for county in scag.county.unique():
    results[county] = MultiInfoTheory(scag[scag.county == county], pop_groups).statistic
    print(f"{county} information theory index: {results[county]:.3f}")


#### 2

rside_gini = Gini(scag[scag.county == "Riverside"], "n_hispanic_persons", "n_total_pop")
vent_gini = Gini(scag[scag.county == "Ventura"], "n_hispanic_persons", "n_total_pop")

print(f"\nRiverside Gini: {rside_gini.statistic:.3f}")
print(f"Ventura Gini: {vent_gini.statistic:.3f}")
ginitest = TwoValueTest(rside_gini, vent_gini)
print(f"p value of the difference: {ginitest.p_value}")
ginitest.plot()
