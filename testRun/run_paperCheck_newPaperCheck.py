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
from testCase.models.paperCheck.newPaperCheck import UpLoadPaperCheck
from testResult.getResultImage import getResultImage

class RunNewPaperCheck(myUnitChrome.UnitChrome):

    def user_login(self):
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("alcheck","f")
        sleep(2)
        upc=UpLoadPaperCheck(self.driver)
        upc.in_PaperCheck()
        sleep(10)

    def file_upload(self,filename):
        '''直接上传，不添加到文件夹'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("alcheck","f")
        sleep(2)
        upc=UpLoadPaperCheck(self.driver)
        upc.in_PaperCheck()
        sleep(20)
        upc.clickUpLoad()
        sleep(2)
        upc.uploadFile_para("chrome",upc.getFilePath(filename))


    def test_download_originalfile_run(self):
        '''下载原文'''

        upc=UpLoadPaperCheck(self.driver)
        self.file_upload("detect_file_pdf.pdf")

        sleep(5)
        flag=upc.verifyExist1()
        if flag is True:
            upc.renameFileName()
            upc.download_originalfile()
            sleep(5)
            print("原文已存在，下载成功!")

        else:
            #单击导出按钮
            upc.download_originalfile()
            sleep(5)
            print("原文下载成功")
        print("下载原文测试成功!")
        #获取页面截图
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"download_originalfile.jpg")

    def test_fileSubmit_fail_run(self):
        '''文件提取失败'''
        upc=UpLoadPaperCheck(self.driver)
        self.file_upload("extract_fail.doc")
        sleep(15)
        self.assertEqual(upc.filesubmit_remind(),"文本提取错误")
        print("文本提交错误测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"fileSubmit_fail.jpg")

    def test_detect_Empty_fail_run(self):
        '''空文件不允许上传'''
        upc=UpLoadPaperCheck(self.driver)
        self.file_upload("uploadfile_blank.docx")
        sleep(10)
        alert_text = upc.verifyExistAlert()
        self.assertEqual(alert_text,u"上传失败\n文件大小为0")

        print("空文件不允许上传测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"fileEmpty_fail.jpg")

    def test_detect_big_fail_run(self):
        '''文件超过30M不允许上传'''
        upc=UpLoadPaperCheck(self.driver)
        self.file_upload("uploadfile_over30m.pdf")
        sleep(15)
        alert_text = upc.verifyExistAlert()
        self.assertEqual(alert_text,u"上传失败\n文件大小超过限制( 30MB )")
        print("文件超过30M不允许上传测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"fileupload_bigfail.jpg")

    def test_detect_PDF_continue_run(self):
        '''上传pdf文件，选择继续检测'''
        upc=UpLoadPaperCheck(self.driver)
        self.file_upload("detect_file_continue.pdf")
        sleep(10)
        upc.start_checkPaper()
        sleep(5)
        upc.continue_checkpaper()
        sleep(5)
        self.assertEqual(upc.continue_checkpaper_remind(),"新论文相似性检测","单击继续检测论文没有停留在上传页面")
        print("PDF继续检测成功")

        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"fileupload_PDF_continue.jpg")

    def test_detect_pdf_checkinfo_run(self):
        '''上传pdf文件，跳转到检测信息页'''
        upc=UpLoadPaperCheck(self.driver)
        self.file_upload("detect_file_pdf.pdf")
        sleep(10)
        upc.start_checkPaper()
        sleep(2)
        upc.jump_checkInfo()
        sleep(2)
        self.assertEqual(upc.jump_checkpaper_remind(),"detect_file_pdf.pdf","没有跳转到检测信息页")
        print("PDF跳转到检测信息页成功")

        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"fileupload_pdf_checkinfo.jpg")

    def test_detect_rtf_lookResult_run(self):
        '''选择rtf文件逐个选择跳转至检测结果页'''
        upc=UpLoadPaperCheck(self.driver)
        self.file_upload("detect_file_rtf.rtf")
        sleep(10)
        upc.start_checkPaper()
        sleep(2)
        upc.jump_checkInfo()
        sleep(2)
        self.assertEqual(upc.jump_checkpaper_remind(),"detect_file_rtf.rtf","没有跳转到检测信息页")
        print("rtf跳转到检测信息页成功")

        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"detect_rtf_lookResult.jpg")

    def test_detect_txt_lookResult_run(self):
        '''选择txt文件逐个选择跳转至检测结果页'''
        upc=UpLoadPaperCheck(self.driver)
        self.file_upload("detect_file_txt.txt")
        sleep(5)
        upc.start_checkPaper()
        sleep(2)
        upc.jump_checkInfo()
        sleep(2)
        self.assertEqual(upc.jump_checkpaper_remind(),"detect_file_txt.txt","没有跳转到检测信息页")
        print("txt跳转到检测信息页成功")

        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"detect_txt_lookResult.jpg")

    def test_detect_docx_lookResult_run(self):
        '''选择docx文件逐个选择跳转至检测结果页'''
        upc=UpLoadPaperCheck(self.driver)
        self.file_upload("detect_file_docx.docx")
        sleep(5)
        upc.start_checkPaper()
        sleep(2)
        upc.jump_checkInfo()
        sleep(2)
        self.assertEqual(upc.jump_checkpaper_remind(),"detect_file_docx.docx","没有跳转到检测信息页")
        print("docx跳转到检测信息页成功")

        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"detect_docx_lookResult.jpg")

    def test_detect_doc_lookResult_run(self):
        '''选择doc文件逐个选择跳转至检测结果页'''
        upc=UpLoadPaperCheck(self.driver)
        self.file_upload("detect_file_doc.doc")
        sleep(5)
        upc.start_checkPaper()
        sleep(5)
        upc.jump_checkInfo()
        sleep(5)
        self.assertEqual(upc.jump_checkpaper_remind(),"detect_file_doc.doc","没有跳转到检测信息页")
        print("doc跳转到检测信息页成功")

        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"detect_doc_lookResult.jpg")

    def test_detect_excel_lookResult_run(self):
        '''选择excel文件逐个选择跳转至检测结果页'''
        upc=UpLoadPaperCheck(self.driver)
        self.file_upload("excel_file_fail.xlsx")
        sleep(5)
        alert_text = upc.verifyExistAlert()
        self.assertEqual(alert_text,u"上传失败\n文件格式不正确，仅限 *.doc; *.docx; *.pdf; *.txt; *.rtf")
        print("excel测试成功")

        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"detect_doc_lookResult.jpg")

    def test_filename_format_run(self):
        '''测试上传文件名格式，在检测列表中提取的信息'''
        upc=UpLoadPaperCheck(self.driver)
        self.file_upload("李硕@相似性检测.doc")
        sleep(10)
        upc.start_checkPaper()
        sleep(3)
        upc.jump_checkInfo()
        sleep(3)
        self.assertEqual(upc.jump_checkpaper_remind(),"相似性检测","题名提取失败")
        #self.assertEqual(upc.checkInfo_author(),"李硕","作者提取失败")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"filename_format.jpg")

    def test_click_movetofolder_run(self):
        '''点击添加论文至分类文件夹，弹出添加文件夹窗口'''
        upc=UpLoadPaperCheck(self.driver)
        self.user_login()
        upc.moveFolder()
        sleep(5)
        verify_addfolder = upc.folder_windowconfirm()
        self.assertEqual(verify_addfolder,"确定","添加至文件夹窗口未弹出")
        #print("文件超过30M不允许上传测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"click_addtofolder.jpg")

    def test_moveto_existfolder_run(self):
        '''添加至已有文件夹，显示文件夹名称'''
        upc=UpLoadPaperCheck(self.driver)
        self.user_login()
        upc.moveFolder()
        sleep(5)
        #选择已存在的文件夹
        upc.choose_existfolder()
        sleep(2)
        #获取选择文件夹的名称
        choose_name=upc.get_existfolder_text()
        sleep(2)
        #单击确定按钮
        upc.click_confirm_button()
        show_name=upc.get_choosefolder_text()
        self.assertEqual(show_name,choose_name,"添加至已存在文件夹失败")
        print("添加至已存在文件夹测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"moveto_existfolder.jpg")


    def test_modifyto_existfolder_run(self):
        '''修改至已有文件夹，显示文件夹名称'''
        upc=UpLoadPaperCheck(self.driver)
        self.user_login()
        upc.moveFolder()
        sleep(5)
        #选择已存在的文件夹
        upc.choose_existfolder()
        sleep(2)
        #单击确定按钮
        upc.click_confirm_button()
        sleep(2)
        #单击修改按钮
        upc.modify_choosefolder_button()
        sleep(2)
        upc.modify_existfolder()
        sleep(2)
        #获取选择文件夹的名称
        modify_name=upc.modify_existfolder_text()
        sleep(2)
        #单击确定按钮
        upc.modify_confirm_button()
        sleep(2)
        show_name=upc.get_choosefolder_text()
        self.assertEqual(show_name,modify_name,"修改至已存在文件夹失败")
        print("修改文件夹测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"modifyto_existfolder.jpg")

    def test_add_foldername_success_run(self):
        '''添加至新文件夹成功'''
        upc=UpLoadPaperCheck(self.driver)
        self.user_login()
        sleep(2)
        foldername=upc.add_to_new_folder()
        sleep(2)

        show_name=upc.get_choosefolder_text()
        sleep(2)
        self.assertEqual(show_name,foldername,"添加至新建文件夹失败")
        print("添加至新建文件夹测试成功！")

        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"add_foldername_success.jpg")

    def test_add_foldername_overlength_run(self):
        '''添加至新文件夹时，名称超长'''
        upc=UpLoadPaperCheck(self.driver)
        self.user_login()
        sleep(2)
        upc.add_to_new_folder_custom("长度的测试长度的测试长度的测试12")
        error_info=upc.create_error_remind()
        self.assertEqual(error_info,"文件夹名称最长为16位，请重新输入！","文件夹名称超长未提示")
        print("新建文件夹名称不能过长测试成功！")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"add_foldername_overlength.jpg")

    def test_add_foldername_isnull_run(self):
        '''添加至新文件夹时，名称为空'''
        upc=UpLoadPaperCheck(self.driver)
        self.user_login()
        sleep(2)
        upc.add_to_new_folder_custom("")
        error_info=upc.create_error_remind()
        self.assertEqual(error_info,"文件夹名称不能为空","文件夹名称为空未提示")
        print("新建文件夹名称不能为空测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"add_foldername_isnull.jpg")

    def test_add_foldername_exist_run(self):
        '''添加至新文件夹时，名称已存在'''
        upc=UpLoadPaperCheck(self.driver)
        self.user_login()
        sleep(2)
        #添加至新文件夹
        foldername=upc.add_to_new_folder()
        #upc.moveFolder()
        upc.modify_choosefolder_button()
        #单击添加到新文件夹
        upc.add_newfolder_button()
        sleep(2)
        #获取输入的文件夹名称
        upc.input_new_foldername(foldername)
        sleep(2)
        #单击确定按钮
        upc.modify_confirm_button1()
        sleep(2)
        #upc.add_to_new_folder_custom(foldername)
        error_info = upc.create_error_remind()
        self.assertEqual(error_info,"文件夹已存在！","名称重复未提示")
        print("新建文件夹名称不能重复测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"add_foldername_duplication.jpg")

    def test_delete_singlePaper_run(self):
        '''删除一篇上传的论文'''
        upc=UpLoadPaperCheck(self.driver)
        self.file_upload("detect_file_pdf.pdf")

        sleep(10)
        #text=upc.paperName()
        upc.delete_singlefile_button()
        sleep(5)
        #单击确认删除
        upc.delete_singlefile_confirm()
        sleep(3)

        text=upc.delete_success_remind()
        self.assertEqual(text,"没有找到匹配的记录","删除失败")
        #self.assertEqual(text,"删除成功","删除失败")
        print("删除一篇论文测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"delete_singlePaper.jpg")

    def test_delete_selectedPaper_run(self):
        '''删除全选的论文'''
        upc=UpLoadPaperCheck(self.driver)
        self.file_upload("detect_file_pdf.pdf")

        sleep(5)
        #全选
        upc.selectAllPaper_button()
        sleep(3)
        #单击more
        upc.moreopration_button()
        sleep(3)
        #单击删除
        upc.delete_selectedfile()
        #单击确认删除
        upc.delete_singlefile_confirm()
        sleep(3)
        text=upc.delete_success_remind()
        self.assertEqual(text,"没有找到匹配的记录","删除失败")
        print("删除全部论文测试成功")
        sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"delete_selectedPaper.jpg")





















