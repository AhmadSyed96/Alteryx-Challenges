The link to the solution for last challenge #34 is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-34-Macro-Development-Date-Time-Formatting/m-p/36437#M11). For this challenge let’s practice some data cleansing.

Use Case: There is a series of data cleansing processes we need to do on our data. Please solve each per the instructions.

Objective:

1.  Remove leading zeroes
2.  Trim leading zeroes and/or descriptive text at the end
3.  If the data value ends with ID, remove the ID
4.  If more than 8 chars, remove anything after 8. If only 6, add “SC” to the front.

**Input 1**


|  numbers  |
|-----------|
|     01234 |
|      1234 |
|    001234 |
| 000001234 |


**Output 1**


|  numbers  | trimmed |
|-----------|---------|
|     01234 |    1234 |
|      1234 |    1234 |
|    001234 |    1234 |
| 000001234 |    1234 |


**Input 2**


|   field 1    |
|--------------|
| 001001       |
| 1001: Report |
| 00123456     |
| 1234         |


**Output 2**


|    field     | fixed  |
|--------------|--------|
| 001001       |   1001 |
| 1001: Report |   1001 |
| 00123456     | 123456 |
| 1234         |   1234 |

**Input 3**

|     field     |
|---------------|
| 91283091283ID |
| 1923          |
| 1513511324ID  |
| ID2454542     |
| 134ID245      |


**Output 3**


|     field     |    fixed    |
|---------------|-------------|
| 91283091283ID | 91283091283 |
| 1923          | 1923        |
| 1513511324ID  | 1513511324  |
| ID2454542     | ID2454542   |
| 134ID245      | 134ID245    |

**Input 4**


|         field          |
|------------------------|
| C11103                 |
| SCC11103               |
| SCC11103: Fire Warning |


**Output 4**

|         field          |  fixed   |
|------------------------|----------|
| C11103                 | SCC11103 |
| SCC11103               | SCC11103 |
| SCC11103: Fire Warning | SCC11103 |


