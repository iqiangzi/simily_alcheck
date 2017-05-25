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
        sleep(5)

    def test_click_addtofolder_run1(self):
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

    def test_addto_existfolder_run2(self):
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
        imagetest.insert_image(self.driver,"addto_existfolder.jpg")

    def test_modify_existfolder_run3(self):
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
        sleep(5)
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
        imagetest.insert_image(self.driver,"modify_existfolder.jpg")

    def test_addtonew_foldername_success_run4(self):
        '''添加至新文件夹成功'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        sleep(5)
        foldername=me.add_to_new_folder()
        sleep(2)

        show_name=me.get_choosefolder_text()
        sleep(2)
        self.assertEqual(show_name,foldername,"添加至新建文件夹失败")
        print("添加至新建文件夹测试成功！")

        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"addtonew_foldername_success.jpg")

    def test_addtonew_foldername_overlength_run5(self):
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
        imagetest.insert_image(self.driver,"addtonew_foldername_overlength.jpg")

    def test_addtonew_foldername_isnull_run6(self):
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
        imagetest.insert_image(self.driver,"addtonew_foldername_isnull.jpg")

    def test_addtonew_foldername_exist_run7(self):
        '''添加至新文件夹时，名称已存在'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        sleep(5)
        #添加至新文件夹
        foldername=me.add_to_new_folder()

        me.modify_choosefolder_button()
        sleep(2)
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
        imagetest.insert_image(self.driver,"addtonew_foldername_exist.jpg")

    def test_addPaper_title_isNull_run8(self):
        '''添加论文-题名为空'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        sleep(5)
        me.input_paperInfo(title="",author="李硕",content="添加至已存在文件夹测试成功")
        sleep(2)
        me.click_startCheck()
        sleep(2)
        self.assertEqual(me.title_error_remind(),"这是必填字段")
        print("题名为空测试成功")

    def test_addPaper_author_isNull_run9(self):
        '''添加论文-作者为空'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        sleep(5)
        me.input_paperInfo(title="野火烧不尽",author="",content="添加至已存在文件夹测试成功")
        sleep(2)
        me.click_startCheck()
        sleep(2)
        self.assertEqual(me.author_error_remind(),"这是必填字段")
        print("作者为空测试成功")

    def test_addPaper_content_isNull_run10(self):
        '''添加论文-内容为空'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        sleep(5)
        me.input_paperInfo(title="野火烧不尽",author="李硕",content="")
        sleep(2)
        me.click_startCheck()
        sleep(2)
        self.assertEqual(me.content_error_remind(),"这是必填字段")
        print("文本内容为空测试成功")

    def test_addPaper_title_more50_run11(self):
        '''添加论文-题名超过50位字符'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        sleep(5)
        me.paper_title("策划项目规划管理服务，并输出策划决策分析报告。策划决策分析服务实现基于模板决策分析和自定义决策分析两种")
        #me.input_paperInfo(title="策划项目规划管理服务，并输出策划决策分析报告。策划决策分析服务实现基于模板决策分析和自定义决策分析两种",author="李硕",content="添加至已存在文件夹测试成功")
        me.paper_author("")
        sleep(2)
        me.click_startCheck()
        sleep(2)
        self.assertEqual(me.get_title_remind(),"题名长度不能大于50个字符")
        print("题名不能超过50字符测试成功")

    def test_addPaper_author_more30_run12(self):
        '''添加论文-作者名超过30位字符'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        sleep(5)
        me.paper_title("策划项目规划管理服务")
        me.paper_author("策划项目规划管理服务，并输出策划决策分析报告。策划决策分析服务")
        me.paper_content("")
        sleep(2)
        me.click_startCheck()
        sleep(2)
        self.assertEqual(me.get_author_remind(),"作者名称不能大于30个字符")
        print("作者不能超过30字符测试成功")


    def test_addPaper_content_more20W_run14(self):
        '''文本内容超过20W'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        sleep(5)
        me.paper_title("野火烧不尽")
        me.paper_author("李硕")
        sleep(2)
        me.readAndInputContent("text.txt")
        sleep(5)
        me.click_startCheck()
        sleep(15)
        self.assertEqual(me.verifyExistAlert(),"文本长度大于20万字")
        print("文本不能超过20W字符测试成功")

    def test_clearPaper_run13(self):
        '''清空文本'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        sleep(5)
        me.paper_title("野火烧不尽")
        me.paper_author("李硕")
        me.paper_content("策划项目规划管理服务，并输出策划决策分析报告。策划决策分析服务")
        sleep(2)
        me.click_clearPaper()
        sleep(2)
        me.click_startCheck()
        sleep(2)
        self.assertEqual(me.content_error_remind(),"这是必填字段","没有清空文本")
        print("清空文本测试成功")

    def test_startCheck_lookresult(self):
        '''开始检测-跳转到检测信息页'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        sleep(5)
        me.input_paperInfo(title="泥石流",author="李硕",content="添加至已存在文件夹测试成功")
        sleep(2)
        me.click_startCheck()
        sleep(2)
        me.jump_checkInfo()
        sleep(5)
        self.assertEqual(me.checkInfo_title(),"泥石流")

    def test_startCheck_continue(self):
        '''开始检测-继续检测论文'''
        me=ManualEnterPaperCheck(self.driver)
        self.user_login()
        sleep(5)
        me.input_paperInfo(title="泥石流",author="李硕",content="添加至已存在文件夹测试成功")
        sleep(2)
        me.click_startCheck()
        sleep(2)
        me.continue_check()
        sleep(2)
        self.assertEqual(me.paperCheck_window(),"新论文相似性检测")














