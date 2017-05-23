#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-16 08:28:19
# @Author  : Nxy
# @Site    : 
# @File    : checkInfo.py
# @Software: PyCharm
from selenium import  webdriver
from selenium.webdriver.common.by import By
from testCase.pageObj.basePage import BasePage
from time import sleep,strftime


class CheckInfo(BasePage):

    #进入检测信息页******************************************************************************************

    checkInfoBtn = (By.CSS_SELECTOR,"#checkInfo")  #检测信息进入按钮
    #批量操作***********************************************************************************************

    checkboxAll = (By.CSS_SELECTOR,"#result>thead th:nth-child(1) input")  #批量全选框按钮
    moreBtn = (By.CSS_SELECTOR,"#btnMore>button")  #more按钮
    addToFolder = (By.CSS_SELECTOR,".dropdown-menu #movein")  #添加至文件夹按钮
    addToNewFolder = (By.CSS_SELECTOR,".layui-layer-content>form>div:nth-child(1)>label:nth-child(2)")  #添加至新文件夹单选框
    folderNameInput = (By.CSS_SELECTOR,'#inpDir')  #文件夹名称输入框
    acceptAddBtn = (By.CSS_SELECTOR,'#layui-layer1>.layui-layer-btn>a:nth-child(1)')  #确认添加按钮
    addSucceedInfo = (By.CSS_SELECTOR,'.layui-layer-content')  #添加至文件夹成功提示

    '''**************************************批量操作相关操作**********************************************'''

    def clickCheckInfoBtn(self):
        '''点击检测信息按钮'''
        super(CheckInfo, self).wait_element_visible(10,self.checkInfoBtn)
        self.find_element(*self.checkInfoBtn).click()
    def clickMoreBtn(self):
        '''点击more按钮'''
        super(CheckInfo, self).wait_element_visible(10,self.moreBtn)
        self.find_element(*self.moreBtn).click()
        print("#####################################")
    def checkAllInfo(self):
        '''勾选全部'''
        super(CheckInfo, self).wait_element_visible(10,self.checkboxAll)
        self.find_element(*self.checkboxAll).click()
    def clickAddToFolder(self):
        '''点击添加至文件夹'''
        super(CheckInfo, self).wait_element_visible(10,self.addToFolder)
        self.find_element(*self.addToFolder).click()
    def AddToNewFolder(self):
        '''添加至新文件夹过程'''
        self.clickAddToFolder()
        #点击添加至新文件夹
        super(CheckInfo, self).wait_element_visible(10,self.addToNewFolder)
        self.find_element(*self.addToNewFolder).click()
        #输入文件夹名称
        tag=strftime("%m%d%H%M%S")
        super(CheckInfo, self).wait_element_visible(10,self.folderNameInput)
        self.find_element(*self.folderNameInput).send_keys("新文件夹 %s"%tag)
        #sleep(5)
        super(CheckInfo, self).wait_element_visible(10,self.acceptAddBtn)
        self.find_element(*self.acceptAddBtn).click()
    def getAddSucceedInfo(self):
        '''获取提示成功信息'''
        sleep(3)
        return self.find_element(*self.addSucceedInfo).text




