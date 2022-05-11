#this text is to inform the user of what the quiz is about 11/5/22
print("Kia ora welcome to the Te Reo quiz, this quiz is designed to test your Te Reo Skills")
print("what part of the language do you struggle with most? or would like to test your skills on?")
#the current number of quizes is not set there might not acctually be 5 options by the end 11/5/22
print("A animals,B objects,C family members,D colours or E all of the above")
#abcde is def so that I can call it at any time its purpose is to personalise thier quiz questions 11/5/22
def abcde():
  abcde = input().lower()
  if input == "a":
    print("")
  if input == "b":
    print("")
  if input == "c":
    print("")
  if input == "d":
    print("")
  if input == "e":
    print("")
  if input == "quit":
    quit()
  else:
    print("answer A/B/C/D/E or anwer quit to quit")
    abcde()