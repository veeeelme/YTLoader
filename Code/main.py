from pytube import YouTube

path = 'YOUR PATH THERE'


link = input('Enter URL of video >> ')
resolution = input('Enter resolution(144p, 240p, 360p, 720p, 1080p...) >> ')


def download():
    try:
        yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
        stream = yt.streams.get_by_resolution(resolution)
        stream.download(path)
    except Exception as e:
        print(f'oops! Error: {e}')


print('wait a minute...')
download()
print('Finish! Your file is in ', path)
