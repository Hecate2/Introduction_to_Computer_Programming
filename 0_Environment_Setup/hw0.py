#coding:utf-8
#井号开头的文字是给你看的，一般不影响程序本身，
#除了开头指定编码的这类特殊注释会有所影响

aa=68.1
print('aa')
print("aa")
print('''aa''')
print("""aaa""")
print("""aaa""",'aaa')

print("-------------我是华丽丽的分割线0-------------")

print(aa)
print('aa'+"""aa""")
print(aa+aa)

print("-------------我是华丽丽的分割线1-------------")
print("")
print("-------------我是华丽丽的分割线2-------------")

print('a','a')
print("\n",'a')
print("a\n")
print(r"\n")
print("\n")

print("-------------我是华丽丽的分割线3-------------")

print("%s"%(aa),"%d"%(aa))  #1 1
print('{0} love {1}{2}'.format('I','ice','cream'))  #I love ice cream
aa='{0} love {1}{2}'.format(aa,'ice','cream')
print(aa)  #I love ice cream
aa='{0} love {1}{2}'.format(aa,'ice','cream')
print(aa)

print("-------------我是华丽丽的分割线4-------------")

'''
这些文字是给你看的，
会被电脑忽略，
不影响程序执行
'''
##这些文字是给你看的，
##会被电脑忽略，
##不影响程序执行

#在IDLE中选中"##"开头的文字，试着按Alt+3和Alt+4
