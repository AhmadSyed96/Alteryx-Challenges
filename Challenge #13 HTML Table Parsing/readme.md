The link to the solution for last  challenge  #12 is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Alteryx-Weekly-Exercise-12-Creating-an-HR-Hierarchy-Advanced/m-p/36740#M36).

For this  challenge let’s look at creating a multi-level hierarchy from employee-manager data. As always there are several ways to do this  challenge, I have designated it as an advanced  challenge because some of the more complex functions like RegEx can be used, but it is not absolutely necessary.

**The use case:**

We have HTML data that is in a single field, the HTML contains an HTML Table.

The input contains a series of name/value pairs within the description field. The description field has a HTML table that contains 14 name/value contained within <td> tags. Each pairing can be found on a different row (designated by the <tr> tag).

The objective is to produce a table containing the 14 name/value pairs.

Good luck, I look forward to your feedback.

**Input**


|    Name     |   Type   |
|-------------|----------|
| RecordID    | Byte     |
| Description | V_String |

**Output**


|   Name   |   Type   |
|----------|----------|
| RecordID | Byte     |
| Name     | V_String |
| Value    | V_String |



