# -*- coding:utf-8 -*
import requests

# def test():
#     url = "https://api.douban.com/v2/movie/search?q=%E5%BC%A0%E8%89%BA%E8%B0%8B"  #测试的接口url
#     headers = {'content-type': 'application/json'}
#     r = requests.get(url=url, headers=headers)
#     return r.json()
#
# if __name__ == "__main__":
#     test()
url='https://api.douban.com/v2/movie/search?'
params=dict(q='刘德华',count=10)
r=requests.get(url,params)
print(r.status_code)
print(r.url)
titles=[]
resultnum=int(r.json()['count'])
print(resultnum)
totals=int(r.json()['total'])
print(r.json()['total'])
page=int(totals/resultnum)
single=int(totals%resultnum)
print(page)
print(single)

for i in range(0,page+1):
    start=i*resultnum
    params=dict(q='刘德华',count=10,start=start)
    print(start)
    r=requests.get(url,params)
    for j in range(0,resultnum):
        title=r.json()['subjects'][j]['title']
        titles.append(title)
        print(i)
        print(j)
print(titles)



