from pytube import YouTube
import ssl

# ignore ssl
ssl._create_default_https_context = ssl._create_unverified_context
link = input('Enter The Youtube Video URL:')
yt = YouTube(link).streams.get_highest_resolution()
yt.download()

print('Your Video Has Been Downloaded')
