from pytube import YouTube

video_url = input("Enter Youtube Video link: ")

yt = YouTube(video_url)

stream = yt.streams.get_highest_resolution()

stream.download()

print("Download completed!")
