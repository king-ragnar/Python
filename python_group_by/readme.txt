Here Our objective is to group and find the sum count of the successfull rows inserted in cube names for the particular date 


given An Excel File(.xlsx) containing 800+ records with Fields - [data cube names , date with hourly successful row count]

How we achieved the objective:

1) Read the excel file using pandas library
2) clean the date field by removing the time example : 21-02-23 11:00 , 21-02-23 12:00 we clean the date field by stripping off the time thereby having  21-02-23
3) now after data cleansing we will group by Date field first and then we will group by cube names
4) export the extracted data into a new excel sheet.

Libraries required:
pandas 
datetime
