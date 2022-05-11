#global variables 11/5/22
questions = []
#this text is to inform the user of what the quiz is about 11/5/22
print("Kia ora welcome to the Te Reo quiz, this quiz is designed to test your Te Reo Skills")
print("what part of the language do you struggle with most? or would like to test your skills on?")
#the current number of quizes is not set there might not acctually be 5 options by the end 11/5/22
print("A animals,B objects,C family members,D colours or E all of the above")
#abcde is def so that I can call it at any time its purpose is to personalise thier quiz questions 11/5/22
def abc():
  abcde = input().lower()
  global questions
  if abcde == "a":
    print("you have selected animals")
    questions = ['pig','horse','cow','chicken','','','','','']
  elif abcde == "b":
    print("you have selected objects")
  elif abcde == "c":
    print("you have selected family members")
  elif abcde == "d":
    print("you have selected colours")
  elif abcde == "e":
    print("you have selected all of the above")
  elif abcde == "quit":
    quit()
  else:
    print("answer A/B/C/D/E or anwer quit to quit")
    abc()
abc()
def quiz():
  print("")