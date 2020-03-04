# coding=utf-8
import  re, urllib.request, base64
from urllib.request import unquote

def foo(var):
  return {
   'CCTV1': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV1.png" tvg-name="CCTV1" group-title="CCTV",CCTV-1综合',
   'CCTV2': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV2.png" tvg-name="CCTV2" group-title="CCTV",CCTV-2财经',
   'CCTV3': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV3.png" tvg-name="CCTV3" group-title="CCTV",CCTV-3综艺',
   'CCTV4': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV4.png" tvg-name="CCTV4" group-title="CCTV",CCTV-4中文国际',
   'CCTV5': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV5.png" tvg-name="CCTV5" group-title="CCTV",CCTV-5体育',
   'CCTV5+': '',
   'CCTV6': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV6.png" tvg-name="CCTV6" group-title="CCTV",CCTV-6电影',
   'CCTV7': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV7.png" tvg-name="CCTV7" group-title="CCTV",CCTV-7国防军事',
   'CCTV8': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV8.png" tvg-name="CCTV8" group-title="CCTV",CCTV-8电视剧',
   'CCTV9': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV9.png" tvg-name="CCTV9" group-title="CCTV",CCTV-9纪录',
   'CCTV10': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV10.png" tvg-name="CCTV10" group-title="CCTV",CCTV-10科教',
   'CCTV11': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV11.png" tvg-name="CCTV11" group-title="CCTV",CCTV-11戏曲',
   'CCTV12': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV12.png" tvg-name="CCTV12" group-title="CCTV",CCTV-12社会与法',
   'CCTV13': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV13.png" tvg-name="CCTV13" group-title="CCTV",CCTV-13新闻',
   'CCTV14': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV14.png" tvg-name="CCTV14" group-title="CCTV",CCTV-14少儿',
   'CCTV15': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV15.png" tvg-name="CCTV15" group-title="CCTV",CCTV-15音乐',
   'CCTV17': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV17.png" tvg-name="CCTV17" group-title="CCTV",CCTV-17农村农业',
   'CCTV体育赛事': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV5+.png" tvg-name="CCTV5+" group-title="CCTV",CCTV-5+体育赛事',
   'CETV教育一台': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/qt/%E4%B8%AD%E5%9B%BD%E6%95%99%E8%82%B21%E5%8F%B0.png" tvg-name="中国教育1台" group-title="CCTV",教育1台',
   'CETV教育四台': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/qt/%E4%B8%AD%E5%9B%BD%E6%95%99%E8%82%B24%E5%8F%B0.png" tvg-name="中国教育4台" group-title="CCTV",教育4台',
   'CGTN国际频道': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/cgtn.png" tvg-name="CGTN" group-title="CCTV",CGTN国际频道',
   'CGTN记录频道': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CGTNDoc.png" tvg-name="CGTNDocumentary" group-title="CCTV",CGTN记录频道',
   'CGTN法语频道': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/cgtn.png" tvg-name="CGTN法语频道" group-title="CCTV",CGTN法语频道',
   '凤凰中文': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/fenghuangzhongwen.png" tvg-name="凤凰中文" group-title="香港电视台",凤凰卫视中文',
   '凤凰咨询': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/fenghuangzixun.png" tvg-name="凤凰资讯" group-title="香港电视台",凤凰资讯',
   '凤凰香港': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/fenghuangxianggang.png" tvg-name="凤凰香港" group-title="香港电视台",凤凰香港高清 ',
   '香港卫视': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/hks.png" tvg-name="HKS" group-title="香港电视台",香港卫视',
   '有线新闻': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/youxianxinwen.png" tvg-name="有线新闻台" group-title="香港电视台",有线新闻台',
   '无线翡翠': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/TVB%E7%BF%A1%E7%BF%A0%E5%8F%B0.png" tvg-name="翡翠台" group-title="香港电视台",無线翡翠台',
   '无线明珠': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/TVB%E6%98%8E%E7%8F%A0%E5%8F%B0.png" tvg-name="明珠台" group-title="香港电视台",明珠台',
   '无线新闻': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/wxxw.png" tvg-name="无线新闻" group-title="香港电视台",無线新闻台',
   '无线财经': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/tvbfinanceinformationchannel.png" tvg-name="无线财经" group-title="香港电视台",无线财经资讯台',
   '无线J2台': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/TVBJ2.png" tvg-name="J2" group-title="香港电视台",无线J2',
   '星河频道': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/TVB%E6%98%9F%E6%B2%B3.png" tvg-name="TVB星河频道" group-title="香港电视台",TVB星河频道',
   '有线娱乐': '#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS6Skdax1wlmiOnSvCkudVBwmC4YgU04n0cv0MWnMhtkvUxEKuW" tvg-name="有线娛樂台" group-title="香港电视台",有线娛樂台',
   '有线财经': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/youxiancaijingzixun.png" tvg-name="有线财经资讯台" group-title="香港电视台",有线财经资讯台',
   '': '',
   
  }.get(var,'#EXTINF:-1 ')  #'error'為預設返回值，可自設定


def ReadData():
  readlist = [1,3]
  #讀取網頁
  
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
    '''
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
rdata=""
for  x in range(len(my_list[0])):
  
  #x = 80
  #tdata+=("#EXTINF:-1 tvg-logo=\"http://epg.51zmt.top:8000/tb1/gt/TVB%E7%BF%A1%E7%BF%A0%E5%8F%B0.png\" tvg-name=\"翡翠台\" group-title=\"香港电视台\",{name} \
  #                    \n{add}\n".format(name=my_list[0][x],add=my_list[1][x]))
  tdata+=(foo(my_list[0][x]))
  tdata+=("- {name}\n{add}\n".format(name=my_list[0][x],add=my_list[1][x]))
  rdata+=("{name}${add}\n".format(name=my_list[0][x],add=my_list[1][x]))
  #print (foo('{name}'))
#print (tdata)

fo = open("3.m3u", "w")
#wdata="#EXTM3U\n"
wdata=tdata
fo.write(wdata)
 # 关闭打开的文件
fo.close()

fo = open("1.db", "w")
#wdata="#EXTM3U\n"
wdata=rdata
fo.write(wdata)

# 关闭打开的文件
fo.close()


#print (zz)
#print (titlea)

