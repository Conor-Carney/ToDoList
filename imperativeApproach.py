to_do_list = ''

while True:
	action = input("\nPlease enter your action:\n'task'\n'event'\n'remove'\n'print'\n'end'\n")

	if action == 'task':
		date = input("Date of task: ")
		start_time = input("Task start time: ")
		duration = input("Duration of task: ")
		assignedPeople = input("Assigned people: ")
		print('\n')
		to_do_list += '\n' + 'Queue' + '\n' + date + '\n' + start_time + '\n' + duration + '\n' + assignedPeople + '\n'

	elif action == "event":
		date = input("Date of event: ")
		start_time = input("Event start time: ")
		location = input("Location of event: ")
		print('\n')
		to_do_list += '\n' + 'Queue' + '\n' + date + '\n' + start_time + '\n' + location + '\n'

	elif action == "remove":
		rm = to_do_list.find('Queue')
		to_do_list = to_do_list[rm+5:]
		rm = to_do_list.find('Queue')
		to_do_list = to_do_list[rm:]

	elif action == "print":
		print(to_do_list)

	elif action == "end":
		break

print("Thank you for using the ToDo List, goodbye!\n")