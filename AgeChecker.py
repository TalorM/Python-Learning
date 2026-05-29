input = input("Submit your age (or 'q' to quit)")
print("You submitted: " + input)

def ageChecker (age):
  if age.lower() == 'quit' or 'q':
    return print('Cya!')
  elif age.isdigit() == True:
    print('input accepted')
    age = int(age)
    if age >= 18 and age < 150:
      print("You are an adult")
    elif age < 18:
      print("You are a minor") 
    else:
      print("Are you really this old?")
  else:
    print('This is not an accepted input')

  print("this should print after the function ends")

ageChecker(input)