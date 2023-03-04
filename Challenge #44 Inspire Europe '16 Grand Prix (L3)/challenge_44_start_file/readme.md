The link to last week’s challenge (challenge #43) is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-43-Inspire-Europe-2016-Grand-Prix-Lap-2/m-p/36598#M20)

As a follow on from last two weekly challenges here is the third and final lap of the Inspire Europe Grand Prix. Keep in mind that the participants only had 10 minutes to complete the race.

If you have what it takes, watch for the qualification rounds of the 2017 Grand Prix to be held at Inspire 2017 (Las Vegas June 5-8, 2017) [http://www.alteryx.com/inspire-2017](http://www.alteryx.com/inspire-2017)

**Input**


|        Name         |   Type    |
|---------------------|-----------|
| Reference Number    | V_String  |
| Easting             | V_String  |
| Northing            | V_String  |
| Number of Vehicles  | V_String  |
| Accident Date       | V_String  |
| Time (24hr)         | Int32     |
| 1st Road Class      | V_String  |
| Road Surface        | V_String  |
| Weather Conditions  | V_String  |
| Casualty Class      | V_String  |
| Casualty Severity   | V_String  |
| Sex of Casualty     | V_String  |
| Age of Casualty     | V_String  |
| Type of Vehicle     | V_String  |
| CentroidX           | V_String  |
| CentroidY           | V_String  |
| Lighting Conditions | String    |
| Accident Date_Date  | Date      |
| Time Bucket         | V_WString |



**Output**


|         Name           |  Type  |
|------------------------|--------|
| Avg_Number of Vehicles | Double |



|    Name     |   Type    |
|-------------|-----------|
| Time Bucket | V_WString |
| Count       | Int64     |



|             Name               | Type  |
|--------------------------------|-------|
| CountDistinct_Reference Number | Int64 |



| Name   |   Type    |
|--------|-----------|
| Name   | V_WString |
| Object | Blob      |


