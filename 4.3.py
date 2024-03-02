import re
#%%
def countdown(n):
    print('start from: ',n)
    while n > 0:
        yield n
        n -=1
    print('thats all')    

