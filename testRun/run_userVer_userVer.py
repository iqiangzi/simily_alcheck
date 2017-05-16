#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-16 08:28:18
# @Author  : Nxy
# @Site    : 
# @File    : run_userVer.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox

class RunUserVer(myUnitChrome.UnitChrome):
    def test_userLogout_run(self):
        pass
