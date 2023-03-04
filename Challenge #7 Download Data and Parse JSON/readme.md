Welcome to 2016 we hope you are enjoying these challenges. The link to the solution for last challenge #6 is  [here](https://community.alteryx.com/t5/Weekly-Challenge/Alteryx-Weekly-Exercise-Week-6-Spatial-Route/m-p/36733#U36733). For the seventh  challenge let’s look at downloading data with an API and parsing that data from JSON into a usable format.

The data we will use comes from Quandl. The Quandl site offers access to several million financial, economic and social datasets. Data is indexed from multiple sources allowing users to find and download in various formats. All Quandl's data are accessible via an API.

For this example the response from these APIs is JSON. Our user is trying to get aggregated Annual Outbound Tourism Statistics for the US dating back to 1995. The Text Input contains the URL for the API request. Your goal is to parse the response.

**HINT**: After parsing the JSON, you will need to further identify the patterns within the data to effectively stage into a table for analytics.

**NOTE**: The data in the API is subject to change. When trying to match the output, the effort should be focused on achieving an identically structured dataset.

We have listed this as an advanced  challenge since configuring the download tool and parsing functions are more advanced topics. We are looking forward to hearing your feedback.

**Input**



| Name |  Type  |
|------|--------|
| URL  | String |



**Output**


|                                          Name                                          |   Type    |
|----------------------------------------------------------------------------------------|-----------|
| Date                                                                                   | V_WString |
| Arrivals - Thousands (TF)                                                              | V_WString |
| Tourism expenditure in the country - US$ Mn (IMF)                                      | V_WString |
| Tourism expenditure in the country - US$ Mn (IMF) - Travel - US$ Mn (IMF)              | V_WString |
| Tourism expenditure in the country - US$ Mn (IMF) - Passenger transport - US$ Mn (IMF) | V_WString |


