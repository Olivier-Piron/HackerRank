# You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i,j,k is not equal to n. Please use list comprehensions rather than multiple loops, as a learning exercise.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
print([[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X+Y+Z != n])