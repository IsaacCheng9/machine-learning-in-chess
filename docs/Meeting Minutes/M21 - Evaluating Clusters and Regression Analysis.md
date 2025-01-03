# M21 – Evaluating Clusters and Regression Analysis (20/04/2023)

## Progress
- Verified with Sareh that my template is fine.
- Fixed the readability of the structure of the data by transposing the table.
- Introduced the design section to explain how it only covers the general methodology, not specific implementations of models etc.
- Introduced the project results and evaluation section to explain the structure.
	- Data exploration
	- Machine learning models
		- Motivation
		- Development
		- Results and evaluation
- Removed outliers of King’s Pawn Game and Queen’s Pawn Game from data set when performing clustering and regression analysis.
	- Mentioned why I removed them in the report – too generic which adds noise to our models.
- Added section about clustering base openings by game results.
	- Added justification of the number of clusters using the elbow method and a table of silhouette scores by number of clusters.
- Added section about regression analysis of base opening popularity and game results.
	- Broke the results down into all players and by rating group.
	- Explained how there’s poor fitness in isolation, but the varying success by rating group suggests different elements of social learning is present.
- Improved the structure of subsections in project results by adding sub-subsections to make them easier to follow.
- Removed Scoutfish from data pipeline and design section.
	- Moved the explanation of Scoutfish to motivation section with an explanation of why we aren’t using it for the project.
	- Will link back to this when discussing future work as a potential avenue to explore.
- Started the project discussion and conclusion section.
- Clustered base openings by average similarity of results in their variations.
	- Variations that achieve similar results will have a low Euclidean distance, and vice versa.

## Questions
- How is the breakdown of my sections? Am I using sub-subsections too much? Should I remove or reduce them?
	- Breakdown is good
- The methods and results for each ML model are contained within the same subsection, and my actual design section talks more about setting up the project as a whole. Is this a problem?
	- Introduction to the design section was intended to provide clarification on this, but it may still be unclear?
		- Good workaround
- Marking specification mentions success criteria in the design section – what does this mean and how could I improve my report accordingly?
	- Specification mentions success criteria separately to ‘aims and objectives’, which is in the prior section.
	- Success criteria could be being able to perform the data processing
		- Download, process, and prepare the data such that it can be used by machine learning – helps the transition to design section
- Are my general ideas for the demonstration a good plan?
	- ~5 minutes going through a PowerPoint explanation that introduces the project, explains the motivation, and the design of data processing
		- Similar to the final report up to and including the design section
		- Won’t explain actual model implementations in this part
	- ~2 minutes demonstrating the Python scripts I created
	- ~10 minutes going through the Jupyter Notebook
		- Similar to the project results section of the final report
		- Show the file structure
			- Get the data from the Lichess website
			- Run the Python scripts with a different data source – split with the data pipeline
		- Point towards the GitHub repo to explain the development process
		- Show intermediary steps when running code?
		- Won’t run live – takes too long (‘this is what I made earlier’ etc.)
		- High-level overview of the code and how it works
			- Focus on the plots and what they mean
	- ~3 minutes going back to the PowerPoint presentation to conclude the project
		- Similar to the conclusion section of the final report
		- Project outcomes, limitations, future work