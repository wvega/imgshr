# coding: utf-8

import os
import unittest

from imgshr import ImgShr


class ImgShrTestCase(unittest.TestCase):

    def test_upload(self):
        imgshr = ImgShr()

        # uploading an non-existing file returns None
        self.assertIsNone(imgshr.upload(''))

        # a succesfull upload should return a URL string
        image = os.path.join(os.path.dirname(__file__), 'image.jpg')
        self.assertIsInstance(imgshr.upload(image), basestring)
