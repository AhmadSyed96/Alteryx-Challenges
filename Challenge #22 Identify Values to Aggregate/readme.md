The link to last week’s challenge (challenge #21) is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-21-Date-Reformatting-Beginner/m-p/36750#M46).

This week’s  challenge is a little special. I have mentioned before that as internal users or Alteryx we all do these exercises every week and we started doing this at the beginning of 2014. There have been a lot of exercises since then and the product has changed a lot of the past few years. The exercise posted here is exercise #1, the inaugural exercise that we completed internally.

In the spirit of that, you will find the workflow will build from top down instead of from left to right, that is the way Alteryx used to work. For some more fun I would ask that before building the workflow, go to the “About” box from the HELP menu and double click the Colorado flag next to the text “Created in Boulder, Colorado” after that, the tool icons will change to the original Alteryx tool icons that used to be in the product. Don’t worry, once you close Alteryx and re-open it the icons will return to normal.

![about.png](https://community.alteryx.com/t5/image/serverpage/image-id/4564i7DB4F9D819806E86/image-size/large?v=v2&px=999 "about.png")

Now for the  challenge , this week’s  challenge is an intermediate difficulty one that requires parsing a text field to get at values to summarize.

Use case: The log files from an ATM machine have the transaction amounts embedded in text strings. The user needs to have these text amounts summarized by row (transaction).

Objective: For this assignment the numbers directly following the text ‘ATM2.’ are dollar amounts for transactions. Summarize the values on a row by row basis.

Have fun!

**Input**


|  Name   |   Type   |
|---------|----------|
| Field_1 | V_String |

**Output**


|       Name       |  Type  |
|------------------|--------|
| RowNum           | Int16  |
| Sum_DollarAmount | Double |


