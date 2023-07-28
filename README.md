YTLoader™ is fully free, lightweight and simple YouTube video downloader.😁


INSTALATION


1. First, clone this repo.

2. Open terminal and type this command for install pytube framework:

	For MacOS and Linux:
		|pip3 install pytube|
	
	For Windows:
		|pip install pytube|

3. Open main.py and on line 3 insert your path where videos will saved.


ERRORS 


If something went wrong;

1. Try to update pytube by type this command: 
	python3 -m pip install --upgrade pytube| or |python -m pip install --upgrade pytube

2. Maybe your path is unveiled.

3. If you have this error; get_throttling_function_name: could not find match for multiple, 
	visit cipher.py in pytube`s directory and find function_patterns variable. Change 		
	pattern to following:

	r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'
	r'\([a-z]\s*=\s*([a-zA-Z0-9$]{2,3})(\[\d+\])?\([a-z]\)'

For other errors, write your problem in issues. Or just visit stack overflow)


TODO


1. Add other resolutions - like 240p, 360p, 720p, 1080p... 'DONE' 

2. Add function for downloading entire playlists.

3. Add function that shows info about videos or playlists.

4. Add function that extract audio from video, and downloading it. 



ONLY FOR EDUCATIONAL PURPOSES. DO NOT SHARE THIS FILES WITH OTHERS. IT IS ILLEGAL.
