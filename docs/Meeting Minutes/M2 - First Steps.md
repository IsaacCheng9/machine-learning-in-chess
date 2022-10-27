# M2 – First Steps (24/06/2022)

## Tools
- Use Lichess open database for standard chess
	- PGN parsing with python-chess
		- Look into how this might work with Python Stockfish library
- Seaborn for data visualisation
	- Requires less configuration than Matplotlib to produce aesthetic visuals
	- Works well with pandas

## Research Ideas
- Compare win rates between pieces, starting with the endgame and then expanding the scope gradually
- Later on, consider training regression or classification of endgame based on how many of each piece are in endgames
	- Worth trying even though there are external factors such as piece combinations rather than just the presence of individual pieces
- Segment games based on player ELO
- Isolate games for different time controls
	- Quantify how strategy changes based on type of time control
	- May use this for data cleaning
- Investigate frequencies of openings and segment them into types of games
	- Varies by player rating, time control, win rate
- Investigate how strategy differs in shorter time control games
	- Lower rated players could be a control group to investigate how higher level players compensate for this
		- May prioritise different pieces

## Strategy
- Good idea to use decision trees as they’re easy to interpret
- Focus on data mining and analysis for the first steps
	- Download database of games and investigate into using Python libraries such as python-chess and stockfish to analyse these
	- Look into loading endgame tables

## Literature Review
- Justify how this project will be useful from both a chess standpoint and data science in cultural
	- Suggest some potential hypotheses and methods
	- Assume that the reader is average lecturer in Computer Science (briefly explain chess concepts, but not machine learning)