sar_twoway = SAR(formula=formula, unit_effects="fixed", time_effects=True, **panel_kwargs)
sar_twoway.fit(**fit_kwargs)

# rho falls by about a third: part of what looked like spillover between neighbors
# was the national rise and fall of homicide that every county shared
sar_twoway.summary(var_names=["rho"], round_to=3)
