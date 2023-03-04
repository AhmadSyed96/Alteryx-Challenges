The link to last week’s challenge (challenge #27) is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-27-Spatial-Telco-Coverage-Smoothing-Intermediate/m-p/36429#M4)

**Use Case:** A company has to process financial data for their visualization tool. Today this is a manual process in Excel.

**Objective:** Build a process in Alteryx that automates the formatting of the daily data feed.

**Note:**  This data comes in daily and is always in the exact same format.

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


