For this week’s  challenge we can look at using Alteryx to automate a repetitive task. The link to last week’s  challenge (challenge #18) is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-18-Predictive-Predicting-Baseball-Wins/m-p/36747#M43).  
  

Use Case: Customer has 100's of xls files with 1 common sheet available in all workbooks. Through one process, the user would like to read across all of the xls files and return the values contained in specific cells - Row 2, Column 3 and Row 8, Column 2 for each sheet within each XLS workbook.  
  

The result should be a table OR browse tool containing 3 columns: XLS File, Row2_ Column3, and Row8_Column2.  
  

You will only have 2 xls files for this  challenge, Book1 and Book2, but keep in mind that the use case is for 100s of Excel files with the same schema. You won’t want to use 2 input tools since that would not scale to 100’s. Also, for all data consumption, please check the box for First Row Contains Data. This is because in the headers for an Excel file are in row #1.  
  

Good luck and keep it simple, this should be an easy  challenge!

**Input**


|   Name   |   Type    |
|----------|-----------|
| F1       | V_String  |
| F2       | V_String  |
| F3       | V_String  |
| F4       | V_String  |
| FileName | V_WString |


**Output**


|     Name     |  Type  |
|--------------|--------|
| XLS File     | String |
| Row2_Column3 | Byte   |
| Row8_Column2 | Byte   |


