from snake import *
#print(s1.score)
with open('F:/Python/Snake_score.txt','r') as o1:
    l1=o1.readlines()
high_score=int(l1[0].split(" ")[-2])
#print(f"high score is {high_score}")
score=int(l1[1].split(" ")[-2])

with open('F:/Python/Snake_score.txt','w') as w1:
  if s1.score > high_score:
      L = [f"Score is {s1.score} \n", f"High Score is {s1.score} \n"]
      w1.writelines(L)
  else:
      L = [f"Score is {s1.score} \n", f"High Score is {high_score} \n"]
      w1.writelines(L)

