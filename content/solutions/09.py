results = {}
for outcome in ["y1", "y2", "y3"]:
    model = SARProbit(formula=formula.replace("y1", outcome), data=katrina, W=graph)
    model.fit(**fit_kwargs)
    effects = model.impacts(scale="probability")
    results[outcome] = {
        "rho": model.summary(var_names=["rho"])["mean"].iloc[0],
        "flood direct": effects.loc["flood_dpth", "direct"],
        "flood indirect": effects.loc["flood_dpth", "indirect"],
        "flood total": effects.loc["flood_dpth", "total"],
    }

# as time passes, rho rises and the direct effect of flooding fades, while its
# indirect effect holds steady: a growing share of the flood's damage runs through neighbors
pd.DataFrame(results).round(3)
