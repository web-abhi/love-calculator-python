print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

couple = name1+name2
pair = couple.lower()
t = pair.count('t')
r = pair.count('r')
u = pair.count('u')
e = pair.count('e')
true = t+r+u+e
l = pair.count('l')
o = pair.count('o')
v = pair.count('v')
e = pair.count('e')
love = l+o+v+e
score = int(str(true)+str(love))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >=40 and score <=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
