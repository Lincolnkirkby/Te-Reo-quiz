#global variables 11/5/22
import random
import time
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

def quizf():
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
    if correct ==50:
      print("e kore e taea")
    l = "list"
    question = 0
    abc()
  if question ==1:
    print("question"+str(question))
  elif question == 6:
    print("Kua whakautua e koe nga patai e 5 ka ",str(correct)+"/"+str(question-1),"/",(correct/(question-1))*100,"% to tatau, tae noa ki tenei wa")
  else:
    print("pātai "+str(question))
  if l == "list":
    l = list(range(len(questionlistb)))
    
  question1 = random.choice(l)
  print("he aha te ingoa Māori o",questionlista[question1])
  answer1 = input().lower()
  
  if answer1 == answersforlistaa[question1]:
    print("congrats")
    correct += 1
    l.remove(question1)
    quizf()
  elif answer1 == questionlistb[question1]:
    print("congrats")
    correct += 1
    l.remove(question1)
    quizf()
  elif answer1 == answersforlistab[question1]:
    print("congrats")
    correct += 1
    l.remove(question1)
    quizf()
  elif answer1 == "quit":
    quit()
  elif answer1 == "return":
    question = 0
    l = "list"
    print("A animals,B objects,C family members,D colours or E all of the above")
    abc()
  else: 
    #this here is testing whether there are multiple answers to display or not
    if answersforlistab[question1] != questionlistb[question1]:
      if answersforlistab[question1] == answersforlistaa[question1]:
        print("sorry but the anwer was either",answersforlistab[question1],"or",questionlistb[question1],"or",answersforlistaa[question1])
        wrong += 1
        l.remove(question1)
        quizf()
      else:
        print("sorry but the anwer was either",answersforlistab[question1],"or",questionlistb[question1])
        wrong += 1
        l.remove(question1)
        quizf()
    elif answersforlistab[question1] != answersforlistaa[question1]:
      print("sorry but the anwer was either",answersforlistab[question1],"or",answersforlistaa[question1])
      wrong += 1
      l.remove(question1)
      quizf()
    else: 
      print("sorry but the anwer was",answersforlistab[question1])
      wrong += 1
      l.remove(question1)
      quizf()
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
    elif question == 6:
      print("you have answerd 5 questions your score is",str(correct)+"/"+str(question-1),"or",(correct/(question-1))*100,"% at any time you can type quit to quit or return to return to the start or you can continue answering the questions to see your final score")
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
      question = 0
      print("A animals,B objects,C family members,D colours or E all of the above")
      abc()
    else:
      print("sorry but the anwer was",questionlista[question1])
      wrong += 1
      l.remove(question1)
      quizb()
  else:
    print("you have answerd all of the questions your final score was",str(correct)+"/"+str(question-1),"or",(correct/(question-1))*100,"%")
    if (correct/(question-1)) == 1:
      print("congratulations on 100% you truly know your stuff")
    print("A animals,B objects,C family members,D colours or E all of the above")
    l = "list"
    question = 0
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
    if correct ==50:
      print("AMAZING WORK you got all the default quizz answers all correct YOUR A NATURAL why not try our secret hard dificulty by typing: F")
    elif (correct/(question-1)) == 1:
      print("congratulations on 100% you truly know your stuff")
    l = "list"
    question = 0
    abc()
  if question ==1:
    print("question"+str(question))
  elif question == 6:
    print("you have answerd 5 questions your score is",str(correct)+"/"+str(question-1),"or",(correct/(question-1))*100,"% at any time you can type quit to quit or return to return to the start or you can continue answering the questions to see your final score")
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
    question = 0
    l = "list"
    print("A animals,B objects,C family members,D colours or E all of the above")
    abc()
  else: 
    if answersforlistab[question1] != questionlistb[question1]:
      if answersforlistab[question1] == answersforlistaa[question1]:
        print("sorry but the anwer was either",answersforlistab[question1],"or",questionlistb[question1],"or",answersforlistaa[question1])
        wrong += 1
        l.remove(question1)
        quiza()
      else:
        print("sorry but the anwer was either",answersforlistab[question1],"or",questionlistb[question1])
        wrong += 1
        l.remove(question1)
        quiza()
    elif answersforlistab[question1] != answersforlistaa[question1]:
      print("sorry but the anwer was either",answersforlistab[question1],"or",answersforlistaa[question1])
      wrong += 1
      l.remove(question1)
      quiza()
    else: 
      print("sorry but the anwer was",answersforlistab[question1])
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
  elif names == "quit":
    quit()
  elif names == "back":
    print("A animals,B objects,C family members,D colours or E all of the above")
    abc()
  else:
    print("answer A/B you can also answer :quit: to quit or :back: to go back ")
    words()
    
