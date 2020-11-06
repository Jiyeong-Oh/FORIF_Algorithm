#!/usr/bin/env python
# coding: utf-8

# 프로그래머스 level1
# https://programmers.co.kr/learn/courses/30/lessons/64061

# In[11]:


import numpy as np

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]


def solution(board, moves):
    board = np.array(board)
    moves = np.array(moves)
    
    empty=[]

    for i in range (len(moves)):
        turn=moves[i]
        column=board[:,turn-1]
    
        for j in range (len(column)):
            if column[j]!=0:
                empty.append(column[j])
                board[j,turn-1]=0
                break

    def pang(lists):
        for i in range(len(lists)-1):
            if lists[i]==lists[i+1]:
                lists.pop(i)
                lists.pop(i)
                break
        return lists

    n = len(empty)

    box=empty.copy()
    while True:
        pang(empty)
        if len(box)==len(empty):
            break
        pang(box)
    return (n-len(empty))


solution(board, moves)


# 프로그래머스 level 2 https://programmers.co.kr/learn/courses/30/lessons/42586

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




