# Setting up the map
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
# Showing user map 
print(f"{row1}\n{row2}\n{row3}")
# Asking for treasure location and saving input to variable 
position = input("Where do you want to put the treasure (column:row)? ")
# Setting desired site to treasure spot and printing resultant map
map[int(position[1])-1][int(position[0])-1] = "❌"
print(f"{row1}\n{row2}\n{row3}")

    