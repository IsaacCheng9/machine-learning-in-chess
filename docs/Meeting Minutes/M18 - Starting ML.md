# M18 – Starting ML (23/03/2023)

## Progress
- Removed bars in plots that represented insignificant sample sizes.
- Added additional plots to the appendices to show differences in popularity of opening categories and base openings at higher and lower rating groups.
	- Added commentary explaining the differences.
- Investigated machine learning with `dask-ml` to implement a decision tree classifier.
	- May not be able to implement decision tree / random forest / XGBoost classifiers in Dask?
	- Worst case scenario – scale down the data sample size significantly so I can use standard `sklearn` code

## Questions
- Implementing things with Dask is slowing my progress significantly. Should I consider abandoning it?
	- Keep current findings but implement machine learning on a much smaller sample so I can use `sklearn`