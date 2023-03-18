# P2 – Project Plan

## To Do
### In Progress
- Review cells with `elo_diff_wins` – are they implemented correctly?
	- Do I need to use `count()` instead of `sum()`?
### Backlog
- Explain how the most popular opening categories and most popular base openings vary by rating.
- Write about the impact of rating differential on White win rate.
- Write about manual data exploration in the report (at the end of the design section?).
- Complete introduction section of the final report (see [[P3 - Final Report and Demonstration Plan]]).
- Look into merging the first pages of the original template with my own template.
### Ideas
#### Machine Learning
- How does the win rate of openings vary with ratings?
	- x-axis – rating bins
	- y-axis – popularity of a specific opening when it wins/loses
		- Split colour of the bar to show win/loss rate?
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
				- StatQuest: [part 1](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ), [part 2](https://www.youtube.com/watch?v=sQ870aTKqiM)
				- More transparent classifier
				- Shorter trees – 1-3 levels deep
				- Train several trees and get the average of them
				- Can also draw a heat map or MDS plot to show the samples are related to each other
			- Win rate differential between base win rate and win rate for opening (feature engineering – makes model less of a black box)
		- Alternatively, try just the opening
		- Regular test-train split or stratified test-train split
			- Stratified on rating bins?
		- Confidence of prediction may differ between rating and opening
			- Initial hypothesis – opening matters more at lower ratings
	- Use it to create a regression to predict win rate given these scenarios?
		- Game theory
			- Table
			- Decision tree?
		- Nash equilibrium?
	- Probability of a win as a function of EloDiff using logistic regression
- Investigate variations of the same opening
	- Do variations share the same performance curves as rating changes?
	- Distance metric for similarity
		- Distances between bars in the performance curves
		- Use agglomerative clustering instead of K-means
	- Cluster openings that perform the same
		- Openings that often result in draws vs. wins
		- No train-test split – cluster and then perform clustering validation
			- Silhouette – tightness of clusters
- SHAP values – feature importance
	- Strength of input values on output
	- How do various features increase the likelihood of a player winning
	- Potential features:
		- RelativeEloDiff
		- Opening
		- Number of games played in sample
			- May be difficult because we’re not using the full population
		- Event
		- Number of moves
		- How does the game end?
			- Need to use Scoutfish for this, or redo pipeline to include number of moves?
#### Misc
- Popularity of openings vs. complexity
	- Complexity measured as number of moves?
	- Initial hypothesis – simpler openings are more popular as they’re easier to learn.
- Look into database for detecting each opening (mapping name of opening to sequence of first moves).
- Calculate the count of games each player has played.
- Try getting Elo distribution of unique players (take highest or lowest Elo for each player).
- Investigate whether we can use the additional fields from chess-openings repository to work with Scoutfish.
	- UCI notation to sub-FEN?

## Metadata Analysis
### High-Level
#### Probability of Chess Piece Positions
- Heat map of chess piece positions
	- Initial hypothesis – probabilities are more spread out at higher ELO
		- Higher skilled players activate their pieces more
	- Initial hypothesis – probabilities are less spread at smaller 
	- Perform analysis based on ECO code categorisations
		- Open and close games, how they cause piece probabilities to differ
#### Categorising Players by Playstyle
- How aggressive they are / tendency to have more open games
- Highlight specific players such as famous pros
	- Chess.com may provide game data
#### Most Popular and Most Effective Openings
- Compare this by ELO rating
- Initial hypothesis – variation in openings converges as ELO rating increases due to social learning theory
	- Potential spike at the tail end – surprise factor
- Difficult to measure variation
	- Probability distribution based on likeliness of playing a given opening – group ELO ratings if individual players isn't possible
		- Backtest against different data sets to validate hypotheses
	- High or low entropy
#### Others
- Distribution of ELO ranges (active player skill distribution)
- White vs. black win rate per game type
- Influence of ELO difference on win probability
	- Normalised by white/black win rate?
	- Differential as a percentage of the mean ELO between players?

### Low-Level
#### Blunder Rate by ELO
- Average number of moves by ELO rating
	- Initial hypothesis – this should increase as ELO rating increases as players are less likely to make game-changing blunders at an earlier stage
		- Talk about lack of universal definition of a game-changing blunder vs. other blunders
		- How we quantified a game-changing blunder – lose a Queen and resigned within a move?
	- Initial hypothesis – rate of resignations after specific pieces increases as ELO rating increases
		- Relative piece value (percentage of their total piece value)
	- If they made a game-changing blunder and didn't resign, what was the outcome?
 - Look at examples of our hypotheses in practice from specific games (in-depth qualitative discretionary analysis to give a human interpretation)
	 - What counts as a blunder?
## Timelines
- February – first directions
- Before April – explore various directions
	- Depends on type of project
- April – stop pursuing new directions and start writing report
	- A lot will be borrowed from the lit review
- May – complete full code implementation and final report
	- Don't worry too much about documentation – enough to remember how useful it is
