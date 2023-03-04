The link to last week’s  challenge (challenge #41) be  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-41-Analytics-PayPeriodCalc-Beginner/m-p/36582#M18)

Last week in bloody England Alteryx celebrated our European customers at Inspire Europe 2016. In th' tradition 'o th' US Inspire conference thar was a Grand Prix contention whar drivers were challenged to solve business problems usin' the mighty Alteryx tool. 'tis exercise be th' first lap in th' rivalry, recollect that th' peasants only had 10 minutes to answer th' 4 questions in th’ lap so ye may want to the be weary of th’ hour yourself.

Do ye have what it takes? Th' correct solution gunna earn ye some lovely booty:

![Pirate.png](https://community.alteryx.com/t5/image/serverpage/image-id/8864iEA8C17E8E81F9B2F/image-size/large?v=v2&px=999 "Pirate.png")

T' upload yer solution - take a wee little screenshot an' don't be spoilin it fer th' rest of us scurvy pirates. Put it in a Spoiler Tag and give ye a hearty YARRR!

A solvin tactic has been posted - but we wanna see yer bloody pirate way!

**Input**


|        Name         |   Type   |
|---------------------|----------|
| Reference Number    | V_String |
| Easting             | V_String |
| Northing            | V_String |
| Number of Vehicles  | V_String |
| Accident Date       | V_String |
| Time (24hr)         | V_String |
| 1st Road Class      | V_String |
| Road Surface        | V_String |
| Lighting Conditions | V_String |
| Weather Conditions  | V_String |
| Casualty Class      | V_String |
| Casualty Severity   | V_String |
| Sex of Casualty     | V_String |
| Age of Casualty     | V_String |
| Type of Vehicle     | V_String |
| CentroidX           | V_String |
| CentroidY           | V_String |



|        Name         |   Type   |
|---------------------|----------|
| Lighting Conditions | V_String |
| Reclassify          | String   |



**Output**


|        Name         |   Type   |
|---------------------|----------|
| Reference Number    | V_String |
| Easting             | V_String |
| Northing            | V_String |
| Number of Vehicles  | V_String |
| Accident Date       | V_String |
| Time (24hr)         | V_String |
| 1st Road Class      | V_String |
| Road Surface        | V_String |
| Lighting Conditions | V_String |
| Weather Conditions  | V_String |
| Casualty Class      | V_String |
| Casualty Severity   | V_String |
| Sex of Casualty     | V_String |
| Age of Casualty     | V_String |
| Type of Vehicle     | V_String |
| CentroidX           | V_String |
| CentroidY           | V_String |




|   Name     |  Type  |
|------------|--------|
| Reclassify | String |
| Count      | Int64  |




|          Name            |   Type   |
|--------------------------|----------|
| Reference Number         | V_String |
| Easting                  | V_String |
| Northing                 | V_String |
| Number of Vehicles       | V_String |
| Accident Date            | V_String |
| Time (24hr)              | V_String |
| 1st Road Class           | V_String |
| Road Surface             | V_String |
| Lighting Conditions      | V_String |
| Weather Conditions       | V_String |
| Casualty Class           | V_String |
| Casualty Severity        | V_String |
| Sex of Casualty          | V_String |
| Age of Casualty          | V_String |
| Type of Vehicle          | V_String |
| CentroidX                | V_String |
| CentroidY                | V_String |
| Accident Date (DateTime) | Date     |




|    Name     |   Type    |
|-------------|-----------|
| Time Bucket | V_WString |
| Count       | Int64     |


