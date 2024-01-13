import funct as fn
import numpy as np



customer=fn.admarketingconversions(1,2,'tiktok')
print(customer)

a=fn.influencermarketingconversions(6,2000)
print(a)



class campaign:
    budget=100000
    
    def __init__(self,budget,div):
        self.budget=budget
        self.div=div
        
        
        

