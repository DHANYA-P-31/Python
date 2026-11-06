student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
maximum_score = max(student_scores)
print(maximum_score)
max_score =0
for i in student_scores:
    if i > max_score:
        max_score = i
print(max_score)