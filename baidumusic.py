#coding = utf-8
import  requests
import  re

#搜索歌曲
name = input("请输入明星名字：")
print("正在爬取......")
data = {
    "key":name
}
#百度音乐搜索url(api)
search_url = 'http://music.baidu.com/search'
#发送http请求
search_response = requests.get(search_url,params=data)#get传参数需要字典的方式
search_response.encoding = 'utf-8'
search_html = search_response.text
#print(search_html)

#获取歌曲sid 正则表达式
song_ids = re.findall(r'sid&quot;:(\d+),',search_html)
#print(song_ids)

#根据id去获取歌曲的信息
song_api = 'http://play.baidu.com/data/music/songlink'
data = {
    'songIds':','.join(song_ids),
    'hq':0,
    'type':'mp3',
    'pt':0,
    'flag':'1',
    's2p':650,
    'prerate':128,
    'bwt':266,
    'dur':231000,
    'bat':266,
    'bp':100,
    'pos':65833,
    'auto':0
}
#发送请求
song_response=requests.post(song_api,data=data)
#print(song_response.text)
#将返回回来的歌曲数据转换成字典
song_info = song_response.json()
song_info = song_info['data']['songList']
#print(song_info)

#遍历下载
for song in song_info:
    song_name = song['songName']

    with open('%s.mp3'%song_name,'wb') as f:
        #下载MP3
       # print(song['songLink'])
        response = requests.get(song['songLink'])
        f.write(response.content)
print("爬取成功")