weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
#new_dict = {new_key : new_value for (Key, value ) in dict.items()}
#new_dict = {new_key : new_value}
#            monday  :  12 
weather_f = {day : temp_c * 9/5 + 32 for (day, temp_c) in weather_c.items()}


print(weather_f)


