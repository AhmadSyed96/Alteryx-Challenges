The link to last week’s challenge (challenge #28) is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-28-Formatting-Morningstar-Data-Intermediate/m-p/36431#M5)

Hi everyone, what an awesome time we had at the Alteryx Inspire 2016 Conference in San Diego last week. It was so nice to meet many of the Community members in person. If you attended the conference and went to the  [Grand Prix](https://community.alteryx.com/t5/Analytics-Blog/Alteryx-Grand-Prix-2016-We-Have-a-Winner/ba-p/22789)  event, this week’s challenge is the first of the four laps. We will cover all of laps as weekly challenges in the next weeks. See if you have what it takes to compete, keep in mind the contestants only had about 10 minutes per lap maximum so maybe time yourself.

Use Case: You are the commissioner for your fantasy baseball team. You recently completed your draft and you want to run some simple statistics about each fantasy team.

You have 3 inputs

1) Fantasy pick summary from your draft

2) Hitter stats on all field players (whether selected in your draft or not)

3) Pitchers stats on all pitchers (whether selected in your draft or not)

Objective: In order to run some stats on your draft, you first need to prep your data. Please combine all 3 files so that you have a single output that contains stats on each player drafted in your draft, ordered by "Overall_Pick."

**Drivers start your engines!**

**Input**


|                                    Name                                    |   Type   |
|----------------------------------------------------------------------------|----------|
| American Funds Fixed Income Funds Daily Mstar/Lipper Blended Percent Ranks | V_String |
| F2                                                                         | String   |
| F3                                                                         | String   |
| F4                                                                         | V_String |
| F5                                                                         | V_String |
| F6                                                                         | Bool     |
| F7                                                                         | Bool     |
| F8                                                                         | Bool     |
| F9                                                                         | V_String |
| F10                                                                        | V_String |
| F11                                                                        | String   |
| F12                                                                        | String   |
| F13                                                                        | String   |
| F14                                                                        | String   |



**Output**


|  Name   |   Type   |
|---------|----------|
| 1 month | V_String |
| 3 month | V_String |
| Y-T-D   | V_String |
| 1 yr    | V_String |
| 3 yrs   | Double   |
| 5 yrs   | Double   |
| 10 yrs  | Double   |
| 15 yrs  | Double   |





