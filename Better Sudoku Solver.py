## This function loops through the puzzle and inserts a valid number 
## from 1 to 9. If there appears to be a violation, backtracking occurs.
def loop_through(grid_list, num, row, col, row_count, col_count):
    
    ## This function returns True when the same number appears twice in
    ## a box, and False otherwise.
    def check_num_box():
        if col in range(0,3):
            col_used = 0
        elif col in range(3,6):
            col_used = 3
        else:
            col_used = 6
        if row in range(0,3):
            for row_used in range(0,3):
                if num in grid_list[row_used][col_used:col_used+3]:
                    return True        
        elif row in range(3,6):
            for row_used in range(3,6):
                if num in grid_list[row_used][col_used:col_used+3]:
                    return True           
        else:
            for row_used in range(6,9):
                if num in grid_list[row_used][col_used:col_used+3]:
                    return True  
        return False          
    
    ## This function returns True when the same number appears twice in
    ## a row, and False otherwise.
    def check_num_row():
        if num in grid_list[row]:
            return True
        else:
            return False
    
    ## This function returns True when the same number appears twice in
    ## a column, and False otherwise.
    def check_num_col():
        for row in range(9):
            if grid_list[row][col] == num:
                return True
        return False
        
    ## This function returns True when it encounters an empty square.    
    def check_empty():
        return grid_list[row][col] == 0
      
    
    if row == 9 and col == 0:
        print(grid_list)
    elif check_empty():
        row_count.append(row)
        col_count.append(col)
        while (check_num_box() or 
               check_num_row() or 
               check_num_col()):
            num += 1
        if num < 10:
            grid_list[row][col] = num
            if col < 8:
                loop_through(grid_list, 1, row, col+1, 
                             row_count, col_count)
                
            else:
                loop_through(grid_list, 1, row+1, 0, 
                             row_count, col_count)
        else:
            row_count.pop(-1)
            col_count.pop(-1)
            prev_row = row_count[-1]
            prev_col = col_count[-1]
            loop_through(grid_list,grid_list[prev_row][prev_col] + 1,
                         prev_row, prev_col, row_count, col_count)
    
    elif row_count != []:
        if row_count[-1] == row and col_count[-1] == col:
            while (check_num_box() or 
                   check_num_row() or 
                   check_num_col()):
                num += 1
            if num < 10:
                grid_list[row][col] = num
                if col < 8:
                    loop_through(grid_list,1, row, col+1, 
                                 row_count, col_count)
                else:
                    loop_through(grid_list,1, row+1, 0,
                                 row_count, col_count)
            else:
                grid_list[row][col] = 0
                row_count.pop(-1)
                col_count.pop(-1)
                prev_row = row_count[-1]
                prev_col = col_count[-1]         
                loop_through(grid_list,grid_list[prev_row][prev_col]+1,
                             prev_row, prev_col, row_count, col_count)
        else:
            if col < 8:
                loop_through(grid_list, 1, row, col+1, row_count, 
                             col_count)
            else:
                loop_through(grid_list, 1, row+1, 0, row_count, 
                             col_count)
    else:
        loop_through(grid_list, 1, row, col+1, row_count, col_count)
            
                
def sudoku_solver(grid_list):
    loop_through(grid_list, 1, 0, 0, [], [])