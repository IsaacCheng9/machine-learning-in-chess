# Initial Meeting (07/06/2022)

## Introduction
-   Not to make an AI that plays chess, but study data on chess
	-   A lot of AI in chess, but not a lot of data science in chess
-   More focus on data science in chess and what can be done
-   For example, someone has studied popularity of openings in Lichess and their timelines
	-   How popularity increases after a popular YouTuber makes a video on them
-   Time series study
-   Easy part is data visualisation
-   More difficult part is dealing with less obvious openings, how many games result in particular endings, probabilities for different scenarios
-   Defining difference between
-   Vectors and clusters – challenge is to find out whether numbers make sense (such as values of a piece)
-   UI not required for this project but possible – focus on data analysis
-   Goal of using results of findings in a publication
	-   Contribute to chess literature – endgames
	-   Contribute to cultural analytics, data science
	-   May create a tool for this, or use it as a research piece for someone else to build upon

## General Ideas
-   Limit the scope to regular game modes
-   Use the Stockfish engine library ([https://pypi.org/project/stockfish/](https://pypi.org/project/stockfish/)) to simulate and analyse positions
-   Precise value of each piece
	-   Win rate with common piece combinations (double bishop, bishop-knight, etc) on average
		-   How this differs in endgames – piece value progression
-   Average number of blunders across ELO ranges
	-   Average win rate for white across ELO ranges
-   Win rate after first ‘blunder’ across ELO ranges
-   Decision trees
	-   Alpha-beta pruning
	-   Can be used for both regression and classification
	-   Random-forest method to produce predictions