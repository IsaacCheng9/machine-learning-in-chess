# M5 – Planning Literature Review (27/10/2022)

## Agenda
- Review initial literature review plan and discuss points to focus on and improve

## Current Progress
- Cleaned up prototype code to improve reusability for future analysis
- Briefly reviewed literature reviews from previous lectures
	- Feeling a bit anxious about the deadline – a lot of progress to make in the upcoming weeks
- Created brief plan for literature review (see below)
	- Slightly confused about the overlap between some sections
	- Would Matthew's structure be more appropriate than Izzy's for my style of project?
		- May need to adjust sections in plan for literature review accordingly

## Plan for Literature Review
### General Advice
- Describe chess concepts as needed, rather than all at the start – makes it flow better
- Use slides 58 onwards from 8.1 of Google Drive lecture slides for clustering etc
- Largest sections are usually preliminary research and design and development

### 1: Introduction – Background and Aim
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

### 2: Preliminary Research
- Focus on previous research in the field
	- Academic research papers and how they're different to what we're proposing
	- Chess bots and engines trained using unsupervised learning
- [chessOpeningStats repository](https://github.com/Paul566/chessOpeningStats)
	- Spike in number of games played daily caused by COVID-19 pandemic and release of 'The Queen's Gambit' series
	- However, continuous growth observed over the last decade regardless
	- Mention that no peer-reviewed academic research has been performed on this, and use it as motivation for this project
	- May need to find more formal studies to back these statements?

### 3: Requirements Analysis
- Functional and non-functional requirements
- Functional requirements should link back to the background and aim of the project
- May be best to use Matthew's example as guidance, as the type of data is similar

### 4: Design and Development
- Start with simpler questions to build a baseline
- Build up to more complex questions using findings from previous questions
- Itemised questions and how we could look to answer them
	- Initial hypotheses based on intuition
	- Methods to investigate these
		- e.g. how to classify
- What questions we won't be looking to answer – restrict scope and set expectations
- Subsection to describe the data
	- Lichess database of games every month
- Libraries used:
	- `python-chess` and `stockfish` libraries to parse and analyse chess games
		- Elaborate more on these, because they're specific to chess
	- `seaborn` for graph visualisations
	- `pandas` for dataframes
	- `numpy` for mathematical analysis

### 5: Evaluation
- Link back to the fulfilment of functional requirements?
- How to measure whether our studies worked
	- Classification
		- e.g. how to measure the quality of the classifications
	- Clustering
	- Regression

### 6: Conclusions
- Zoom back out to summarise what we've talked about
- Link back to the motivations of the project

### 7: References and Appendices
- Try to focus on peer-reviewed research over non-peer reviewed research

## Links
- [Strategic social learning and the population dynamics of human behavior: the game of Go](https://www.sciencedirect.com/science/article/pii/S109051381400049X)
- [COM1011 Fundamentals of Machine Learning – Lecture Slides](https://drive.google.com/drive/folders/16V96NyqGOzwkR-Ixy-CF2teF2ijBeA1_)

## Next Steps
- Review content Chico's project resources email (from 17th October)
	- Look into unsupervised learning
	- Read previous years' literature reviews in more detail
- Continue to build plan and start writing draft of literature review
	- Write paragraphs corresponding to bullet points from the plan