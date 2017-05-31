#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-16 08:28:19
# @Author  : Nxy
# @Site    : 
# @File    : titlePapersCheck.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from testCase.pageObj.basePage import BasePage
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from util.commonUtils.clickButton import ClickButton
from util.toolUtils.getPath import GetPath
from util.commonUtils.fileOption import FilesOption
import os
import time

class TitlePapersCheck(BasePage):

    #进入论文检测模块
    in_paperCheck_button_loc=(By.ID,"paperCheck")
    #定位职称论文相似性检测
    titlepaper_module_loc=(By.XPATH,"html/body/div[1]/aside/div/section/ul/li[3]/ul/li[2]/a")
    #本地上传按钮
    upload_button_loc=(By.XPATH,".//*[@id='file_upload']")
    #上传前选择待检测论文要放入的文件夹
    upload_moveFolder_button=(By.ID,"isAddToFloder")



     #添加到新文件夹
    add_newfolder=(By.CSS_SELECTOR,"#radioinput")
    #添加至已有文件夹
    add_existfolder_button=(By.ID,"radioselect")

    #选择已有文件夹中的一个
    existfolder=(By.XPATH,".//*[@id='selDir']/option[2]")
    existfolder1=(By.XPATH,".//*[@id='selDir']/option[3]")


    #获取已选择文件夹的名称
    choosefolder=(By.XPATH,".//*[@id='hasSelect']")
    #修改已选择的文件夹
    modify_folder=(By.ID,"editFloder")
    #添加到文件夹确认按钮
    add_existfolder_confirm=(By.XPATH,".//*[@id='layui-layer1']/div[3]/a[1]")
    #修改文件夹确定按钮
    modifyfolder_confirm=(By.XPATH,".//*[@id='layui-layer2']/div[3]/a[1]")
    modifyfolder_confirm1=(By.XPATH,".//*[@id='layui-layer3']/div[3]/a[1]")


    #新建文件夹输入框
    createfolder=(By.XPATH,".//*[@id='inpDir']")
    #新建文件夹错误信息提示
    create_newfolder_error=(By.XPATH,".//*[@id='errmsg']")



    #开始检测按钮
    startCheck_button_loc=(By.ID,"beginDetect")
    #清空文本
    clearPaper_button_loc=(By.ID,"clearPaper")
    #继续添加论文
    addPaper_button_loc=(By.ID,"addPaper")
    #提示补充完整信息
    paperInfo_incomplete_remind=(By.CLASS_NAME,"layui-layer-content")

    #已检测过的继续检测
    continue_checked_button=(By.CLASS_NAME,"layui-layer-btn0")
    #停止检测
    stop_checked_button=(By.CLASS_NAME,"layui-layer-btn1")


    #题名
    title=(By.ID,"title")
    author=(By.ID,"author")
    source=(By.ID,"source")
    publishDate=(By.ID,"publishDate")
    dateTime=(By.XPATH,".//*[@id='datetimepicker']/span/span")
    paper=(By.ID,"paper")


    #跳转到检测信息页
    jump_checkInfo_button=(By.CLASS_NAME,"layui-layer-btn0")

    #继续检测论文
    continue_checkpapar_button=(By.CLASS_NAME,"layui-layer-btn1")

    #检测信息页题名/作者名
    checkInfo_title=(By.XPATH,".//*[@id='result']/tbody/tr[1]/td[4]")
    #职称论文页面
    titlePaparcheck_title=(By.XPATH,"html/body/div[1]/div[1]/section/ol/li[2]")

    #删除已添加的论文
    delete_Paper=(By.XPATH,"html/body/div[1]/div[1]/div/div[2]/div[1]/div[1]/span[1]")

    #查找论文按钮
    search_paper=(By.ID,"lookForPaper")




    #进入论文检测模块
    def in_PaperCheck(self):
        self.find_element(*self.in_paperCheck_button_loc).click()
    #进入新论文相似性检测模块
    def in_titlePaperCheck(self):
        self.find_element(*self.titlepaper_module_loc).click()

    #添加到文件夹按钮
    def add_to_folder_button(self):
        self.find_element(*self.upload_moveFolder_button).click()


    #选择已有文件夹
    def choose_existfolder(self):
       self.find_element(*self.existfolder).click()
    #获取已存在文件夹的文本
    def get_existfolder_text(self):
        return self.find_element(*self.existfolder).text

    #获取文件夹页面的确定按钮文本
    def folder_windowconfirm(self):
        return self.find_element(*self.add_existfolder_confirm).text
    #单击确定按钮
    def click_confirm_button(self):
        self.find_element(*self.add_existfolder_confirm).click()

    #获取已选择文件夹的名称
    def get_choosefolder_text(self):
        return self.find_element(*self.choosefolder).text
     #修改文件夹按钮
    def modify_choosefolder_button(self):
        self.find_element(*self.modify_folder).click()
    #修改到已存在文件夹
    def modify_existfolder(self):
        self.find_element(*self.existfolder1).click()

    #修改已存在的文件夹名称
    def modify_existfolder_text(self):
        return self.find_element(*self.existfolder1).text
     #修改文件夹确定按钮
    def modify_confirm_button(self):
        self.find_element(*self.modifyfolder_confirm).click()
    def modify_confirm_button1(self):
        self.find_element(*self.modifyfolder_confirm1).click()

    #添加到新文件夹
    def add_newfolder_button(self):
        self.find_element(*self.add_newfolder).click()

    #输入新文件夹名称
    def input_new_foldername1(self):
        date = time.strftime("%Y%m%d%H%M")
        folder_name = "%sFile"%(date)
        self.find_element(*self.createfolder).send_keys(folder_name)
        return folder_name

    #创建新文件夹
    def input_new_foldername(self,foldername):
        self.find_element(*self.createfolder).clear()
        self.find_element(*self.createfolder).send_keys(foldername)
        return foldername

    #添加至新文件夹过程
    def add_to_new_folder(self):
        #单击移动到文件夹
        self.add_to_folder_button()
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
        self.add_to_folder_button()
        sleep(5)
        self.add_newfolder_button()
        sleep(5)
        text = self.input_new_foldername(foldername)
        sleep(5)
        self.click_confirm_button()
        sleep(2)
        return text

    #创建文件夹错误提示
    def create_error_remind(self):
        return self.find_element(*self.create_newfolder_error).text

    #点击插件按钮方法
    def clickUpLoad(self):
        click = ClickButton()
        #获取位置并点击
        #print(self.get_where())
        pos=(1340, 443)

        #click.click(click.get_win_handle(self.get_where()),self.get_where())
        click.click(click.get_win_handle(pos),pos)


    def get_where(self):
        click = ClickButton()
        above=self.find_element(*self.upload_button_loc)
        ActionChains(self.driver).move_to_element(above).perform()
        time.sleep(8)
        return click.get_curpos()

    clickupload_button=(By.ID,"SWFUpload_2")
    def clickUpLoad1(self):
        self.find_element(*self.clickupload_button).click()

    #调用autoit生成的exe，并传入浏览器、需要上传至页面文件的地址两个参数
    def uploadFile_para(self,browserName,filePath):
        #注意路径中不能存在空格并且文件夹名称不能过长
        ab_path = GetPath().getAbsoluteFilePath("testvb.exe",r"uploadApp\testvb.exe")

        os.system(ab_path+ " "+browserName+" "+filePath)

    #获取上传文件的绝对路径
    def getFilePath(self,filename):
        file_path = GetPath().getAbsoluteFilePath("%s"%filename,r"SubmitPaperTestData\%s"%filename)
        return file_path

    #开始上传按钮
    def startCheck_button(self):
        self.find_element(*self.startCheck_button_loc).click()
    #清空文本按钮
    def clearPaper_button(self):
        self.find_element(*self.clearPaper_button_loc).click()
    #继续添加论文按钮
    def continue_addPaper_button(self):
        self.find_element(*self.addPaper_button_loc).click()
    #获取补充论文完整提示
    def supply_incompletePaper_remind(self):
        return self.find_element(*self.paperInfo_incomplete_remind).text


    #已上传文件
    #题名
    def paper_title(self):
        return self.find_element(*self.title).text
    def addPaper_title(self,title):
        self.find_element(*self.title).clear()
        self.find_element(*self.title).send_keys(title)
    #作者
    def paper_author(self):
        return self.find_element(*self.author).text
    def addPaper_author(self,author):
        self.find_element(*self.author).clear()
        self.find_element(*self.author).send_keys(author)

    #来源
    def paper_source(self):
        return self.find_element(*self.source).text
    def addPaper_source(self,source):
        self.find_element(*self.source).clear()
        self.find_element(*self.source).send_keys(source)
    def paper_datetime(self):
        self.find_element(*self.dateTime).click()
    #论文内容
    def add_paper(self):
        return self.find_element(*self.paper).text()

    #补全论文信息
    def supply_paperInfo(self,title,author,source):
        self.addPaper_title(title)
        sleep(2)
        self.addPaper_author(author)
        sleep(2)
        self.addPaper_source(source)
        sleep(2)
        self.paper_datetime()

    #继续检测论文
    def continue_checkpaper(self):
        self.find_element(*self.continue_checkpapar_button).click()

    #继续检测论文提示
    def continue_checkpaper_remind(self):
        return self.find_element(*self.titlePaparcheck_title).text
    #跳转到检测信息页
    def jump_checkInfo(self):
        self.find_element(*self.jump_checkInfo_button).click()

    #跳转到检测信息页-题名
    def jump_checkpaper_remind(self):
        return self.find_element(*self.checkInfo_title).text

    #获取检测信息提示
    def get_check_content(self):
        return self.find_element(*self.paperInfo_incomplete_remind).text

    def stop_checked(self):
        self.find_element(*self.stop_checked_button).click()

    def continue_checked(self):
        self.find_element(*self.continue_checked_button).click()

    def deletePaper_button(self):
        self.find_element(*self.delete_Paper).click()


    #手工录入论文内容
    def inputPaperContent(self,filename):
        #self.find_element(*self.paperContent).clear()
        #self.find_element(*self.paperContent).send_keys(Keys.TAB)
        self.find_element(*self.paper).send_keys(filename)
        #sleep(10)
    #逐行读取文本内容并逐行写入文本框
    def readAndInputContent(self,filename):
        f = FilesOption()
        g = GetPath()
        manu = TitlePapersCheck(self.driver)
        filePath =g.getAbsoluteFilePath(filename,r"paperDetectionEntry\%s"%filename)
        print(filePath)
        Flist = f.readFileContent(filePath)
        #self.ManualNoText("文本信息正确开始检测","作者")
        for i in range(0,len(Flist)):
            con = Flist[i].decode('utf8')
            con=con.replace("\t","")
            manu.inputPaperContent(con)
        sleep(2)

    #查找论文按钮
    def search_paper_button(self):
        self.find_element(*self.search_paper).click()

    #获取第一条
    get_firstPaper=(By.XPATH,".//*[@id='papersbody']/li[1]/input")
    def choose_firstPaper(self):
        self.find_element(*self.get_firstPaper).click()
    #选择确定按钮
    choose_confirm=(By.ID,"lookforPaperOk")
    def choose_confirm_button(self):
        self.find_element(*self.choose_confirm).click()


    #第二篇论文

    #作者
    author1=(By.CSS_SELECTOR,".container>div:nth-child(2) .col-xs-9>#author")
    #题名
    title1=(By.CSS_SELECTOR,".container>div:nth-child(2) .col-xs-9>#title")
    #查找论文
    lookForPaper1=(By.CSS_SELECTOR,".container>div:nth-child(2) #lookForPaper")
    choose_secondPaper1=(By.CSS_SELECTOR,".container>div:nth-child(2) #papersbody>li:nth-child(1)>input")
    #确定按钮
    cloose_confirm_button1=(By.CSS_SELECTOR,".container>div:nth-child(2) #lookforPaperOk")
    #继续添加按钮
    continue_add1=(By.CSS_SELECTOR,".container>div:nth-child(2) .funButton>#addPaper")
    #清空文本
    clearPaper1=(By.CSS_SELECTOR,".container>div:nth-child(2) #clearPaper")

    #最多上传篇数提示
    max_paper=(By.ID,"max")
    def max_uploadPaper(self):
        return self.find_element(*self.max_paper).text
    #添加第二篇-查找论文上传流程
    def lookForPaper_upload(self):
        #输入作者
        self.find_element(*self.author1).clear()
        self.find_element(*self.author1).send_keys("李硕")
        sleep(5)
        #单击查找
        self.find_element(*self.lookForPaper1).click()
        sleep(5)
        #选择一篇论文
        self.find_element(*self.choose_secondPaper1).click()
        sleep(5)
        #单击确定按钮
        self.find_element(*self.cloose_confirm_button1).click()
        sleep(5)
        self.continue_checked()
        sleep(5)



    #第三篇论文
    #作者
    author2=(By.CSS_SELECTOR,".container>div:nth-child(3) .col-xs-9>#author")
    #题名
    title2=(By.CSS_SELECTOR,".container>div:nth-child(3) .col-xs-9>#title")
    #查找论文
    lookForPaper2=(By.CSS_SELECTOR,".container>div:nth-child(3) #lookForPaper")
    choose_thirdPaper=(By.CSS_SELECTOR,".container>div:nth-child(3) #papersbody>li:nth-child(2)>input")
    #确定按钮
    cloose_confirm_button2=(By.CSS_SELECTOR,".container>div:nth-child(3) #lookforPaperOk")
    #继续添加按钮
    continue_add2=(By.CSS_SELECTOR,".container>div:nth-child(3) .funButton>#addPaper")
    #开始检测按钮
    startCheck2=(By.CSS_SELECTOR,".container>div:nth-child(3) #beginDetect")
    def start_batch_check(self):
        self.find_element(*self.startCheck2).click()

    #添加第三篇-查找论文上传流程
    def lookForPaper_upload1(self):

        self.find_element(*self.continue_add1).click()
        sleep(10)
        #输入作者
        self.find_element(*self.author2).clear()
        self.find_element(*self.author2).send_keys("李硕")
        sleep(5)
        #单击查找
        self.find_element(*self.lookForPaper2).click()
        sleep(10)
        #选择一篇论文
        self.find_element(*self.choose_thirdPaper).click()
        sleep(5)
        #单击确定按钮
        self.find_element(*self.cloose_confirm_button2).click()
        sleep(5)
        self.continue_checked()
        sleep(5)


    #第四篇论文
    #作者
    author3=(By.CSS_SELECTOR,".container>div:nth-child(4) .col-xs-9>#author")
    #题名
    title3=(By.CSS_SELECTOR,".container>div:nth-child(4) .col-xs-9>#title")
    #查找论文
    lookForPaper3=(By.CSS_SELECTOR,".container>div:nth-child(4) #lookForPaper")
    choose_fourthPaper=(By.CSS_SELECTOR,".container>div:nth-child(4) #papersbody>li:nth-child(3)>input")
    #确定按钮
    cloose_confirm_button3=(By.CSS_SELECTOR,".container>div:nth-child(4) #lookforPaperOk")
    #继续添加按钮
    continue_add3=(By.CSS_SELECTOR,".container>div:nth-child(4) .funButton>#addPaper")

    #添加第四篇-查找论文上传流程
    def lookForPaper_upload2(self):

        self.find_element(*self.continue_add2).click()
        sleep(5)
        #输入作者
        self.find_element(*self.author3).clear()
        self.find_element(*self.author3).send_keys("李硕")
        sleep(10)
        #单击查找
        self.find_element(*self.lookForPaper3).click()
        sleep(5)
        #选择一篇论文
        self.find_element(*self.choose_fourthPaper).click()
        sleep(5)
        #单击确定按钮
        self.find_element(*self.cloose_confirm_button3).click()
        sleep(5)
        self.continue_checked()
        sleep(5)

    #第五篇论文
    #作者
    author4=(By.CSS_SELECTOR,".container>div:nth-child(5) .col-xs-9>#author")
    #题名
    title4=(By.CSS_SELECTOR,".container>div:nth-child(5) .col-xs-9>#title")
    #查找论文
    lookForPaper4=(By.CSS_SELECTOR,".container>div:nth-child(5) #lookForPaper")
    choose_fifthPaper=(By.CSS_SELECTOR,".container>div:nth-child(5) #papersbody>li:nth-child(4)>input")
    #确定按钮
    cloose_confirm_button4=(By.CSS_SELECTOR,".container>div:nth-child(5) #lookforPaperOk")
    #继续添加按钮
    continue_add4=(By.CSS_SELECTOR,".container>div:nth-child(5) .funButton>#addPaper")

    #添加第5篇-查找论文上传流程
    def lookForPaper_upload3(self):

        self.find_element(*self.continue_add3).click()
        sleep(5)
        self.find_element(*self.author4).clear()
        self.find_element(*self.author4).send_keys("李硕")
        sleep(10)
        self.find_element(*self.lookForPaper4).click()
        sleep(5)
        self.find_element(*self.choose_fifthPaper).click()
        sleep(5)
        self.find_element(*self.cloose_confirm_button4).click()
        sleep(5)
        self.continue_checked()
        sleep(5)

    #第六篇论文
    #作者
    author5=(By.CSS_SELECTOR,".container>div:nth-child(6) .col-xs-9>#author")
    #题名
    title5=(By.CSS_SELECTOR,".container>div:nth-child(6) .col-xs-9>#title")
    #查找论文
    lookForPaper5=(By.CSS_SELECTOR,".container>div:nth-child(6) #lookForPaper")
    choose_sixthPaper=(By.CSS_SELECTOR,".container>div:nth-child(6) #papersbody>li:nth-child(5)>input")
    #确定按钮
    cloose_confirm_button5=(By.CSS_SELECTOR,".container>div:nth-child(6) #lookforPaperOk")
    #继续添加按钮
    continue_add5=(By.CSS_SELECTOR,".container>div:nth-child(6) .funButton>#addPaper")

    #添加第6篇-查找论文上传流程
    def lookForPaper_upload4(self):

        self.find_element(*self.continue_add4).click()
        sleep(5)
        self.find_element(*self.author5).clear()
        self.find_element(*self.author5).send_keys("李硕")
        sleep(10)
        self.find_element(*self.lookForPaper5).click()
        sleep(10)
        self.find_element(*self.choose_sixthPaper).click()
        sleep(5)
        self.find_element(*self.cloose_confirm_button5).click()
        sleep(5)
        self.continue_checked()
        sleep(5)

    #第七篇论文
    #作者
    author6=(By.CSS_SELECTOR,".container>div:nth-child(7) .col-xs-9>#author")
    #题名
    title6=(By.CSS_SELECTOR,".container>div:nth-child(7) .col-xs-9>#title")
    #查找论文
    lookForPaper6=(By.CSS_SELECTOR,".container>div:nth-child(7) #lookForPaper")
    choose_seventhPaper=(By.CSS_SELECTOR,".container>div:nth-child(7) #papersbody>li:nth-child(6)>input")
    #确定按钮
    cloose_confirm_button6=(By.CSS_SELECTOR,".container>div:nth-child(7) #lookforPaperOk")
    #继续添加按钮
    continue_add6=(By.CSS_SELECTOR,".container>div:nth-child(7) .funButton>#addPaper")

    #添加第7篇-查找论文上传流程
    def lookForPaper_upload5(self):

        self.find_element(*self.continue_add5).click()
        sleep(5)
        self.find_element(*self.author6).clear()
        self.find_element(*self.author6).send_keys("李硕")
        sleep(5)
        self.find_element(*self.lookForPaper6).click()
        sleep(5)
        self.find_element(*self.choose_seventhPaper).click()
        sleep(5)
        self.find_element(*self.cloose_confirm_button6).click()
        sleep(5)
        self.continue_checked()
        sleep(5)

    #第8篇论文
    #作者
    author7=(By.CSS_SELECTOR,".container>div:nth-child(8) .col-xs-9>#author")
    #题名
    title7=(By.CSS_SELECTOR,".container>div:nth-child(8) .col-xs-9>#title")
    #查找论文
    lookForPaper7=(By.CSS_SELECTOR,".container>div:nth-child(8) #lookForPaper")
    choose_eighthPaper=(By.CSS_SELECTOR,".container>div:nth-child(8) #papersbody>li:nth-child(7)>input")
    #确定按钮
    cloose_confirm_button7=(By.CSS_SELECTOR,".container>div:nth-child(8) #lookforPaperOk")
    #继续添加按钮
    continue_add7=(By.CSS_SELECTOR,".container>div:nth-child(8) .funButton>#addPaper")

    #添加第8篇-查找论文上传流程
    def lookForPaper_upload6(self):

        self.find_element(*self.continue_add6).click()
        sleep(5)
        self.find_element(*self.author7).clear()
        self.find_element(*self.author7).send_keys("李硕")
        sleep(5)
        self.find_element(*self.lookForPaper7).click()
        sleep(5)
        self.find_element(*self.choose_eighthPaper).click()
        sleep(5)
        self.find_element(*self.cloose_confirm_button7).click()
        sleep(5)
        self.continue_checked()
        sleep(5)

    #第9篇论文
    #作者
    author8=(By.CSS_SELECTOR,".container>div:nth-child(9) .col-xs-9>#author")
    #题名
    title8=(By.CSS_SELECTOR,".container>div:nth-child(9) .col-xs-9>#title")
    #查找论文
    lookForPaper8=(By.CSS_SELECTOR,".container>div:nth-child(9) #lookForPaper")
    choose_ninthPaper=(By.CSS_SELECTOR,".container>div:nth-child(9) #papersbody>li:nth-child(8)>input")
    #确定按钮
    cloose_confirm_button8=(By.CSS_SELECTOR,".container>div:nth-child(9) #lookforPaperOk")
    #继续添加按钮
    continue_add8=(By.CSS_SELECTOR,".container>div:nth-child(9) .funButton>#addPaper")

    #添加第9篇-查找论文上传流程
    def lookForPaper_upload7(self):

        self.find_element(*self.continue_add7).click()
        sleep(5)
        self.find_element(*self.author8).clear()
        self.find_element(*self.author8).send_keys("李硕")
        sleep(5)
        self.find_element(*self.lookForPaper8).click()
        sleep(5)
        self.find_element(*self.choose_ninthPaper).click()
        sleep(5)
        self.find_element(*self.cloose_confirm_button8).click()
        sleep(5)
        self.continue_checked()
        sleep(5)

    #第10篇论文
    #作者
    author9=(By.CSS_SELECTOR,".container>div:nth-child(10) .col-xs-9>#author")
    #题名
    title9=(By.CSS_SELECTOR,".container>div:nth-child(10) .col-xs-9>#title")
    #查找论文
    lookForPaper9=(By.CSS_SELECTOR,".container>div:nth-child(10) #lookForPaper")
    choose_tenthPaper=(By.CSS_SELECTOR,".container>div:nth-child(10) #papersbody>li:nth-child(9)>input")
    #确定按钮
    cloose_confirm_button9=(By.CSS_SELECTOR,".container>div:nth-child(10) #lookforPaperOk")
    #继续添加按钮
    continue_add9=(By.CSS_SELECTOR,".container>div:nth-child(10) .funButton>#addPaper")

    #添加第10篇-查找论文上传流程
    def lookForPaper_upload8(self):

        self.find_element(*self.continue_add8).click()
        sleep(5)
        self.find_element(*self.author9).clear()
        self.find_element(*self.author9).send_keys("李硕")
        sleep(5)
        self.find_element(*self.lookForPaper9).click()
        sleep(5)
        self.find_element(*self.choose_tenthPaper).click()
        sleep(5)
        self.find_element(*self.cloose_confirm_button9).click()
        sleep(5)
        self.continue_checked()
        sleep(5)
        self.find_element(*self.continue_add9).click()



















