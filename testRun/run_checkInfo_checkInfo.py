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
            succeed_info = ci.getAlertInfo()
            self.assertEqual(succeed_info,'移动成功！','*****添加至文件夹失败*****')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addToFolder_allToNew.jpg")
            sleep(2)

    def test_addToFolder_oneToNew_run02(self):
        '''添加首页首条检测信息至新建文件夹'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        ci.clickCheckboxFirst()
        ci.clickMoreBtn()
        name = ci.AddToNewFolder()
        try:
            succeed_info = ci.getAlertInfo()
            self.assertEqual(succeed_info,'移动成功！','*****添加至文件夹失败*****')
            confirm_name = ci.getFolderNameFirst()
            self.assertEqual(confirm_name,name,"*****添加至文件夹失败*****")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addToFolder_oneToNew.jpg")
            sleep(2)

    def test_addToFolder_allToExist_run03(self):
        '''添加首页全部检测信息至已有文件夹'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        ci.checkAllInfo()
        ci.clickMoreBtn()
        ci.AddToExistFolder()
        try:
            succeed_info = ci.getAlertInfo()
            self.assertEqual(succeed_info,'移动成功！','*****添加至已有文件夹失败*****')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addToFolder_allToExist.jpg")
            sleep(2)

    def test_addToFolder_oneToExist_run04(self):
        '''添加首页首条检测信息至已有文件夹'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        ci.clickCheckboxFirst()
        ci.clickMoreBtn()
        name = ci.AddToExistFolder()
        try:
            succeed_info = ci.getAlertInfo()
            self.assertEqual(succeed_info,'移动成功！','*****添加至文件夹失败*****')
            confirm_name = ci.getFolderNameFirst()
            self.assertEqual(confirm_name,name,"*****添加至文件夹失败*****")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addToFolder_oneToExist.jpg")
            sleep(2)

    def test_addToFolder_checkNone_run05(self):
        '''不勾选检测信息点击添加至文件夹'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        ci.clickMoreBtn()
        ci.clickAddToFolder()
        try:
            alert_info = ci.getAlertInfo()
            self.assertEqual(alert_info,'请至少勾选一条数据！','*****未勾选检测信息点击后未做提示*****')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addToFolder_checkNone.jpg")
            sleep(2)

    def test_addToFolder_allToNew_isnull_run06(self):
        '''新建文件夹时，输入文件夹名称为空'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        ci.checkAllInfo()
        ci.clickMoreBtn()
        ci.clickAddToFolder()
        try:
            errMsg = ci.AddToNewFolderAlertVerify("")
            self.assertEqual(errMsg,'文件夹名称不能为空！','*****文件夹名称为空时提示错误*****')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addToFolder_allToNew_isnull.jpg")
            sleep(2)

    def test_addToFolder_allToNew_isduplicate_run07(self):
        '''新建文件夹时，输入文件夹名称重复'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        ci.checkAllInfo()
        ci.clickMoreBtn()
        ci.clickAddToFolder()
        existName = ci.getExistFolderName()
        try:
            errMsg = ci.AddToNewFolderAlertVerify(existName)
            self.assertEqual(errMsg,'文件夹已存在！','*****文件夹名称重复时提示错误*****')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addToFolder_allToNew_isduplicate.jpg")
            sleep(2)

    def test_addToFolder_allToNew_overlong_run08(self):
        '''新建文件夹时，输入文件夹名称超过长度限制'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        ci.checkAllInfo()
        ci.clickMoreBtn()
        ci.clickAddToFolder()
        try:
            overlongName = '长度的测试长度的测试长度的测试长度的测试'
            errMsg = ci.AddToNewFolderAlertVerify(overlongName)
            self.assertEqual(errMsg,'文件夹名称最长为16位，请重新输入！','*****文件夹名称超过长度限制时提示错误*****')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addToFolder_allToNew_overlong.jpg")
            sleep(2)

    def test_downloadCheckInfo_allSimple_run09(self):
        '''勾选全部检测信息，下载简明报告至本地'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        ci.downloadReport_allcheck_simple()
        try:
            pass
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"downloadCheckInfo_allSimple.jpg")
            sleep(2)

    def test_downloadCheckInfo_allDetail_run10(self):
        '''勾选全部检测信息，下载详细报告至本地'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        ci.downloadReport_allcheck_detail()
        try:
            pass
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"downloadCheckInfo_allDetail.jpg")
            sleep(2)

    def test_downloadCheckInfo_oneSimple_run11(self):
        '''勾选首条检测信息，下载简明报告至本地'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        ci.downloadReport_firstcheck_simple()
        try:
            pass
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"downloadCheckInfo_oneSimple.jpg")
            sleep(2)

    def test_downloadCheckInfo_oneDetail_run12(self):
        '''勾选首条检测信息，下载详细报告至本地'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        ci.downloadReport_allcheck_detail()
        try:
            pass
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"downloadCheckInfo_oneDetail.jpg")
            sleep(2)

    def test_downloadCheckInfo_unsucceed_run13(self):
        '''下载报告时勾选包含未检测成功的信息'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        err_info = ci.downloadReport_unsucceed()
        try:
            self.assertEqual(err_info,"选中论文中有等待检测或检测失败或账户到期或余额不足的论文，请重新选择后再下载！","*****下载检测不成功的报告未提示*****")
        finally:
            sleep(2)
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"downloadCheckInfo_unsucceed.jpg")
            sleep(2)

    def test_downloadCheckInfo_uncheck_run14(self):
        '''未勾选检测信息点击下载报告'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        err_info = ci.downloadReport_uncheck()
        try:
            self.assertEqual(err_info,"请至少勾选一条数据！","*****未勾选检测信息未提示*****")
        finally:
            sleep(2)
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"downloadCheckInfo_uncheck.jpg")
            sleep(2)

    def test_redetectCheckInfo_succeed_run15(self):
        '''重新检测报告'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        status_info = ci.redetect_succeed()
        try:
            self.assertEqual(status_info,"等待检测","*****未开始重新检测*****")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"redetectCheckInfo_succeed.jpg")
            sleep(2)

    def test_redetectCheckInfo_hasSucceedReport_run16(self):
        '''重新检测报告中包含已成功或待检测的报告'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        err_info = ci.redetect_hasSucceedReport()
        try:
            self.assertEqual(err_info,"选中论文中有等待检测或 检测成功的论文，请重新选择后再开始检测！","*****检测包含成功和待检测状态的论文未提示*****")
        finally:
            sleep(2)
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"redetectCheckInfo_hasSucceedReport.jpg")
            sleep(2)

    def test_redetectCheckInfo_uncheck_run17(self):
        '''未勾选检测信息点击重新检测'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        err_info = ci.redetectReport_uncheck()
        try:
            self.assertEqual(err_info,"请至少勾选一条数据！","*****未勾选检测信息未提示*****")
        finally:
            sleep(2)
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"redetectCheckInfo_uncheck.jpg")
            sleep(2)

    def test_deleteCheckInfo_succeed_run18(self):
        '''删除检测信息'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        info_count_befor = ci.getInfoCount()
        succeed_info = ci.deleteReport()
        try:
            self.assertEqual(succeed_info,"删除成功!","*****删除信息成功未提示*****")
            info_count_after = ci.getInfoCount()
            self.assertEqual(info_count_befor-1,info_count_after,"*****删除成功但记录条数未减少*****")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"deleteCheckInfo_succeed.jpg")
            sleep(2)

    def test_deleteCheckInfo_uncheck_run19(self):
        '''未勾选检测信息点击删除'''
        self.toCheckInfo()
        ci = CheckInfo(self.driver)
        err_info = ci.deletReport_uncheck()
        try:
            self.assertEqual(err_info,"请至少勾选一条数据！","*****未勾选检测信息未提示*****")
        finally:
            sleep(2)
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"deleteCheckInfo_uncheck.jpg")
            sleep(2)


    def test_downloadReport_run(self):
        pass
    def test_retesting_run(self):
        pass
    def test_delRecord_run(self):
        pass
