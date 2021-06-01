import random
print("Welcome to ludo Game 2021")
start = 1
stop = 6
score1= 0

player1 = input("Enter your name")
player2 = input("Enter your name")
value= 0


i=6
j=7
b1= input("Do you want to start the game(Y/N)")
k=1 
value2 =0
if b1=="Y":
  while k>0 :
    i=6
    j=7
    n1=0
    n=0
    if b1=="Y":
      while i>0 :
        print(player1 +",It's your turn")
        a= input("Roll(R)/Skip(S) ?")
        if a=="R" :
          def play1():
            value= random.randint(1, 6)
            return value
          score =play1()
          print(str(score)+" (Dice Score)") #Strings can only be concatinated
          value= value +score
          if score==6 :
            i=i+1
            n1=n1+1
          else:
            i=0
          if n1==2:
            value= 0
            print(str(value)+" ("+player1+"'s Score)" )
            break
          print(str(value)+" ("+player1+"'s Score)")
          if value>=100:
            print(player1+" won the game")
            break
        else:
          break
      if value>=100 or value2>=100:
        break
    else:
      break
    while j>0 :
        print(player2 +",It's your turn")
        a= input("Roll(R)/Skip(S) ?")
        if a=="R" :
          def play2():
            value2= random.randint(1, 6)
            return value2
          score2 =play2()
          print(str(score2)+" (Dice Score)")
          if score2==6 :
              n=n+1
              j=1 
          else:
            j=0
          value2= value2 +score2
          if n==2:
            value2=0
            print(str(value2)+" ("+player2+"'s Score)")
            break
          print(str(value2)+" ("+player2+"'s Score)")
          if value2>=100:
              print(player2 +" won the game")
              break
    if value>=100 or value2>=100:
      break
else:
  print("Thanks for visiting")


    
        


