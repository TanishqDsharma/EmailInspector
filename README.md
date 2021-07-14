# EmailInspector
Email Header Analysis is a web + CLI based project developed with the aim of investigating emails to distinguish malicious emails from genuine ones.

In today’s scenario where everything is going on in online mode and the main mode of communication is through emails, it becomes very difficult to identify fake/phishing emails and because of this the amount of fake/phishing email attacks have increased drastically. Employees with no knowledge about cyber security are the most vulnerable to such attacks and pose a major security concern to their organizations. 

Therefore having a solution to identify such emails with just one click would be a great help to society.  

## Intial Setup:
* <b>Follow the below steps and make sure you satisfy all requirements:</b>
  1. Install Python 3+: If you don't already have Python 3+ installed, grab it from https://www.python.org/downloads/. You'll want to download and install the latest version of        Python 3.x. As of 2019-10-14, that is Version 3.8.
  2. Install Dependencies: In a command prompt or Terminal window, navigate to the directory containing this repository's files. Then, type the following, and press enter:
     pip install -r requirements.txt
 
## Intial Setup using docker:
* <b>Follow the below steps:</b>
   1. docker pull tanishq512/email-image1:2
   2. docker run -p 80:80 tanishq512/email-image1:2  
     
### EmailInspector Usage with web Interface:
* Follow the below steps:
  1. In command prompt type python EmailInspector-Web.py, this will run the server then follow the link: http://127.0.0.1:5000
  
     ![alt text](https://github.com/TanishqDsharma/EmailInspector/blob/main/screenshots/2021-06-27%2015_05_24-EmailInspector-Web.py%20-%20EmailInspector.png)
  
  2. Now paste your email data in text area  
     
     ![alt text](https://github.com/TanishqDsharma/EmailInspector/blob/main/screenshots/2021-06-27%2015_10_17-Mail.png)
  
  3. After pasting your email data in Click on "Analyze it" button and you will get your email data Analyzed.
     
     ![alt text](https://github.com/TanishqDsharma/EmailInspector/blob/main/screenshots/2021-06-27%2015_10_58-Response.png)
     
     ![alt text](https://github.com/TanishqDsharma/EmailInspector/blob/main/screenshots/2021-06-27%2015_11_22-Response.png)

### EmailInspector Usage with CLI:
* Follow the below steps:
  1. In the command prompt or Terminal window, type the following, and press enter: <b>python EmailInspector.py<b> <file>
     Replace <file> with any txt which have the email data. [you can get the email data by logging into your gmail selecting any email and after that clicking on "show original
      message",copy the data from "show original message" and paste it in a txt file]
  

     
     




