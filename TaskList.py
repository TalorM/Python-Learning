import time
import json

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
    ListTasks()
  elif option == "1":
    CreateTaskFile()
  elif option == "2":
    ChangeTaskFilePath()
  else:
    print("Not a valid option. Give it another try!")
    time.sleep(3)
    ListTaskOptions()

  return

def ListTasks():
  # Pull tasks
  # Display tasks
  # Display options to edit, add, or remove
  print("Grabbing Tasks from " + task_file_path)
  # try:
  #   with open(task_file_path)
  # except
  # tasks = json.load()
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

def CreateTaskFile():
  return

ListTaskOptions()