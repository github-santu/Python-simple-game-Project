print("welcome to quiz")
playing=input("Do you want to Play :")
if playing.lower()!="yes":
    quit()
print("okay..! Lets  Play...")
score=0;


answer=input("1) who developed python")
if answer.lower()=="guido van russum":
    print("correct")
    score=score+1
else:
    print("incorect")
    
    
answer=input("2) what is the correct extension of python file? ")
if answer.lower()==".py":
    print("The 2ns answer  is right")
    score=score+1
else:
    print("Incorrect Answer")

answer=input("3) What do we use to define a block a block of code in python? ")
if answer.lower()=="indentation":
    print("The 3rd answer is correct")
    score=score+1
else:
    print("Incorrect")
    
answer=input("4) What are collection of Object? ")
if answer.lower()=="classes":
    print("The 4th answer is correct")
    score=score+1
else:
    print("Incorrect")
    
answer=input("5) What are methodes inside the class in python? ")
if answer.lower()=="function":
    print("The fifth answer is correct")
    score=score+1
else:
    print("Incorrect")
    
    
answer=input("6) What is syntax errors also callwd as? ")
if answer.lower()=="parssing errors":
    print("The sixth answer is correct")
    score=score+1
else:
    print("Incorrect")
    
    
answer=input("7) What is sequence of charecter that form a search Patterns? ")
if answer.lower()=="reguler expression":
    print("The 7th answern is correct")
    score=score+1
else:
    print("Incorrect")
    
answer=input("8) What are entity of class? ")
if answer.lower()=="objects":
    print("The  answer is correct")
    score=score+1
else:
    print("Incorrect")
    
answer=input("9) What are the functions called which calls itself reatedly? ")
if answer.lower()=="recursive function":
    print("The 9th answern is correct")
    score=score+1
else:
    print("Incorrect")
    
answer=input("10)  what are specified after function name,inside parenthisis? ")
if answer.lower()=="arguments":
    print("The 10th answern is correct")
    score=score+1
else:
    print("Incorrect")
    
    
print("you got " +str(score)+ " questions correct")
print("you have  got :"+str((score/10)*100)+"%")

print("THANK YOU FOR PLAYING")