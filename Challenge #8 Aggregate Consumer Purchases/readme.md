
**Aggregate Consumer Purchases:**

For this week’s exercise we will look at customer purchase behavior to decide if we should offer a “Meal Deal” that would add a side and drink to a purchase of pizza or a burger. The incoming data is larger than usual for these exercises so I have packaged the workflow as an Alteryx Package. The link to the solution for last  challenge #7 is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Alteryx-Weekly-Exercise-7-Download-data-and-parse-JSON-Advanced/m-p/36734#M31).

**This week’s Objective:**

In order to decide if we should start including a new "Meal Deal" on our menu we want to study the potential impact on recent transactions. Please identify the number and percentage of orders since July 1, 2013 which include the following categories of food: Pizza OR Burger along with a Side and Drink.

**Summary of Data:**

Point of Sale data includes the ticket level information, and the lookup table categorizes items into higher level food categories.

**Hint:**

Don't forget to join to the lookup table and filter by date.

As always we look forward to your feedback and suggestions!


**Input**

`Point of Sale`


|   Name   |   Type   |
|----------|----------|
| TicketID | V_String |
| Date     | V_String |
| MemberID | V_String |
| Desc     | V_String |
| Price    | V_String |

`Lookup`


| Name |   Type   |
|------|----------|
| Desc | V_String |
| Type | String   |


**Output**


|        Name         |  Type  |
|---------------------|--------|
| Potential Meal Deal | Int16  |
| Total               | Int16  |
| %                   | Double |