#abc is def so that I can call it at any time its purpose is to personalise thier quiz questions 11/5/22
def abc():
  abcde = input().lower()
  global questionlista
  global questionlistb
  global answersforlistaa
  global answersforlistab
  if abcde == "a":
    print("you have selected animals")
    print("do you want to guess A: the Māori names of english words or B: the english names of Māori words")
    questionlista = ['cat','dog','sheep','pig','cow','horse','chicken','rabbit']
    questionlistb = ['ngeru','kuri','hipi','poaka','kau','hooiho','heihei','raapeti']
    answersforlistaa = ['ngeru','kuri','hipi','poaka','kau','hooiho','heihei','raapeti']
    answersforlistab = ['ngeru','kuri','hipi','poaka','kau','hooiho','heihei','raapeti']
    words()
  elif abcde == "b":
    print("you have selected objects")
    print("A:household objects or B: school objects?")
    ab = input().lower()
    if ab == "a":
      print("do you want to guess A: the Māori names of english words or B: the english names of Māori words")
      questionlista = ['pen','pencil','book','scissors','paper','eraser','ruler']
      questionlistb = ['pene','peneraakau','pukapuka','kutikuti','pepa','uukui','Raakauine']
      answersforlistaa = ['pene','peneraakau','pukapuka','kutikuti','pepa','uukui','Raakauine']
      answersforlistab = ['pene','pene','pukapuka','kutikuti','pepa','uukui','Raakauine']
      words()
    if ab == "b":
      print("do you want to guess A: thee Māori names of english words or B: the english names of Māori words")
      questionlista = ['book','computer','oven','door','window','cupboard','chair','table','fan']
      questionlistb = ['pukapuka','rorohiko','oumu','tatau','wini','kaapata','tuuru','papa-kai','kooheuheu']
      answersforlistaa = ['pukapuka','rorohiko','oomu','tatau','wini','kaapata','nohoanga','paparahua','koowhiuwhiu']
      answersforlistab = ['pukapuka','rorohiko','imu','whatitoka','matapihi','kaapata','tuuru','paparahua','koowhiuwhiu']
      words()
    else:
      print("answer A/B/C/D/E/F or anwser quit to quit")
      abc()
  elif abcde == "c":
    print("you have selected family members 17 questions")
    print("the quiz you have chosen can only be done with the Māori names of english words")
    print("*hint use double vowels instead of macrons*")
    questionlista = ['family','parents','father','mother','child','son','daughter','brother of a female','younger brother of a male','older brother of a male','eldest brother/sister','older sister of a female','younger sister of a female','sister of a male','grandparents','grandfather','grandmother']
    questionlistb = ['whaamere','maatua','matua','maamaa','tamaiti','tama','tamaahine','tungaane','tiana','tuaakana','kauaemua','tuaakana','teina','kaikuahine','tuupuna','tupuna taane','tipuna wahine']
    answersforlistaa = ['whanau','maatua','paapara','whaea','tamaiti','tama','tamaahine','tungaane','teina','tuaakana','kauaemua','tuaakana','teina','kaikuahine','tuupuna','tupuna taane','tupuna wahine']
    answersforlistab = ['ngare','maatua','paapaa','kookara','taitamaiti','tama','tamawahine','tungaane','tiena','tuaakana','maataamua','tuaakana','taina','kaikuahine','tiipuna','tipuna taane','taaua']
    quiza()
  elif abcde == "d":
    print("you have selected colours")
    questionlista = ['red','green','blue','yellow','white','pink','purple','black','orange']
    questionlistb = ['whero','kakariki','kikorangi','kowhai','ma','mawhero','waiporoporo','Mangu','karaka']
    answersforlistaa = ['whero','kakariki','kikorangi','kowhai','ma','mawhero','tawa','mangumangu','karaka']
    answersforlistab = ['whero','kakariki','kikorangi','kowhai','ma','mawhero','paapura','pango','karaka']
    print("do you want to guess A: the Māori names of english words or B: the english names of Māori words or C: both")
    words()
  elif abcde == "e":
    questionlista = ['cat','dog','sheep','pig','cow','horse','chicken','rabbit','pen','pencil','book','scissors','paper','eraser','ruler','book','computer','oven','door','window','cupboard','chair','table','fan','family','parents','father','mother','child','son','daughter','brother of a female','younger brother of a male','older brother of a male','eldest brother/sister','older sister of a female','younger sister of a female','sister of a male','grandparents','grandfather','grandmother','red','green','blue','yellow','white','pink','purple','black','orange']
    questionlistb = ['ngeru','kuri','hipi','poaka','kau','hooiho','heihei','raapeti','pene','peneraakau','pukapuka','kutikuti','pepa','uukui','raakauine','pukapuka','rorohiko','oumu','tatau','wini','kaapata','tuuru','papa-kai','kooheuheu','whaamere','maatua','matua','maamaa','tamaiti','tama','tamaahine','tungaane','tiana','tuaakana','kauaemua','tuaakana','teina','kaikuahine','tuupuna','tupuna taane','tipuna wahine','whero','kakariki','kikorangi','kowhai','ma','mawhero','waiporoporo','mangu','karaka']
    answersforlistaa = ['ngeru','kuri','hipi','poaka','kau','hooiho','heihei','raapeti','pene','peneraakau','pukapuka','kutikuti','pepa','uukui','raakauine','pukapuka','rorohiko','oomu','tatau','wini','kaapata','nohoanga','paparahua','koowhiuwhiu','whanau','maatua','paapara','whaea','tamaiti','tama','tamaahine','tungaane','teina','tuaakana','kauaemua','tuaakana','teina','kaikuahine','tuupuna','tupuna taane','tupuna wahine','whero','kakariki','kikorangi','kowhai','ma','mawhero','tawa','mangumangu','karaka']
    answersforlistab = ['ngeru','kuri','hipi','poaka','kau','hooiho','heihei','raapeti','pene','pene','pukapuka','kutikuti','pepa','uukui','raakauine','pukapuka','rorohiko','imu','whatitoka','matapihi','kaapata','tuuru','paparahua','koowhiuwhiu','ngare','maatua','paapaa','kookara','taitamaiti','tama','tamawahine','tungaane','tiena','tuaakana','maataamua','tuaakana','taina','kaikuahine','tiipuna','tipuna taane','taaua','whero','kakariki','kikorangi','kowhai','ma','mawhero','paapura','pango','karaka']
    print("you have selected all of the above, 50 questions")
    print("for simplicity and because family members are included in this quiz the quiz you have chosen can only be done with the Māori names of english words")
    quiza()
  elif abcde =="f":
    print("Kua whiriwhiria e koe tetahi patai tino uaua 50 nga patai e tino mohio ana koe kei te hiahia haere tonu koe")
    questionlista = ['cat','dog','sheep','pig','cow','horse','chicken','rabbit','pen','pencil','book','scissors','paper','eraser','ruler','book','computer','oven','door','window','cupboard','chair','table','fan','family','parents','father','mother','child','son','daughter','brother of a female','younger brother of a male','older brother of a male','eldest brother/sister','older sister of a female','younger sister of a female','sister of a male','grandparents','grandfather','grandmother','red','green','blue','yellow','white','pink','purple','black','orange']
    questionlistb = ['ngeru','kuri','hipi','poaka','kau','hooiho','heihei','raapeti','pene','peneraakau','pukapuka','kutikuti','pepa','uukui','raakauine','pukapuka','rorohiko','oumu','tatau','wini','kaapata','tuuru','papa-kai','kooheuheu','whaamere','maatua','matua','maamaa','tamaiti','tama','tamaahine','tungaane','tiana','tuaakana','kauaemua','tuaakana','teina','kaikuahine','tuupuna','tupuna taane','tipuna wahine','whero','kakariki','kikorangi','kowhai','ma','mawhero','waiporoporo','mangu','karaka']
    answersforlistaa = ['ngeru','kuri','hipi','poaka','kau','hooiho','heihei','raapeti','pene','peneraakau','pukapuka','kutikuti','pepa','uukui','raakauine','pukapuka','rorohiko','oomu','tatau','wini','kaapata','nohoanga','paparahua','koowhiuwhiu','whanau','maatua','paapara','whaea','tamaiti','tama','tamaahine','tungaane','teina','tuaakana','kauaemua','tuaakana','teina','kaikuahine','tuupuna','tupuna taane','tupuna wahine','whero','kakariki','kikorangi','kowhai','ma','mawhero','tawa','mangumangu','karaka']
    answersforlistab = ['ngeru','kuri','hipi','poaka','kau','hooiho','heihei','raapeti','pene','pene','pukapuka','kutikuti','pepa','uukui','raakauine','pukapuka','rorohiko','imu','whatitoka','matapihi','kaapata','tuuru','paparahua','koowhiuwhiu','ngare','maatua','paapaa','kookara','taitamaiti','tama','tamawahine','tungaane','tiena','tuaakana','maataamua','tuaakana','taina','kaikuahine','tiipuna','tipuna taane','taaua','whero','kakariki','kikorangi','kowhai','ma','mawhero','paapura','pango','karaka']
    quizf()
  elif abcde == "quit":
    quit()
  else: 
    print("answer A/B/C/D/E/F or answer quit to quit")
    abc()
abc()