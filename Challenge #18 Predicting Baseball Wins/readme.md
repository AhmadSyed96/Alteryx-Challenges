This week let’s have some fun and look at predicting baseball wins. For those looking for the solution to last week’s (challenge #17) the link is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-17-Batch-Macro-Calculating-a-24-month-retention/m-p/36746#M42).

The use case: The Baseball season has completed and it's time to project next year's win totals.

The objective: Determine the top 10 variables that correlate to wins (excluding [Win_Pct] and [Games] from the correlation). Leverage those top 10 variables to predict the # of wins the team will have in next year’s season.

Isolate the teams to only use Boston - BOS, Los Angles of Anaheim - LAA, Chicago Cub - CHC, San Francisco Giants - SFG, Colorado Rockies - COL and Texas Rangers - TEX.

Create what the final standing will be and how many games out of first place each team is assuming each team plays 162 games.

Good luck, I hope you are having fun with these exercises and expanding your knowledge of Alteryx. Thanks to all that have provided feedback

**Input**


|  Name   |   Type    |
|---------|-----------|
| Tm      | V_WString |
| Games   | Int32     |
| Wins    | Int32     |
| Win_Pct | Double    |
| X_Bat   | Int32     |
| BatAge  | Double    |
| R_G     | Double    |
| PA      | Int32     |
| AB      | Int32     |
| R       | Int32     |
| H       | Int32     |
| X2B     | Int32     |
| X3B     | Int32     |
| HR      | Int32     |
| RBI     | Int32     |
| SB      | Int32     |
| CS      | Int32     |
| BB      | Int32     |
| SO      | Int32     |
| BA      | Double    |
| OBP     | Double    |
| SLG     | Double    |
| OPS     | Double    |
| OPS_Adj | Int32     |
| TB      | Int32     |
| GDP     | Int32     |
| HBP     | Int32     |
| SH      | Int32     |
| SF      | Int32     |
| IBB     | Int32     |

**Output**


|       Name       |  Type  |
|------------------|--------|
| Tm               | String |
| Projected Wins   | Byte   |
| Projected losses | Byte   |
| Games Back       | String |


