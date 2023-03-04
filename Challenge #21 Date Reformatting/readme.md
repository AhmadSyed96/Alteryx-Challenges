
The link to last week’s  challenge (challenge #20) is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-20-List-Parsing-Advanced/m-p/36749#M45). For this week’s  challenge we have an easier one that requires the reformatting date fields. The input data has very poorly formatted month and year information that will require you to build some logic to make it usable.

Use Case: A company needs to reformat a month/year flag in a data asset they received for a consulting project.

You will need to take the Date field provided and separate it into fields for the Month and Year. For example, F07 should become 2 columns where month is Feb and year is 07.

Have fun!

**Input**


| Name |  Type  |
|------|--------|
| Date | String |


**Output**


| Name  |  Type  |
|-------|--------|
| Date  | String |
| Month | String |
| Year  | String |


