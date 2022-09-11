import pandas as pd
emp_data = {"Emp_id":[1,2,3,4,5],
            "Emp_Name":["Satish","Vani","Ramesh","Praveen","Pallavi"],
            "Salary":[5000,7000,10000,9500,4500],
            "Start_date":["01-11-2013","05-06-2011","21-09-1999","13-09-2005","23-10-2000"]}
df = pd.DataFrame(emp_data)

#Extracting two column names using column name
print("----Extracting two column names using column name----")
print(df.loc[:,"Emp_Name"])

#Extracting the first two rows
print("\n----Extracting the first two rows----")
print(df.loc[0])
print("\n",df.loc[1])

#Extracting all columns
print("\n----Extracting all columns----")
print(df.loc[:,["Emp_id","Emp_Name","Salary","Start_date"]])

#Extracting 3rd and 5th row with 2nd and 4th column
print("\n----Extracting 3rd and 5th row with 2nd and 4th column----")
print(df.loc[(df['Emp_Name']=='Ramesh') & (df['Start_date']=='21-09-1999')])
print("\n",df.loc[(df['Emp_Name']=='Pallavi') & (df['Start_date']=='23-10-2000')])
