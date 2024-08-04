student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}
for student in student_scores:
  student_score = student_scores[student]
  if student_score>=91 and student_score<=100:
    student_grades[student] = "Outstanding"
  elif student_score>=81 and student_score<=90:
    student_grades[student] = "Exceeds Expectations"
  elif student_score>=71 and student_score<=80:
    student_grades[student] = "Acceptable"
  elif student_score<=70:
    student_grades[student] = "Fail"

print(student_grades)