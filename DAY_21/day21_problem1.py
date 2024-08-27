def inverted_full_hollow_triangle(rows):
    for i in range(rows):
        if i==0 or i==rows-1:
            print(" " * (i + 1) + ("*" * ((rows - i) * 2 - 1)))
        else:
            print(" " * (i + 1) + ("*" +" "* ((rows - i) * 2 - 3)+"*"))
        

inverted_full_hollow_triangle(6)
