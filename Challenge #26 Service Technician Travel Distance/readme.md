The link to last week’s challenge (challenge #25) is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-39-Trouble-shooting-a-broken-macro-Intermediate/m-p/36427#M2)

This week’s  challenge is a use case faced by one of our customers that can leverage the geo-spatial tools available in Alteryx. If you have the spatial data available you can output your results as drive-distance, in the event that you do not have the drive-distance data available, please use the straight-line distance. The basic tools and setup of the data needed will be identical. Output results will be provided for both methods. In the event that you use drive-distance and your results vary slightly from the sample output, it may be due to variance in the data set used for the exercise.

Use Case: in order to audit their employee expense reports, a service company would like to calculate how far (in miles) their technician is traveling from their hotels, to the worksite, then to their destination hotel on a daily basis.

The Data: The source is collected in a way that record 1 contains the spatial object for the beginning hotel for day 1, record 2 is the spatial object for the worksite for day 1, and record 3 is the spatial object for the ending hotel for day 1. This pattern repeats for three successive days.

Find the distance on a daily basis the technician is either driving or straight line distance if you don’t have the spatial data available.

Enjoy!

**Input**


|    Name    |    Type    |
|------------|------------|
| Site       | String     |
| SpatialObj | SpatialObj |
| Date       | String     |



**Output**


|          Name          |  Type  |
|------------------------|--------|
| Date                   | String |
| Sum_DriveDistanceMiles | Double |




|       Name        |  Type  |
|-------------------|--------|
| Date              | String |
| Sum_DistanceMiles | Double |




