graph_knn = Graph.build_knn(chi.representative_point(), k=6).transform("r")

ols_knn = OLS(formula=formula, data=chi, W=graph_knn)
ols_knn.fit(**fit_kwargs)

# the robust tests again fail to separate the lag from the error, and the tree again picks the lag
print(ols_knn.spatial_diagnostics())
ols_knn.spatial_diagnostics_decision()
