#Let's learn about list comprehensions! You are given three integers X, Y and Z representing the dimensions 
# of a cuboid along with an integer N. You have to print a list of all possible coordinates given by (i,j,k) 
# on a 3D grid where the sum of i+j+k is not equal to N. Here, 0<=i<=X; 0<=j<=Y; 0<=k<=Z
# Please use list comprehensions rather than multiple loops, as a learning exercise.

# Input Format
# Four integers X, Y, Z and N each on four separate lines, respectively.

# Constraints
# Print the list in lexicographic increasing order.

# Sample Input 0
# 1
# 1
# 1
# 2

# Sample Output 0
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]

# Explanation 0

#Each variable x,y,z will have values of 0 or 1. All permutations of lists in the form [i,j,k] are printed.
#[i,j,k] = [[0,0,0], [0,0,1], [0,1,0],[0,1,1] ,[1,0,0],[1,0,1],[1,1,0],[1,1,1]]




if __name__ == '__main__':
   
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    output = []
    abc = []
    for X in range(x+1):
        for Y in range(y+1):
            for Z in range(z+1):
                if X+Y+Z != n:
                    abc = [X,Y,Z]
                    output.append(abc)
print(output)
     