This is the final lap in the Grand Prix series, last week’s (challenge #31) solution is posted  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-31-Alteryx-Grand-Prix-Race-2-Lap1-Intermediate/m-p/36434#M8).

Here is the Scenario for this lap: Now that I know the best four locations for me to visit (from last weeks exercise), I want to estimate how much it’s going to cost for me to take an Uber to each of the sites. If I start at this hotel, and head to the northern most location and head south to visit each surf site, how many miles will I drive? If Uber is $1.10 per mile, how much will that cost me?

The objective is to: Identify the total drive distance from inspire to the northern point and work south to visit all four sites ending at the last site. Calculate the Uber estimate.

*Remember to time yourself, contestants only had about ten minutes per lap.

**Input**


|      Name       |   Type   |
|-----------------|----------|
| Surf Site       | V_String |
| Swell Direction | V_String |
| Tide            | V_String |
| Wind Direction  | V_String |
| Boards          | V_String |
| Skill_Level     | V_String |
| Surf Season     | String   |
| Location        | V_String |
| Lat             | Double   |
| Long            | Double   |



|    Name    |    Type    |
|------------|------------|
| Label      | String     |
| SpatialObj | SpatialObj |



|       Name        |  Type  |
|-------------------|--------|
| Sum_DistanceMiles | Double |
| Uber cost         | Double |


**Output**


|       Name        |  Type  |
|-------------------|--------|
| Sum_DistanceMiles | Double |
| Uber cost         | Double |


