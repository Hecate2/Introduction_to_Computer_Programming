#coding:utf-8

import requests

import re

s=requests.Session()
r=s.get('https://tieba.baidu.com/p/6483064313')  #要填https://
image_names=re.findall('''src="http://tiebapic.baidu.com/forum/w%3D580/sign=.*/(.*).jpg"''',r.text)
#print(image_names)

images=[('''http://tiebapic.baidu.com/forum/pic/item/{}.jpg'''.format(name),name+".jpg") for name in image_names]
print(images)

for image in images:
    r=s.get(image[0])
    with open(image[1],"wb") as f:
        f.write(r.content)
