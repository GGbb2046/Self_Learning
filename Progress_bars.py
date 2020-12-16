
# importing modules 
import time 
import sys 
from tqdm import trange 
  
# random function 
def random_task(): 
    time.sleep(0.5)     
  
# another random function 
def another_random_task(): 
    time.sleep(0.2) 
  
# Outer loop 
for i in trange(3, file=sys.stdout, desc='Outer loop'): 
    random_task() 
      
    # inner loop 
    for j in trange(5,file=sys.stdout, desc='Inner loop'): 
        another_random_task() 