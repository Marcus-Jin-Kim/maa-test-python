import statsmodels.api as sm
import numpy as np
duncan_prestige = sm.datasets.get_rdataset("Duncan", "carData")

print(duncan_prestige.data)

Y = duncan_prestige.data['income']
X = duncan_prestige.data['education']



X = sm.add_constant(X)
model = sm.OLS(Y,X)
results = model.fit()
print(results.params)

print(results.summary())
