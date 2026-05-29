import time
import json

# TODO Add a way to select file from file explorer gui menu?
task_file_path = "C:\\source\\Python Learning\\Task-List.json"
tasks = {}

def ListTaskOptions():
  # TODO Clear console text - How do I make it a >>> prompt?
  # os.system('cls') is deprecated so..?
  print("NOTE: The current file path is " + task_file_path)
  print("Enter 0-5 to pick from the options below")
  print("0 or 'Enter' - View Tasks at current file path")
  print("1 - Create new Task file")
  print("2 - Change current path")
  option = input("Enter option: ")

  if option == "0" or option == "" or option =="Enter":
    ViewCurrentTasks()
  elif option == "1":
    CreateTaskFile()
  elif option == "2":
    ChangeTaskFilePath()
  else:
    print("Not a valid option. Give it another try!")
    time.sleep(3)
    ListTaskOptions()

  return

def ViewCurrentTasks():
  LoadTasks()
  # TODO Display tasks
  # TODO Display task options (Remove, Add, Edit)
  return

def LoadTasks(permission="r"):
  global tasks
  print("Grabbing Tasks from " + task_file_path)
  try:
    with open(task_file_path, permission) as task_list:
      tasks = json.load(task_list)
  except:
    print("The file was not found at this location! Change file path?")
    confirmation = input("Confirm? (y/n): ")
    if confirmation == "y" or confirmation == "":
      ChangeTaskFilePath()
    else:
      print("Canceled. Returning to Main Menu...")
      time.sleep(3)
      ListTaskOptions()
  return 'Error'

def CreateTaskFile():
  return

def ChangeTaskFilePath():
  global task_file_path 
  print("Your current path is " + task_file_path)
  new_task_file_path = input("Enter new file path: (or press 'q' to quit.) ")
  if new_task_file_path == "q" or new_task_file_path == "quit":
    print("Returning to Main Menu...")
    time.sleep(3)
    ListTaskOptions()
    return
  else:
    print("You entered " + new_task_file_path)
    confirmation = input("Confirm? (y/n): ")
    if confirmation == "y" or confirmation == "":
      # TODO find how to make this permanent by editing and saving current file.
      print("Confirmed! Returning to Main Menu...")
      task_file_path = new_task_file_path
      time.sleep(3)
      ListTaskOptions()
    else:
      print("Canceled. Returning to previous input")
      time.sleep(3)
      ChangeTaskFilePath()
  return

ListTaskOptions()