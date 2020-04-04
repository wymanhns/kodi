# coding=utf-8
import  re, urllib.request, base64
from urllib.request import unquote

def foo(var):                 # 大視界資源加入標題
  #print (var)
  return {
   'CCTV1': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV1.png" tvg-name="CCTV1" group-title="CCTV",CCTV-1综合',
   'CCTV2': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV2.png" tvg-name="CCTV2" group-title="CCTV",CCTV-2财经',
   'CCTV3': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV3.png" tvg-name="CCTV3" group-title="CCTV",CCTV-3综艺',
   'CCTV4': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV4.png" tvg-name="CCTV4" group-title="CCTV",CCTV-4中文国际',
   'CCTV5': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV5.png" tvg-name="CCTV5" group-title="CCTV",CCTV-5体育',
   'CCTV5+': '#EXTINF:-1 tvg-logo="" tvg-name="CCTV5+" group-title="CCTV",CCTV-5体育+',
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
   'CCTV怀旧剧场': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/qt/CCTVPAYFEE7.jpg" tvg-name="怀旧剧场" group-title="CCTV",中数怀旧剧场',
   'CCTV风云剧场': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/qt/CCTVPAYFEE7.jpg" tvg-name="风云剧场" group-title="CCTV",中数风云剧场',
   'CCTV风云音乐': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTVfengyunyinyue.png" tvg-name="风云音乐" group-title="CCTV",中数风云音乐',
   'CCTV高夫网球': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/qt/CCTVPAYFEE13.jpg" tvg-name="高尔夫网球" group-title="CCTV",中数高尔夫网球',
   'CCTV兵器科技': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/qt/CCTVPAYFEE8.jpg" tvg-name="兵器科技" group-title="CCTV",中数兵器科技',
   'CCTV发现之旅': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTVfaxianzhilv.png" tvg-name="发现之旅" group-title="CCTV",中数发现之旅',
   'CCTV世界地理': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTVshijiedili.png" tvg-name="世界地理" group-title="CCTV",中数世界地理',
   'CCTV4K超高清': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/CCTV/CCTV4k.png" tvg-name="CCTV4K" group-title="CCTV",CCTV4K',
   'CHC家庭影院': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/qt/CHC1.jpg" tvg-name="CHC高清电影" group-title="CCTV",CHC高清电影',
   '凤凰资讯': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/fenghuangzixun.png" tvg-name="凤凰资讯" group-title="香港电视台",凤凰卫视资讯台',
   '澳亚卫视': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/%E6%BE%B3%E4%BA%9A%E5%8D%AB%E8%A7%86.png" tvg-name="澳亚卫视" group-title="CCTV",澳亚卫视',
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
   'TVBJ2': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/TVBJ2.png" tvg-name="J2" group-title="香港电视台",无线J2',
   '星河频道': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/TVB%E6%98%9F%E6%B2%B3.png" tvg-name="TVB星河频道" group-title="香港电视台",TVB星河频道',
   '有线娱乐': '#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS6Skdax1wlmiOnSvCkudVBwmC4YgU04n0cv0MWnMhtkvUxEKuW" tvg-name="有线娛樂台" group-title="香港电视台",有线娛樂台',
   '有线财经': '#EXTINF:-1 tvg-logo="http://epg.51zmt.top:8000/tb1/gt/youxiancaijingzixun.png" tvg-name="有线财经资讯台" group-title="香港电视台",有线财经资讯台',
   '': '',
   
  }.get(var,'#EXTINF:-1 tvg-name="' + var + '" ,' +var )   #'error'為預設返回值，可自設定

def WriteFile1(str):    # 寫入檔案
  #print (str)
  FileNa=str[0]
  #print (FileNa)
  fo = open(FileNa, "w")
  #wdata="#EXTM3U\n"
  wdata=str[1]
  fo.write(wdata)
  # 关闭打开的文件
  fo.close()
  return

def ReadtData(var):  # 讀入大視界資源
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
  
  my_list = title,add1
  
  tdata=""
  rdata=""
  for  x in range(len(my_list[0])):
    #print (my_list[0][x])
    tdata+=(foo(my_list[0][x]))
    
    tdata+=("\n{add}\n".format(name=my_list[0][x],add=my_list[1][x]))
    #rdata+=("{name}${add}\n".format(name=my_list[0][x],add=my_list[1][x]))
    #print (tdata)

  
  if var == 0:
    tdata=""
    print('大視界0資源')    
  else:
    print('大視界',len(my_list[0]),'資源')

	# end 
  return tdata
  
