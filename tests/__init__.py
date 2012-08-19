# coding: utf-8

import unittest

from tests.test_imgshr import ImgShrTestCase


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ImgShrTestCase('test_upload'))
    return suite
