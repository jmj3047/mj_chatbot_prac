#!C:\Python310\python.exe
# -*- coding:utf-8 -*-
import sys
import codecs
sys.stdout =codecs.getwriter("utf-8")(sys.stdout.detach())
import cgi
# cgitb는 CGI 프로그래밍시 디버깅을 위한 모듈로 cgitb.enable()할 경우 런타임 에러를 웹브라우저로 전송함
# cgitb.enable() 하지 않은 상태로 실행 중 오류가 발생한 경우 웹서버는 클라이언트에게 HTTP응답 코드 500을 전송함
import cgitb
cgitb.enable()
# HTTP 규격에서 헤더 전송 이후에는 반드시 줄 바꿈을 하게되어 있음으로 마지막에 \r\n을 전송
# 마지막에 \r\n을 전송하지 않으면 브라우저 측에서 오류가 발생
print("Content-type: text/html;charset=utf-8\r\n")
print("""
      <!doctype html>
      <html>
      <head>
      <meta charset='utf-8'>
      <h1>안녕?</h1>
      <h2>Thank you so much</h2>
      <h3>This page is made by Python</h3>     
      """)
a = 3+4+5
b = a/3
print('b는 :', b)
print("</head>")
print("</html>")