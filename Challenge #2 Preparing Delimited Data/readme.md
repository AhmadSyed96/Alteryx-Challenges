We hope you enjoyed last week's  challenge. The solution has been posted  [here](https://community.alteryx.com/t5/Weekly-Challenge/Alteryx-Weekly-Exercise-Week-1-Join-to-Range/m-p/36621#U36621). For the second  challenge  lets look at removing characters and splitting data into columns based on delimiters.

Many products will export textual data with delimiters such as quotes. This is done so that strings can contain delimiters or control characters within them. Having more than one type of delimiter can be hard for ETL programs to interpret. In the input text file, there are two different delimiters (double quotes, single quotes) and they surround different data types.

Use Alteryx to strip out the delimiters as superfluous and format the data as represented in the output.

You may notice that we have started classifying the exercises into beginner, Intermediate and advanced. This classification is used by Alteryx internally to sequence exercises as users advance

**Input**


| Name |   Type   |
|------|----------|
| Date | V_String |
| Time | V_String |



**Output**



|     Name      |   Type   |
|---------------|----------|
| DateTime Conv | DateTime |





