# P2 – Project Plan

## Final Report Structure
- Change this to be similar to the structure of the literature review
	- Provided structure is more for software engineering projects
- Introduce methods at the start vs. introduce methods as they're used
	- Whatever is easier to navigate

### Introduction – Background and Aim

### Preliminary Research
- How much should this differ from the literature review?
	- Should it contain a subset of this, alongside new findings during development?
### Analysis of Requirements
- How much should this differ from the literature review?
	- Include new findings about difficulties with big data
### Design
- How does this work? In our case, how does it differ from analysis of requirements?
### Development

### Evaluation

### Conclusions
- Limitations
	- Challenges in collecting and parsing data – may be difficult for future work
- What worked
- What didn't work
- What we didn't explore but could be useful in the future
### References/Appendices

## Demonstration
- Is this an uploaded video or a live presentation?

## Metadata Analysis
### High-Level
#### Blunder rate by ELO
- Average number of moves by ELO rating
	- Initial hypothesis – this should increase as ELO rating increases as players are less likely to make game-changing blunders at an earlier stage
		- Talk about lack of universal definition of a game-changing blunder vs. other blunders
		- How we quantified a game-changing blunder – lose a Queen and resigned within a move?
	- Initial hypothesis – rate of resignations after specific pieces increases as ELO rating increases
		- Relative piece value (percentage of their total piece value)
	- If they made a game-changing blunder and didn't resign, what was the outcome?
#### Categorising players by playstyle
- How aggressive they are / tendency to have more open games
- Highlight specific players such as famous pros
	- Chess.com may provide game data
#### Most popular and most effective openings
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
#### New
### Low-Level
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