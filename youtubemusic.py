import yt_dlp as youtube_dl
from ytmusicapi import YTMusic
import os
import sys

def get_user_desktop_folder():
    user_folder = os.path.expanduser("~")
    folder = os.path.join(user_folder, "OneDrive\Desktop")
    return folder

dfolder = get_user_desktop_folder()
print(dfolder)

make = os.path.join(dfolder, "ganba")

print(make)
os.makedirs(make, exist_ok=True)
print(f"{make}フォルダを作成しました！")

# フォルダ移動
os.chdir(make)



ytmusic=YTMusic()


whichchange = input("もしキーワードなら'k',urlなら'u'を入力してください")
if whichchange == "k":
    search_name = input("楽曲名またはキーワードを入力してね！")
    search_result = ytmusic.search(search_name)

    first_result = search_result[0]
    video_id = first_result['videoId']
    url = f'https://www.youtube.com/watch?v={video_id}'

elif whichchange == "u":
    url = input("URLを入力してください")

else:
    print("無効な入力です。")
    sys.exit()

ydl_opts = {
     'outtmpl':'%(title)s.%(ext)s',
     'format': 'bestaudio/best',
     'merge_output_format': 'mp3'
     }
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          ydl.download([url])

print("ダウンロードが完了しました！")


continue_or_not = input("続けますか？(y/n)")
if continue_or_not == "y":
     os.system("python youtubemusic.py")
elif continue_or_not == "n":
    print("終了します。")
    sys.exit()
else:
    print("無効な入力です。")
    sys.exit()
     


# ユーザーのデスクトップフォルダを取得
