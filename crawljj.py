# 네이버 블로그 크롤링
import parser

import requests # HTTP 접속
from bs4 import BeautifulSoup  # 웹페이지 파싱
from selenium import webdriver
import requests
import time
import parsing_blog
from parsing_blog import Parser
import download_naver_blog

""" 키워드 설정하기 """
driver = webdriver.Chrome("./chromedriver")
keyword = "서큘레이터"
accurate = ["\"정확\"", "\"자주\""]
mustin = ["%2B자주", "%2B포함"]
exceptf = [" -광고", " -빼고"]
driver.get("https://search.naver.com/search.naver?where=post&sm=tab_jum&query="+keyword+"+"+mustin[0]+exceptf[0])

'''
각 게시물 컨테이너 : li.sh_blog_top
게시물 제목 내의 링크 : li.sh_blog_top dt a 내부의 href 속성
게시물 텍스트 : div.se-module.se-module-text p span <- 문장단위로 태그가 달려있음
해시태그 : span.ell
공감 수 : em.u_cnt._count
'''
bloglinklist = driver.find_elements_by_css_selector("li.sh_blog_top dt a")
k=1
for i in bloglinklist:
    link=i.get_attribute('href')
    filename=str(k)+'.txt'
    k+=1
    download_naver_blog.run(link, filename)






