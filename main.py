#global variables 11/5/22
import random
questionlista = []
questionlistb = []
answersforlistaa = []
answersforlistab = []
question = 0
correct = 0
wrong = 0
l = "list"
#this text is to inform the user of what the quiz is about 11/5/22
print("Kia ora welcome to the Te Reo quiz, this quiz is designed to test your Te Reo Skills")
print("what part of the language do you struggle with most? or would like to test your skills on?")
#the current number of quizes is not set there might not acctually be 5 options by the end 11/5/22
print("A animals,B objects,C family members,D colours or E all of the above")
def quizb():
  global questionlista
  global questionlistb
  global question
  global correct
  global wrong
  global l
  question += 1
  if l == "list":
    l = list(range(len(questionlistb)))
  if l:
    question1 = random.choice(l)
    if question ==1:
      print("question"+str(question))
    else:
      print("question"+str(question))
    print("what is the English name for",questionlistb[question1])
    answer1 = input().lower()
  
    if answer1 == questionlista[question1]:
      print("congrats")
      correct += 1
      l.remove(question1)
      quizb()
    elif answer1 == "quit":
      quit()
    elif answer1 == "return":
      l = "list"
      print("A animals,B objects,C family members,D colours or E all of the above")
      abc()
    else:
      print("sorry but the anwer was",questionlista[question1])
      wrong += 1
      l.remove(question1)
      quizb()
  else:
    print("you have answerd all of the questions your final score was",str(correct)+"/"+str(question-1),"or",(correct/(question-1))*100,"%")
    print("A animals,B objects,C family members,D colours or E all of the above")
    abc()
#this is the quiz for the Māori names of english words 13/5/22
def quiza():
  global questionlista
  global questionlistb
  global answersforlistaa
  global answersforlistab
  global question
  global correct
  global wrong
  global l
  question += 1
  if not l:
    print("you have answerd all of the questions your final score was",str(correct)+"/"+str(question-1),"or",(correct/(question-1))*100,"%")
    print("A animals,B objects,C family members,D colours or E all of the above")
    abc()
  if question ==1:
    print("question"+str(question))
  else:
    print("question"+str(question))
  if l == "list":
    l = list(range(len(questionlistb)))
  question1 = random.choice(l)
  print("what is the Māori name for",questionlista[question1])
  answer1 = input().lower()
  
  if answer1 == answersforlistaa[question1]:
    print("congrats")
    correct += 1
    l.remove(question1)
    quiza()
  elif answer1 == questionlistb[question1]:
    print("congrats")
    correct += 1
    l.remove(question1)
    quiza()
  elif answer1 == answersforlistab[question1]:
    print("congrats")
    correct += 1
    l.remove(question1)
    quiza()
  elif answer1 == "quit":
    quit()
  elif answer1 == "return":
    l = "list"
    print("A animals,B objects,C family members,D colours or E all of the above")
    abc()
  else: 
    print("sorry but the anwer was",questionlistb[question1])
    wrong += 1
    l.remove(question1)
    quiza()
#words is to ask the player whether they want to traslate english words or Te Reo words 13/2/22
def words():
  global questionlista
  global questionlistb
  names = input().lower()
  if names == "a":
    print("you have selected: the Māori names of english words 8 questions")
    print("*hint use double vowels instaid of macrons*")
    quiza()
  elif names == "b":
    print("you have selected: the english names of Māori words")
    quizb()
  elif names == "c":
    print("you have selected: Both")
  elif names == "quit":
    quit()
  elif names == "back":
    print("A animals,B objects,C family members,D colours or E all of the above")
    abc()
  else:
    print("answer A/B/C you can also answer :quit: to quit or :back: to go back ")
    words()
    
#abcde is def so that I can call it at any time its purpose is to personalise thier quiz questions 11/5/22
def abc():
  abcde = input().lower()
  global questionlista
  global questionlistb
  global answersforlistaa
  global answersforlistab
  if abcde == "a":
    print("you have selected animals")
    print("do you want to guess A: the Māori names of english words or B: the english names of Māori words or C: both")
    questionlista = ['cat','dog','sheep','pig','cow','horse','chicken','rabbit']
    questionlistb = ['ngeru','kuri','hipi','poaka','kau','hooiho','heihei','raapeti']
    answersforlistaa = ['ngeru','kuri','hipi','poaka','kau','hooiho','heihei','raapeti']
    answersforlistab = ['ngeru','kuri','hipi','poaka','kau','hooiho','heihei','raapeti']
    words()
  elif abcde == "b":
    print("you have selected objects")
    print("do you want to guess A: the Māori names of english words or B: the english names of Māori words or C: both")
    words()
  elif abcde == "c":
    print("you have selected family members 17 questions")
    print("the quiz you have chosen can only be done with the Māori names of english words")
    print("*hint use double vowels instaid of macrons*")
    questionlista = ['family','parents','father','mother','child','son','daughter','brother of a female','younger brother of a male','older brother of a male','eldest brother/sister','older sister of a female','younger sister of a female','sister of a male','grandparents','grandfather','grandmother']
    questionlistb = ['whaamere','maatua','matua','maamaa','tamaiti','tama','tamaahine','tungaane','tiana','tuaakana','kauaemua','tuaakana','teina','kaikuahine','tuupuna','tupuna taane','tipuna wahine']
    answersforlistaa = ['whanau','maatua','paapara','whaea','tamaiti','tama','tamaahine','tungaane','teina','tuaakana','kauaemua','tuaakana','teina','kaikuahine','tuupuna','tupuna taane','tupuna wahine']
    answersforlistab = ['ngare','maatua','paapara','kookara','taitamaiti','tama','tamawahine','tungaane','tiena','tuaakana','maataamua','tuaakana','taina','kaikuahine','tiipuna','tipuna taane','tāua']
    quiza()
  elif abcde == "d":
    print("you have selected colours")
    print("do you want to guess A: the Māori names of english words or B: the english names of Māori words or C: both")
    words()
  elif abcde == "e":
    print("you have selected all of the above")
    print("do you want to guess A: the Māori names of english words or B: the english names of Māori words or C: both")
    words()
  elif abcde == "quit":
    quit()
  else:
    print("answer A/B/C/D/E or anwer quit to quit")
    abc()
abc()
def quiz():
  print("")