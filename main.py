#this text is to inform the user of what the quiz is about 11/5/22
print("Kia ora welcome to the Te Reo quiz, this quiz is designed to test your Te Reo Skills")
print("what part of the language do you struggle with most? or would like to test your skills on?")
#the current number of quizes is not set there might not acctually be 5 options by the end 11/5/22
print("A animals,B objects,C family members,D colours or E all of the above")
#abcde is def so that I can call it at any time its purpose is to personalise thier quiz questions 11/5/22
def abc():
  abcde = input().lower()
  if abcde == "a":
    print("")
  elif abcde == "b":
    print("")
  elif abcde == "c":
    print("")
  elif abcde == "d":
    print("")
  elif abcde == "e":
    print("")
  elif abcde == "quit":
    quit()
  else:
    print("answer A/B/C/D/E or anwer quit to quit")
    abc()
abc()