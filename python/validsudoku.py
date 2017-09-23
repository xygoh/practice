# tfw ur a n00b ._.
'''
checks if sudoku is valid. ie. no common numbers in rows,cols and 3x3 boxes
'''

def check(thing,e,hm):
    if thing in hm:
        temp=hm[thing]
        if e in temp:
            return False
        else:
            temp.append(e)
    else:
        hm[thing]=[e]
    
    return True

def sudoku2(grid):
    hm={}
    for i in range(9):
        for j in range(9):
            if grid[i][j]!='.':
                r_str='row '+str(i)
                c_str='col '+str(j)
                bi=0
                bj=0
                if i>=6:
                    bi=6
                elif i>=3:
                    bi=3
                
                if j>=6:
                    bj=2
                elif j>=3:
                    bj=1

                b_str='box '+str(bi+bj)
                if (check(r_str,grid[i][j],hm) and check(c_str,grid[i][j],hm) and check(b_str,grid[i][j],hm)) is False:
                    return False    
                
    return True
