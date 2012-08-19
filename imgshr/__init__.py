#coding: utf-8

import os
import re

import requests


class ImgShr(object):

    regex = re.compile(r'"http://imgshr\.com/([^"]+)"', re.IGNORECASE)

    def __init__(self):
        self.url = 'http://imgshr.com/upload/send'

    def upload(self, image, legend=None):

        if not os.path.exists(image):
            return None

        f = {"0_file": open(image, 'rb')}
        d = {"0_source": "computer", "NBR_FILE": 1, "MAX_FILE_SIZE": 1000000}
        r = requests.post(self.url, data=d, files=f)

        match = self.regex.search(r.text)

        if match is not None and match.lastindex == 1:
            return 'http://imgshr.com/i/%s' % match.group(1)
        return None
