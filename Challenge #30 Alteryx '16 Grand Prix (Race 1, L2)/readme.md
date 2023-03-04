I hope you all had fun with last week’s challenge, completing lap one form the Inspire 2016 Grand Prix event (challenge #29). The solution is posted  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-29-Alteryx-GrandPrix-Lap-1-Intermediate/m-p/36432#M6).

Now that you have your data prepped it is time for Race 1 lap 2, you need to answer some questions so you will have content for your annual "Draft Recap" newsletter.

Objective: Please use Alteryx to answer the following questions –

1.  Who has the youngest team and what is the average age?
2.  Which team has the best (lowest) average pitcher rank?
3.  What is the Pearson correlation between 2015 Team Rank and Hitter Rank?
4.  Please build a table containing the count of players on each fantasy team by position, the sum of home runs for the hitters by fantasy team, and sum of wins for the pitchers by fantasy team, ordered by 2015 team rank.

*Keep in mind the contestants only had about 10 minutes per lap maximum so time yourself.

**Input**


|          Name          |   Type   |
|------------------------|----------|
| Year                   | Int16    |
| Round                  | Byte     |
| Pick                   | Byte     |
| Overall_Pick           | Byte     |
| Player                 | V_String |
| Fantasy Team           | V_String |
| Hitter Rank            | Int16    |
| Team                   | String   |
| Position               | String   |
| Age                    | Byte     |
| Average Draft Position | V_String |
| At Bats                | Int16    |
| Hits                   | Byte     |
| Batting Average        | String   |
| Home Runs              | Byte     |
| Runs                   | Byte     |
| Runs Batted In         | Byte     |
| Stolen Bases           | Byte     |
| Stike Outs             | Byte     |
| Pitcher Rank           | Byte     |
| Innings Position       | V_String |
| Wins                   | Byte     |
| Saves                  | Byte     |
| Holds                  | Byte     |
| Strike Outs            | Int16    |
| Walks                  | Byte     |
| Earned Run Average     | V_String |
| 2015 Team Rank         | Byte     |


**Output**


|     Name     |  Type  |
|--------------|--------|
| Fantasy Team | String |
| Avg_Age      | Double |




|       Name       |  Type  |
|------------------|--------|
| Fantasy Team     | String |
| Avg_Pitcher Rank | Double |




|  Name  |  Type  |
|--------|--------|
| Result | Double |




|      Name      |   Type   |
|----------------|----------|
| Fantasy Team   | V_String |
| 1B             | Byte     |
| 2B             | Byte     |
| 3B             | Byte     |
| C              | Byte     |
| DH             | Byte     |
| OF             | Byte     |
| R              | Byte     |
| S              | Byte     |
| SS             | Byte     |
| 2015 Team Rank | Byte     |
| Sum_Home Runs  | Int16    |
| Sum_Wins       | Byte     |




