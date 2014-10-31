"""
epvpimg uploader
"""

__title__ = 'epvpimg uploader'
__version__ = '0.1.0'
__build__ = "0000"
__author__ = 'sharpshadow (github.sharpshadow@gmail.com)'
__license__ = 'Apache 2.0'


import json
import os

import requests

class Epvpimg:
    """Upload a single image to epvpimg.com and return the values in a dict"""
    def __init__(self):
        self.allowed_filetypes = ['BMP', 'GIF', 'JPE', 'JPG', 'JPEG', 'PNG', 'SVG', 'TIF', 'TIFF']
        self.max_filesize = 10000000
        self.max_filesize_gif = 2000000
    
    def upload(self, path, directlink=None):
        """directlink: return only image url"""
        
        if os.path.exists(path) is True:
            filesize = os.path.getsize(path)
            filename = path.split('\\').pop()
            filetype = filename.split('.').pop()

            if (filetype.upper() not in self.allowed_filetypes or
                filesize > self.max_filesize or
                filetype.upper() == 'GIF' and filesize > self.max_filesize_gif
                ):
                raise Exception('Image does not match the terms of epvpimg.com.')
            
            files = {'files[]': (filename, open(path, 'rb'), 'image/{}'.format(filetype.lower()))}
            response = requests.post('http://epvpimg.com/upload/', files=files)

            if directlink is True:
                return json.loads(response.text).pop()['thumbnail_url']
            else:
                return json.loads(response.text).pop()
        else:
            raise Exception('File does not exists.')
