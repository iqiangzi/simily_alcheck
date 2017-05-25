#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-16 08:28:19
# @Author  : Nxy
# @Site    : 
# @File    : newPaperCheck.py
# @Software: PyCharm
from selenium import webdriver
import unittest
from testCase.pageObj.basePage import BasePage
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from util.commonUtils.clickButton import ClickButton
from util.toolUtils.getPath import GetPath
import os
import time
class UpLoadPaperCheck(BasePage):
    '''新论文检测'''
    #进入论文检测模块
    in_paperCheck_button_loc=(By.ID,"paperCheck")
    #进入新论文相似性检测
    in_newPaperCheck_loc=(By.XPATH,"html/body/div[1]/aside/div/section/ul/li[3]/ul/li[1]/a")
    #本地上传按钮
    upload_button_loc=(By.XPATH,".//*[@id='file_upload']")

    #上传前选择待检测论文要放入的文件夹
    upload_moveFolder_button=(By.ID,"up_move")
    #添加到文件夹窗口确定按钮
    addfolder_windowconfirm_loc=(By.XPATH,".//*[@id='layui-layer1']/div[3]/a[1]")
    #修改文件夹确定按钮
    modifyfolder_confirm=(By.XPATH,".//*[@id='layui-layer2']/div[3]/a[1]")
    modifyfolder_confirm1=(By.XPATH,".//*[@id='layui-layer3']/div[3]/a[1]")
    #添加到新文件夹
    add_newfolder=(By.CSS_SELECTOR,"#radio1")
    #添加至已有文件夹
    add_existfolder_button=(By.XPATH,".//*[@id='radio2']")
    #选择已有文件夹中的一个
    existfolder=(By.XPATH,".//*[@id='selDir']/option[2]")
    existfolder1=(By.XPATH,".//*[@id='selDir']/option[3]")
    defaultfolder=(By.XPATH,".//*[@id='selDir']/option[1]")
    #获取已选择文件夹的名称
    choosefolder=(By.XPATH,".//*[@id='hasSelDir']")
    #修改已选择的文件夹
    modify_folder=(By.XPATH,".//*[@id='showSel']/a")

    #新建文件夹输入框
    createfolder=(By.XPATH,".//*[@id='inpDir']")
    #新建文件夹错误信息提示
    create_newfolder_error=(By.XPATH,".//*[@id='errmsg']")






    #上传状态-成功或失败
    upload_status_loc=(By.XPATH,".//*[@id='result']/tbody/tr/td[5]/span")
    #文本提取错误
    fileSubmit_fail_remind=(By.XPATH,".//*[@id='result']/tbody/tr/td[6]")
    #单个删除论文
    singledelete_button_loc=(By.XPATH,".//*[@id='result']/tbody/tr/td[7]/div/a[1]")
    #确认删除按钮
    delete_singleconfirm=(By.XPATH,".//*[@id='layui-layer1']/div[3]/a[1]")
    cancel_delete=(By.XPATH,".//*[@id='layui-layer1']/div[3]/a[2]")
    #删除成功
    delete_success=(By.XPATH,".//*[@id='result']/tbody/tr/td")


    #论文全选按钮
    selectAll_button=(By.XPATH,".//*[@id='result']/thead/tr/th[1]/input")
    #more按钮
    more_button=(By.XPATH,".//*[@id='targetStep4']")
    #删除多个论文
    more_deleteFile_button=(By.XPATH,"html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/div[1]/div/ul/li/a")
    #下载原文
    download_original_button=(By.XPATH,".//*[@id='result']/tbody/tr/td[7]/div/a[2]")
    #文件名
    fileName=(By.XPATH,".//*[@id='result']/tbody/tr/td[3]")

    #开始检测按钮
    startCheck_button_loc=(By.ID,"step6")
    #跳转到检测信息页
    jump_checkInfo_button=(By.XPATH,".//*[@id='layui-layer1']/div[3]/a[1]")
    #继续检测论文
    continue_checkpapar_button=(By.XPATH,".//*[@id='layui-layer1']/div[3]/a[2]")
    #检测信息页题名/作者名
    #checkInfo_title=(By.XPATH,"html/body/div[1]/div[1]/section/ol/li")
    checkInfo_title=(By.XPATH,".//*[@id='result']/tbody/tr[1]/td[4]")
    checkinfo_author=(By.XPATH,".//*[@id='result']/tbody/tr[1]/td[3]")
    #新论文检测页面导航
    newPaparcheck_title=(By.XPATH,"html/body/div[1]/div[1]/section/ol/li[2]")



    #进入论文检测模块
    def in_PaperCheck(self):
        self.find_element(*self.in_paperCheck_button_loc).click()
    #进入新论文相似性检测模块
    def in_newPaperCheck(self):
        self.find_element(*self.in_newPaperCheck_loc).click()

    #上传前选择待检测论文要放入的文件夹
    def moveFolder(self):
        self.find_element(*self.upload_moveFolder_button).click()
    #单击确定按钮
    def click_confirm_button(self):
        self.find_element(*self.addfolder_windowconfirm_loc).click()
    #获取文件夹页面的确定按钮文本
    def folder_windowconfirm(self):
        return self.find_element(*self.addfolder_windowconfirm_loc).text
    #选择已有文件夹
    def choose_existfolder(self):
       self.find_element(*self.existfolder).click()
    #获取已存在文件夹的文本
    def get_existfolder_text(self):
        return self.find_element(*self.existfolder).text
    #修改已存在的文件夹名称
    def modify_existfolder_text(self):
        return self.find_element(*self.existfolder1).text
    #修改到已存在文件夹
    def modify_existfolder(self):
        self.find_element(*self.existfolder1).click()
    #修改文件夹按钮
    def modify_choosefolder_button(self):
        self.find_element(*self.modify_folder).click()
    #修改文件夹确定按钮
    def modify_confirm_button(self):
        self.find_element(*self.modifyfolder_confirm).click()
    def modify_confirm_button1(self):
        self.find_element(*self.modifyfolder_confirm1).click()
    #默认文件夹
    def get_defaultfolder_text(self):
        return self.find_element(*self.defaultfolder).text

    #获取已选择文件夹的名称
    def get_choosefolder_text(self):
        return self.find_element(*self.choosefolder).text
    #添加到新文件夹
    def add_newfolder_button(self):
        self.find_element(*self.add_newfolder).click()
    #创建新文件夹
    def input_new_foldername(self,foldername):
        self.find_element(*self.createfolder).clear()
        self.find_element(*self.createfolder).send_keys(foldername)
        return foldername
    #创建文件夹错误提示
    def create_error_remind(self):
        return self.find_element(*self.create_newfolder_error).text

    #输入新文件夹名称
    def input_new_foldername1(self):
        date = time.strftime("%Y%m%d%H%M")
        folder_name = "%sFile"%(date)
        self.find_element(*self.createfolder).send_keys(folder_name)
        return folder_name

    #添加至新文件夹过程
    def add_to_new_folder(self):
        #单击移动到文件夹
        self.moveFolder()
        sleep(2)
        #单击添加到新文件夹
        self.add_newfolder_button()
        sleep(2)
        #获取输入的文件夹名称
        text = self.input_new_foldername1()
        sleep(2)
        #单击确定按钮
        self.click_confirm_button()
        sleep(2)
        return text



    #添加至新文件夹过程自定义
    def add_to_new_folder_custom(self,foldername):
        self.moveFolder()
        sleep(5)
        self.add_newfolder_button()
        sleep(5)
        text = self.input_new_foldername(foldername)
        sleep(5)
        self.click_confirm_button()
        sleep(2)
        return text





    #获取上传状态信息
    def upload_status_remind(self):
        return self.find_element(*self.upload_status_loc).text
    def filesubmit_remind(self):
        return self.find_element(*self.fileSubmit_fail_remind).text
    #删除单个论文
    def delete_singlefile_button(self):
        self.find_element(*self.singledelete_button_loc).click()
    def delete_singlefile_confirm(self):
        self.find_element(*self.delete_singleconfirm).click()
    def delete_success_remind(self):
        return self.find_element(*self.delete_success).text


    #全选按钮
    def selectAllPaper_button(self):
        self.find_element(*self.selectAll_button).click()
    #MORE按钮
    def moreopration_button(self):
        self.find_element(*self.more_button).click()
    #删除选中论文按钮
    def delete_selectedfile(self):
        self.find_element(*self.more_deleteFile_button).click()

    #下载原文
    def download_originalfile(self):
        self.find_element(*self.download_original_button).click()
    #获取文件名
    def paperName(self):
        return self.find_element(*self.fileName).text
    #开始检测按钮
    def start_checkPaper(self):
        self.find_element(*self.startCheck_button_loc).click()

    #继续检测论文
    def continue_checkpaper(self):
        self.find_element(*self.continue_checkpapar_button).click()
    #跳转到检测信息页
    def jump_checkInfo(self):
        self.find_element(*self.jump_checkInfo_button).click()
    #继续检测论文提示
    def continue_checkpaper_remind(self):
        return self.find_element(*self.newPaparcheck_title).text
    #跳转到检测信息页-题名
    def jump_checkpaper_remind(self):
        return self.find_element(*self.checkInfo_title).text
    #检测信息页-作者名
    def checkInfo_author(self):
        return self.find_element(*self.checkinfo_author).text




    #判断是否有alert弹窗
    def verifyExistAlert(self):
        text = super(UpLoadPaperCheck,self).confirm_broserAlert()
        print(text)
        return text



    #点击插件按钮方法
    def clickUpLoad(self):
        click = ClickButton()
        #获取位置并点击
        #print(self.get_where())
        pos = (879, 320)
        click.click(click.get_win_handle(pos),pos)

    def get_where(self):
        click = ClickButton()
        above=self.find_element(*self.upload_button_loc)
        ActionChains(self.driver).move_to_element(above).perform()
        time.sleep(8)
        return click.get_curpos()


    #判断文件夹是否为空，不为空则重命名同名文件，以保证新下载的文件的唯一性。为空则直接下载
    def renameFileName(self):
        name=time.strftime("%Y-%m-%d %H_%M_%S")
        dir_path=GetPath().getAbsoluteDirPath("downloadFiles")
        if os.listdir(dir_path):
            text=self.paperName()
            os.rename(dir_path+"/"+text,dir_path+r"\%s.doc"%(name))
        else:
            pass

    def verifyExist1(self):
        #判断是否下载到本地,返回bool类型的True或False
        #判断文件是否存在
        dir_path=GetPath().getAbsoluteDirPath("downloadFiles")
        text=self.paperName()
        flag = os.path.exists(dir_path+"/"+text)
        return flag

    #调用autoit生成的exe，并传入浏览器、需要上传至页面文件的地址两个参数
    def uploadFile_para(self,browserName,filePath):
        #注意路径中不能存在空格并且文件夹名称不能过长
        ab_path = GetPath().getAbsoluteFilePath("testvb.exe",r"uploadApp\testvb.exe")

        os.system(ab_path+ " "+browserName+" "+filePath)

    #获取上传文件的绝对路径
    def getFilePath(self,filename):
        file_path = GetPath().getAbsoluteFilePath("%s"%filename,r"SubmitPaperTestData\%s"%filename)
        return file_path

    def choose_filefolder(self):
        self.find_element(*self.upload_moveFolder_button).click()







