The link to the solution for last challenge #38 is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-38-Data-Blending-for-Batch-Output-Beginner/m-p/36578#M15).

This week is a little different, as we work with Alteryx workflows and macros that were created by other people it may be necessary to ‘de bug’ someone else work or make modifications to get components to function in your workflow. In this case you will start with a macro that had errors and work through the process of fixing it.

Use Case: A bank is looking to calculate customer retention rate month over month. The denominator in the calculation are all of the accounts open 24 months prior to the start of the month. For example, for June 2013, the denominator would be the total number of accounts open between June 1, 2011 and May 31, 2013. The numerator will be total number of accounts closed in June 2013 or between June 1, 2013 and June 30, 2013.

Objective: The included macro should calculate the retention rate for May through Dec 2013 but there are errors in the macro. Your job is to fix the broken Macro.

Have fun…

**Input**

| Name  | Type |
|-------|------|
| Month | Date |


|   Name     |  Type  |
|------------|--------|
| RecordID   | Byte   |
| Open Date  | String |
| Close Date | String |



**Output**


|     Name       |  Type  |
|----------------|--------|
| Start of Month | Date   |
| Open           | Byte   |
| Close          | Byte   |
| %              | Double |


