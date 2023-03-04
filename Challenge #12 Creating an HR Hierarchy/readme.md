
Here is this week’s  challenge, I would like to thank everyone for playing along and for your feedback. You can find the solution to the previous  challenge [here](https://community.alteryx.com/t5/Weekly-Challenge/Alteryx-Weekly-Exercise-11-Identify-Logical-Groups-from-Text/m-p/36739#M35).

For this  challenge let’s look at creating a multi-level hierarchy from employee-manager data. As always there are several ways to do this  challenge, I have designated it as an advanced  challenge because there is an elegant way to solve it using iterative macros. The advantage to the iterative macro solution is that it becomes very dynamic. Other hard coded solutions would get you to the answer with this data, but if the depth of the hierarchy were to change, you would have to modify the workflow to support the change. It is a great example to see how iterative macros can make a workflow dynamic.

**The use case:**

An HR department wants to use Alteryx to quickly understand the reporting structure for employees across their organization.

The Input source contains 5 employees and an identifier that uniquely identifies the individual and the manager they report to.

The goal is to create a hierarchy field identifying each relationship between employee and manager(s). For example, a Director reports directly to the Vice President which is 1 level up. The Director is then 2 levels away from the CEO (in this data set). As a result the hierarchy identifier represents how many levels removed the employee is from management team they report into.

Give it a try, I look forward to your feedback.

**Input**


|   Name   |   Type   |
|----------|----------|
| employee | V_String |
| id       | Byte     |
| man_id   | Byte     |



**Output**


|   Name    |   Type   |
|-----------|----------|
| employee  | V_String |
| Manager   | V_String |
| Hierarchy | Byte     |


