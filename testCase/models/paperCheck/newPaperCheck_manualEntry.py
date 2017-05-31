from testCase.pageObj.basePage import BasePage
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from util.commonUtils.clickButton import ClickButton
from util.toolUtils.getPath import GetPath
import os
import time
from util.toolUtils.getPath import GetPath
from util.commonUtils.fileOption import FilesOption


class ManualEnterPaperCheck(BasePage):

    #进入论文检测模块
    in_paperCheck_button_loc=(By.ID,"paperCheck")
    #进入新论文相似性检测
    in_newPaperCheck_loc=(By.XPATH,"html/body/div[1]/aside/div/section/ul/li[3]/ul/li[1]/a")
    #单击进入手工录入
    manualEnter_button=(By.XPATH,".//*[@id='step7']/a")



    #将论文添加到分类文件夹
    addFolder_button=(By.ID,"movein")
    #确定按钮
    confirm_button=(By.CLASS_NAME,"layui-layer-btn0")
    #取消按钮
    cancel_button=(By.CLASS_NAME,"layui-layer-btn1")
    #已存在的文件夹
    existfolder=(By.XPATH,".//*[@id='selDir']/option[2]")
    #已经选择的文件夹
    choosefolder=(By.ID,"input_label")
    #修改按钮
    modify_button=(By.XPATH,".//*[@id='input_showDir']/a")

    modify_existfolder_loc=(By.XPATH,".//*[@id='selDir']/option[3]")



    #添加到新文件夹
    add_newfolder=(By.ID,"radio1")
    #添加新文件夹按钮
    createfolder=(By.ID,"inpDir")

    #新建文件夹错误信息提示
    create_newfolder_error=(By.XPATH,".//*[@id='errmsg']")

    title=(By.ID,"title")
    author=(By.ID,"author")
    content=(By.ID,"step9")

    checkbutton=(By.ID,"btnCheck")
    clear=(By.ID,"step10")

    title_error=(By.ID,"title-error")
    author_error=(By.ID,"author-error")
    content_error=(By.ID,"step9-error")



    def in_PaperCheck_button(self):
        self.find_element(*self.in_paperCheck_button_loc).click()
    #进入手工录入
    def in_manualEnter(self):
        self.find_element(*self.manualEnter_button).click()
    #将论文放到文件夹
    def add_to_folder(self):
        self.find_element(*self.addFolder_button).click()
    #获取窗口上确定按钮的文本
    def get_confirmbutton(self):
        return self.find_element(*self.confirm_button).text
    def click_confirm_button(self):
        self.find_element(*self.confirm_button).click()
    #选择一个已存在的文件夹
    def choose_existfolder(self):
        self.find_element(*self.existfolder).click()
    #获取要选择的文件夹的名称
    def get_existfolder_text(self):
        return self.find_element(*self.existfolder).text
    #获取已经选择的文件夹的名称
    def get_choosefolder_text(self):
        return self.find_element(*self.choosefolder).text
    #修改按钮
    def modify_choosefolder_button(self):
        self.find_element(*self.modify_button).click()
    #修改为已存在文件夹
    def modify_existfolder(self):
        self.find_element(*self.modify_existfolder_loc).click()
    #获取已选择的文件夹
    def modify_existfolder_text(self):
        return self.find_element(*self.modify_existfolder_loc).text


    #添加到新文件夹
    def add_to_newfolder(self):
        self.find_element(*self.add_newfolder).click()

    #创建文件夹错误提示
    def create_error_remind(self):
        return self.find_element(*self.create_newfolder_error).text




    #创建新文件夹
    def input_new_foldername(self,foldername):
        self.find_element(*self.createfolder).clear()
        self.find_element(*self.createfolder).send_keys(foldername)
        return foldername

    #输入新文件夹名称
    def input_new_foldername1(self):
        date = time.strftime("%Y%m%d%H%M")
        folder_name = "%sFile"%(date)
        self.find_element(*self.createfolder).send_keys(folder_name)
        return folder_name


    #添加至新文件夹过程自定义
    def add_to_new_folder_custom(self,foldername):
        self.add_to_folder()
        sleep(5)
        self.add_to_newfolder()
        sleep(5)
        text = self.input_new_foldername(foldername)
        sleep(5)
        self.click_confirm_button()
        sleep(2)
        return text


    #添加至新文件夹过程
    def add_to_new_folder(self):
        #单击移动到文件夹
        self.add_to_folder()
        sleep(2)
        #单击添加到新文件夹
        self.add_to_newfolder()
        sleep(2)
        #获取输入的文件夹名称
        text = self.input_new_foldername1()
        sleep(2)
        #单击确定按钮
        self.click_confirm_button()
        sleep(2)
        return text


    #输入论文信息
    def paper_title(self,title):
        self.find_element(*self.title).clear()
        self.find_element(*self.title).send_keys(title)
    def paper_author(self,author):
        self.find_element(*self.author).clear()
        self.find_element(*self.author).send_keys(author)
    def paper_content(self,content):
        self.find_element(*self.content).clear()
        self.find_element(*self.content).send_keys(content)
    def get_paperContent(self):
        return self.find_element(*self.content).text


    def input_paperInfo(self,title,author,content):
        self.paper_title(title)
        sleep(2)
        self.paper_author(author)
        sleep(2)
        self.paper_content(content)
        sleep(2)
    titleerror=(By.ID,"titlemsg")
    authorerror=(By.ID,"authormsg")

    #获取为空提示
    def title_error_remind(self):
        return self.find_element(*self.title_error).text
    def author_error_remind(self):
        return self.find_element(*self.author_error).text
    def content_error_remind(self):
        return self.find_element(*self.content_error).text
    #获取输入格式不正确的限制
    def get_title_remind(self):
        return self.find_element(*self.titleerror).text
    def get_author_remind(self):
        return self.find_element(*self.authorerror).text
    #单击开始检测按钮
    def click_startCheck(self):
        self.find_element(*self.checkbutton).click()
    #单击清空文本按钮
    def click_clearPaper(self):
        self.find_element(*self.clear).click()


    #检测信息页题名
    checked_title=(By.XPATH,".//*[@id='result']/tbody/tr[1]/td[4]")
    #论文检测页面
    check_window=(By.XPATH,"html/body/div[1]/div[1]/section/ol/li[2]")
    def checkInfo_title(self):
        return self.find_element(*self.checked_title).text
    def paperCheck_window(self):
        return self.find_element(*self.check_window).text


    #跳转到检测信息页
    def jump_checkInfo(self):
        self.find_element(*self.confirm_button).click()
    #继续检测论文
    def continue_check(self):
        self.find_element(*self.cancel_button).click()








    #手工录入论文内容
    def inputPaperContent(self,filename):
        #self.find_element(*self.paperContent).clear()
        #self.find_element(*self.paperContent).send_keys(Keys.TAB)
        self.find_element(*self.content).send_keys(filename)
        #sleep(10)
    #逐行读取文本内容并逐行写入文本
    def readAndInputContent(self,filename):
        f = FilesOption()
        g = GetPath()
        manu = ManualEnterPaperCheck(self.driver)
        filePath =g.getAbsoluteFilePath(filename,r"paperDetectionEntry\%s"%filename)
        print(filePath)
        Flist = f.readFileContent(filePath)
        #self.ManualNoText("文本信息正确开始检测","作者")
        for i in range(0,len(Flist)):
            con = Flist[i].decode('gbk')
            con=con.replace("\t","")
            manu.inputPaperContent(con)
        sleep(2)


     #判断是否有alert弹窗
    def verifyExistAlert(self):
        text = super(ManualEnterPaperCheck,self).confirm_broserAlert()
        print(text)
        return text








