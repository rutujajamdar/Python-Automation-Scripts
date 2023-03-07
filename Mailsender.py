import time
import smtplib
import schedule
from sys import argv
from email import encoders
from urllib.request import urlopen
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import ssl
import psutil
from sys import argv
import os
import time
from datetime import datetime

def is_connected() :
    try : 
        urlopen('http://www.google.com/',timeout=1)
        return True

    except Exception as err :
        return False

def MailSender(filename,time) :
    try :
        fromaddr = ""
        toaddr = ""

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """
        Hello %s,
        Welcome to our Application.
        Please find attached documnet which contains Log of Running Process.
        Log file is created at : %s

        This is auto generated mail.

        Thanks & Regards,
        Rutuja Jamdar

        """%(toaddr,time)

        subject = """
        Process log generated at : %s

        """%(time)

        msg['Subject'] = subject

        msg.attach(MIMEText(body,'plain'))

        fname =(os.path.splitext(os.path.basename(filename))[0])+'.log'
        attachment = open(filename,"rb")

        p = MIMEBase('applocation','octet-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition',"attachment;filename = %s" %fname)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com',587)

        s.starttls()

        s.login(fromaddr,"")

        text = msg.as_string()

        s.sendmail(fromaddr,toaddr,text)

        s.quit()

        print("Log file successfully send through mail")

        
    
    except Exception as E :
        print("Unable to send mail",E)

    
def ProcessLog(Directory_name) :
    listprocess = []
    log_dir = os.path.abspath(Directory_name)
    if not os.path.exists(log_dir):
        try :
            os.mkdir(log_dir)
        except :
            pass
    
    separator = "-" * 80
    dir_name = datetime.now().strftime('Marvellous_%H_%M_%d_%m_%Y.log')
    log_path = os.path.join(log_dir,dir_name)
    print(log_path)
    f = open(log_path,'w')
    f.write(separator + "\n")
    f.write("Process Logger : "+time.ctime()+"\n")
    f.write(separator + "\n")

    for proc in psutil.process_iter() :
        try :
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess) :
            pass

    for procinfo in listprocess :
        f.write("%s\n" % procinfo)

    MailSender(log_path,time.ctime())


def main() :
    if(is_connected()) :
        print("Connection successful")

    else :
        print("Connection failed")

    print("----------MailSender Application---------")

    print("Application name : "+argv[0])

    if(len(argv)!=2) :
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H") :
        print("This Script is used log record of running processess")
        exit()

    if(argv[1] == '-u') or (argv[1] == '-U') :
        print("usage : ApplicationName AbsolutPath_of_Directory")
        exit()

    try :
        schedule.every(1).minutes.do(ProcessLog,argv[1])
        while True :
            schedule.run_pending()
            time.sleep(1)

    except ValueError :
        print("Error : Invalid datatype of input")

    # except Exception as E :
    #     print("Error : Invalid input ",E)


if __name__ == "__main__" :
    main()

