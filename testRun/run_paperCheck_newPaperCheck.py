#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-16 08:28:19
# @Author  : Nxy
# @Site    : 
# @File    : run_newPaperCheck.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox

class RunNewPaperCheck(myUnitChrome.UnitChrome):
    def test_manualEntry_run(self):
        pass
