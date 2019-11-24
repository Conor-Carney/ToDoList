# Object Oriented Approach

 
import sys

class Queue():
	def __init__(self):
		self.items = []
	
	def isEmpty(self): # if queue is empty
		return self.items == []

	def enqueue(self,item): # adding something to our queue
		return self.items.append(item)

	def dequeue(self):
		item = self.items
		item.pop(0)
		return item

	def size(self): #size of our queue
		return len(self.items)

# Our ToDoList class inherits our Queue class
class ToDoList(Queue):
	def __init__(self):
		super().__init__()

	def accept(self,item): # adding to the queue
		self.enqueue(item)

	def discard(self): # removing from the queue
		self.dequeue()

	def printToDoList(self):
		for item in self.items:
			print(item.show())

# Tasks have a date, a start time, a duration and a list of people assigned to the task
class Task():
	def __init__(self,date,start_time,duration,assigned_people):
		self.date = date
		self.start_time = start_time
		self.duration = duration
		self.assigned_people = assigned_people

	def show(self):
		return "Date of task: {}\nStart time of task: {}\nDuration of task: {}\nPeople assigned to task: {}\n".format(self.date,self.start_time,self.duration,self.assigned_people)
# Events have a date, start time and a location
class Event():
	def __init__(self,date,start_time,location):
		self.date = date
		self.start_time = start_time
		self.location = location

	def show(self):
		return "Date of event: {}\nStart time of task: {}\nLocation of the event: {}\n".format(self.date,self.start_time,self.location)

def main():
	tdl = ToDoList()
	#tdl = Queue()
	print("\nPlease enter your action:\n'task'\n'event'\n'remove'\n'print'\n'end'")

	for action in sys.stdin:
		action = action.strip()
		print("Action = {}\n".format(action))

		if action == "task":
			date = input("Date of task: ")
			start_time = input("Task start time: ")
			duration = input("Duration of task: ")
			assigned_people = (input("First name of people seperated by a space: ")).split(" ")
			
			print("\n")
			print('-'*5 + 'Start of queue'+ '-'*5 )
			task = Task(date,start_time,duration,assigned_people)
			tdl.accept(task)
			tdl.printToDoList()
			print('-'*5 + 'End of queue'+ '-'*5)
			print("Task added to queue\n")
			print("Choose another action:\n'task'\n'event'\n'remove'\n'print'\n'end'\n")

		elif action == "event":
			date = input("Date of event: ")
			start_time = input("Event start time: ")
			location = input("Location of event: ")
			
			print("\n")
			print('-'*5 + 'Start of queue'+ '-'*5)
			event = Event(date,start_time,location)
			tdl.accept(event)
			tdl.printToDoList()
			print('-'*5 + 'End of queue'+ '-'*5)
			print("Item removed from queue\n")
			print("Choose another action:\n'task'\n'event'\n'remove'\n'print'\n'end'\n")

		elif action == "remove":
			try:
				print("\n")
				print('-'*5 + 'Start of queue'+ '-'*5)
				tdl.discard()
				tdl.printToDoList()
				print('-'*5 + 'End of queue'+ '-'*5)
				print("Event added to queue\n")
				print("Choose another action:\n'task'\n'event'\n'remove'\n,'print'\n'end'\n")
			except:
				print("ToDo List is empty! \n")
				print("Choose another action:\n'task'\n'event'\n'remove'\n'print'\n'end'\n")

		elif action == "print":
			print('-'*5 + 'Start of queue'+ '-'*5)
			tdl.printToDoList()
			print('-'*5 + 'End of queue'+ '-'*5)
			print("Choose another action:\n'task'\n'event'\n'remove'\n'print'\n'end'\n")

		elif action == "end":
			print("Thank you for using the ToDo List, goodbye!\n")
			sys.exit()

if __name__ == '__main__':
	main()