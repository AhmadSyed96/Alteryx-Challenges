
Here is this week’s  challenge, I would like to thank everyone for playing along and for your feedback. The link to the solution for last  challenge #10 is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Alteryx-Weekly-Exercise-10-Date-Time-Calculations-Intermediate/m-p/36737#M34).

The use case:

A manufacturing company receives customer complaint data on a daily basis from their call centers about the medical parts they distribute to their customers. The company monitors these comments to understand which parts and part groups have the highest complaint rate. This helps the company prioritize which parts to focus on from a development standpoint.

In this exercise, take the customer complaint data and identify which bucket the complaint falls within. The complaint can fall into multiple buckets and needs to be flagged as these complaints take highest priority. Create an aggregate view of which buckets or bucket pairings have the highest # of complaints.

This is only a subset of data so all records will not be assigned to buckets and can be ignored.

**Input**


|  Name  |  Type  |
|--------|--------|
| Search | String |
| Bucket | String |


**Output**


|   Name    |  Type  |
|-----------|--------|
| Bucket(s) | String |
| Count     | Byte   |


