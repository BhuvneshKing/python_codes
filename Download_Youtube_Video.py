from pytube import YouTube
link = input("Enter the URL of Video")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()