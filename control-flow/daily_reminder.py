task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
error_message = "something went wrong!"
first_part = f"{task} is a {priority} priority task"
match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"{first_part} that requires immediate attention today!"
        elif time_bound == "no":
            reminder = f"{first_part} but it is not time bound you can schedule it."
        else:
            reminder = error_message
    case "medium":
        if time_bound == "yes":
            reminder = f"{first_part}, you can do it if you have free time"
        elif time_bound == "no":
            reminder = f"{first_part}, you can schedule it for later"
        else:
            reminder = error_message
    case "low":
        if time_bound == "yes":
            reminder = f"{first_part} but it's time bound, you can delegate it"
        elif time_bound == "no":
            reminder = f"{first_part} and it is not time bound you can ignore it"
        else:
            reminder = error_message
    case _ :
        reminder = error_message
print(reminder)