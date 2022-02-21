# This takes a list of numbers and gives the largest value
# Taking input and splitting into an arry and setting highest score var
student_scores = input("Enter scores seperated by a space: ").split(" ")
highest_score = 0
# Looping through array and if a higher score is found, var changes to that
for score in student_scores: 
    if int(score) > highest_score:
        highest_score = int(score)
# Printing anwser
print(f"The highest score is {highest_score}")
    
