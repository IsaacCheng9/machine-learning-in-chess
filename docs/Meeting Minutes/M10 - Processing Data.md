# M10 – Processing Data (19/01/2023)

## Agenda
- Focused on data processing

### Difficulties with Big Data
- Starting by focusing on rated Blitz, Rapid, and Bullet games
- Mention this in the final report
	- Testing Scoutfish – reason to use it, what it is, and the conclusion
	- How useful is performing analysis on just a single day?
		- Large scale of people playing on a given day might still produce good insights
		- Compare one day with one week to see whether patterns are clearer
	- Are the least random patterns found amongst the elite players?
		- What percentile are within this ELO range?
		- Patterns found amongst the elite may not necessarily apply to the general population
	- Explain directions and why you chose them
- [Parsing Large PGN Files Efficiently](https://www.reddit.com/r/learnpython/comments/gmogd0/how_do_i_parse_large_pgn_files_efficiently/)
- [Estimating Playing Strength in Chess](https://patzersreview.blogspot.com/2020/05/estimating-playing-strength.html)
- [Kaggle Example of Lichess DB EDA](https://www.kaggle.com/code/ironicninja/converting-raw-chess-pgn-to-readable-data/notebook)
#### Individual Game Analysis
- Analysing each game takes a long time, even if only looking at the last move. How should we approach this?
	- Perform stratified sampling on the types of games
		- Proportion of players in each bin etc.
		- Need to think about what scale is manageable – could also mention this in the report
#### Metadata Analysis
- Even analysing the metadata takes a long time due to the large number of games.
	- Multi-threading seems like it's no good (useful for IO-bound tasks, but we're CPU-bound)
	- Multi-processing is likely to be useful – need to look into this more
		- Use this on chunks of PGN files (split into 10 segments)
	- Probably only have to do this once
	- Do you have alternative suggestions?
		- Iterate on a smaller sample – first ~3 million games of the month?
- Processing could be faster on Chico's machine?
	- Set up access and perform some benchmarks so we can see whether it's actually faster for our use case – single-core performance seems most important
#### Potential Workarounds
- Use [Scoutfish](https://github.com/mcostalba/scoutfish) for fast processing
	- Also recommended by Lichess
	- Generates a `.scout` file which indexes the PGN file and is much smaller in size
		- 213.91 GB -> 13.38 GB for August 2022 sample
	- Currently unable to get the queries working – need to spend more time investigating this
- Convert PGN to CSV with [pgn2data](https://github.com/zq99/pgn2data) library
	- Advantage of sticking to common data structures
	- Likely similar performance to my implementation, but may enable converting to Pandas DataFrame, which uses NumPy
		- NumPy library is written in C and wrapped in Python for easy access – significant performance gains
	- Potential limitation in DataFrame size (100GB?)
		- Use `chunksize` parameter in `pandas.read_csv()` function as a workaround
- Use [Dask](https://docs.dask.org/en/stable/) as a parallel computing alternative to Pandas
	- [Comparison of Dask vs. Pandas](https://medium.com/featurepreneur/pandas-vs-dask-the-power-of-parallel-computing-994a202a74bd)
	- [Explanation of Dask vs. Pandas](https://towardsdatascience.com/are-you-still-using-pandas-for-big-data-12788018ba1a)
	- Likely significant performance gains
- Use [Lichess Elite Database](https://database.nikonoel.fr/) (only games of 2500+ vs. 2300+ ELO players)?
	- Smaller data sample – trivial size to process
	- Limits our ELO-based research, which could be a significant loss
	- Could use it as a guinea pig for types of analysis that we want to perform

### Types of Analysis
- What types of metadata analysis might be most useful to begin with?
	- Distribution of ELO ranges (active player skill distribution)
	- White vs. black win rate per game type
	- Most popular and most effective openings
	- Influence of ELO difference on win probability
		- Normalised by white/black win rate?
		- Differential as a percentage of the mean ELO between players?
	- **Blunder rate by ELO**
	- **Categorising players by playstyle**
		- How aggressive they are / tendency to have more open games
		- Highlight specific players such as famous pros
			- Chess.com may provide game data
- Could test conclusions near the end of the project by looking at examples from specific games (in-depth qualitative discretionary analysis to give a human interpretation)
	- Low priority?
	- [Scid Chess DB Analyser](https://scid.sourceforge.net/)
	- For example, what counts as a blunder?

### Timelines
- What were your experiences with previous students and their timelines?
- Rough targets for:
	- First directions – February
	- Explore various directions – before April
		- Depends on type of project
	- Stop pursuing new directions and start writing report – April
		- A lot will be borrowed from the lit review
	- Complete full code implementation and final report – May
		- Don't worry too much about documentation – enough to remember how useful it is
## Other Feedback
- Continue doing what I'm doing so far and coming up with new directions such as blunder rate by ELO