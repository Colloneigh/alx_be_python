#prompt the user for the task, priority and time-bound

task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

#process the task based on priority and time sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"{task} is a high priority task that requires immediate attention today!"
        else:
            reminder = f"{task} is a high priority task that needs to be done today!"
    case "medium":
        if time_bound =="yes":
            reminder = f"{task} schedule time to do this task today!"
        else:
            reminder = f"{task} delegate sommeone to do this task today!"
    case "low":
        if time_bound == "yes":
            reminder = f"{task} do the task only when you are free!"
        else:
            reminder = f"{task} is a low priority task. Consider completing it when you have free time."

print(f"Reminder: {reminder}")