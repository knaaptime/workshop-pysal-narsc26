from neighbayes.models import SDEM

sdem = SDEM(formula=formula, data=chi, W=graph)
sdem.fit(**fit_kwargs)

# the error process does not enter the effects, so SDEM's effects are SLX's,
# and all three models agree once the neighbors' covariates are in
sdem.impacts()
