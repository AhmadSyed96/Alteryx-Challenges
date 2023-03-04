The link to last week’s  challenge (challenge #19) is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-19-Excel-Record-Locator-Beginner/m-p/36748#M44). For this week’s  challenge we need to clean up an unformatted text file with unstructured data.

Use Case: A sales executive got a series of leads from the DMA conference. Unfortunately it’s a text file that we want to restructure into a tabular form to load into Salesforce.

The result should be a table formatted the same as the output sample.

As always there are many ways to approach the same problem in Alteryx. I am looking forward hear about some of your solutions.

Enjoy!

**Input**

|  Name   |   Type   |
|---------|----------|
| Field_1 | V_String |

**Output**

|     Name     |   Type   |
|--------------|----------|
| RecordNumber | Int16    |
| Company_Name | V_String |
| Address      | V_String |
| Phone        | V_String |
| FAX          | V_String |
| Notes        | V_String |
| Website      | V_String |


