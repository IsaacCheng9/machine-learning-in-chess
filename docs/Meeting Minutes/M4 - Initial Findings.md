# M4 – Initial Findings (20/10/2022)

## Agenda
- Provide access to GitHub repository
	- Demonstrate current analysis prototype and future possibilities
- Discuss initial questions to investigate
	- Start simpler and build up to more complex?

## Links
- [GitHub repository: machine-learning-in-chess](https://github.com/IsaacCheng9/machine-learning-in-chess)
- [Lichess Monthly Databases](https://database.lichess.org/#standard_games)
- [Chess analysis in Python](https://blog.propelauth.com/chess-analysis-in-python/)
- [How to Reproduce a Lichess Advantage Chart in Python](https://www.landonlehman.com/post/2021-01-25-how-to-reproduce-a-lichess-advantage-chart-in-python/)
- [Lichess EDA Using Python](https://www.kaggle.com/code/atdata/lichess-chess-games-dataset-eda-using-python)
- [Analysis of Lichess Games](https://www.kaggle.com/code/wojciechmokrzycki/analysis-of-lichess-games/notebook)
- [Analysing Chess Games in Python Part 1: Get the Games](https://yellowtardis.de/2022/03/30/analyzing-chess-games-in-python-part-1-get-the-games/)

## Questions to Investigate
- Easy:
	- Most common openings and their success rates (split by ELO rating and time mode)
	- Popularity of openings over time
	- Distribution of ELO ratings
- Medium:
	- Best counters against particular openings
	- Understanding social learning in chess
		- More advanced players might be more affected by this, as they learn from books, videos, etc.
		- Measure diversity in move set – games may get more homogeneous as rating advances
			- May be true up to a terminal level
- Hard:
	- Clustering similar chess matches
	- Exploring whether the clusters match the classifications into openings and endings
	- Performing dimensionality reduction and classification on a chess match
	- Train a simple, naive neural network, using similar embeddings (vector representation) to predict the new chess moves
		- Could predict based on what pieces are present
		- Decision tree vs neural network to cluster stages of the game
	- How good are current metrics for predicting win probability
		- How accurate this is at different ELO ratings – newer players behave unpredictably

## Current Progress
- Created prototype to parse PGN games using python-chess, and analysing it with Stockfish library
	- Start by looking at final composition (what pieces are on the board) and position
		- Look at all games that finish with a particular endgame, and see if we can identify metrics to differentiate between them

## Literature Review
- Structure:
	- Explain economic and social importance, or why we need to know this
		- Money invested in chess, or to understand cognition and human behaviour
	- Review similar papers to see how they justify this
	- Explaining key words
		- Dealing with unstructured data, vector representations, etc.
	- Explaining existing research on chess, cultural analytics, machine learning
	- Explain the dataset
		- Scale and challenges involved
	- Provide initial ideas for a rough plan
- How clustering is done, and how we validate that it works
	- Could validate by extrinsic methods – comparing whether two types of partitions overlap when they use different clustering methods
	- Could check that points within a cluster are close, and points in different clusters are far apart
		- Silhouette score (Python library) finds the ratio between differences in clusters

## Next Steps
- Improve prototype by writing wrapper functions to use for data analysis
- Focus on initial questions to target
- Create skeleton of the literature review to identify missing areas
- Review content Chico's project resources email (from 17th October)