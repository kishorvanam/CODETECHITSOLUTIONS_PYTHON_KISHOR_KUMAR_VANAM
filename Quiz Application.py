import random
questions = [["A.where is the taj mahal located"],
            ["B.where is the charminar located"],
            ["C.where is the redfort located"],
            ["C.where is the indiagate located"],
            ["D.where is the TTD located"]]
answers = [["A.Agra", "B.HYD","C.Delhi","D.AP"],
          ["A.Agra", "B.HYD","C.Delhi","D.AP"],
           ["A.Agra", "B.HYD","C.Delhi","D.AP"],
           ["A.Agra", "B.HYD","C.Delhi","D.AP"],
           ["A.Agra", "B.HYD","C.Delhi","D.AP"]]
correct_answers =["A","B","C","C","D"]



def random_questions():
    order = []
    for i in  range(len(questions)):
        order.append(i)
    
    random.shuffle(order)
    return order

score = 0
qestion_order = random_questions()
for i in qestion_order :
    print(questions[i])
    for j in answers[i]:and
        print( j)
    user_answer = input("\npls enter the correct  ans:-  ").upper()
    if user_answer == "A" or "B" or "C" or "D":
        kishor = user_answer == "A" or "B" or "C" or "D"
        
        
        if user_answer == correct_answers[i]:
            score+=1
            print("\ncorrect answer\n")
        else:
        
            print("\nwrong answer")
    else:
        print("pls enter valid options")
print(f"Result your score {score} out of {len(questions)}")
if score >=3:
    print("\n***congratulations***")
else:
    print("Better Luck Nxt Time")