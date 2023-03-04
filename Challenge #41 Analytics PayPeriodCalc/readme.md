The link to last week’s challenge (challenge #40) is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-40-Data-Prep-HTML-Parsing-Dr-Names-Intermediate/m-p/36581#M17)

This week’s exercise looks at using Alteryx to calculate the number of weekdays during each pay period. Employees get paid twice monthly so the number of weekend days within a period can vary.

Objective: For each month and pay period, calculate the # of weekdays that make up the pay period (i.e. exclude weekend days from the calculation).

**Input**

|  Name    |  Type  |
|----------|--------|
| P1 Start | String |
| P1 End   | String |
| P2 Start | String |
| P2 End   | String |

**Output**

|    Name     |  Type  |
|-------------|--------|
| Month       | String |
| P1 Weekdays | Byte   |
| P2 Weekdays | Byte   |


