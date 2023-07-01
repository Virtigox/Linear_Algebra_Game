import random
#one step problem
def one_step_problem():
  ran_ops = ['+','-','/','*']
  random_Unknown1 = random.randint(1,100)
  random_Unknown2 = random.randint(1,100)
  random_ops_choice = random.choice(ran_ops)
  print(f"x {random_ops_choice} {random_Unknown1} = {random_Unknown2}")
  if random_ops_choice == '+':
    answer = random_Unknown2 - random_Unknown1
  elif random_ops_choice == '-':
    answer = random_Unknown2 + random_Unknown1
  elif random_ops_choice == '*':
    answer = round(float(random_Unknown2 / random_Unknown1),2)
  else:
    answer = float(random_Unknown2 * random_Unknown1)
  user_ans = float(input("Enter your answer: "))
  if user_ans == float(answer):
    print("You are right!")
  else:
    print(f"Wrong!, x = {answer}")

#two step problem
def two_step_problem():
  ran_ops1 = ['/','*']
  ran_ops2 = ['+', '-']
  random_Unknown1 = random.randint(1,100)
  random_Unknown2 = random.randint(1,100)
  random_Unknown3 = random.randint(1,100)
  random_ops_choice1 = random.choice(ran_ops1)
  random_ops_choice2 = random.choice(ran_ops2)
  print(f" ({random_Unknown1} {random_ops_choice1} x) {random_ops_choice2} {random_Unknown2} = {random_Unknown3}")
  if random_ops_choice2 == '+':
    if random_ops_choice1 == '*':
      answer = round(float((random_Unknown3 - random_Unknown2)/random_Unknown1),2)
    else:
      answer = (random_Unknown3 - random_Unknown2)*random_Unknown1
  else:
    if random_ops_choice1 == '*':
      answer = round(float((random_Unknown3 + random_Unknown2)/random_Unknown1),2)
    else:
      answer = (random_Unknown3 + random_Unknown2)*random_Unknown1
  user_ans = float(input("Enter your answer: "))
  if user_ans == float(answer):
    print("You are right!")
  else:
    print(f"Wrong!, x = {answer}")

one_step_problem()
two_step_problem()
