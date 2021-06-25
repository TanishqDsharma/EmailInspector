from flask import Flask, render_template, request, redirect
from argparse import ArgumentParser, FileType
from email import message_from_file
from email.parser import HeaderParser
import re

sample=Flask(__name__)

@sample.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        header = request.form['headers']
        parser = HeaderParser()
        h = parser.parsestr(header)
        list1=[h['Subject'],h['Message-ID'],h['Received-SPF'],h['From'],h['To'],h['DKIM-Signature'],h['Return-Path'],h['X-Google-Smtp-Source']
                 ,h['X-Received'],h['Authentication-Results'],h['REPLY-TO'],h['X-SMTPAPI'],h['X-SENDCLOUD-LOG-NEW'],h['MIME-Version'],h['Content-Type']
                 ,h['Content-Transfer-Encoding'],h['Delivered-To'],h['ARC-Seal'],h['ARC-Message-Signature']]
        received_header=h.get_all('Received')
        str(received_header)
        p1=re.compile(r"by\s([a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+|[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+|[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+|[a-zA-Z0-9-]+\s[a-zA-Z0-9-]+\s[a-zA-Z0-9-]+)")
        m1=p1.findall(str(received_header))
        p2=re.compile(r"from\s([a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+|[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+|[a-zA-Z0-9-]+)")
        m2=p2.findall(str(received_header))
        p5=re.compile(r"with\s[a-zA-Z]+")
        m5=p5.findall(str(received_header))
        p4=re.compile(r"([a-zA-Z]+,\s\d{1,2}\s[a-zA-Z]+\s\d{1,4}\s\d{1,2}:\d{1,2}:\d{1,2}\s[+-][0-9]+|[a-zA-Z]+,\s\d{1,2}\s[a-zA-Z]+\s\d{1,4}\s\d{1,2}:\d{1,2}:\d{1,2}\.[0-9]|[a-zA-Z]+,\s\d{1,2}\s[a-zA-Z]+\s\d{1,4}\s\d{1,2}:\d{1,2}\d{1,2}|\d{1,2}\s[a-zA-Z]+\s[0-9]+\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}\s[+-][0-9]+)")
        m4=p4.findall(str(received_header))
        m1_len=len(m1)
        m2_len=len(m2)
        m4_len=len(m4)
        m5_len=len(m5)
       
       

        return render_template('result.html',list1= list1,received_header=received_header,m1=m1,m5=m5,m4=m4,m2=m2,m1_len=m1_len,m2_len=m2_len,m4_len=m4_len,m5_len=m5_len)
    else:
        return render_template('index.html')



sample.run(debug=True)