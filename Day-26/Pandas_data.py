student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}
#---------------------------------------------------------------------------------
#looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

#---------------------------------------------------------------------------------
import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
# print(student_data_frame)

#---------------------------------------------------------------------------------
#Loop throught a data frame
# for (key, value) in student_data_frame.items():
#     print(key)
#     #key : student , score
#     #value ["Angela", "James", "Lily"], score : [56, 76, 98]

#---------------------------------------------------------------------------------
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

#     print(row)
    #student        Angela
    #score          56
    #Name:0,    dtype : object

