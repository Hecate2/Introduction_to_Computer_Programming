import requests,re,AdvancedHTMLParser

s=requests.Session()

r=s.get("https://m.medsci.cn/wh.asp",headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'})

#现存确诊等
data=re.findall('''">(.*)</strong>''',r.text)
print(data)

#表格
parser=AdvancedHTMLParser.AdvancedHTMLParser()
parser.parseStr(r.text)

data=parser.getElementsByTagName("tr")
print(data[0].innerHTML)

data=parser.getElementsByTagName("td")
print(data[0].innerHTML,data[1].innerHTML,data[2].innerHTML,data[6].innerHTML)
