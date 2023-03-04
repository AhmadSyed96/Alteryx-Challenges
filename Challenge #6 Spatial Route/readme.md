
We hope you enjoyed  [last week's challenge](https://community.alteryx.com/t5/Weekly-Challenge/Alteryx-Weekly-Exercise-Week-5-HR-Position-Finder-Application/m-p/36732#M29). For the sixth  challenge lets look at some of the geospatial capabilities in Alteryx.

The  challenge for week 6 will focus on analyzing distance traveled by sales reps.  
  

Sales reps are travelling all over the US. The data contained in the workflow details the travel paths for 7 Reps to 7 different cities. The travel route is detailed as well. The objective of this  challenge is to determine which Rep has logged the most miles. Please include the route traveled as a spatial object in the output.

We have listed this as an intermediate  challenge since not everyone is familiar with the Spatial tools. As always, we love to hear your comments. We hope you are having fun with the  challenges!

**Input**


|     Name     |    Type    |
|--------------|------------|
| Airport City | V_String   |
| Centroid     | SpatialObj |
| REP          | String     |
| TripOrder    | Byte       |


**Output**


|       Name       |    Type    |
|------------------|------------|
| REP              | String     |
| SpatialObj_Built | SpatialObj |
| LengthMi         | Double     |


