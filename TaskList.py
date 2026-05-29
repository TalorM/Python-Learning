import time

def ListTaskOptions():
  # TODO Clear console text - How do I make it a >>> prompt?
  # os.system('cls') is deprecated so..?
  print("NOTE: The current default location is 'C:\source\Python Learning'")
  print("Enter 0-5 to pick from the options below")
  print("0 or 'Enter' - View Tasks at JSON file in default location.")
  print("1 - Create new JSON Task file.")
  print("2 - Change default location?")
  option = input("Submit here: ")

  if option == 0:
    ListTasks()
  elif option == 1:
    CreateJSONFile()
  elif option == 2:
    print("Mmm idk how to do this yet but ill circle back if i can get it working nicely.")
    time.sleep(3)
    ListTaskOptions()
  else:
    print("Not a valid option. Give it another try!")
    time.sleep(3)
    ListTaskOptions()
  
  return

def ListTasks():
  return

def CreateJSONFile():
  return



ListTaskOptions()