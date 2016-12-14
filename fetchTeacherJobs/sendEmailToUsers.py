# -*- coding: utf-8 -*- 

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import codecs
import json

def _fromat_addr(s):
	name, addr = parseaddr(s)
	return formataddr((\
		Header(name, 'utf-8').encode(), \
		addr.encode('utf-8') if isinstance(addr, unicode) else addr))


def writeMail():
	with codecs.open('first.json', 'r', encoding='utf-8') as f:
		td='<html><body>'
		i = 1
		for line in f.readlines():
			data = json.loads(line)
			title = data['title']
			time = data['time']
			category = data['category']
			count = data['count']
			address = data['content']
			link = data['herf']
			hasEng = False
			teach = ''
			index = -1
			for teacher in category:
				if (u'英语' in teacher) :
					teach = teacher
					hasEng = True
					index = index + 1
					break
			print title[0]
			print time[0]
			print teach
			print count[index]
			print link[0]
			if (hasEng) :
				tip = u'<p>-----------------------------第' + str(i) + u'条------------------------------</p>'
				tip = tip + u'<p>标题:' + title[0] + '</p>' 
				tip = tip + u'<p>发布日期：' + time[0] + '</p>'
				tip = tip + u'<p>招聘老师：' + teach + '</p>'
				tip = tip + u'<p>数量：' + count[index] + '</p>'
				tip = tip + u'<p><a href=\"' + link[0] + '\"' + u'>链接地址：' + link[0] + '</a></p>'
				td = td + tip
				i = i + 1
		td = td + "</body></html>"
		td = td.encode('utf-8')
		return td


from_addr = "15158074877@163.com"
from_password = "lpsb1992"
to_addr = "15158074877@163.com"
cc_addr = "18208986919@163.com"
smtp_server = "smtp.163.com"
msg = MIMEText(writeMail(), 'html', 'utf-8')
msg['From']=_fromat_addr(u'爬虫大师 <%s>' % from_addr)
msg['To']=_fromat_addr(u'管理员 <%s>' % to_addr)
msg['Cc']=cc_addr
msg['Subject']=Header(u'最近教师招聘信息', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, from_password)
server.sendmail(from_addr, [to_addr, cc_addr], msg.as_string())
server.quit()