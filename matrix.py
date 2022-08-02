#convert a matrix

def matrix():
    matrix1 = [[1,2], [3,4], [5,6], [7,8]]

    for row in matrix1:
        print(row)
        for i in range(2):
            print(row[i])
matrix()