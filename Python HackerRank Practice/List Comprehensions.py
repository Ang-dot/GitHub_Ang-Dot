if __name__ == '__main__':
   
    #Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n. Please use list comprehensions rather than multiple loops, as a learning exercise.
    
    (a, b, c, d) = (int(input()) for _ in range(4))
    
    print([[x, y, z] for x in range(0, a+1) for y in range(0, b+1) for z in range (0, c+1) if x + y + z != d])