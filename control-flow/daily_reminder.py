task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
error_message = "something went wrong!"
first_part = f"{task} is a {priority} priority task"
match priority:
    case "high":
        reminder = "that requires immediate attention today!"
    case "medium":
       reminder = "schedule it for later"
    case "low":
        reminder = "Consider completing it when you have free time."
    case _ :
        message = error_message
if time_bound == "yes":
    reminder = "that requires immediate attention today!"
elif time_bound == "no":
    reminder = "Consider completing it when you have free time."
else:
    message = error_message 

message = f"{task} is a {priority} priority task.{reminder}."
print(message)