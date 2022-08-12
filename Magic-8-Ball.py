# The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.
# Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.

# Code:

import random
random_number = random.randint(1, 9)
name = 'User'
question = "Can you read my future?"
answer = ''
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"

if question == '':
  print("You did not ask a question")
else:
  if name == '':
    print('asks:', question)
    print("Magic 8-Ball's answer:",
  answer)
  else:
    print(name, 'asks:', question)
    print("Magic 8-Ball's answer:",
  answer)
