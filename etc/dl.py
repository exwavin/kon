!pip install youtube-dl

import os
import youtube_dl

def download_vimeo_video(video_url, quality):
    ydl_opts = {
        'format': 'bestvideo[height<={}]'.format(quality),
        'outtmpl': 'vimeo_video.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# Ganti URL dan kualitas sesuai kebutuhan Anda
video_url = 'https://vimeo.com/xxxxxxx'  # Ganti dengan URL video Vimeo Anda
quality = 720  # Ganti dengan kualitas yang Anda inginkan (misal: 240, 360, 480, 720, 1080)

download_vimeo_video(video_url, quality)
