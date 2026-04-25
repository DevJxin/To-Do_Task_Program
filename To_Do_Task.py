import time
import sys
from colorama import Fore, Style, init

FILE_PATH = "To-Do.txt"
file_task = open(FILE_PATH, "a+")

print()
print("\t \t \033[1;4;36mWELCOME TO THE TO-DO LIST SOFTWARE\033[0m")
print()

init()

def line():
    print("--------------------------------------------------------------------------")

def doubleline():
    print("==============================================================================")

def menu():
    print("=====================================================================")
    print(f"\t{Fore.GREEN}1 : Add a New task")
    print(f"\t{Fore.GREEN}2 : See All Task ")
    print(f"\t{Fore.GREEN}3 : Clear All Task")
    print(f"\t{Fore.GREEN}4 : Set a task to Edit a task")
    print(f"\t{Fore.GREEN}5 : Set a task complete ")
    print(f"\t{Fore.GREEN}0 : ------EXIT-------{Style.RESET_ALL}")
    line()

def Display_Task():
    with open(FILE_PATH,"r") as f:
        for i,lines in enumerate(f,start=1):
            print(f"{i} : {lines.strip()}")
    file_task.seek(0)
    line()

def Task_Status():
    return "[PENDING]"

def Remove_Pending(line):
    if "[PENDING]" in line:
        return line.replace(
            "[PENDING]",
            f"[COMPLETED] At [{time.ctime()}]"
        )
    return line

def Add_a_task(Task):
    try: 
        global file_task
        file_task.write(f"{Task_Status()}\tTask : {Task}\t \tSTART : [{time.ctime()}]\n")
        file_task.flush()
    except (ValueError,FileNotFoundError) as er:
        print(f"{Fore.RED}Error : {er}")

def task_set_complete():
    Display_Task()
    
    file_task.seek(0) 
    num_lines = file_task.readlines()
    Msg = int(input("Select the number of the task to set it complete \n"))
    
    num_lines[Msg - 1] = Remove_Pending(num_lines[Msg - 1])

    with open(FILE_PATH, "w") as f:
        f.writelines(num_lines)

def Edit_file():
    Display_Task()

    doubleline()

    try:
        Re_edit = int(input("Enter the task you want to edit OR Mark completed \n"))
        file_task.seek(0)
        num_lines = file_task.readlines()
        Text_to_edit = input("Write the Task to edit or replace \n")
        num_lines[Re_edit-1]=(f"[EDITED]\tTASK : {Text_to_edit}  [{time.ctime()}]\n")

        with open(FILE_PATH, "w") as f:
            f.writelines(num_lines)
    except (ValueError,FileNotFoundError) as err:
        print(f"{Fore.RED}Error : {err}")

def exits():
    line()
    print("EXITING..........")
    time.sleep(2)
    sys.exit()

def input_from_user():
    inputInt = int(input("Enter the respected number to perfrom specific task\n"))
    line()
    return inputInt

def task_managment(num):
    if num == 1:
        Add_Task = input("Enter Your Task\n")
        Add_a_task(Add_Task)
    elif num == 2:
        Display_Task()
    elif num == 3:
        file_task.seek(0)
        file_task.truncate(0)
    elif num == 4:
        Edit_file()
    elif num == 5:
        task_set_complete()
    elif num == 0:
        exits()
    else:
        print(f"{Fore.RED}****Error Invalid input : Please enter a valid number****{Style.RESET_ALL}")

while True:
    time.sleep(0)
    menu()
    try :
        input_number = input_from_user()
        task_managment(input_number)
    except ValueError as e:
        print(f"{Fore.RED}****Error Invalid input : Please enter a valid number****{Style.RESET_ALL}")