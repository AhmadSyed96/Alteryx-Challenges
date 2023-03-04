The link to the solution for last challenge #36 is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-36-Data-Cleansing-Extract-Authors-Intermediate/m-p/36439#M13).

Using raw XML files as input can present some interesting challenges. The challenge is that the data is nested into the records in a way that requires you to extract it through parsing steps, sometimes drilling many levels into the data (Root and child levels). Alteryx makes this easier to do using the XML Parsing tool. We will explore the process in this exercise.

Use Case: A company receives customer purchase and shipping data on a weekly level based on web and catalog purchases. The company would like to analyze their customers and produce a profile by market by SKU. The challenge is that the data feed contains XML that needs to be parsed in order effectively analyze the data.

Objective: The column called customer_OuterXML contains the data that needs to be parsed into 25 unique fields detailing the customer contact information for both the “Bill To” and “Ship To” attributes.

Note: As of 9/11/2019, the Start file and Solution files were edited. Based on when you complete this challenge, you may see that the solutions posted here may reference a dataset that was previously available. Posted solutions (as files) using the previous dataset have been replaced with the Alteryx Academy logo to acknowledge that user's contribution that we can no longer share publicly.

**Input**


|       Name        |   Type   |
|-------------------|----------|
| date              | Date     |
| source            | V_String |
| Order Number      | String   |
| customer_OuterXML | V_String |
| purchase2         | String   |
| shipment2         | String   |
| purchase          | V_String |
| shipment          | String   |


**Output**


|          Name           |   Type   |
|-------------------------|----------|
| Date                    | Date     |
| Source                  | String   |
| Order Number            | String   |
| Purchase                | String   |
| Shipment                | String   |
| Billing_first_name      | String   |
| Billing_last_name       | String   |
| Billing_home_phone      | Int64    |
| Billing_email           | String   |
| Billing_Street address  | String   |
| Billing_city            | String   |
| Billing_State           | String   |
| Billing_State Code      | String   |
| Billing_postal_code     | String   |
| Billing_country_code    | String   |
| Shipping_first_name     | String   |
| Shipping_last_name      | String   |
| Shipping_home_phone     | Int64    |
| Shipping_email          | String   |
| Shipping_Street address | V_String |
| Shipping_city           | String   |
| Shipping_State          | String   |
| Shipping_State Code     | String   |
| Shipping_postal_code    | String   |
| Shipping_country_code   | String   |
| Date                    | Date     |
| Source                  | String   |
| Order Number            | String   |
| Purchase                | String   |
| Shipment                | String   |
| Billing_first_name      | String   |
| Billing_last_name       | String   |
| Billing_home_phone      | Int64    |
| Billing_email           | String   |
| Billing_Street address  | String   |
| Billing_city            | String   |
| Billing_State           | String   |
| Billing_State Code      | String   |
| Billing_postal_code     | String   |
| Billing_country_code    | String   |
| Shipping_first_name     | String   |
| Shipping_last_name      | String   |
| Shipping_home_phone     | Int64    |
| Shipping_email          | String   |
| Shipping_Street address | V_String |
| Shipping_city           | String   |
| Shipping_State          | String   |
| Shipping_State Code     | String   |
| Shipping_postal_code    | String   |
| Shipping_country_code   | String   |


