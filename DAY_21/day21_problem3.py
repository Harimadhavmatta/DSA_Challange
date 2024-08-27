def left_triangle(height):
    for i in range(height):
        pattern=' '*(height-(i+1))+('*'*(i+1))
        print(pattern)
        
left_triangle(5)