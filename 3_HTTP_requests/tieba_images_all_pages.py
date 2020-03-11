#coding:utf-8

import requests
import re,time

inp='https://tieba.baidu.com/p/5539155708'  #要填https://

def save_tieba_images(html,s=requests.Session()):
    #https://imgsa.baidu.com/forum/w%3D580/sign=0b4be530c8fdfc03e578e3b0e43d87a9/e5424ed2d539b600f9441c79e250352ac45cb780.jpg
    image_names=re.findall('''src="https://imgsa.baidu.com/forum/w%3D580/sign=.*/(.*).jpg"''',html)
    images=[('''http://imgsrc.baidu.com/forum/pic/item/{}.jpg'''.format(name),name+".jpg") for name in image_names]
    print(images)
    for image in images:
        r=s.get(image[0])
        with open(image[1],"wb") as f:
            f.write(r.content)


start_time=time.time()

s=requests.Session()
r=s.get(inp)

'''
document.getElementsByClassName("l_pager pager_theme_4 pb_list_pager")[0]
.lastElementChild.href
'''
pages=re.findall('''href="/p/.*?pn=(.*)"''',r.text)
pages=int(pages[-1])  #['2', '3', '4', '5', '2', '5', '2', '3', '4', '5', '2', '5']

save_tieba_images(r.text,s)
for pagenum in (range(2,pages+1)):
    save_tieba_images(s.get(inp+"?pn="+str(pagenum)).text,s)

end_time=time.time()
print("Time elapsed: %f seconds."%(end_time-start_time))

