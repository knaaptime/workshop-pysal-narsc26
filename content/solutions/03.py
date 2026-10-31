income = san_diego["median_household_income"]
income_graph = graph
if income.isna().any():
    # drop tracts without income and rebuild the graph on the rest
    keep = income.notna()
    income = income[keep]
    income_graph = Graph.build_contiguity(san_diego[keep], rook=False).transform("r")

np.random.seed(12345)
mi_income = esda.Moran(income, income_graph)
print(f"Moran's I, income: {mi_income.I:.3f} (home value: {mi.I:.3f})")

np.random.seed(12345)
li_income = esda.Moran_Local(income, income_graph)
clusters = san_diego.loc[income.index].assign(
    income_cluster=li_income.get_cluster_labels(crit_value=0.05)
)
print(pd.crosstab(clusters["cluster"], clusters["income_cluster"]))
li_income.plot(san_diego.loc[income.index], crit_value=0.05, figsize=(8, 8));
