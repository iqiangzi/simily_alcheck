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
from time import sleep
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox
from testCase.models.userVer.userVer import UserVer
from testCase.models.paperCheck.newPaperCheck_manualEntry import ManualEnterPaperCheck
from testResult.getResultImage import getResultImage

class RunNewPaperCheck(myUnitChrome.UnitChrome):

    def user_login(self):
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("alcheck","f")
        sleep(2)
        me=ManualEnterPaperCheck(self.driver)
        me.in_PaperCheck_button()
        sleep(2)
        me.in_manualEnter()

    def test_click_movetofolder_run1(self):
        '''点击添加论文至分类文件夹，弹出添加文件夹窗口'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        me.add_to_folder()
        sleep(5)
        verify_addfolder = me.get_confirmbutton()
        self.assertEqual(verify_addfolder,"确定","添加至文件夹窗口未弹出")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"click_addtofolder.jpg")

    def test_moveto_existfolder_run(self):
        '''添加至已有文件夹，显示文件夹名称'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        me.add_to_folder()
        sleep(5)
        #选择已存在的文件夹
        me.choose_existfolder()
        sleep(2)
        #获取选择文件夹的名称
        choose_name=me.get_existfolder_text()
        sleep(2)
        #单击确定按钮
        me.click_confirm_button()
        show_name=me.get_choosefolder_text()
        self.assertEqual(show_name,choose_name,"添加至已存在文件夹失败")
        print("添加至已存在文件夹测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"moveto_existfolder.jpg")

    def test_modifyto_existfolder_run(self):
        '''修改至已有文件夹，显示文件夹名称'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        me.add_to_folder()
        sleep(5)
        #选择已存在的文件夹
        me.choose_existfolder()
        sleep(2)
        #单击确定按钮
        me.click_confirm_button()
        sleep(2)
        #单击修改按钮
        me.modify_choosefolder_button()
        sleep(2)
        me.modify_existfolder()
        sleep(2)
        #获取选择文件夹的名称
        modify_name=me.modify_existfolder_text()
        sleep(2)
        #单击确定按钮
        me.click_confirm_button()
        sleep(2)
        show_name=me.get_choosefolder_text()
        self.assertEqual(show_name,modify_name,"修改至已存在文件夹失败")
        print("修改文件夹测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"modifyto_existfolder.jpg")

    def test_add_foldername_success_run(self):
        '''添加至新文件夹成功'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        me.add_to_folder()
        sleep(5)
        foldername=me.add_to_new_folder()
        sleep(2)

        show_name=me.get_choosefolder_text()
        sleep(2)
        self.assertEqual(show_name,foldername,"添加至新建文件夹失败")
        print("添加至新建文件夹测试成功！")

        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"add_foldername_success.jpg")

    def test_add_foldername_overlength_run(self):
        '''添加至新文件夹时，名称超长'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()

        sleep(5)
        me.add_to_new_folder_custom("长度的测试长度的测试长度的测试12")
        error_info=me.create_error_remind()
        self.assertEqual(error_info,"文件夹名称最长为16位，请重新输入！","文件夹名称超长未提示")
        print("新建文件夹名称不能过长测试成功！")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"add_foldername_overlength.jpg")

    def test_add_foldername_isnull_run(self):
        '''添加至新文件夹时，名称为空'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        sleep(5)
        me.add_to_new_folder_custom("")
        error_info=me.create_error_remind()
        self.assertEqual(error_info,"文件夹名称不能为空","文件夹名称为空未提示")
        print("新建文件夹名称不能为空测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"add_foldername_isnull.jpg")

    def test_add_foldername_exist_run(self):
        '''添加至新文件夹时，名称已存在'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        sleep(5)
        #添加至新文件夹
        foldername=me.add_to_new_folder()

        me.modify_choosefolder_button()
        #单击添加到新文件夹
        me.add_to_newfolder()
        sleep(2)
        #获取输入的文件夹名称
        me.input_new_foldername(foldername)
        sleep(2)
        #单击确定按钮
        me.click_confirm_button()
        sleep(2)
        error_info = me.create_error_remind()
        self.assertEqual(error_info,"文件夹已存在！","名称重复未提示")
        print("新建文件夹名称不能重复测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"add_foldername_duplication.jpg")


