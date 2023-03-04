Here is a new challenge for this week, it is a continuation from last week’s warehouse distribution challenge. If you did not complete last week’s challegne don’t worry, you will not need any output from part one to complete this part. The link to the solution for last week’s challenge is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Alteryx-Weekly-Exercise-14-Warehouse-Distribution-Intermediate/m-p/36743#M39). I posted two solutions for last week’s challenge. The first is a solution without a macro and is in my opinion a more straight forward approach to solving the problem. I included the second macro approach because it is an excellent example of how to utilize an iterative macro.

The use case:

Based on data from last week’s warehouse distribution  challenge, we want to calculate the total shipped miles per item. The products are available from 3 different warehouses, lat/lon data is provide for each warehouse and each store location.

Your goal is to find the total distance travelled as straight line miles for each item based on it being shipped from the closest warehouse.

Good luck, I hope you are having fun with these  challenge and expanding your knowledge of Alteryx. Thanks to all that have provided feedback.

**Input**


|  Name   |   Type   |
|---------|----------|
| Field_1 | V_String |
| Field_2 | Int16    |
| Field_3 | String   |

**Output**


|      Name      |   Type   |
|----------------|----------|
| Poem           | V_String |
| Poem_ID        | Int16    |
| Poem_Read_Date | Date     |


