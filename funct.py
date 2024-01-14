
instagram=414.28
facebook=726.66
googleadsense=248.57
tiktok=758.97




def admarketingconversions(ctr,cost,platform,cpm):
    
    #debugging line
    print(platform,'conversionrate is ',ctr)
    
    #defining views locally
    views=0
    #converting as per platform
    
    if platform=='instagram':
        views=(cost/instagram)*1000-((cost/instagram)*1000)%1
    elif platform=='facebook':
        views=(cost/facebook)*1000-((cost/facebook)*1000)%1
    elif platform=='googleadsense':
        views=((cost/googleadsense)*1000)-((cost/googleadsense)*1000)%1
    elif platform=='tiktok':
        views=cost/tiktok*1000-((cost/googleadsense)*1000)%1
    else:
        views=(cost/cpm)*1000-((cost/cpm)*1000)%1
        
    #debugging line    
    print(views,'views')

    return (views*ctr/100)-(views*ctr/100)%1



def influencermarketingconversions(conversionrate,views):
    print('test')#debugging lines
    
    #findding number of customers via simple conversionrate mathematics
    visitors=views*conversionrate/1000
    return visitors


def servicecharges(customers,tier1,tier2,tier3):
    print('test')
    
    
def adcampaignconversions(views,conversionrate):
    visitors=views*conversionrate/100
    return visitors


def totalcustoeraquired(input):
    total=0
    divid=('div1','div2','div3','div4','div5','div6','div7','div8')
    for i in divid:
        a=input[i]
        total+=a  
        
    return total