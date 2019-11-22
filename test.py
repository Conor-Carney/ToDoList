to_do = ''

def add_task(date, start_time, duration, attendees, curr_list):
    global to_do
    curr_list = date + '\n' + start_time + '\n' + duration + '\n' + attendees + '\n' + "NEW:" + '\n'
    to_do += curr_list

def add_event(date, time, location, curr_list):
    global to_do
    curr_list = '\n'  + date + '\n' + time + '\n' + location + '\n' + "NEW:"
    to_do += curr_list

def remove_item(to_do_list):
    global to_do
    if to_do.count('\n') > 5:
        to_do = to_do[to_do.index("NEW:"):]

    elif to_do.count('\n') == 4 or to_do.count('\n') == 5 or to_do.count('\n') == 6:
        to_do = ''

    else:
        to_do = ''
        print('Everything has been done! Nothing to remove.')


item = input('If you would like to add a task or event, please type task or event. If you want to remove, type rm:{}'.format('\n'))


while item != 'Exit':

    if item == 'task':
        add_task(input('Date: '), input('Start Time: '), input('Duration: '), input('Attendees: '), to_do)
        print(to_do)

    elif item == 'event':
        add_event(input('Date: '), input('Time: '), input('Location: '), to_do)
        print(to_do)
    
    elif item == 'rm':
        remove_item(to_do)
        print(to_do)
        
    item = input('What else would you like to add or remove?')