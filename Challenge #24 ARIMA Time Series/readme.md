For those of you following along, thank you, you can find the solution to last week’s  challenge (challenge #23) is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-23-Advanced-Data-Parsing-CPG-Data-Advanced/m-p/36752#U36752).

This week’s  challenge will use the predictive time series tool called  [ARIMA](https://help.alteryx.com/current/designer/arima-tool). If you don’t have the predictive tools you can find the installer at  [http://downloads.alteryx.com/downloads.html](http://downloads.alteryx.com/downloads.html)  look for the link to “Predictive tools only”. The predictive tools in Alteryx execute the analytics in an open source application called ‘R’, the advantage of using Alteryx vs. R is that Alteryx provides a straight-forward user interface and eliminates the need to program directly in the R language. If you want to read more about what is happening under the hood, here is a link to the Wiki on ARIMA.  [https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average)

The use case: A retailer would like to forecast how many units of a particular product will be purchased from their locations based on a historical trend.

The source data contains weekly data for 2012 and 2013 details how many units have been moved. Some of the data, however, is populated with NULL values. For the NULL values, please assign the monthly average. If the monthly average is also NULL, assign the annual average.

Objective: Forecast the number of units that will be sold in the six weeks following the available data.

**Input**


|        Name        |  Type  |
|--------------------|--------|
| Product            | String |
| Fiscal Year        | Int16  |
| Fiscal Month       | String |
| Fiscal Week Number | String |
| Units              | Int16  |


**Output**


|       Name       |  Type  |
|------------------|--------|
| Period           | Byte   |
| Sub_Period       | Byte   |
| forecast         | Double |
| forecast_high_95 | Double |
| forecast_high_80 | Double |
| forecast_low_80  | Double |
| forecast_low_95  | Double |


