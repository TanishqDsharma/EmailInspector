from __future__ import print_function
from argparse import ArgumentParser, FileType
from email import message_from_file
from email.parser import HeaderParser


import re
import csv
__authors__ = ["Tanishq", "Shikhar"]
__date__ = "18/06/2021"
__description__ = "Utility to parse text and attachments from EML files"

def main(input_file):
    csv_file=input("Enter name of csv_file where you want to store analyzed headers:")
    emlfile = message_from_file(input_file)
    parser = HeaderParser()
    h = parser.parsestr(str(emlfile))
    received=h.get_all('Received')

    print("          ")

    print("\033[1;31;40mBasic Information about the email:\033[39m ")
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mFrom:\033[39m" + " "+str(h['From']))
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mTo:\033[39m"+" "+str(h['To']))
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mDate:\033[39m"+" "+str(h['Date']))
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mSubject:\033[39m"+" "+str(h['Subject']))
    print("          ")

    print("\033[1;31;40mCaptured Received headers for anaylsis:\033[39m")
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mTop-most received header:\033[39m"+" "+str(received[0]))
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mMiddle received header:\033[39m"+" "+str(received[1]))
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mBottom-most received header:\033[39m"+" "+str(received[2]))

    str(received)
    p1=re.compile(r"by\s([a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+|[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+|[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+|[a-zA-Z0-9-]+\s[a-zA-Z0-9-]+\s[a-zA-Z0-9-]+)")
    m1=p1.findall(str(received))
    p2=re.compile(r"from\s([a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+|[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+|[a-zA-Z0-9-]+)")
    m2=p2.findall(str(received))
    p5=re.compile(r"with\s[a-zA-Z]+")
    m5=p5.findall(str(received))
    p3=re.compile(r"[a-zA-Z]+,\s\d{1,2}\s[a-zA-Z]+\s\d{1,4}")
    m3=p3.findall(str(received))
    p4=re.compile(r"([a-zA-Z]+,\s\d{1,2}\s[a-zA-Z]+\s\d{1,4}\s\d{1,2}:\d{1,2}:\d{1,2}\s[+-][0-9]+|[a-zA-Z]+,\s\d{1,2}\s[a-zA-Z]+\s\d{1,4}\s\d{1,2}:\d{1,2}:\d{1,2}\.[0-9]|[a-zA-Z]+,\s\d{1,2}\s[a-zA-Z]+\s\d{1,4}\s\d{1,2}:\d{1,2}\d{1,2})")
    m4=p4.findall(str(received))
    v=len(m2)
    a=len(m5)
    
    print("          ")

    print("\033[1;31;40mAnalysis made on Received headers:\033[39m")
    print("-----------------------------------------------------------------------")
    
    print("\033[1;31;40mFor Topmost header:\033[39m")
    print("BY :" + m1[0])
    print("FROM :" + "NONE")
    print("With :" + m5[0])
    print("Date:"  + m3[0])
    print("Time:"  + m4[0])
    print("       ")
    print("\033[1;31;40mFor Middle header:\033[39m")
    print("BY :" + m1[1])
    print("FROM :" + m2[0])
    print("With :" + m5[1])
    print("Date:"  + m3[1])
    print("Time:"  + m4[1])
    print("       ")
    print("\033[1;31;40mFor Bottom-most header:\033[39m")
    print("BY :" + m1[2])
    if v==1:
        print("FROM :" + "NONE")
    else:
        print("FROM :" + m2[1])
    if a<3:
        print("With :" + "NONE")
    else:
        print("With :" + m5[2])
    print("Date:"  + m3[2])
    print("Time:"  + m4[2])
    


    print("          ")

    print("\033[1;31;40mSecurity Headers:\033[39m")
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mReceived-spf:\033[39m"+" "+str(h['Received-SPF']))
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mDKIM-Signature:\033[39m"+" "+str(h['DKIM-Signature']))
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mMessage-ID\033[39m"+" "+str(h['Message-ID']))
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mReturn-Path:\033[39m"+" "+str(h['Return-Path']))
    print("-----------------------------------------------------------------------")

    print("          ")

    print("\033[1;31;40mOther Informational Email Headers:\033[39m")
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mDelivered-To:\033[39m"+" "+str(h['Delivered-To']))
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mX-Received:\033[39m"+" "+str(h['X-Received']))
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mARC-Seal\033[39m"+" "+str(h['ARC-Seal']))
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mARC-Authentication-Results:\033[39m"+" "+str(h['ARC-Authentication-Results']))
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mReply-to:\033[39m"+" "+str(h['REPLY-TO']))
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mMIME-Version:\033[39m"+" "+str(h['MIME-Version']))
    print("-----------------------------------------------------------------------")
    print("\033[1;32;40mSender:\033[39m"+" "+str(h['Sender']))
    print("-----------------------------------------------------------------------")

   


    
    with open(csv_file, mode='w') as employee_file:
        header_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header_writer.writerow(['Basic Information about the email:'])
        header_writer.writerow(['From', h['From']])
        header_writer.writerow(['Subject', h['To']])
        header_writer.writerow(['Date', h['Date']])
        header_writer.writerow(['Subject', h['Subject']])
        
        header_writer.writerow(['Recevied Header analysis:'])
        header_writer.writerow(['Top-most Recevied Header:',received[0]])
        header_writer.writerow(['Middle Recevied Header:',received[1]])
        header_writer.writerow(['Bottom-most Recevied Header:',received[2]])
        
        header_writer.writerow(['Security Related Headers :'])
        header_writer.writerow(['Received-SPF', h['Received-SPF']])
        header_writer.writerow(['DKIM-Signature', h['DKIM-Signature']])
        header_writer.writerow(['Return-Path', h['Return-Path']])
        header_writer.writerow(['Message-id', h['Message-ID']])

        header_writer.writerow(['Other Headers :'])
        header_writer.writerow(['Delivered-To', h['Delivered-To']])
        header_writer.writerow(['X-Received', h['X-Received']])
        header_writer.writerow(['ARC-Seal', h['ARC-Seal']])
        header_writer.writerow(['ARC-Authentication-Results', h['ARC-Authentication-Results']])
        header_writer.writerow(['REPLY-TO', h['REPLY-TO']])
        header_writer.writerow(['MIME-Version', h['MIME-Version']])
        header_writer.writerow(['X-SMTPAPI', h['X-SMTPAPI']])
        header_writer.writerow(['Sender', h['Sender']])

if __name__ == '__main__':
    parser = ArgumentParser(
        description=__description__,
        epilog="Developed by {} on {}".format(
            ", ".join(__authors__), __date__)
    )
    parser.add_argument("EML_FILE",help="Path to EML File", type=FileType('r'))

                    
    args = parser.parse_args()

    main(args.EML_FILE)