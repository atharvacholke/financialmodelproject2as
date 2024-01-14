import funct as fn
import numpy as np
import matplotlib.pyplot as plt

budget=0

customer=fn.admarketingconversions(1,200,'instagram',200)
print(customer,'last step')

a=fn.influencermarketingconversions(6,2000)
print(a)

#total available customers
potentialclients=18000000



class adscampaign:
    
    def __init__(self,budget,divno):
        #defining the budget
        self.budget=budget
        #defining the number of divisions
        self.div=divno
        i=0
        
        #this All advertiser with 4 generic
        
        adplat=('instagram','facebook','tiktok','googleadsense','gen1','gen2','gen3','gen4')
        
        #This is divid for division used to store customer numbers
        
        divid=('div1','div2','div3','div4','div5','div6','div7','div8')
        
        #this is total number of customers saved as a dictionary
        
        divisions={'div1':0,'div2':0,'div3':0,'div4':0,'div5':0,'div6':0,'div7':0,'div8':0}
        
        
        while i<divno:
            div=budget/divno
            asc=fn.admarketingconversions(0.5,div,adplat[i],800)
            cust=fn.adcampaignconversions(asc,5)
            divisions.update({divid[i]:cust})
            print(adplat[i],divisions[divid[i]])
            i+=1
            
    
        #test lines
        print("testover")
        self.mp=divisions
        print('mantest',divisions)
        self.customeraquired=divisions
        
   


test=adscampaign(1000,4)

print(test)
print(test.customeraquired)     

day1=adscampaign(1000,4)
day2=adscampaign(2000,4)
day3=adscampaign(3000,4)
day4=adscampaign(4000,4)
day5=adscampaign(5000,4)
day6=adscampaign(6000,4)
day7=adscampaign(7000,4)

day1customer=day1.customeraquired
day2customer=day2.customeraquired
day3customer=day3.customeraquired
day4customer=day4.customeraquired
day5customer=day5.customeraquired
day6customer=day6.customeraquired
day7customer=day7.customeraquired

totalday1=fn.totalcustoeraquired(day1customer)
totalday2=fn.totalcustoeraquired(day2customer)+totalday1
totalday3=fn.totalcustoeraquired(day3customer)+totalday2
totalday4=fn.totalcustoeraquired(day4customer)+totalday3
totalday5=fn.totalcustoeraquired(day5customer)+totalday4
totalday6=fn.totalcustoeraquired(day6customer)+totalday5
totalday7=fn.totalcustoeraquired(day7customer)+totalday6


print(totalday1,'customers')

y= np.array([totalday1,totalday2,totalday3,totalday4,totalday5,totalday6,totalday7])
x=np.array([1,2,3,4,5,6,7])

plt.plot(x,y)
plt.show()