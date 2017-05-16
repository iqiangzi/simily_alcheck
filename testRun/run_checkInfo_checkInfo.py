#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-16 08:28:19
# @Author  : Nxy
# @Site    : 
# @File    : run_checkInfo.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox

class RunCheckInfo(myUnitChrome.UnitChrome):
    def test_addToFolder_run(self):
        pass
    def test_downloadReport_run(self):
        pass
    def test_retesting_run(self):
        pass
    def test_delRecord_run(self):
        pass
