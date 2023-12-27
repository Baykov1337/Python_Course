# Task manager - create a program that manages the tasks 
#   Function that could add, view and delete tasks

# 1.1 Create task
list_tasks = ["Create list","Use while/for for add a new info and add it to that list"]
# 1.2 Use loop(while/for) for insert new task
inputstr = ''


while inputstr != 'end':
    inputstr = input("Please add a new task, Type 'end' when you finish adding a tasks: ")
    if inputstr == 'end':
        break
    list_tasks.append(inputstr)

#print (list_tasks)
    
# 2 View tasks 
# 2.1 Use loop (while/for) to overview all the tasks with index staring from 1 
dict_list = {}
for x in range(len(list_tasks)):
    dict_list[x+1] = list_tasks[x]
    print (f"{x+1} {list_tasks[x]}" )
# 3.0 Change the name of the task from the index generated in the previous step 
#    3.1 use the index to change the task 
print (dict_list)
Change_task_by_index = input("If you consider changing the task order please enter the 'change' ")

if Change_task_by_index == 'change':
    inputstr = input("Please enter the valid index of the task you want to change:")
    try:
        dict_list[int(inputstr)] = input(f"You're about to change task with index {inputstr}, please enter the new task:")
    except ValueError:   
        print ("You've entered incorrect value!") 

print (dict_list.items())      
#print (dict_list.keys())
# 4.0 Change the place of 2 task by index

inputstr = input("Whould you like to change the task order? type 'reorder' to oontinue:")
#print (list(dict_list.items())[1])
if inputstr == 'reorder':
    inputstr = input("Please enter the first ID you want to change:")
    try : 
        int(inputstr)  
    except ValueError:   
        print ("You've entered incorrect value!")
    inputstr2 = input("Please enter the Second ID you want to change:")
    try: 
        int(inputstr2) 
    except ValueError:   
        print ("You've entered incorrect value!")    
    try:
        if int(inputstr) not in dict_list:
            print("Cannot find the first value in dictionary")
        elif int(inputstr2) not in dict_list:
            print("Cannot find the second value in dictionary")
        elif int(inputstr) == int(inputstr2):
            print ("Both values have to be different")
            exit()
        else:
            swaped = {i:v for i, v in dict_list.items()}
            val1 = dict_list[int(inputstr)]  
            val2 = dict_list[int(inputstr2)]  
            swaped[int(inputstr)] = val2
            swaped[int(inputstr2)] = val1
            dict_list = swaped
    except ValueError:   
        print ("You've entered incorrect value!")  

print (dict_list)   

# 5.0 Delete task 
# 5.1 Find the task based on ID or Name and delete it. 
inputstr = input("If you want to remove task by ID or name please enter 'delete':")

if inputstr == 'delete':
    inputstr = input("To delete by ID or Name type 'ID' or Name ")
    if inputstr == 'ID':
        inputstr = input("Please enter the ID of the task you want to delete: ")
        if int(inputstr) not in dict_list.keys:
            print("Cannot find the value in dictionary")
            exit()
        else: 
            if int(inputstr) in dict_list:
                del dict_list[int(inputstr)]
                print(f"{int(inputstr)} deleted from the dictionary.")
            else:
                print(f"{int(inputstr)} not found in the dictionary.")
    elif inputstr == 'Name':
        inputstr = input("Please enter the Name of the task you want to delete: ")
        for key, value in list(dict_list.items()):
            if value == inputstr:
                del dict_list[key]
                print(f"Deleted key '{key}' with value {inputstr}")
            else:
                print(f"{inputstr} not found in the dictionary.")
    else:
        print ("You have entered an invalid value")            
                        
