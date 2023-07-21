from pytube import YouTube

path = 'YOUR PATH HERE'


link = input('Enter URL of video >> ')


def download():
    try:
        yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
        stream = yt.streams.get_lowest_resolution()
        stream.download(path)
    except Exception as e:
        print(f'oops! Error: {e}')


print('wait a minute...')
download()
