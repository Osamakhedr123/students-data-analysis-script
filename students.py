# Importing needed modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Reading CSV file
df=pd.read_csv("StudentsPerformance.csv")

# to make the program repetititve
check="yes"
while check=="yes" or check=="y":

# Main menu ceation
    while True:
        # Handling non-integer input
        try:
            operation=int(input("Choose a number\n\
                                    1- Display the data for a specific student.\n\
                                    2- Display the data for all students.\n\
                                    3- Display the results for a specific student.\n\
                                    4- Display the results for all students.\n\
                                    5- Display the total grades for each student.\n\
                                    6- Make a graph for the student's grades for each subject.\n\
                                    7- Display the failed students and excellent students.\n\
                                    8- Display basic statistics for each subject grades.\n\
                                    9- Search for specific student/subject grade for a specific student.\n\
                                    10- Delete student record/ grade for a subject of a student.\n\
                                    11- Partition the file into two equal files of data.\n\
                                Your choice: ").strip())
            # Handling output that's not in range
            if operation in range(1,12):
                break
            else:
                print("The number you entered is out of range!\nTry again:")
        except ValueError:
            print("Invalid input.\nPlease choose a number between 1 and 11.")    
    if operation==1:
        in_stu_id=int(input("Enter student Id: ").strip())
        if in_stu_id in df["student_id"].values:
            print(df.loc[df["student_id"]==in_stu_id][["student_id","name","address"]])
        else:
            print("You entered an invalid id\n")

    if operation==2:
        print(df[["student_id","name","address"]])

    if operation==3:
        in_stu_id=int(input("Enter student Id: ").strip())
        if in_stu_id in df["student_id"].values:
            print(df.loc[df["student_id"]==in_stu_id,df.columns != "address"])
        else:
            print("You entered an invalid id\n")
    if operation==4:
        print(df.loc[:,df.columns !='address'])
            
    if operation==5:
        df["total"]=df.database+df.algorithms+df.system_analysis+df.organization+df.software_development+df.logic+df.math
        print(df[["student_id","name","total"]])

    if operation==6:
        for col in ["database","algorithms","system_analysis","organization","software_development","logic","math"]:
            plt.hist(data=df,x=col)
            plt.title("Distribution of grades in {}".format(col))
            plt.xlabel("Grades in {}".format(col))
            plt.ylabel("Number of students")
            plt.show()

    if operation==7:
        df["total"]=df.database+df.algorithms+df.system_analysis+df.organization+df.software_development+df.logic+df.math
        df_failed=df.query('total<=350')
        df_succeeded=df.query('total>350')
        print("Failed students:\n{}".format(df_failed))
        print('-'*40)
        print("Succeded students:\n{}".format(df_succeeded))

    if operation==8:
        for subject in ["database","algorithms","system_analysis","organization","software_development","logic","math"]:
            print("Mean of grades in {}: {}".format(subject,df[subject].mean()))
            print("Standard deviation of grades in {}: {}".format(subject,df[subject].std()))

    if operation==9:
        in_stu_id=int(input("Enter student Id: ").strip())
        in_stu_sub=input("Enter the subject: ").strip().lower().replace(" ","_")
        if in_stu_id in df["student_id"].values and in_stu_sub in df.columns:
            name=df.loc[df["student_id"]==in_stu_id,"name"][0]
            grade=df.loc[df["student_id"]==in_stu_id,in_stu_sub][0]
            print("{} got {}/100 in {}".format(name,grade,in_stu_sub))
        else:
            print("You entered an invalid id or subject\n")

    if operation==10:
        print("Please close the csv file if it's opened")
        in_stu_id=int(input("Enter student Id: ").strip())
        in_stu_sub=input("Enter the subject: ").strip().lower().replace(" ","_")
        if in_stu_id in df["student_id"].values and in_stu_sub in df.columns:
            df.at[df["student_id"]==in_stu_id,in_stu_sub]=None
            try:
                os.remove("StudentsPerformance.csv")
                df.to_csv("StudentsPerformance.csv",index=False)
                print("CSV file updated successfully")
            except:
                print("The csv file is opened! please close it and try again.")
            
        else:
            print("You entered an invalid id or subject\n")

    if operation==11:
        num_rows=df.shape[0]
        df1=df.iloc[:num_rows//2,:]
        df2=df.iloc[num_rows//2:,:]
        df1.to_csv("first_half.csv",index=False)
        df2.to_csv("second_half.csv",index=False)
        
    # Checking if the user wants to choose another option

    check=input("Do you want to continue? (enter yes to continue or no to exit): ").strip().lower()



