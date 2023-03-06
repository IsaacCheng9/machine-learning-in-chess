# M13 – Improving Data Pipeline (09/02/2023)

## Agenda
### Progress
- Finalised the data pipeline from downloading the games to generating data inputs that can be analysed in pandas.
	- Performed stratified sampling on the first 5m Bullet/Blitz/Rapid games.
- Created a diagram to represent the data pipeline.
- Investigated problems with big data ingestion.
	- CSV file with 60m games (5m per month) is too large to load in-memory.
		- 'my rule of thumb for pandas is that you should have 5 to 10 times as much RAM as the size of your dataset' – [Wes McKinney, pandas creator](https://wesmckinney.com/blog/apache-arrow-pandas-internals/)
	- Dask (parallel computing with pandas) seems to work well, but need to investigate further.
	- Alternatively, will look into querying from SQL DB

### Questions
- What do you think about the diagram of the data pipeline? What improvements could I make?
	- Change the diagram to be vertically oriented – see how it looks in the report.
	- Alternatively, add a simpler version of the diagram in the report, and refer to the appendix for a more detailed diagram.
	- Currently represents the pipeline for a single game – need to show how this works for the final 2022 data set
		- Arrow from first cell to a cell representing the merging of CSV files into final 2022 data file
			- Annotate with '1' and '2' or similar
- How might we handle queries for specific occurrences in games?
	- Scoutfish is useful, but the `.scout` file is currently indexed for an entire month's PGN, not just the subset of games that we've taken
		- Would this create unfair comparisons, or is it okay?
	- Could alternatively index on the first 5m games (by splitting original PGN file into 5m game chunks), but this will be an underestimate as it'll include Rated Classical games that we don't want
	- Use just over 5m for both Scoutfish and CSV queries
- Is there an allowance to purchase an external SSD for database storage?
	- Peers have been given £100 for equipment to help them with their project – would I be eligible?
	- External SSD would be extremely useful as a large part of my bottleneck is network speeds when downloading data sets
		- Wouldn't need to constantly shuffle data in and out if I could permanently store these in a fast external SSD
		- Can get a 1TB external NVMe SSD within £100 on Amazon