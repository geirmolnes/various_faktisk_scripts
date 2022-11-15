import os
import youtube_dl

filedir = os.path.join("/Users/geir/Code/facebook_video_downloader/downloads")

# Open urls.txt and read the urls
with open("new_url.txt", "r") as f:
    urls = f.readlines()

# Loop through the urls and download the videos using youtube-dl
for url in urls:
    ydl_opts = {
        "outtmpl": f"{filedir}/%(title)s.%(ext)s",
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception:
            print(f"Error downloading video\n{url}")
            # Write the url to a file called failed.txt
            with open("failed.txt", "a") as f:
                f.write(url)
