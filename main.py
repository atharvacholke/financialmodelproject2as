import funct as fn
import numpy as np

budget=0

customer=fn.admarketingconversions(1,200,'instagram',200)
print(customer,'last step')

#a=fn.influencermarketingconversions(6,2000)
#print(a)

potentialclients=18000000



class campaign:
    
    def __init__(self,budget,divno):
        self.budget=budget
        self.div=divno
        i=0
        adplat=('instagram','facebook','tiktok','googleadsense','gen1','gen2','gen3','gen4')
        divid=('div1','div2','div3','div4','div5','div6','div7','div8')
        divisions={'div1':0,'div2':0,'div3':0,'div4':0,'div5':0,'div6':0,'div7':0,'div8':0}
        while i<divno:
            div=budget/divno
            asc=fn.admarketingconversions(0.5,div,adplat[i],800)
            divisions.update({divid[i]:asc})
            print(adplat[i],divisions[divid[i]])
            i+=1
        print("testover")
        self.mp=divisions
        print(divisions)
        
    
    def __str__(self):
        pass


test=campaign(100000,8)

print(test)     
        