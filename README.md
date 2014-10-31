epvpimg.com uploader

Place epvpimg.py into your project folder or into 'python27/Lib/site-packages/' to use it globally.

For Python 2.7 and 3.x

Required Libraries
---
[requests](https://pypi.python.org/pypi/requests/2.4.0)


Usage/Test
---
    from epvpimg import Epvpimg
    
	# Full path
    imagefile = r'C:\someimage.png'
	
	# Returns servers response as dictionary
	response = Epvpimg.upload(imagefile)
	print(response)
	
	# Get image type and url
	imgtype, imgurl = (response['type'], response['thumbnail_url'])
	print(imgtype, imgurl)
	
	# Return only the image url
	imgurl = Epvpimg.upload(imagefile, directlink=True)
	print(imgurl)
    
    
