"""tutopian tree."""


num_trees = int(input("How many trees do you want to test: "))


for j in range(num_trees):
    height = 1
    num_cicles = int(input(f"How many cycles do your want to test for tree {j+1}: "))
    for i in range(num_cicles):
        if i % 2 == 0:
            height = height + 1
        else:
            height = height * 2    
    print(f"The height will be {height} for tree {j+1} after {num_cicles}")
