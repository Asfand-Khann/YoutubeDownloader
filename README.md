# YouTube Video Downloader (Python)

This simple script allows you to download YouTube videos using the **pytube** library.

## Requirements

- Python 3.x
- pytube library

Install pytube using:
```
pip install pytube
```

## Usage

1. Run the script:
```
python youtube_downloader.py
```

2. Enter a valid YouTube video link when prompted.

3. The highest‑resolution version of the video will be downloaded to your current directory.

## Script Contents

```python
from pytube import YouTube

video_url = input("Enter Youtube Video link: ")

yt = YouTube(video_url)

stream = yt.streams.get_highest_resolution()

stream.download()

print("Download completed!")
```

## Notes

- Some videos may not download due to region restrictions or YouTube-side issues.
- Ensure your network connection is stable during the download.



