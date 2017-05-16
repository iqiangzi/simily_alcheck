#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-16 08:28:19
# @Author  : Nxy
# @Site    : 
# @File    : run_fileManager.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox

class RunFileManager(myUnitChrome.UnitChrome):
    def test_folderDowload_run(self):
        pass
    def test_folderDelete_run(self):
        pass
    def test_folderRename_run(self):
        pass
