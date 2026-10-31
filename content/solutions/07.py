graph_rook = Graph.build_contiguity(chi).transform("r")

model_rook = SAR(formula="ypll ~ Blk14P + Hisp14P + HIS_ct", data=chi, W=graph_rook)
model_rook.fit(draws=1000, tune=1000, chains=4, random_seed=42)

# rho moves from about 0.12 to about 0.15, less than half a posterior standard deviation
model_rook.summary(var_names=["rho"], round_to=3)
