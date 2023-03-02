# P2 – Project Plan

## To Do
### In Progress
- Discuss most common games
	- Mention grouping openings by splitting opening name by colon.
	- '90% of openings are either x, y, or z' – provides context to the reader
- Perform metadata analysis.
### Backlog
- Add one or two examples of openings (screenshots) in the appendix to provide context to the reader.
- Calculate the count of games each player has played.
- Try getting Elo distribution of unique players (take highest or lowest Elo for each player).
- Look into merging the first pages of the original template with my own template.
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
