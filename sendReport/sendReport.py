import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

from utils.parseXml import parseXml


def send():
    sender = 'shjpl23801@163.com'
    receiver = 'liujun@jielema.com'
    username = 'shjpl23801'
    password = '111235422a'

    # 邮件主题
    mail_title = '时光序接口测试报告'

    # 读取html文件内容
    f = open('F:\\code\\apitest\\report\\report.html', 'rb')
    mail_body = f.read()
    f.close()

    #拼接html
    h = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Title</title></head><body><h2>时光序接口自动化测试报告</h2>'
    dotime = "<p>测试时间：" + str(datetime.datetime.now())
    total = "<p>执行接口用例： " + parseXml()["tests"] + " 条"
    runTime = "<p>测试耗时：" + parseXml()["time"] + "秒"
    passCounts = "<p>测试通过：" + str(int(parseXml()["tests"]) - int(parseXml()["failures"])) + "条"
    failCounts = "<p>测试失败：" + parseXml()["failures"] + "条"
    a = "<p>================================执行失败用例及详情请打开附件网址========================="
    end = "<p></body></html>"

    body = h+dotime+total+runTime+passCounts+failCounts+a+end

    # 邮件内容, 格式, 编码
    message = MIMEMultipart()
    message.attach(MIMEText(body, 'html', 'utf-8'))
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open('H:\\code\\apitest\\report\\report.html', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    message.attach(att1)

    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, message.as_string())
        print("发送邮件成功！！！")
        smtp.quit()
    except smtplib.SMTPException:
        print("发送邮件失败！！！")

