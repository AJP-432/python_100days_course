# Give a list of heights and i'll calcaulte the average
# Asking and saving input as an array and initiating sum var
student_heights = input("Enter heights seperated by a space: ").split(" ")
sum = 0
length_of_array = 0
# Looping through array and calculing the avearge
for height in student_heights: 
    sum += float(height)
    length_of_array += 1
# Dividing sum by number of items and printing result
print(f"The average height is {round(sum/length_of_array)}")
print(f"Also, the sum and amount of students are {sum} and {length_of_array}")
