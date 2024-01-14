
instagram=414.28
facebook=726.66
googleadsense=248.57
tiktok=758.97




def admarketingconversions(conversionrate,cost,platform,cpm):
    print(platform,'conversionrate is ',conversionrate)
    views=0
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
        
    print(views,'views')

    return (views*conversionrate/100)-(views*conversionrate/100)%1



def influencermarketingconversions(conversionrate,views):
    print('test')
    customer=views*conversionrate/1000
    return customer