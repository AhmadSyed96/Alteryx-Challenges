The link to the solution for last challenge #37 is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-37-Data-Preparation-Parsing-XML-Intermediate/m-p/36577#M14).

One of the powers of Alteryx is to be able to batch processes without the need to write scripts of use complicated code. A single output tool can be configured to generate many output files.

Use Case: A company needs to blend data from three sources and generate an output file for each product - region combination, a total of 15 output files.

Objective: Create a cross join between the Product Group, Region Reference and Data tables to produce 15 unique CSV Data files. Please note that only 1 output tool should be leveraged in your solution.

Thanks to all that are playing along!

**Input**


|       Name        |  Type  |
|-------------------|--------|
| Analysis Data Row | Byte   |
| Client            | Int16  |
| Product Group     | String |
| CCY Group         | String |
| Sector            | String |
| Region            | String |
| Size              | Double |
| Buy/Sell          | Int16  |



|   Name     |  Type  |
|------------|--------|
| Region     | String |
| Region Key | Byte   |



|     Name      |   Type   |
|---------------|----------|
| Product Group | V_String |
| Product Key   | Byte     |


**Output**


|       Name        |  Type  |
|-------------------|--------|
| Analysis Data Row | Byte   |
| Client            | Int16  |
| Product Group     | String |
| CCY Group         | String |
| Sector            | String |
| Region            | String |
| Size              | Double |
| Buy/Sell          | Int16  |
| Region Key        | Byte   |
| Product Key       | Byte   |


