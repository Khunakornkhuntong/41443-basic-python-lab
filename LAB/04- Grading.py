
score_homework = 25       
score_midterm = 25        
score_final = 30          
total_score = score_homework + score_midterm + score_final
if 90 <= total_score <= 100:
    grade = "A"
elif 80 <= total_score <= 89:
    grade = "B+"
elif 70 <= total_score <= 79:
    grade = "B"
elif 60 <= total_score <= 69:
    grade = "C"
elif 55 <= total_score <= 59:
    grade = "D+"
elif 50 <= total_score <= 54:
    grade = "D"
else:
    grade = "F"

# แสดงผลลัพธ์
print(grade)
