# P1 – Literature Review Plan

## General Advice
- Describe chess concepts as needed, rather than all at the start – makes it flow better
- Use slides 58 onwards from 8.1 of Google Drive lecture slides for clustering etc
- Largest sections are usually preliminary research and design and development
- Title doesn't have to be a question – may change the wording to read better at a later point if needed.
- Use [arxiv.org](https://arxiv.org/) as an additional source of academic papers (but not peer-reviewed)
## Next Steps
- Improve the Evaluation subsection.
- Improve the Conclusion section.
- Create the Abstract.
- Improve the Analysing the Data subsection.
	- Add more detail to the steps.
	- Ensure that the description matches the steps from the Gantt chart.
- Add more to the Preliminary Research section.
	- Potential topics:
		- Research on chess in general
		- Research on cultural analytics
		- About chess theory
		- About chess databases
	- Improve sections:
		- Growth in the popularity of chess (what about growth before The Queen's Gambit?)
	- Focus on breadth overall, but delve into further detail in specific parts
		- No need for the history of Elo system, but explain what it is, how it works, how it's used to compare the skill sets of players (development section, not background)
		- One or two lines describing how it works
		- Demonstrate the changes between all the computers that played chess
			- Was DeepBlue just faster, or other improvements?
			- e.g. expand one or two sentences from Monte-Carlo tree search algorithm
	- No need to go deep into machine learning methods in background
		- However, compare and contrast to show a good understanding of existing solutions
			- Trade-offs
		- Could go deeper into the clustering algorithms in development section?
- Consider renaming the project.
- Complete a full draft of literature review for Friday submission.
## Abstract
- Hourglass shape
	- Zoom out -> zoom in -> zoom back out again
- Mini-introduction – purpose of this project
	- 'Chess is a popular game...'
- Mini-explanation on what we'll be doing
	- 'I'll be looking at these tools'
- Mini-conclusion – desired outcomes of the project
	- 'These can be useful because'
## 1: Introduction – Background and Aim
- Focus on motivation and general statements in the introduction
	- Consider changing order of introduction – perhaps move the motivation for studying chess in particular to the top
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
### History of Computer Chess
#### Early History
- Turing's Turochamp (with Champernowne)
- Prinz's first chess program
- IBM Deep Blue
#### Modern Developments
- Stockfish, its iterations, and prevalence
- Google AlphaZero
#### Relevance of Computer Chess
- Link the patterns that computer chess is extracting into how we can use it for our analysis
### Practical Use of Chess Databases
- Cheating in chess (Hans Niemann scandal)
- The patterns that we find could be used to identify players who are cheating
	- If their playstyle doesn't fit into patterns we've found, we could try to find the likelihood that they're cheating
	- If they don't fit in clusters of players (similar to finding 'top-right Messi')
		- Finding parameter space of chess players – x and y-axes
		- Players who are close together in clustering play similarly to each other, and vice versa
- Look into Kenneth Regan's academic papers
### Piece Valuation
- How it works and how piece values were defined
	- Avoid talking about the history of this – not relevant
### Growth in the Popularity of Chess
- [chessOpeningStats repository](https://github.com/Paul566/chessOpeningStats)
	- Spike in number of games played daily caused by COVID-19 pandemic and release of 'The Queen's Gambit' series
	- However, continuous growth observed over the last decade regardless
	- Mention that no peer-reviewed academic research has been performed on this, and use it as motivation for this project
	- May need to find more formal studies to back these statements?
- Could delve into some of the research performed about chess openings, but they're very simple, lack depth, and aren't formal academic pieces of research
	- May not need to investigate more breadth – just focus on how there's interest
## 3: Project Aims and Objectives
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
## 4: Project Management
### Overview of Plan
- Gantt chart
### Planning Our Approach
- Explain use of Lichess database of games every month
- Libraries used:
	- `python-chess` and `stockfish` libraries to parse and analyse chess games
		- Elaborate more on these, because they're specific to chess
	- `seaborn` for graph visualisations
	- `pandas` for dataframes
	- `numpy` for mathematical analysis
### Project Risks
- Size of data set
- Whether data set is representative
### Legal and Ethical Issues
- Use of Stockfish
- Use of personal information
### Downloading the Data
- Lichess Open Database
### Preparing the Data
- Sequence of things that need to be achieved
	- How are we going to investigate the things we've outlined in the scope?
	- Downloading the data (Lichess database, how we'll be storing the data), filtering the data, analysing the data, making data visualisations etc.
### Analysing the Data
- Regression and classification
- Examples:
	- Using frequency of openings to predict Elo ratings
	- Cluster strategies into player types
	- Cluster games based on the types of moves that are played
		- Open-ended games and closed games
			- Bishops are better in open-ended games whereas knights are better in closed games
			- Quantify the difference between these
- Mention success criteria and how we'll go into it into further detail in Evaluation
	- For example, evaluate results of prediction, evaluate results of clustering
### Evaluation
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
		- Accuracy, precision, recall, F1
	- Clustering
		- Silhouette score (see Google Drive lectures)
	- Regression
		- $R^2$ for linear
### Visualising Our Results
- Most popular chess openings by percentage, win rate, and ELO
- Most popular chess openings over time
- Importance of features of games containing less popular openings
## 5: Conclusion
- Zoom back out to summarise what we've talked about
- Link back to the motivations of the project
---
- Critically reviewed:
	- Uses of ML in chess, challenges that arise, and potential applications
	- Increasing influence of chess in popular culture
	- How the study of chess has great social importance (e.g. social learning theory)
- Formed hypothesis:
	- Machine learning can be used to analyse chess games to identify patterns in how people play chess
- Proposed a project:
	- Study large samples of rated Lichess games
	- Explore areas like:
		- The degree of social learning that exists in chess
		- How good existing metrics are for predicting the outcome of a game
---
-  Briefly mention some of the methods we could use
	- Focus on the prediction/clustering methods as opposed to the evaluation
	- 'identify patterns in how people play chess, such as...'
- Mention more potential outcomes of this project:
	- Detecting cheating in chess
## 6: References and Appendices
- Try to focus on peer-reviewed research over non-peer reviewed research