# Object Oriented Approach
# We must create seperate classes to create new user defined data structures 
# which hold arbitrary information about our program
# Our classes will be our 'Queue','toDoList', 'Event', and finally our 'Task'


# Create the Queue class first
# 
class Queue():
	def __init__(self):
		self.items = []
	
	def isEmpty(self): # if queue is empty
		return self.items == []

	def enqueue(self,item): # adding something to our queue
		return self.items.append(item)

	# with our queue we work with a #fifo method so when we
	# remove something from the queue it is the first item 
	# that was added onto the queue that is taken off
	def dequeue(self):
		item = self.items
		item.pop(0)
		return item

	def size(self): #size of our queue
		return len(self.items)

# Our ToDoList class inherits our Queue class
class ToDoList(Queue):
	def __init__(self):
		self.items = []

	def accept(self,item): # adding to the queue
		self.enqueue(item)

	def discard(self): # removing from the queue
		self.dequeue()

	def printToDoList(self):
		for item in self.items:
			print(item)

# Tasks have a date, a start time, a duration and a list of people assigned to the task
class Task():
	def __init__(self,date,startTime,duration,assignedPeople):
		self.date = date
		self.startTime = startTime
		self.duration = duration
		self.assignedPeople = assignedPeople


	def show_task(self):
		return "Date of task: {}\nStart time of task: {}\nDuration of task: {}\nPeople assigned to task: {}\n".format(self.date,self.startTime,self.duration,self.assignedPeople)
# Events have a date, start time and a location
class Event():
	def __init__(self,date,startTime,location):
		self.date = date
		self.startTime = startTime
		self.location = location

	def show_event(self):
		return "Date of event: {}\nStart time of task: {}\nLocation of the event: {}\n".format(self.date,self.startTime,self.location)

def main():
	l = ToDoList()
	task = Task("15/11/1997","2:00pm","2hrs", ["conor","ben"])
	task2 = Task("21/7/2019", "4pm", "5hrs", ["conor","james","ben"])
	event = Event("29/2/2120","4pm","l135")
	event2 = Event("30/2/2010","4pm","xg19")

	l.accept(task.show_task())
	l.accept(event.show_event())
	l.accept(task2.show_task())
	l.discard()
	l.accept(event2.show_event())
	l.discard()
	l.printToDoList()

if __name__ == '__main__':
	main()