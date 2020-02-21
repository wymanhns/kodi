# coding=utf-8
import  re, urllib.request, base64
from urllib.request import unquote




def ReadData():
  readlist = [1,3]
  #讀取網頁
  '''
  url = 'http://luotuo.oss-cn-beijing.aliyuncs.com/list.txt'
  html = urllib.request.urlopen(url).read()
  html = html.decode('utf-8')     #python3版本中需要加入
  '''
  # 本地文件測試
  f = open('list.txt')
  lines = f.readlines()
  for line in lines:
    html = (line)
    f.close()
    
  html = unquote(bytes.decode(base64.b64decode(html))) #解編碼
  html = html.split('\n\n');  
  groupname=[]
  titlea=[]
  title=[]
  add1=[]
  
  # Read Groupname
  for i in html:
    group = i.split(',#genre#\n')[0]
    group = group.split(' ')[0]
    titlea.append(i.split(',#genre#\n')[1])
    groupname.append(group)
    #print (i,'>', groupname, '\n')        # 输出
    #print (titlea)
  # End

  for x in readlist: 
    
    zz = titlea[x].split('\n')
    
    ##print (zz)
    
    for y in zz:
      #qq = zz[y].split(',')
      
      # clean space & 0
      ta = y.split(',')[0]
      ta = ''.join(ta.split(' 0'))
      ta = ''.join(ta.split())
      
      if ('#' in y.split(',')[1]):
        out1 = y.split(',')[1]
        for z in out1.split('#'):
          title.append(ta)
          add1.append(z)
          #print (z)
        #print (y,'>   ',title[y], add1[y])
      else :
        title.append(ta)
        add1.append(y.split(',')[1])




      
      #print (y, title[y],'\n', add1[y])
	# Read Title name

  
  #for x in range(len(title)):
    
   # print (title[x], add1[x] )




  '''
	zz = titlea[3].split('\n')
	##print (i, '>',zz)

	for x in range(len(zz)): 
	    ##zz = zz[i].split(',')
	    title.append(zz[x].split(',')[0])
	    add1.append(zz[x].split(',')[1])
	    #print (x, '台名 >',title[x], '     地址 >', add1[x])

  '''

	# end 
  return title,add1
  
'''
str = input("请输入：")
print ("你输入的内容是: ", str)
'''
my_list = ReadData()

print(len(ReadData()[0]))
#print (ReadData()[1])
tdata="#EXTM3U\n"
for  x in range(len(my_list[0])):
  #x = 80
  tdata+=("#EXTINF:-1 tvg-logo=\"http://epg.51zmt.top:8000/tb1/gt/TVB%E7%BF%A1%E7%BF%A0%E5%8F%B0.png\" tvg-name=\"翡翠台\" group-title=\"香港电视台\",{name} \
                      \n{add}\n".format(name=my_list[0][x],add=my_list[1][x]))

#print (tdata)

fo = open("3.m3u", "w")
#wdata="#EXTM3U\n"
wdata=tdata

fo.write(wdata)
 
# 关闭打开的文件
fo.close()



#print (zz)
#print (titlea)




























