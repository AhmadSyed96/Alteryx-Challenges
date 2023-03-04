The link to last week’s challenge (challenge #26) is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-26-Service-Technician-Travel-Distance-Beginner/m-p/36428#M3)  
  

This week’s challenge is a spatial use case to preprocess a spatial object for mapping. The input file is a single complex polygon that represents a coverage area.

Use Case: A wireless telecommunications company wants to remove holes and splatter from their coverage area for simplified map display. Splatter can be define as unnecessary pieces of the whole polygon.

Objective: Remove all splatter less than 2 square miles and holes from the coverage area.

This exercise can generate varying answers based on the configuration of the spatial tools used for the process. As a result the challenge does not contain an output.

Have fun!

**Input**


|    Name    |    Type    |
|------------|------------|
| Break      | String     |
| SpatialObj | SpatialObj |

**Output**


|    Name    |    Type    |
|------------|------------|
| SpatialObj | SpatialObj |


