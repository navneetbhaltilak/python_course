from functools import lru_cache
import time
@lru_cache(maxsize=32)
def fx(n):
    time.sleep(5)
    return n*5
print("Done for 20 : ",fx(20))
print("Done for 2 : ",fx(2))
print("Done for 20 : ",fx(20))   #it uses the stored value result from chache and does not take 5 sec for execution
print("Done for 2 : ",fx(2))
print("Done for 21 : ",fx(21))