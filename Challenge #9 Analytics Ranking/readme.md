
Here is the new weekly challenge. The link to the solution for last challenge is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Alteryx-Weekly-Exercise-08-Aggregate-Consumer-Purchases/m-p/36735#M32). For this  challenge let’s look at ranking records when multiple records can have the same rank.  
  
The objective is to determine the top 5 ranking based on the count, however since there are multiple rows with same count (similar to a round of golf) multiple people can be in the same place (Rank) if they have the same score.

We have listed this as a beginner  challenge and I expect it will go very quickly for many of you. Let us know what you think, we are looking forward to hearing your feedback.

**Input**

| Name  |  Type  |
|-------|--------|
| First | String |
| count | Byte   |


**Output**


| Name  |  Type  |
|-------|--------|
| First | String |
| count | Byte   |
| Rank  | Byte   |


