Happy Monday… oh wait it's Tuesday already. Sorry for the delay if you are an international Alteryx community member, yesterday the USA and Canada celebrated Labor Day in honor of working people.

Hopefully everyone had fun debugging the Macro last week, the link to the solution for that challenge (#39) is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-39-Trouble-shooting-a-broken-macro-Intermediate/m-p/36580#M16). For this week we look at what needs to be done to process raw HTML data after using the download tool to scrape the web.

One of the features of the Alteryx download tool is that it can pull down the raw HTML code from a web page. This practice sometimes referred to as web scraping is useful when there is embedded data in the page you want to access from Alteryx. The challenge is that the raw HTML needs to parsed to prepare the data for use.

Use case: 5280 Magazine in Denver published a list of the  [best doctors in the Denver metro area](http://www.5280.com/topdocslist?title=&specialty=All&hospital=All&distance%5Bpostal_code%5D=&distance%5Bsearch_distance%5D=5&distance%5Bsearch_units%5D=mile&field_year_value=&field_doctor_current_year_value_checkbox=0&page=full), you need to download that list in database form. (Note the Raw HTML has been provided in the workflow)  

Objective: Parse the HTML into a database format containing fields for the ID, Physician, Address, City and Practice

Good luck, I hope you are having fun with these  challenges and expanding your knowledge of Alteryx. Thanks to all that participate and have provided feedback.

**Input**


|      Name       |   Type    |
|-----------------|-----------|
| URL             | String    |
| DownloadData    | V_WString |
| DownloadHeaders | V_String  |


**Output**


|   Name    |   Type    |
|-----------|-----------|
| ID        | Int16     |
| Physician | V_WString |
| Address   | V_String  |
| City      | V_String  |
| Practice  | V_String  |


