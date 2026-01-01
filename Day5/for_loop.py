# fruits = ["Apple","Peach","Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# print(fruits)

student_score = [123,45,74,744,52,623,112,242,14,156,673,50,990,74]

# total_exam_score = sum(student_score)
# print(total_exam_score)

# sum = 0
# for score in student_score:
#     sum += score

# print(sum)

max_score = 0

for score in student_score:
   if score > max_score:
      max_score = score
print(max_score)
