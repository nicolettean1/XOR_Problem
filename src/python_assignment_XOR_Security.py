#Check Verticals
def vertical(grid):
    num_rows = len(grid)
    final_list = []
    greatest_curr_num = 0  # Greatest Current Number
    for r in range(num_rows):  # Each Row
        for c in range(num_rows-3):  # Not 20 b/c index out of range, each col element
            total_value = grid[c][r] * grid[c + 1][r] * grid[c + 2][r] * grid[c + 3][r]

            # Check to see if total is greatest than what greatest num is
            if total_value > greatest_curr_num:
                greatest_curr_num = total_value
                #greatest_nums = (grid[c][r], grid[c + 1][r], grid[c + 2][r], grid[c + 3][r])
                indices = [(c, r), (c + 1, r), (c + 2, r), (c + 3, r)]
    final_list.append(greatest_curr_num)
    final_list.append(indices)
    return final_list


#Check Horizontals
def horizontal(grid):
    num_rows = len(grid)
    greatest = 0
    final_list = []
    for index, row in enumerate(grid):
        i = 0
        while i < num_rows-3:
            total = grid[index][i] * grid[index][i + 1] * grid[index][i + 2] * grid[index][i + 3]

            # Check to see if total is greatest than what greatest num is
            if total > greatest:
                greatest = total
                #greatest_nums = (grid[index][i],grid[index][i+1],grid[index][i+2],grid[index][i+3])
                indices = [(index, i), (index, i + 1), (index, i + 2), (index, i + 3)]
            i += 1

    final_list.append(greatest)
    final_list.append(indices)
    return final_list


#Check diagonals  left to right
def diagonals(grid):
    num_rows = len(grid)
    greatest_curr_num = 0
    final_list = []
    for r in range(num_rows-3): #Row Starter
        for c in range(num_rows-3): #Column Starter
            total_value = grid[c][r]*grid[c+1][r+1]*grid[c+2][r+2]*grid[c+3][r+3] #Solution total value

            if total_value > greatest_curr_num:
                greatest_curr_num = total_value
                #greatest_nums = (grid[c][r], grid[c + 1][r + 1], grid[c + 2][r + 2], grid[c + 3][r + 3]) #List of nums used to create the greatest
                indices = [(c, r), (c + 1, r + 1), (c + 2, r + 2), (c + 3, r + 3)] #Indices

    final_list.append(greatest_curr_num)
    final_list.append(indices)
    return final_list


#Reverse Matrix
def reverse(grid):
    temp_list = []
    final_list = []
    for i in grid:
        for j in reversed(i):
            temp_list.append(j)
        final_list.append(temp_list)
        temp_list = []
    return final_list

def final(grid):
    #Concatted List of potential solutions
    revGrid = reverse(grid)
    concatted_list = []
    concatted_list.append(horizontal(grid))
    concatted_list.append(vertical(grid))
    concatted_list.append(diagonals(grid))
    concatted_list.append(diagonals(revGrid))

    #Because I reversed the matrix and just called the same diagnol function for the reversal, if that's the greatest
    #Product then the indices will have to be transformed back to the orginial matrix and not the reversed one

    new_indices = []
    largest_num = 0
    indices = []
    #Traversing through possible solutions and getting the largest four adjacent number total and indices corresponding to it
    for i in concatted_list:
        if i[0] > largest_num:
            largest_num = i[0]
            indices = i[1]

    #Here I am checking like I said above to see if the reversed matrix or right to left diagnol is the largest
    #If it is, I am going to have to transform indices back to its orginal matrix
    if largest_num == diagonals(revGrid)[0]:
        for i,j in diagonals(revGrid)[1]:
            j = 19 - j
            new_indices.append((i,j))
        #return largest_num ---> Unit Testing Purposes
        #return new_indices #---> Unit Testing Purposes

        print("The greatest product of four adjacent numbers in the same direction is:", largest_num)
        print("The indices of this number is:", new_indices)

    else:
        #return largest_num #---> Unit Testing Purposes
        #return indices #---> Unit Testing Purposes

        print("The greatest product of four adjacent numbers in the same direction is:",largest_num)
        print("The indices of this number are:", indices)



#Main function
def main():

#Enter a matrix of you choice in the grid variable below!!!
    grid = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
            [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
            [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
            [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
            [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
            [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
            [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
            [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
            [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
            [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
            [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
            [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
            [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
            [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
            [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
            [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
            [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
            [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
            [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
            [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]


    num_rows = len(grid)
    num_cols = len(grid[0])
    if (num_rows < 4 or num_rows > 50) or (num_cols < 4 or num_cols > 50):
        print("Matrix not well defined, Please have matrix be rows and columns be greater than 3 and less than 51")
        return 0
    print(final(grid))

main()

