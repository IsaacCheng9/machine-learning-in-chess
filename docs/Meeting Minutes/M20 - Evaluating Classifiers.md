# M20 – Evaluating Classifiers (12/04/2023)

## Progress
- Completed preliminary research section.
- Added a small paragraph linking the project specification to the preliminary research and design sections for a sense of continuity.
- Added a subsection about subsampling games for machine learning models in the design section.
- Wrote about the results of the classifier models and evaluated them.
- Updated section headers and sub-headers to align with the marking specification.
	- Reduces friction for the second marker especially.
	- Moved data exploration section to the results section.
- Created a prototype final report submission which merges the provided template with my own.
- Investigated popularity of BaseOpening vs. win rate.
	- K-means clustering of BaseOpening by result.
		- Somewhat successful – silhouette score of 0.478 after testing different number of clusters.
	- Linear regression of BaseOpening popularity and White win rate / Black win rate / draw rate.
		- Unsuccessful – no real trend. Popularity of a opening is more complex than just the success rates, otherwise this strategy would be used by every player thus causing an equilibrium?
			- Future work – time series of win rate for specific openings, as we only have data from a specific year
		- Games are also long enough that the opening may not matter as much / to a limited extent

## Questions
- It seems that the literature review part of the final report isn’t explicitly required unlike in the previous year – should I adjust my final report accordingly?
	- Tried to link preliminary research with the motivation for my project to make a stronger case.
	- Is this subsection currently too long?
		- Currently at a good length.
- Merging the pdfs works well, except the clickable hyperlinks break, so I’ve removed them. Is this acceptable for markers, or would I be punished for this?
	- Doesn’t matter – won’t be punished.
- Do you think there are things I could follow-up for my investigation into popularity of BaseOpening vs. win rate, or should I write about them and move on?
	- Regression analysis with different rating ranges
	- In future work, propose potential patterns such as specific/niche openings being more present in players who are rising the ranks quickly.