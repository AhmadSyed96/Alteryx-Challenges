The link to last week’s challenge (challenge #42) is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Th-Weekly-Exercise-42-Ye-Inspire-Europe-2016-Grand-Prix-Lap-1/m-p/36596#M19)

As a follow on from last week’s challenge here is the second lap of the Inspire Europe Grand Prix. Keep in mind that the participants only had 10 minutes to complete the race. Fasten your seatbelt and give it a try.

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




|     Name      |    Type    |
|---------------|------------|
| Postcode Area | WString    |
| SpatialObj    | SpatialObj |



**Output**


|     Name      |  Type   |
|---------------|---------|
| Postcode Area | WString |
| Count         | Int64   |




|    Name     |   Type    |
|-------------|-----------|
| Count       | Int64     |
| Right_Count | Int64     |
| Pct         | V_WString |




|        Name          | Type  |
|----------------------|-------|
| pct since 09-01-2015 | Float |
| 2014                 | Float |
| diff                 | Float |