def ReadoData(var):  # 讀入IPTV345.com 資源
  readlist = [1,3]
  #讀取網頁  
  '''
  url = 'http://m.iptv345.com/?act=play&token=67487d7def751b4e516e197015d2866d&tid=gt&id=1'
  request_headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36'
  }

  req = urllib.request.Request(url,  headers=request_headers)
  html = urllib.request.urlopen(req).read()
  html = html.decode('utf-8')     #python3版本中需要加入
  '''
  
  # 變數測試
  html=  """<!DOCTYPE html>
      <html>
      <head>
      <title>TVB翡翠台 - 電視直播</title>
      <meta charset="utf-8">
      <meta name="application-name" content="網絡電視直播移動版,IPTV電視直播手机版" />
      <meta name="title" content="TVB翡翠台 - 電視直播"/>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta name="keywords" content="網絡電視,網路電視,電視直播,手机版,電視,免費電視">
      <meta name="description" content="網絡電視,網路電視,全球電視直播,高清電視,免費電視,IPTV電視直播手机版">
      <link rel="stylesheet" href="http://code.jquery.com/mobile/1.3.2/jquery.mobile-1.3.2.min.css" />
      <script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
      <script src="http://code.jquery.com/mobile/1.3.2/jquery.mobile-1.3.2.min.js"></script>
      <style type="text/css">
      .headerNfooter {background-color: #C00;color: #fff;text-shadow: none;}
      .headerNfooter a:link,.headerNfooter a:hover,.headerNfooter a:visited,.headerNfooter a:active { color: #fff; text-decoration: none;}
      .headerNfooter h1 {text-indent: -999em; }
      </style>

      <body>
      <div data-role="page">
      <div class="headerNfooter" data-role="header" data-theme="f" data-position="fixed">
      <h1>TVB翡翠台 - 電視直播</h1><a href="#" data-iconpos="left" data-icon="back" data-rel="back">返回</a>
      <a href="?act=home" data-icon="home" data-role="button" data-inline="true">首頁</a>
      </div>
      <!--top--><div align="center"><a href="http://dse34s.sap7f.cn/m/8CbaJ?t=760c64" target="_blank"><img src="/ad/1465719759.gif" width="100%"></a></div><div data-role="content"><div align="center">如不能播放,請選擇其他線路!</div><center><a href="http://down.iptv2020.com/down.php" target="_blank" >或點擊下載安卓版網絡電視觀看</a></center><ul data-role="listview" data-inset="true" data-divider-theme="a"><script src="/player.js?t=20200403"></script>
      <li data-role="list-divider"><center><video name="vstPlayer" id="vstPlayer" width="100%" controls="controls" webkit-playsinline="webkit-playsinline" playsinline></video><br/></center><center id="url_select">
      <select onchange="startPlayer(this.options[this.selectedIndex].value)" id="playURL"><option value="http://104.233.176.70:13164/play.m3u8?token=MK8rRKHOjvFWMmJLIhKzGURb&tid=gt&id=1">線路1</option><option value="http://104.233.176.70:13164/play.m3u8?token=MK8rRKHOjvFWMmJLIhKzGURb&tid=gt&id=1&p=1">線路2</option><option value="http://104.233.176.70:13164/play.m3u8?token=MK8rRKHOjvFWMmJLIhKzGURb&tid=gt&id=1&p=2">線路3</option><option value="http://104.233.176.70:13164/play.m3u8?token=MK8rRKHOjvFWMmJLIhKzGURb&tid=gt&id=1&p=3">線路4</option><option value="http://104.233.176.70:13164/play.m3u8?token=MK8rRKHOjvFWMmJLIhKzGURb&tid=gt&id=1&p=4">線路5</option></select></center></li><li data-role="list-divider">TVB翡翠台 2020-04-03 節目預告</li><div align="center"></div><li><a href="http://dse34s.sap7f.cn/m/8CbaJ?t=760c64" target="_blank">美女视频直播</a></li>
      <li><a href="https://s.click.taobao.com/DJSXPuv" target="_blank">点击领取淘宝/天猫优惠券</a></li><li>00:55 宣傳易[粵]</li><li>01:00 高朋滿座#83[粵]</li><li>01:30 宣傳易[粵]</li><li>01:35 流行都市[粵]</li><li>02:20 X偏方 全民拆解II[粵]</li><li>02:50 無間音樂[粵]</li><li>03:45 樓住有情人#11[粵]</li><li>04:40 活著[粵]</li><li>05:05 活著[粵]</li><li>05:30 眉精眼企[粵]</li><li>06:00 香港早晨[粵] 及 交通消息[粵]</li><li>07:40 環球新聞檔案[粵]</li><li>07:45 香港早晨[粵] 及 交通消息[粵]</li><li>08:10 香港早晨[粵]</li><li>08:55 瞬間看地球[粵]</li><li>09:00 交易現場[粵]</li><li>09:30 深港滬通[粵]</li><li>09:45 快樂長門人[粵]</li><li>09:55 數碼暴龍App世代[粵/日]</li><li>10:25 真情#280[粵]</li><li>11:05 三國機密之潛龍在淵#83[粵/普]</li><li>11:30 宣傳易[粵] 及 新聞提要[粵]</li><li>11:35 交易現場[粵]</li><li>11:45 樓住有情人#12[粵]</li><li>12:40 宣傳易[粵]</li><li>12:45 交易現場[粵]</li><li>13:00 午間新聞[粵]</li><li>13:15 瞬間看地球[粵]</li><li>13:20 流行都市[粵]</li><li>14:05 超級勁歌推介[粵]</li><li>14:10 宣傳易[粵]</li><li>14:15 你估我唔到[粵]</li><li>14:40 交易現場[粵] 及 深港滬通[粵]</li><li>14:45 張保仔#28[粵][PG]</li><li>15:45 每日媽媽[粵/日] 及 交易現場[粵]</li><li>16:15 咕嚕咕嚕魔法陣[粵/日]</li><li>16:50 Think Big天地[粵]</li><li>17:20 閃電十一人 獵戶座的刻印[粵/日]</li><li>17:50 財經新聞[粵]</li><li>18:00 獨孤皇后#84[粵/普] 及 新聞檔案[粵]</li><li>18:30 六點半新聞報道[粵]</li><li>19:20 世界觀[粵]</li><li>19:25 天氣報告[粵]</li><li>19:30 東張西望[粵]</li><li>20:00 愛.回家之開心速遞#834[粵]</li><li>20:30 機場特警#4[粵][PG]</li><li>21:30 慶餘年28[粵/普]</li><li>22:30 娛樂大家10點半[粵] 及 環球新聞檔案[粵]</li><li>23:00 晚間新聞[粵]</li><li>23:30 新聞檔案[粵]</li><li>23:35 天氣報告[粵]</li><li>23:40 瞬間看地球[粵]</li><li>23:45 娛樂頭條[粵]</li><li>23:50 On Call 36小時II#7[粵]</li></ul></div>
      <!--end--> 
      <div data-role="footer">
      <h4>版權聲明 &copy; 所有源來源於互聯網搜索</h4>
      </div>
      </div>
      <div id="fb-root"></div>
      </body>
      <span style="display:none">
      <script src="https://s13.cnzz.com/z_stat.php?id=1273922221&web_id=1273922221" language="JavaScript"></script><!-- Global site tag (gtag.js) - Google Analytics -->
      <script async src='https://www.googletagmanager.com/gtag/js?id=UA-120439249-1'></script>
      <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'UA-120439249-1');
      </script>
      </span>
      </html>"""
  
  theader = re.findall('<h1>(.*?) - 電視直播',html)
  tdata = re.findall('<option value="(.*?)">',html)
  #results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
  print (theader,tdata)
  #tdata=html
	# end 
  return tdata


# **************************************************************************************************************
tData1= ReadtData(1)  #                            讀入大視界資源                       0  測試用不讀入資源  / 任何值正常讀入資源

# **************************************************************************************************************
#tData1= ReadtData(1)  #                       讀入IPTV345.com 資源               0  測試用不讀入資源  / 任何值正常讀入資源
tvb='http://m.iptv345.com/?act=play&token=67487d7def751b4e516e197015d2866d&tid=gt&id=1'

#tData1= ReadoData(1)

#print (len(tData1))
#print (tData1)
tdata="#EXTM3U\n"
tdata+=tData1



Mylist=['3.m3u',tdata]
WriteFile1(Mylist)   # 寫入檔案



