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
    addToFolder = (By.CSS_SELECTOR,".dropdown-menu #movein")  #添加至文件夹-按钮
    downloadReportBtn = (By.CSS_SELECTOR,'.dropdown-menu #download')  #下载报告-按钮
    redetectReportBtn = (By.CSS_SELECTOR,'.dropdown-menu #beginDetect')  #重新检测-按钮
    deleteReportBtn = (By.CSS_SELECTOR,'.dropdown-menu #delrecord')  #删除-按钮
    addToNewFolder = (By.CSS_SELECTOR,".layui-layer-content>form>div:nth-child(1)>label:nth-child(2)")  #添加至新文件夹单选框
    folderNameInput = (By.CSS_SELECTOR,'#inpDir')  #文件夹名称输入框
    acceptAddBtn = (By.CSS_SELECTOR,'#layui-layer1>.layui-layer-btn>a:nth-child(1)')  #确认添加按钮
    alertInfo = (By.CSS_SELECTOR,'.layui-layer-content')  #页面中提示
    checkboxFirst = (By.CSS_SELECTOR,'tr:nth-child(1)>td:nth-child(1)>input')  #首条检测信息的-复选框
    folderNameFirst = (By.CSS_SELECTOR,'tr:nth-child(1)>td:nth-child(6)')  #首条-文件夹的信息
    detectStatusFirst = (By.CSS_SELECTOR,'tr:nth-child(1)>td:nth-child(8)')  #首条-检测状态的信息
    selectBoxfirst = (By.CSS_SELECTOR,'#selDir>option:nth-child(1)')  #下拉选项第一个
    selectBoxSecend = (By.CSS_SELECTOR,'#selDir>option:nth-child(2)')  #下拉选项第二个
    addNewfolderErrMessage = (By.CSS_SELECTOR,'#errmsg')  #添加至新文件夹时异常提示
    confirmDownloadBtn = (By.CSS_SELECTOR,'.layui-layer-btn>a:nth-child(1)')  #确认下载按钮
    detailBtn = (By.CSS_SELECTOR,'tbody>tr>td>#detail2')  #下载详细报告选择按钮
    infoCount = (By.CSS_SELECTOR,'.pagination-info')  #列表页记录条数


    #筛选检测信息操作*****************************************************************************************

    moreOptionBtn = (By.CSS_SELECTOR,'#foldspan')  #查询框中的更多选项按钮
    checkStatusSucceed = (By.CSS_SELECTOR,'#status>option:nth-child(2)')  #帅选条件-检测状态-检测成功
    checkStatusFail = (By.CSS_SELECTOR,'#status>option:nth-child(3)')  #帅选条件-检测状态-检测失败
    searchMoreBtn = (By.CSS_SELECTOR,'#btnSearch1')  #更多选项下的查询按钮

    #下载列表数据操作*****************************************************************************************

    downloadListBtn = (By.CSS_SELECTOR,'.glyphicon.glyphicon-download-alt')  #点击下载列表按钮

    '''**************************************批量操作相关操作**********************************************'''


    '''************************添加至文件夹操作************************'''

    def clickCheckInfoBtn(self):
        '''点击检测信息按钮'''
        super(CheckInfo, self).wait_element_visible(10,self.checkInfoBtn)
        self.find_element(*self.checkInfoBtn).click()

    def clickMoreBtn(self):
        '''点击more按钮'''
        super(CheckInfo, self).wait_element_visible(10,self.moreBtn)
        self.find_element(*self.moreBtn).click()

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
        name = "新文件夹 %s"%tag
        self.find_element(*self.folderNameInput).send_keys(name)
        #sleep(5)
        super(CheckInfo, self).wait_element_visible(10,self.acceptAddBtn)
        self.find_element(*self.acceptAddBtn).click()
        sleep(3)
        return name

    def AddToExistFolder(self):
        '''添加至已有文件夹过程'''
        self.clickAddToFolder()
        #选择已有文件夹
        super(CheckInfo, self).wait_element_visible(10,self.selectBoxSecend)
        name = self.find_element(*self.selectBoxSecend).text
        self.find_element(*self.selectBoxSecend).click()
        super(CheckInfo, self).wait_element_visible(10,self.acceptAddBtn)
        self.find_element(*self.acceptAddBtn).click()
        sleep(3)
        return name

    def getAlertInfo(self):
        '''获取提示信息'''
        return self.find_element(*self.alertInfo).text

    def clickCheckboxFirst(self):
        '''点击勾选首条信息的复选框'''
        super(CheckInfo, self).wait_element_visible(10,self.checkboxFirst)
        self.find_element(*self.checkboxFirst).click()

    def getFolderNameFirst(self):
        '''得到列表首条信息文件夹的名称'''
        super(CheckInfo, self).wait_element_visible(10,self.folderNameFirst)
        return self.find_element(*self.folderNameFirst).text

    def AddToNewFolderAlertVerify(self,name):
        '''添加至新文件夹过程'''
        #点击添加至新文件夹
        super(CheckInfo, self).wait_element_visible(10,self.addToNewFolder)
        self.find_element(*self.addToNewFolder).click()
        #输入文件夹名称
        super(CheckInfo, self).wait_element_visible(10,self.folderNameInput)
        self.find_element(*self.folderNameInput).send_keys(name)
        super(CheckInfo, self).wait_element_visible(10,self.acceptAddBtn)
        self.find_element(*self.acceptAddBtn).click()
        #获取异常提示
        super(CheckInfo, self).wait_element_visible(10,self.addNewfolderErrMessage)
        errMsg = self.find_element(*self.addNewfolderErrMessage).text
        return errMsg

    def getExistFolderName(self):
        '''获得下拉列表首个已有文件夹名称'''
        super(CheckInfo, self).wait_element_visible(10,self.selectBoxfirst)
        name = self.find_element(*self.selectBoxfirst).text
        return name

    '''************************下载报告操作************************'''

    def clickDownloadReportBtn(self):
        '''点击下载报告下拉选项'''
        super(CheckInfo, self).wait_element_visible(10,self.downloadReportBtn)
        self.find_element(*self.downloadReportBtn).click()

    def clickConfirmDownloadBtn(self):
        '''点击确认下载按钮'''
        super(CheckInfo, self).wait_element_visible(10,self.confirmDownloadBtn)
        self.find_element(*self.confirmDownloadBtn).click()

    def choiceDetailBtn(self):
        '''选择下载详细报告'''
        super(CheckInfo, self).wait_element_visible(10,self.detailBtn)
        self.find_element(*self.detailBtn).click()

    def downloadReport_allcheck_simple(self):
        '''勾选全部时，下载简明报告过程'''
        self.clickMoreOptionBtn()
        self.searchCheckStatus()
        self.clickSearchMoreBtn()
        self.checkAllInfo()
        self.clickMoreBtn()
        self.clickDownloadReportBtn()
        self.clickConfirmDownloadBtn()

    def downloadReport_firstcheck_simple(self):
        '''勾选首条时，下载简明报告过程'''
        self.clickMoreOptionBtn()
        self.searchCheckStatus()
        self.clickSearchMoreBtn()
        self.clickCheckboxFirst()
        self.clickMoreBtn()
        self.clickDownloadReportBtn()
        self.clickConfirmDownloadBtn()

    def downloadReport_allcheck_detail(self):
        '''勾选全部时，下载详细报告过程'''
        self.clickMoreOptionBtn()
        self.searchCheckStatus()
        self.clickSearchMoreBtn()
        self.checkAllInfo()
        self.clickMoreBtn()
        self.clickDownloadReportBtn()
        self.choiceDetailBtn()
        self.clickConfirmDownloadBtn()

    def downloadReport_onecheck_detail(self):
        '''勾选首条时，下载详细报告过程'''
        self.clickMoreOptionBtn()
        self.searchCheckStatus()
        self.clickSearchMoreBtn()
        self.clickCheckboxFirst()
        self.clickMoreBtn()
        self.clickDownloadReportBtn()
        self.choiceDetailBtn()
        self.clickConfirmDownloadBtn()

    def downloadReport_unsucceed(self):
        '''勾选全部，选择未成功的信息下载报告过程'''
        self.clickMoreOptionBtn()
        self.searchCheckStatusFail()
        self.clickSearchMoreBtn()
        self.checkAllInfo()
        self.clickMoreBtn()
        self.clickDownloadReportBtn()
        errInfo = self.getAlertInfo()
        return errInfo

    def downloadReport_uncheck(self):
        '''未勾选检测信息，点击下载报告过程'''
        self.clickMoreBtn()
        self.clickDownloadReportBtn()
        errInfo = self.getAlertInfo()
        return errInfo

    '''************************重新检测操作************************'''

    def redetect_succeed(self):
        '''选择首条信息进行重新检测'''
        self.clickMoreOptionBtn()
        self.searchCheckStatusFail()
        self.clickSearchMoreBtn()
        self.clickCheckboxFirst()
        self.clickMoreBtn()
        self.clickRedetectReportBtn()
        statusInfo = self.getDetectStatusFirst()
        return statusInfo

    def redetect_hasSucceedReport(self):
        '''选择首条信息进行重新检测'''
        self.clickMoreOptionBtn()
        self.searchCheckStatus()
        self.clickSearchMoreBtn()
        self.clickCheckboxFirst()
        self.clickMoreBtn()
        self.clickRedetectReportBtn()
        errInfo = self.getAlertInfo()
        return errInfo

    def clickRedetectReportBtn(self):
        '''点击重新检测按钮'''
        super(CheckInfo, self).wait_element_visible(10,self.redetectReportBtn)
        self.find_element(*self.redetectReportBtn).click()

    def getDetectStatusFirst(self):
        '''获取首条检测信息的检测状态文本'''
        super(CheckInfo, self).wait_element_visible(10,self.detectStatusFirst)
        return self.find_element(*self.detectStatusFirst).text

    def redetectReport_uncheck(self):
        '''未勾选检测信息，点击重新检测报告过程'''
        self.clickMoreBtn()
        self.clickRedetectReportBtn()
        errInfo = self.getAlertInfo()
        return errInfo

    '''************************删除检测报告操作************************'''

    def clickDeleteReportBtn(self):
        '''点击下拉列表的删除按钮'''
        super(CheckInfo, self).wait_element_visible(10,self.deleteReportBtn)
        self.find_element(*self.deleteReportBtn).click()

    def getInfoCount(self):
        '''获取列表中的记录条数'''
        super(CheckInfo, self).wait_element_visible(10,self.infoCount)
        info = self.find_element(*self.infoCount).text
        infoCount = int(info.split('共 ')[1].split(' 条')[0])
        return infoCount

    def deleteReport(self):
        '''删除首条检测报告过程'''
        self.clickCheckboxFirst()
        self.clickMoreBtn()
        self.clickDeleteReportBtn()
        self.clickConfirmDownloadBtn()
        sleep(2)
        deleteInfo = self.getAlertInfo()
        return deleteInfo

    def deletReport_uncheck(self):
        '''未勾选检测信息，点击删除过程'''
        self.clickMoreBtn()
        self.clickDeleteReportBtn()
        errInfo = self.getAlertInfo()
        return errInfo


    '''**************************************筛选检测信息相关操作**********************************************'''

    def clickMoreOptionBtn(self):
        '''点击更多选项按钮'''
        super(CheckInfo, self).wait_element_visible(10,self.moreOptionBtn)
        self.find_element(*self.moreOptionBtn).click()

    def searchCheckStatus(self):
        '''点击并选择检测状态为检测成功'''
        super(CheckInfo, self).wait_element_visible(10,self.checkStatusSucceed)
        self.find_element(*self.checkStatusSucceed).click()

    def searchCheckStatusFail(self):
        '''点击并选择检测状态为检测成功'''
        super(CheckInfo, self).wait_element_visible(10,self.checkStatusFail)
        self.find_element(*self.checkStatusFail).click()

    def clickSearchMoreBtn(self):
        '''点击更多选项下的查询按钮'''
        super(CheckInfo, self).wait_element_visible(10,self.searchMoreBtn)
        self.find_element(*self.searchMoreBtn).click()
        sleep(10)


    '''**************************************下载列表数据相关操作**********************************************'''

    def clickDownloadListBtn(self):
        super(CheckInfo, self).wait_element_visible(10,self.downloadListBtn)
        self.find_element(*self.downloadListBtn).click()



    '''**************************************常用功能操作**********************************************'''
    def isElementExist(self,waittime,loc):
        flag = True
        #star = time()
        wait_time = 0
        while flag:
            isVisiable = super(CheckInfo, self).is_element_visible(loc)
            #end = time()
            #wait_time = int(end-star)
            if isVisiable == True:
                print("-----加载成功！------")
                return isVisiable
            elif isVisiable == False:
                print("等待加载: %ss"%wait_time)
                if wait_time >= waittime:
                    print("-----等待加载超时！-----")
                    return isVisiable
                else:
                    wait_time+=1
                    sleep(1)
                    continue


