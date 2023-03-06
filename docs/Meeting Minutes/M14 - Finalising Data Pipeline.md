# M14 – Finalising Data Pipeline

## Agenda
### Progress
- Asked Sarah about the provided template.
	- Not required to use it – others have also complained about the wasted space on the first page for each chapter.
	- Likely going to look at recreating my own template, but copying the title page and abstract and declaration page.
		- Low priority, but would speed up my workflow when writing the final report as it should then work with VS Code – much faster compile times (currently ~20s with template on Overleaf) and easier edits.
		- Worst case scenario – use my own template for the main body, references, and appendices, and compile the pdf.
			- Compile the title page and abstract and declaration page from the template, then merge the two pdfs into one for submission.
- Investigated better ways of storing the pandas DataFrame.
	- Decided to store it as a folder of Parquet files.
		- Multiple files enables Dask's parallel processing.
		- Merge CSVs -> convert CSV to Parquet files with Dask
- Started calculating and plotting early metadata analysis.
	- Most common openings
		- Grouped variations of the same opening together for a clearer representation (e.g. different variations of Sicilian Defense are merged)
	- Most common opening categories
		- Added labels showing the ECO category and what it represents for each bar
	- Distribution of Elo ranges in games in 2022.
		- Includes repeated players so it may tend towards a higher rating – players who play more often and likely have better ratings will be overrepresented.
- Updated data pipeline to represent merging the months into a data set for the entire year.
	- Will change this to an actual flow chart with the shapes etc.
- Started writing the design section for my final report.
	- Mentioned my current findings from downloading the data and data processing.

### Questions
- What could I do to improve my plots?
	- Seaborn – font size should be roughly the same as the body text
	- Horizontal bar charts
- Does the flow of the data pipeline make sense?
	- Concerned about how easy it is to understand downloading each month (x12)
- How do you find my explanation on the early findings of my project? Do you have any suggestions for improvement?
- Data pipeline strongly favours high-level game analysis over low-level turn-based analysis – is this going to be a problem?
	- Scoutfish queries are very hacky and difficult to create – poor time-to-results ratio.
	- For example, average number of moves per game is difficult to calculate.
		- Not provided in the game info – would need to slowly iterate through each game to find this.
	- Potential solution – make assumptions based on high-level analysis and test it on a small sample of games?
		- For example, if time forfeit occurs more at lower Elos, suggest that this may be due to more blunders occurring at this level.
			- Go through 1,000 or so games at each Elo grouping, and record the number of moves.
			- Compare the average and median number of moves at each Elo range.
	- Justify the pivot towards more high-level analysis in the report and problems with Scoutfish – mention in the design section to start with and go back to it in the conclusion
- How should we decide what plots to include in the final report?
	- There will be a lot of plots in our Jupyter Notebook at the end.
	- Include the EDA plots to provide context, then only highlights from our insights?
- How much detail should we include in the background research / literature review?
	- Sarah was a bit unclear in our lecture – she said that there would be almost no literature review and that this means we may not have many references in the final report?
	- For a 20 page report, how many pages would you roughly use for the project specification, motivation, and aims (10% of mark)?
		- 1-2 pages for introduction and project specification
			- Introduction ~0.5 pages
			- Project specification is essentially a summary of the introduction – could probably merge sections
			- Screenshot of Lichess board
- Need to start thinking about how to convert the initial data analysis into machine learning.
	- What factors influence win rate?
		- Elo difference (absolute vs relative based on how the system works)
			- Potentially discount players who have only played one game or so?
		- Difference in number of games played by each player – captures uncertainty?