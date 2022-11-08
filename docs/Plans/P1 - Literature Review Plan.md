# P1 – Literature Review Plan

## General Advice
- Describe chess concepts as needed, rather than all at the start – makes it flow better
- Use slides 58 onwards from 8.1 of Google Drive lecture slides for clustering etc
- Largest sections are usually preliminary research and design and development
- Title doesn't have to be a question – may change the wording to read better at a later point if needed.

## 1: Introduction – Background and Aim
- Focus on motivation and general statements in the introduction
- Economic importance
	- Large amount of money invested in chess
		- 'The Queen's Gambit' was released in 2020 and is the most poignant example of chess in popular culture
		- The rise of Twitch streamers has made chess become a more mainstream form of entertainment
			- Sponsors such as chess.com have incentivised streamers
	- Number of games played per day has increased drastically recently
- Social importance
	- Cognition and human behaviour in chess games can be applied generally
	- Social learning is a key aspect in chess strategy – players learn from the same material and likely develop homogeneous habits
- Mention that research have been performed on other games like Go – chess isn't the first game to be studied

## 2: Preliminary Research
- Focus on previous research in the field
	- Academic research papers and how they're different to what we're proposing
### 2.1: Growth in the Popularity of Chess
- [chessOpeningStats repository](https://github.com/Paul566/chessOpeningStats)
	- Spike in number of games played daily caused by COVID-19 pandemic and release of 'The Queen's Gambit' series
	- However, continuous growth observed over the last decade regardless
	- Mention that no peer-reviewed academic research has been performed on this, and use it as motivation for this project
	- May need to find more formal studies to back these statements?
### 2.2: Chess Bots and Engines
- Training them using unsupervised learning

## 3: Design and Development
### 3.1: Requirements
- Functional and non-functional requirements
- Functional requirements should link back to the background and aim of the project
- May be best to use Matthew's example as guidance, as the type of data is similar
---
- Start with simpler questions to build a baseline
- Build up to more complex questions using findings from previous questions
- Itemised questions and how we could look to answer them
	- Initial hypotheses based on intuition
	- Methods to investigate these
		- e.g. how to classify
- What questions we won't be looking to answer – restrict scope and set expectations
### 3.2: Design
- Explain use of Lichess database of games every month
- Libraries used:
	- `python-chess` and `stockfish` libraries to parse and analyse chess games
		- Elaborate more on these, because they're specific to chess
	- `seaborn` for graph visualisations
	- `pandas` for dataframes
	- `numpy` for mathematical analysis
### 3.3: Development
- Sequence of things that need to be achieved
	- How are we going to investigate the things we've outlined in the scope?
	- Downloading the data (Lichess database, how we'll be storing the data), filtering the data, analysing the data, making data visualisations etc.
- Name success criteria
	- For example, evaluate results of prediction, evaluate results of clustering
### 3.4: Evaluation
- How we'll be judging the success of the project
	- See Izzy and Matt for examples
	- Assess the quality of our model – how effective/robust
		- Easier with supervised learning
- Link back to the success criteria – how to measure whether our studies worked
	- Discuss what we need to evaluate – how we'll be evaluating results of prediction/clustering etc.
		- Validation methods, R-squared, etc.
		- Using external data, comparing internal data, etc.
	- Classification
		- e.g. how to measure the quality of the classifications
	- Clustering
	- Regression

## 4: Conclusion
- Zoom back out to summarise what we've talked about
- Link back to the motivations of the project

## 5: References and Appendices
- Try to focus on peer-reviewed research over non-peer reviewed research