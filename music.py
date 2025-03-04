from ytmusicapi import YTMusic
import vlc
import os
import yt_dlp as youtube_dl

# VLCのインストールディレクトリを環境変数に追加
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')

ytmusic = YTMusic()


music_name = input("楽曲名またはキーワードを入力してね！")
# 楽曲を検索して最初の結果を取得
search_results = ytmusic.search(music_name)
first_result = search_results[0]

# 楽曲のURLを取得
video_id = first_result['videoId']
youtube_url = f"https://www.youtube.com/watch?v={video_id}"

# yt-dlpを使用して動画のストリームURLを取得
ydl_opts = {
    'format': 'bestaudio/best',
    'noplaylist': True,
    'quiet': True,
    'extract_flat': True,
    'outtmpl':'%(title)s.%(ext)s'
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(youtube_url, download=False)
    stream_url = info_dict['url']

# VLCを使用して音楽を再生
player = vlc.MediaPlayer(stream_url)
player.play()

# 再生が終了するまで待機
try:
    while True:
        state = player.get_state()
        if state in [vlc.State.Ended, vlc.State.Error]:
            break
        # ユーザー入力を待機して再生を停止
        user_input = input(" 'stop'を入力してエンターを押すと再生を停止します ")
        if user_input.lower() == 'stop':
            player.stop()
            break
except KeyboardInterrupt:
    player.stop()
