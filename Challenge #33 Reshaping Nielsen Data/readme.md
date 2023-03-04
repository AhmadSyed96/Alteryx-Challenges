
Hopefully everyone had fun with the Grand Prix challenges and a few of you are ready to jump in the ring next year for the 2017 Grand Prix at Inspire in Las Vegas. The solution for the final lap (challenge #32) is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-32-Alteryx-Grand-Prix-Race-2-Lap-2-Intermediate/m-p/36435#M9).

Let’s dial it back this week and look another real world example of using Alteryx to reshape data into a usable format for analysis.

Use Case: A radio station is trying to analyze data they receive from Nielsen disclosing the number of listeners the station has on a weekly basis by program. The challenge is that the data is formatted in a way that makes it challenging to use for analytics.

Objective: Reshape the data detailing the listening stats for the 30 programs listed in the data.

**Input**


|           Name           |   Type   |
|--------------------------|----------|
| Nielsen Audio Metro Area | V_String |
| Field_2                  | V_String |
| Field_3                  | V_String |
| Field_4                  | String   |
| Field_5                  | V_String |
| Field_6                  | String   |
| Field_7                  | Bool     |
| Field_8                  | V_String |
| Field_9                  | String   |
| Field_10                 | String   |
| Field_11                 | String   |
| Field_12                 | String   |

**Output**


|      Name       |  Type  |
|-----------------|--------|
| AQHP12+         | Int32  |
| AQHP12+Rating   | Double |
| P12+Consume     | Int32  |
| P12+ConsumRtg   | Double |
| AQHP25-54       | Int32  |
| AQHP25-54Rating | Double |
| P25-34Consume   | Int32  |
| P25-54ConsumRtg | Double |


