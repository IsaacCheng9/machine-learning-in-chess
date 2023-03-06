# M12 – Investigating Data Pipeline (02/02/2023)

## Agenda
### Progress
- Managed to find a way to split up PGN files to make things easier to handle
	- Enables multiprocessing to improve performance when extracting data
- Fixed problems with Scoutfish
	- Works very quickly, but with limited data insights as it just returns offset of the  matching game in the original PGN file
	- Able to quickly check for specific openings, but it's unintuitive
		- Need to specify the exact sub-FEN string – no automatic labelling of openings
		- Would need to record a map of opening to sub-FEN string to automate this process
- Implemented and tested script to convert PGN to CSV
	- Generates a game info CSV file and a moves CSV file
		- Moves CSV file is too large – probably better to use Scoutfish for move analysis
		- Game info CSV file is likely to be useful
		- Could be easier to implement my own version if we won't use moves CSV file
	- Stores the opening category – [ECO (Encyclopedia of Chess Openings) code](https://en.wikipedia.org/wiki/Encyclopaedia_of_Chess_Openings)
		- Many openings share the same code
			- Original PGN file includes the specific name of the opening, which is lost when converting with this library
			- May be better to implement my own version to keep this data
				- Prototype analysis code already does this – need to check whether it performs worse than this library
					- Test on a small file like Lichess Elite August 2022 and time it
		- ECO code can be used to categorise similar openings
		- Original version mapped 500 openings
		- Independent revisions have been made to include more openings – [Lichess have created their own](https://github.com/lichess-org/chess-openings)
			- Will use this so that it matches the data source
- Performed further research on chess analysis with Python.
	- [Probability of chess piece positions](https://medium.com/analytics-vidhya/analyzing-chess-positions-with-python-26d73b7c892)
- Started implementing metadata analysis – found most popular openings by ECO code.
### To-Do
- Investigate whether we can use the additional fields from chess-openings repository to work with Scoutfish.
	- UCI notation to sub-FEN?
- Start to implement metadata analysis.
	- ELO distribution
	- Most popular opening categories by ELO range
- Optimise data pipeline so that we can perform our analysis on a larger data sample.
	- Investigate whether creating my own library to parse Lichess PGNs to CSV would be performant.
		- Advantage of including specific opening labels per game.
	- Implement concurrency on the split PGN files.
### Questions
- Is it worth creating a diagram to represent the complex data pipeline?
	- Using multiple different methods for different use cases (.scout and .csv files)
	- May not be formally assessed if it's in the appendix, but may help with planning things out and discussing it in meetings
		- Useful to put it in the main text as it's an important part of the data pipeline
- Is the demonstration live or is it a recorded video?
	- Recorded video
	- Presentation – introducing the project
	- Demonstration of code
		- Print different steps to show something to the viewers
	- Demonstration of results
- How do you feel about the progress so far? Do you have any concerns or general advice?
	- Focus on results-oriented processes – avoid premature optimisation