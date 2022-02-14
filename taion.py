#!/usr/bin/python
# -*- coding: utf-8 -*-

# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import chromedriver_binary
import random

###==初期設定==###
yournumber = (input('クラス、番号(1年A組1番==>1101) : '))
yourname = input('あなたのお名前(名字と名前の間に全角スペース) : ')
startdate = int(input('初めの日付(1月1日==>101,最初の0は取ってください) : '))
finishdate = int(input('終了日(1月30日終わりの場合は131) : '))

# ブラウザを開く。
driver = webdriver.Chrome()
# 体温入力画面を開く。
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe5-bqz3SZIGimnE5fc8KXd2JsSXYO5Q14Qf80F-OV8Zy05Yw/viewform")
driver.maximize_window()


#繰り返し処理したい    
for num in range(startdate,finishdate):

    # クラスと番号を入力する
    search = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    search.send_keys(yournumber)

    #名前の入力
    search = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    search.send_keys(yourname)

    #日付の入力
    search = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    if num < 1000:
        search.send_keys(0,num)
    if num > 1000:
        search.send_keys(num)
    
    #体温生成
    tem =random.randrange(5)
    #体温入力
    search = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]")
    search.click()
    sleep(0.2)
    
    if tem == 0:
        search = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[6]")
        search.click()
    if tem == 1:
        search = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[7]")
        search.click()
    if tem == 2:
        search = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[8]")
        search.click()
    if tem == 3:
        search = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[9]")
        search.click()
    if tem == 4:
        search = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[10]")
        search.click()
    
    sleep(0.1)

    #二つ選択
    search = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]")
    driver.execute_script('arguments[0].click();', search)
    search = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]")
    driver.execute_script('arguments[0].click();', search)

    #送信する
    search = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div")
    driver.execute_script('arguments[0].click();', search)

    ###==ページが変わる==###

    search = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    driver.execute_script('arguments[0].click();', search)
    
    print(num)

