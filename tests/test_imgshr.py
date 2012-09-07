# coding: utf-8

import os
import unittest

from imgshr import ImgShr


class ImgShrTestCase(unittest.TestCase):

    def test_upload(self):
        imgshr = ImgShr()

        # trying to uploading an non-existing file raises IOError
        self.assertRaises(IOError, imgshr.upload, [''])

        # pass the path to a single image
        filename = os.path.join(os.path.dirname(__file__), 'image.jpg')
        response = imgshr.upload(filename)
        self.assertIsInstance(response, dict)
        self.assertIsNotNone(response['image.jpg'])

        # pass a file object
        image = open(filename, 'rb')
        self.assertIsInstance(imgshr.upload(image), dict)

        # pass a list of image filenames
        filenames = [filename] * 3
        self.assertIsInstance(imgshr.upload(filenames), dict)

        # pass a list of file objects
        images = [image] * 3
        self.assertIsInstance(imgshr.upload(images), dict)
