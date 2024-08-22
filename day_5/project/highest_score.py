# this will print highest score from the list of scores
# and this will print average score from the list of scores

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest_score = 0
sum_of_scores = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

    sum_of_scores += score

print(f"The highest score in the class is: {highest_score}")
print(f"The average score in the class is: {sum_of_scores/len(student_scores)}")

# Output:
# The highest score in the class is: 91
# The average score in the class is: 77.0

