# M17 – Finding Correlations (16/03/2023)

## Progress
- Resampled games to exclude Rated Bullet and abandoned games.
	- Updated the final report commentary accordingly.
- Explored metrics and plotted distribution of `EloDiff` and  `RelativeEloDiff` bins.
- Plotted the correlation between rating differential and White win rate using both `EloDiff` and `RelativeEloDiff` bins.
- Improved readability of plots by using the `darkgrid` style.
- Calculated the popularity of the Sicilian Defense by rating group.
	- Try stacked bars, otherwise have separate plots.
- Improved readability of instructions in the README.

## Questions
- Should I avoid plotting data for bins where the sample size is very small (e.g. bins with high rating differential, top tiers of rated players)?
	- Shorten x-axis to exclude groups with very small samples
- How would the introduction be different in the final report to the literature review for my project specifically?
	- Focus more on the emphasising the process of data mining and extracting data to such a large scale?
		- Fairly structured data, but not necessarily suited for analytics
		- Too much information / information that’s difficult to extract?
		- Mention creating a framework for future studies into chess games.
- How could I create a regression using rating bins (x-axis) and the popularity of an opening when it wins/loses (y-axis)?
	- Probability of a win as a function of EloDiff using logistic regression
	- Predict whether someone will win based on three factors:
		- Their ELO (numerical)
		- Opponent’s rating (numerical)
		- Opening (categorical – may need to encode to numerical)
			- 100 dimensional vector for 100 possible openings
				- 0s represent opening not played, single 1 to represent opening played
				- May be limited as we don’t know how many openings there are, but can’t predict with new openings with other methods either
					- Cold start problem
			- Decision trees
				- [R2D3 Visual Intro to ML](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)
				- scikit-learn identifies entropy for me
				- Count outcomes from each leave to determine probability
			- Random forest – trains ensemble of trees to classify
				- [StatQuest YouTube channel](https://www.youtube.com/@statquest/videos)
				- More transparent classifier
				- Shorter trees – 1-3 levels deep
				- Train several trees and get the average of them
			- Win rate differential between base win rate and win rate for opening (feature engineering – makes model less of a black box)
		- Alternatively, try just the opening
		- Regular test-train split or stratified test-train split
			- Stratified on rating bins?
		- Confidence of prediction may differ between rating and opening
			- Initial hypothesis – opening matters more at lower ratings