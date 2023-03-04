
Here is this week’s  challenge, I would like to thank everyone for playing along and for your feedback. The link to the solution for last  challenge #09 is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Alteryx-Weekly-Exercise-09-Analytics-Ranking-Beginner/m-p/36736#M33). For this  challenge let’s look at the date and time functions in Alteryx.

The use case:  
A distribution center receives a package. At the point of receipt, the package is scanned and a timestamp is captured for arrival date/time. The company is trying to reduce the amount of time the package is at its facility and as a result is trying to analyze how long packages remain at the facility.

The objective for this  challenge is to calculate the delta between arrival date/time and the Time_Now field (this field has the date/time of the creation of this  challenge and will be changing as time goes on). Create a unique field for Days, Hours, Minutes and Seconds.

We have listed this as an intermediate  exercise and I expect it will go very quickly for many of you. Let us know what you think, we are looking forward to hearing your feedback.

**Input**


|     Name      |   Type   |
|---------------|----------|
| Registrant ID | String   |
| TIMESTAMP     | DateTime |
| Time_Now      | DateTime |

**Output**


|     Name      |   Type   |
|---------------|----------|
| Registrant ID | String   |
| TIMESTAMP     | DateTime |
| Time_Now      | DateTime |
| Days          | Byte     |
| Hours         | Byte     |
| Minutes       | Byte     |
| Seconds       | Byte     |


