
We hope you enjoyed  [last week's challenge](https://community.alteryx.com/t5/Weekly-Challenge/Alteryx-Weekly-Exercise-Week-4-Date-Parsing/m-p/36731#U36731). For the fifth  challenge let’s look at building an analytic application.

An HR department has a defined hierarchy for job identification across the organization. Depending on the job, the position within the hierarchy can change.

The goal is to create an analytical application that allows a HR rep to enter a position # (in this example, 33333) and return all records where the position is found within the hierarchy system.

We have listed this as an intermediate  challenge since parameterizing a workflow and converting it to an application is slightly more advanced however the workflow to answer the question should be beginner level. As always, we love to hear your comments. We hope you are having fun with the  challenges!

**Input**

|    Name    |   Type   |
|------------|----------|
| Team       | V_String |
| Result     | V_String |
| For        | V_String |
| Aga        | V_String |
| Diff       | V_String |
| HTf        | V_String |
| HTa        | V_String |
| Opposition | V_String |
| Venue      | V_String |
| Date       | V_String |


**Output**

|        Name        |   Type   |
|--------------------|----------|
| Venue              | V_String |
| No of Games Played | Int64    |
| Avg Rank           | Int32    |
| Max Rank           | Int32    |
| Min Rank           | Int32    |


