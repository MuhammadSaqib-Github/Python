num = eval(input("enter a number"))
h_score=num
num = eval(input("enter a number"))
s_h_score = num
if h_score > s_h_score:
    h_score = h_score
    s_h_score = s_h_score
else:
    h_score ,  s_h_score = s_h_score , h_score

for i in range(2,5):
    num = eval(input("enter a number"))
    if h_score < num:
        if h_score != s_h_score:
            s_h_score = h_score
        h_score = num
    elif s_h_score<num:
        s_h_score = num
    else:
        h_score = h_score
        s_h_score = s_h_score
print("highes and sec highest score is " , h_score , s_h_score)