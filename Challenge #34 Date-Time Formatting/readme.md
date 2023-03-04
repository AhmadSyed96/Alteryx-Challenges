Here is this week’s challenge, I would like to thank everyone for playing along and for your feedback. The link to the solution for last challenge #33 is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-33-Reshaping-Nielsen-Data-Intermediate/m-p/36436#M10). For this chalenge let’s look at creating a macro from scratch. I recommend you first solve the problem with tools on the canvas, then cake a macro from the tools.

Use Case: Our customer has a need to convert date/time strings into a date-time format.

Examples of the different input formats include: 4/8/2015 4:00, 5/10/2015 13:00. The conversion is automatic when the hours are 2 digits (10-24), but it ignores hours 1-9 (creates NULL values on conversion).

Objective: Create a macro to effectively convert and preserve the data in a date-time format.

**Input**


|   Name    |  Type  |
|-----------|--------|
| date_time | String |



**Output**


|     Name     |   Type   |
|--------------|----------|
| date_time    | String   |
| DateTime_Out | DateTime |


