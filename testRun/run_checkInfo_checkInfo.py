#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-16 08:28:19
# @Author  : Nxy
# @Site    : 
# @File    : run_checkInfo.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from testResult.getResultImage import getResultImage
from testCase.models.userVer.userVer import UserVer
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox
from time import sleep
from testCase.models.checkInfo.checkInfo import CheckInfo


class RunCheckInfo(myUnitFirefox.UnitFirefox):
    #**************************************************************

    def login(self):
        '''用户登录'''
        userver=UserVer(self.driver)
        userver.userLogin("alcheck","f")
        sleep(2)
    def toCheckInfo(self):
        '''用户进入检测信息页面'''
        ci = CheckInfo(self.driver)
        self.login()
        ci.clickCheckInfoBtn()

    #************************************************************

    def test_addToFolder_allToNew_run01(self):
        '''添加首页全部检测信息至新建文件夹'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        ci.checkAllInfo()
        ci.clickMoreBtn()
        ci.AddToNewFolder()
        try:
            succeed_info = ci.getAddSucceedInfo()
            self.assertEqual(succeed_info,'移动成功！','*****添加至文件夹失败*****')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addToFolder_allToNew.jpg")
            sleep(2)



    def test_downloadReport_run(self):
        pass
    def test_retesting_run(self):
        pass
    def test_delRecord_run(self):
        pass
