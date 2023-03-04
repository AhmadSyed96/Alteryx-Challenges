The link to last week’s challenge (challenge #22) is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-22-Identify-Values-to-Aggregate-Intermediate/m-p/36751#M47).

Restructuring poorly formatted data is one of the most common Alteryx use cases. For this challenge we will attempt to straighten out some Very poorly formatted data that is representative of an actual customer request.

The use case: A CPG company is having difficulty managing its data for analytics. The data they receive via an excel spreadsheet contains empty rows and misaligned fields.

The objective: reformat the data in order to enable the analytics team to spend less time staging the data and more time doing analytics.

**Input**

| Name |   Type   |
|------|----------|
| F1   | V_String |
| F2   | V_String |
| F3   | V_String |
| F4   | V_String |
| F5   | V_String |
| F6   | V_String |
| F7   | V_String |
| F8   | V_String |
| F9   | V_String |
| F10  | V_String |
| F11  | V_String |
| F12  | V_String |
| F13  | V_String |
| F14  | V_String |
| F15  | V_String |
| F16  | V_String |
| F17  | V_String |
| F18  | V_String |
| F19  | V_String |
| F20  | V_String |
| F21  | V_String |
| F22  | V_String |
| F23  | V_String |
| F24  | V_String |
| F25  | V_String |
| F26  | V_String |
| F27  | V_String |
| F28  | V_String |
| F29  | V_String |
| F30  | V_String |
| F31  | V_String |
| F32  | V_String |
| F33  | V_String |
| F34  | V_String |
| F35  | V_String |
| F36  | V_String |
| F37  | V_String |
| F38  | V_String |
| F39  | V_String |
| F40  | V_String |
| F41  | V_String |
| F42  | Double   |
| F43  | Double   |
| F44  | Double   |
| F45  | Double   |
| F46  | Double   |
| F47  | Double   |
| F48  | Double   |
| F49  | Double   |
| F50  | Double   |
| F51  | Double   |
| F52  | Double   |
| F53  | Double   |
| F54  | Double   |

**Output**


|         Name         |   Type   |
|----------------------|----------|
| Holding Co           | String   |
| WEEK                 | String   |
| Brand                | V_String |
| AVG_PRICE            | V_String |
| BL_DOLLARS           | V_String |
| BL_UNITS             | V_String |
| DISP_ONLY__ACV__MAX_ | V_String |
| DOLLARS              | V_String |
| FEAT_ONLY__ACV__MAX_ | V_String |
| INC_DOLLARS          | V_String |
| INC_UNITS            | V_String |
| PRICEDISC__ACV__MAX_ | V_String |
| UNITS                | V_String |



