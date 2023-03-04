Here is a new challenge for this week, it is a two part challenge so next week’s challenge will be a continuation. The link to the solution for last week’s challenge is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Challenge-13-HTML-Table-Parsing/m-p/36741#U36741).

This week we are looking at a retail distribution analysis. We need to allocate products from the warehouse to stores based on priority. I have seen this  challenge solved both with and without the use of an iterative macro.

The use case:

A retail chain has 25 stores carrying variety of items. Not every store carries the same items and each has its own level of prioritization within the chain and different required stock levels. There is a central warehouse that contains all of the available items.

The objective is to distribute items from the warehouse to each store, filling the available stock at each store in order of the store's priority.

Good luck, I look forward to hearing your feedback. Thank you for playing along.

**Input**


|   Name   |  Type  |
|----------|--------|
| Store    | String |
| Priority | Byte   |
| City     | String |
| State    | String |
| Lon      | Double |
| Lat      | Double |


|   Name   |  Type  |
|----------|--------|
| Store    | String |
| Item     | Byte   |
| Required | Byte   |


|   Name    |  Type  |
|-----------|--------|
| Warehouse | String |
| Item      | Byte   |
| Count     | Int16  |



**Output**


|   Name    |  Type  |
|-----------|--------|
| Store     | String |
| Priority  | Byte   |
| City      | String |
| State     | String |
| Item      | Byte   |
| Required  | Byte   |
| Warehouse | String |
| Assigned  | Byte   |


