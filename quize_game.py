print("Welcome to my computer quize!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
  quit()

print("Okay! Let's play :)")
score = 0

#Q.1
answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
  print('Correct!')
  score += 1
else:
  print('Incorret')

# Q.2 
answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
  print('Correct!')
  score += 1
else:
  print('Incorret')

# Q.3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
  print('Correct!')
  score += 1
else:
  print('Incorret')

#Q.4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
  print('Correct!')
  score += 1
else:
  print('Incorret')

print("You got " + str(score) + " question correct!")

print("You got " + str((score / 4) * 100) + "%.")