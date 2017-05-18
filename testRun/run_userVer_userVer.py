#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-16 08:28:18
# @Author  : Nxy
# @Site    : 
# @File    : run_userVer.py
# @Software: PyCharm
from testCase.models import myUnitChrome
import unittest
import time
from testCase.models.userVer.userVer import UserVer
from testResult.getResultImage import getResultImage
from time import sleep
import random
class RunUserVer(myUnitChrome.UnitChrome):
    def test_userLogout_run(self):
        pass
    def user_login_verify_run(self,username,password):
        '''
        用户登录用例运行
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        #print ("获取当前句柄",self.driver.current_window_handle)
        UserVer(self.driver).userLogin(username,password)

    def test_login_userpwdNull_run(self):
        '''用户名、密码为空登录'''
        time.sleep(2)
        self.user_login_verify_run("","")
        userver=UserVer(self.driver)
        self.assertEqual(userver.uname_error_remind(),"用户名不能为空")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"user_pwd_empty.jpg")
    def test_login_pwdNull_run(self):
        '''用户名正确，密码为空登录'''
        time.sleep(2)
        self.user_login_verify_run('alcheck',"")
        userver=UserVer(self.driver)
        self.assertEqual(userver.pwd_error_remind(),"密码不能为空")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"pwd_empty.jpg")
    def test_login_userNull_run(self):
        '''用户名为空，密码正确'''
        time.sleep(2)
        self.user_login_verify_run(username="",password="f")
        userver=UserVer(self.driver)
        self.assertEqual(userver.uname_error_remind(),"用户名不能为空")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uname_empty.jpg")
    def test_login_error_run(self):
        '''用户名与密码不匹配'''
        time.sleep(2)
        character=random.choice('123456rtyhj')
        username="alcheck"+character
        self.user_login_verify_run(username,"f")
        po=UserVer(self.driver)
        self.assertEqual(po.pwd_error_remind(),"用户名或密码不正确!")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uname_pwd_error.jpg")
    def test_login_success_run(self):
        '''用户名，密码正确'''
        self.user_login_verify_run(username="alcheck",password="f")
        sleep(2)
        userver=UserVer(self.driver)
        self.assertEqual(userver.user_login_success_verify(),"alcheck")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"user_login_ok.jpg")

    def test_userRegist_run(self):
        pass

if __name__=="__main__":
    unittest.main()
