#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-16 08:28:19
# @Author  : Nxy
# @Site    : 
# @File    : run_titlePapersCheck.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
from time import sleep
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox
from testCase.models.userVer.userVer import UserVer
from testCase.models.paperCheck.titlePapersCheck import TitlePapersCheck
from testResult.getResultImage import getResultImage


class RunTitlePapersCheck(myUnitChrome.UnitChrome):

    def user_login(self):
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("alcheck","f")
        sleep(2)
        tpc=TitlePapersCheck(self.driver)
        tpc.in_PaperCheck()
        sleep(5)
        tpc.in_titlePaperCheck()
        sleep(10)

    def file_upload(self,filename):
        '''直接上传，不添加到文件夹'''
        #登录系统
        self.user_login()
        sleep(10)
        tpc=TitlePapersCheck(self.driver)
        tpc.clickUpLoad()
        sleep(2)
        tpc.uploadFile_para("chrome",tpc.getFilePath(filename))

    def test_click_movetofolder_run(self):
        '''点击添加论文至分类文件夹，弹出添加文件夹窗口'''
        tpc=TitlePapersCheck(self.driver)
        self.user_login()
        tpc.add_to_folder_button()
        sleep(5)
        verify_addfolder = tpc.folder_windowconfirm()
        self.assertEqual(verify_addfolder,"确定","添加至文件夹窗口未弹出")
        print("添加到文件夹窗口弹出成功")

        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"click_addtofolder.jpg")

    def test_moveto_existfolder_run(self):
        '''添加至已有文件夹，显示文件夹名称'''
        tpc=TitlePapersCheck(self.driver)
        self.user_login()
        tpc.add_to_folder_button()
        sleep(5)
        #选择已存在的文件夹
        tpc.choose_existfolder()
        sleep(2)
        #获取选择文件夹的名称
        choose_name=tpc.get_existfolder_text()
        sleep(2)
        #单击确定按钮
        tpc.click_confirm_button()
        show_name=tpc.get_choosefolder_text()
        self.assertEqual(show_name,choose_name,"添加至已存在文件夹失败")
        print("添加至已存在文件夹测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"moveto_existfolder.jpg")

    def test_modifyto_existfolder_run(self):
        '''修改至已有文件夹，显示文件夹名称'''
        tpc=TitlePapersCheck(self.driver)
        self.user_login()
        tpc.add_to_folder_button()
        sleep(5)
         #选择已存在的文件夹
        tpc.choose_existfolder()
        sleep(2)
        #单击确定按钮
        tpc.click_confirm_button()
        sleep(2)
        #单击修改按钮
        tpc.modify_choosefolder_button()
        sleep(2)
        tpc.modify_existfolder()
        sleep(2)
        #获取选择文件夹的名称
        modify_name=tpc.modify_existfolder_text()
        sleep(2)
        #单击确定按钮
        tpc.modify_confirm_button()
        sleep(2)
        show_name=tpc.get_choosefolder_text()
        self.assertEqual(show_name,modify_name,"修改至已存在文件夹失败")
        print("修改文件夹测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"modifyto_existfolder.jpg")

    def test_add_foldername_success_run(self):
        '''添加至新文件夹成功'''
        tpc=TitlePapersCheck(self.driver)
        self.user_login()

        foldername=tpc.add_to_new_folder()
        sleep(2)

        show_name=tpc.get_choosefolder_text()
        sleep(2)
        self.assertEqual(show_name,foldername,"添加至新建文件夹失败")
        print("添加至新建文件夹测试成功！")

        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"add_foldername_success.jpg")

    def test_add_foldername_overlength_run(self):
        '''添加至新文件夹时，名称超长'''
        tpc=TitlePapersCheck(self.driver)
        self.user_login()
        sleep(2)
        tpc.add_to_new_folder_custom("长度的测试长度的测试长度的测试12")
        error_info=tpc.create_error_remind()
        self.assertEqual(error_info,"文件夹名称最长为16位，请重新输入！","文件夹名称超长未提示")
        print("新建文件夹名称不能过长测试成功！")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"add_foldername_overlength.jpg")

    def test_add_foldername_isnull_run(self):
        '''添加至新文件夹时，名称为空'''
        tpc=TitlePapersCheck(self.driver)
        self.user_login()
        sleep(2)
        tpc.add_to_new_folder_custom("")
        error_info=tpc.create_error_remind()
        self.assertEqual(error_info,"文件夹名称不能为空","文件夹名称为空未提示")
        print("新建文件夹名称不能为空测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"add_foldername_isnull.jpg")

    def test_add_foldername_exist_run(self):
        '''添加至新文件夹时，名称已存在'''
        tpc=TitlePapersCheck(self.driver)
        self.user_login()
        sleep(2)
        #添加至新文件夹
        foldername=tpc.add_to_new_folder()
        #upc.moveFolder()
        tpc.modify_choosefolder_button()
        #单击添加到新文件夹
        tpc.add_newfolder_button()
        sleep(2)
        #获取输入的文件夹名称
        tpc.input_new_foldername(foldername)
        sleep(2)
        #单击确定按钮
        tpc.modify_confirm_button1()
        sleep(2)
        error_info = tpc.create_error_remind()
        self.assertEqual(error_info,"文件夹已存在！","名称重复未提示")
        print("新建文件夹名称不能重复测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"add_foldername_duplication.jpg")

    def test_uploadpaper_incomplete_run(self):
        '''上传信息不完整'''
        self.file_upload("detect_file_rtf.rtf")
        tpc=TitlePapersCheck(self.driver)
        sleep(10)
        tpc.startCheck_button()
        sleep(2)
        self.assertEqual(tpc.supply_incompletePaper_remind(),"请将已有论文补充完整！","论文信息完整")
        print("论文信息不完整测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uploadpaper_incomplete.jpg")

    def test_uploadpaper_complete_jump_run(self):
        '''上传信息完整,检测，跳转到检测信息页'''
        self.file_upload("detect_file_txt.txt")
        tpc=TitlePapersCheck(self.driver)
        sleep(10)
        tpc.supply_paperInfo(title="detect_file_txt.txt",author="齐小明",source="北京农学院学报")
        sleep(2)
        tpc.startCheck_button()
        sleep(2)
        text1=tpc.get_check_content
        text2="您的检测命令已提交至系统，系统需要一些时间完成检测任务，在此期间您可以关闭浏览器等待检测，再次登录系统时可在检测信息页查看您的检测结果！"

        if text1 == text2:
            tpc.jump_checkInfo()
            sleep(2)
            self.assertEqual(tpc.jump_checkpaper_remind(),"detect_file_txt.txt","没有跳转到检测信息页面")
            print("跳转到检测信息页测试成功")
        else:
            tpc.continue_checked()
            sleep(5)
            tpc.jump_checkInfo()
            sleep(5)
            self.assertEqual(tpc.jump_checkpaper_remind(),"detect_file_txt.txt","没有跳转到检测信息页面")
            print("跳转到检测信息页测试成功")


        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uploadpaper_complete_jump.jpg")

    def test_uploadpaper_complete_continue_run(self):
        '''上传信息完整,检测，继续检测'''

        self.file_upload("detect_file_txt.txt")
        tpc=TitlePapersCheck(self.driver)
        sleep(10)
        tpc.supply_paperInfo(title="detect_file_txt.txt",author="齐小明",source="北京农学院学报")
        sleep(2)
        tpc.startCheck_button()
        sleep(2)
        text1=tpc.get_check_content()
        text2="您的检测命令已提交至系统，系统需要一些时间完成检测任务，在此期间您可以关闭浏览器等待检测，再次登录系统时可在检测信息页查看您的检测结果！"

        if text1 == text2:
            tpc.continue_checkpaper()
            sleep(2)
            self.assertEqual(tpc.continue_checkpaper_remind(),"职称论文相似性检测","没有留在论文检测页面")
            print("继续送检论文测试成功")

        else:
            tpc.continue_checked()
            sleep(5)
            tpc.continue_checkpaper()
            sleep(2)
            self.assertEqual(tpc.continue_checkpaper_remind(),"职称论文相似性检测","没有留在论文检测页面")
            print("继续送检论文测试成功")

        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uploadpaper_complete_continue.jpg")

    def test_stopcheck_tested_run(self):
        '''停止检测已经检测过的论文'''
        self.file_upload("detect_file_txt.txt")
        tpc=TitlePapersCheck(self.driver)
        sleep(10)
        tpc.supply_paperInfo(title="detect_file_txt.txt",author="齐小明",source="北京农学院学报")
        sleep(2)
        tpc.startCheck_button()
        sleep(2)
        print(tpc.get_check_content)
        tpc.stop_checked()
        sleep(2)
        self.assertEqual(tpc.continue_checkpaper_remind(),"职称论文相似性检测","没有留在论文检测页面")
        print("停止检测已检测过的论文")

    def test_fileSubmit_fail_run(self):
        '''上传文件解析失败'''
        self.file_upload("extract_fail.doc")
        tpc=TitlePapersCheck(self.driver)
        sleep(10)
        self.assertEqual(tpc.get_check_content(),"文件格式不正确，请上传 .doc、.docx、.txt、.pdf、.rtf 格式文件")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"fileSubmit_fail.jpg")

    def test_detect_big_fail_run(self):
        '''上传文件超过30M'''
        self.file_upload("uploadfile_over30m.pdf")
        tpc=TitlePapersCheck(self.driver)
        sleep(10)
        self.assertEqual(tpc.get_check_content(),"上传失败 文件大小超过限制( 30MB )")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"detect_big_fail.jpg")

    def test_detect_Empty_fail_run(self):
        '''文件大小为0'''
        self.file_upload("uploadfile_blank.docx")
        tpc=TitlePapersCheck(self.driver)
        sleep(10)
        self.assertEqual(tpc.get_check_content(),"上传失败 文件大小为0")
        print("空文件不允许上传测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"fileEmpty_fail.jpg")

    def test_uploadfile_pdf_run(self):
        '''上传PDF格式的文件'''
        self.file_upload("detect_file_pdf.pdf")
        tpc=TitlePapersCheck(self.driver)
        sleep(10)
        self.assertEqual(tpc.paper_title(),"detect_file_pdf.pdf")
        print("pdf上传测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uploadfile_PDF.jpg")

    def test_uploadfile_rtf_run(self):
        '''上传rtf格式的文件'''
        self.file_upload("detect_file_rtf.rtf")
        tpc=TitlePapersCheck(self.driver)
        sleep(10)
        self.assertEqual(tpc.paper_title(),"detect_file_rtf.rtf")
        print("rtf上传测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uploadfile_rtf.jpg")


    def test_uploadfile_doc_run(self):
        '''上传doc格式的文件'''
        self.file_upload("detect_file_doc.doc")
        tpc=TitlePapersCheck(self.driver)
        sleep(10)
        self.assertEqual(tpc.paper_title(),"detect_file_doc.doc")
        print("doc上传测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uploadfile_doc.jpg")

    def test_uploadfile_docx_run(self):
        '''上传docx格式的文件'''
        self.file_upload("detect_file_docx.docx")
        tpc=TitlePapersCheck(self.driver)
        sleep(10)
        self.assertEqual(tpc.paper_title(),"detect_file_docx.docx")
        print("docx上传测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uploadfile_docx.jpg")


    def test_clearPaper_run(self):
        '''清空文本'''
        self.file_upload("detect_file_rtf.rtf")
        tpc=TitlePapersCheck(self.driver)
        sleep(10)
        #tpc.startCheck_button()
        #sleep(2)
        tpc.clearPaper_button()
        text=tpc.paper_title()
        self.assertEqual(text,"","论文清空失败")
        print("论文清空测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"clearPaper.jpg")

    def test_delete_uploaded_run(self):
        '''删除已上传的论文'''
        self.file_upload("detect_file_doc.doc")
        tpc=TitlePapersCheck(self.driver)
        sleep(10)
        tpc.supply_paperInfo(title="detect_file_doc.doc",author="陶爱文",source="国家开放大学")
        sleep(2)
        tpc.continue_addPaper_button()
        sleep(2)
        tpc.deletePaper_button()
        sleep(2)
        self.assertEqual(tpc.paper_title(),"","删除失败")
        print("删除上传的论文成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"delete_uploaded.jpg")

    def test_continue_addPaper_run(self):
        '''继续上传论文'''
        self.file_upload("detect_file_doc.doc")
        tpc=TitlePapersCheck(self.driver)
        sleep(10)
        tpc.supply_paperInfo(title="detect_file_doc.doc",author="陶爱文",source="国家开放大学")
        sleep(2)
        tpc.continue_addPaper_button()
        sleep(2)
        print(tpc.paper_title())
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"continue_addPaper.jpg")

    def test_Inputcontent_toomuch_run(self):
        '''粘贴文本不能超过20万字'''
        self.user_login()
        tpc=TitlePapersCheck(self.driver)
        tpc.supply_paperInfo(title="big_text.txt",author="陶爱文",source="国家开放大学")
        tpc.readAndInputContent("big_text.txt")

        sleep(10)
        tpc.startCheck_button()
        self.assertEqual(tpc.get_check_content(),"文本内容不能超过20W字符！")
        print("文本内容不能超过20W字测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"Inputcontent_toomuch.jpg")


    def test_Inputcontent_less20W_run(self):
        '''粘贴文本少于20万字'''
        self.user_login()
        tpc=TitlePapersCheck(self.driver)
        tpc.supply_paperInfo(title="less20W.txt",author="陶爱文",source="国家开放大学")
        tpc.readAndInputContent("less20W.txt")

        sleep(10)
        tpc.startCheck_button()
        text1=tpc.get_check_content
        text2="您的检测命令已提交至系统，系统需要一些时间完成检测任务，在此期间您可以关闭浏览器等待检测，再次登录系统时可在检测信息页查看您的检测结果！"
        self.assertEqual(text1,text2,"文本少于20W字检测不成功")
        print("文本内容少于20W字测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"Inputcontent_less20W.jpg")

    def test_searchPaper_author_run(self):
        '''作者-查找论文'''
        self.user_login()
        tpc=TitlePapersCheck(self.driver)
        tpc.addPaper_author("李硕")
        sleep(2)
        tpc.search_paper_button()
        sleep(2)
        tpc.choose_firstPaper()
        sleep(2)
        tpc.choose_confirm_button()
        sleep(5)
        text="该论文无收稿日期，该日期为万方数据默认发表日期，为确保检测结果的准确性，建议将日期提前1-3个月进行检测。"
        self.assertEqual(tpc.get_check_content(),text,"论文选中不成功")
        print("查找论文并选中成功")

    def test_searchPaper_author_notexist_run(self):
        '''作者-查找论文-未收录'''
        self.user_login()
        tpc=TitlePapersCheck(self.driver)
        tpc.addPaper_author("刚讽德诵功")
        sleep(2)
        tpc.search_paper_button()
        sleep(2)
        tpc.choose_firstPaper()
        sleep(2)
        tpc.choose_confirm_button()
        sleep(5)
        text="您的文献未在本数据库收录，请粘贴或上传文献进行检测！"
        self.assertEqual(tpc.get_check_content(),text,"论文选中不成功")
        print("查找论文并选中成功")

    def test_searchPaper_title_run(self):
        '''题名-查找论文'''
        self.user_login()
        tpc=TitlePapersCheck(self.driver)
        tpc.addPaper_title("泥石流")
        sleep(2)
        tpc.search_paper_button()
        sleep(2)
        tpc.choose_firstPaper()
        sleep(2)
        tpc.choose_confirm_button()
        sleep(5)
        text="该论文无收稿日期，该日期为万方数据默认发表日期，为确保检测结果的准确性，建议将日期提前1-3个月进行检测。"
        self.assertEqual(tpc.get_check_content(),text,"论文选中不成功")
        print("查找论文并选中成功")

    def test_searchPaper_title_notexist_run(self):
        '''题名-查找论文-未收录'''
        self.user_login()
        tpc=TitlePapersCheck(self.driver)
        tpc.addPaper_title("刚讽德诵功")
        sleep(2)
        tpc.search_paper_button()
        sleep(2)
        tpc.choose_firstPaper()
        sleep(2)
        tpc.choose_confirm_button()
        sleep(5)
        text="您的文献未在本数据库收录，请粘贴或上传文献进行检测！"
        self.assertEqual(tpc.get_check_content(),text,"论文选中不成功")
        print("查找论文并选中成功")

    def test_searchPaper_source_notexist_run(self):
        '''来源-查找论文-未收录'''
        self.user_login()
        tpc=TitlePapersCheck(self.driver)
        tpc.addPaper_source("期刊论文")
        sleep(2)
        tpc.search_paper_button()
        sleep(2)
        tpc.choose_firstPaper()
        sleep(2)
        tpc.choose_confirm_button()
        sleep(5)
        text="您的文献未在本数据库收录，请粘贴或上传文献进行检测！"
        self.assertEqual(tpc.get_check_content(),text,"论文选中不成功")
        print("查找论文并选中成功")

    def test_searchPaper_source_run(self):
        '''来源-查找论文'''
        self.user_login()
        tpc=TitlePapersCheck(self.driver)
        tpc.addPaper_source("计算机应用")
        sleep(2)
        tpc.search_paper_button()
        sleep(2)
        tpc.choose_firstPaper()
        sleep(2)
        tpc.choose_confirm_button()
        sleep(5)
        text="该论文无收稿日期，该日期为万方数据默认发表日期，为确保检测结果的准确性，建议将日期提前1-3个月进行检测。"
        self.assertEqual(tpc.get_check_content(),text,"论文选中不成功")
        print("查找论文并选中成功")

    def test_searchPaper_datetime_run(self):
        '''收稿日期-查找论文'''
        self.user_login()
        tpc=TitlePapersCheck(self.driver)
        tpc.paper_datetime()
        sleep(2)
        tpc.search_paper_button()
        sleep(2)
        tpc.choose_firstPaper()
        sleep(2)
        tpc.choose_confirm_button()
        sleep(5)
        text="请输入作者、题名或来源进行查找！"
        self.assertEqual(tpc.get_check_content(),text)
        print("查找论文并选中成功")

    def test_searchPaper_allInfo_run(self):
        '''查找论文-所有条件'''
        self.user_login()
        tpc=TitlePapersCheck(self.driver)
        tpc.supply_paperInfo(title="野火烧不尽",author="李硕",source="艺术科技")
        sleep(2)
        tpc.search_paper_button()
        sleep(2)
        tpc.choose_firstPaper()
        sleep(2)
        tpc.choose_confirm_button()
        sleep(5)
        text="该论文无收稿日期，该日期为万方数据默认发表日期，为确保检测结果的准确性，建议将日期提前1-3个月进行检测。"
        self.assertEqual(tpc.get_check_content(),text)
        print("查找论文并选中成功")

    def test_searchPaper_continueCheck_run(self):
        '''查找论文-检测之后继续上传'''
        self.user_login()
        tpc=TitlePapersCheck(self.driver)
        tpc.supply_paperInfo(title="",author="李硕",source="")
        sleep(2)
        tpc.search_paper_button()
        sleep(2)
        tpc.choose_firstPaper()
        sleep(2)
        tpc.choose_confirm_button()
        sleep(2)
        tpc.continue_checked()
        sleep(2)
        tpc.startCheck_button()
        sleep(5)
        text1=tpc.get_check_content()
        text2="您的检测命令已提交至系统，系统需要一些时间完成检测任务，在此期间您可以关闭浏览器等待检测，再次登录系统时可在检测信息页查看您的检测结果！"

        if text1 == text2:
            tpc.continue_checkpaper()
            sleep(2)
            self.assertEqual(tpc.continue_checkpaper_remind(),"职称论文相似性检测","没有留在论文检测页面")
            print("继续送检论文测试成功")

        else:
            tpc.continue_checked()
            sleep(5)
            tpc.continue_checkpaper()
            sleep(2)
            self.assertEqual(tpc.continue_checkpaper_remind(),"职称论文相似性检测","没有留在论文检测页面")
            print("继续送检论文测试成功")


    def test_batch_uploadPaper_run(self):
        '''批量上传论文进行检测'''
        self.file_upload("detect_file_doc.doc")
        tpc=TitlePapersCheck(self.driver)
        sleep(10)
        tpc.supply_paperInfo(title="detect_file_doc.doc",author="陶爱文",source="国家开放大学")
        sleep(2)
        #单击继续添加论文
        tpc.continue_addPaper_button()
        sleep(10)
        tpc.lookForPaper_upload()
        sleep(5)
        print("添加第2篇成功")
        tpc.lookForPaper_upload1()
        sleep(5)
        print("添加第3篇成功")
        #单击开始检测按钮
        tpc.start_batch_check()

        sleep(5)
        text1=tpc.get_check_content()
        text2="您的检测命令已提交至系统，系统需要一些时间完成检测任务，在此期间您可以关闭浏览器等待检测，再次登录系统时可在检测信息页查看您的检测结果！"

        if text1 == text2:
            tpc.continue_checkpaper()
            sleep(2)
            self.assertEqual(tpc.continue_checkpaper_remind(),"职称论文相似性检测","没有留在论文检测页面")
            print("批量检测测试成功")

        else:
            tpc.continue_checked()
            sleep(5)
            tpc.continue_checkpaper()
            sleep(2)
            self.assertEqual(tpc.continue_checkpaper_remind(),"职称论文相似性检测","没有留在论文检测页面")
            print("批量检测论文测试成功")


    def test_batch_uploadPaper_more10_run(self):
        '''批量上传论文-添加10篇不能继续添加'''
        self.file_upload("detect_file_doc.doc")
        tpc=TitlePapersCheck(self.driver)
        sleep(10)
        tpc.supply_paperInfo(title="detect_file_doc.doc",author="陶爱文",source="国家开放大学")
        sleep(2)
        #单击继续添加论文
        tpc.continue_addPaper_button()
        print("添加第1篇成功")
        sleep(10)
        tpc.lookForPaper_upload()
        sleep(5)
        print("添加第2篇成功")
        tpc.lookForPaper_upload1()
        sleep(5)
        print("添加第3篇成功")

        tpc.lookForPaper_upload2()
        sleep(5)
        print("添加第4篇成功")

        tpc.lookForPaper_upload3()
        sleep(5)
        print("添加第5篇成功")
        tpc.lookForPaper_upload4()
        sleep(5)
        print("添加第6篇成功")
        tpc.lookForPaper_upload5()
        sleep(5)
        print("添加第7篇成功")
        tpc.lookForPaper_upload6()
        sleep(2)
        print("添加第8篇成功")
        tpc.lookForPaper_upload7()
        sleep(2)
        print("添加第9篇成功")
        tpc.lookForPaper_upload8()
        sleep(2)
        print("添加第10篇成功")
        self.assertEqual(tpc.max_uploadPaper(),"待检测论文已到10篇，无法添加新论文","超过十篇依旧可以上传")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"batch_uploadPaper_more10.jpg")



















