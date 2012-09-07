#coding: utf-8

import os
import re

import requests


class ImgShr(object):

    regex = re.compile(r'"http://imgshr\.com/([^"]+)"', re.IGNORECASE)

    def __init__(self):
        self.url = 'http://imgshr.com/upload/send'

    def upload(self, images=[], label=None):
        uploaded = {}

        if isinstance(images, basestring):
            images = [images]
        if isinstance(images, file):
            images = [images]

        for image in images:
            if not isinstance(image, file):
                image = open(image, 'rb')

            f = {"0_file": image}
            d = {"0_legend": label, "0_source": "computer", "NBR_FILE": 1, "MAX_FILE_SIZE": 1000000}
            r = requests.post(self.url, data=d, files=f)

            name = os.path.basename(image.name)
            match = self.regex.search(r.text)

            if match is not None and match.lastindex == 1:
                uploaded[name] = 'http://imgshr.com/i/%s' % match.group(1)
            else:
                uploaded[name] = None

        return uploaded if len(uploaded) > 0 else None
