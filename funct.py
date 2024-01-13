instagram=5
facebook=8.77
googleadsense=3
tiktok=9.16




def admarketingconversions(conversionrate,cost,platform):
    print(platform,'conversionrate is ',conversionrate)
    views=0
    if platform==instagram:
        views=(cost/instagram)*1000-((cost/instagram)*1000)%1
    elif platform==facebook:
        views=(cost/facebook)*1000-((cost/facebook)*1000)%1
    elif platform==googleadsense:
        views=((cost/googleadsense)*1000)-((cost/googleadsense)*1000)%1
    else:
        views=(cost/tiktok)*1000-((cost/tiktok)*1000)%1
        
    print(views)

    return (views*conversionrate/100)-(views*conversionrate/100)%1



def influencermarketingconversions(conversionrate,views):
    print('test')
    customer=views*conversionrate/1000
    return customer