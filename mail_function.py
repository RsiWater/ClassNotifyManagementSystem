import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def prepare(account,password):
    smtp=smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(account,password)
    return smtp

def hw(schoolnum_l,score_l,account,smtp):
    for i in range(len(schoolnum_l)):
        from_addr=account
        to_addr=schoolnum_l[i]+'@mail.nuk.edu.tw'

        s='作業分數: '+score_l[i]+'分'
        mime=MIMEText(s, "plain", "utf-8")
        mime["Subject"]='作業'

        msg=mime.as_string()
        status=smtp.sendmail(from_addr, to_addr, msg)
        if status=={}:
            print("郵件傳送成功!")
        else:
            print("郵件傳送失敗!")

def hw_total(schoolnum_l,score_l,account,smtp):
    for i in range(len(schoolnum_l)):
        from_addr=account
        to_addr=schoolnum_l[i]+'@mail.nuk.edu.tw'

        s='作業累積總分數: '+score_l[i]+'分'
        mime=MIMEText(s, "plain", "utf-8")
        mime["Subject"]='作業累積總分'

        msg=mime.as_string()
        status=smtp.sendmail(from_addr, to_addr, msg)
        if status=={}:
            print("郵件傳送成功!")
        else:
            print("郵件傳送失敗!")

def roll_call(schoolnum_l,account,smtp):
    for i in range(len(schoolnum_l)):
        from_addr=account
        to_addr=schoolnum_l[i]+'@mail.nuk.edu.tw'

        s='點名成功'
        mime=MIMEText(s, "plain", "utf-8")
        mime["Subject"]='點名'

        msg=mime.as_string()
        status=smtp.sendmail(from_addr, to_addr, msg)
        if status=={}:
            print("郵件傳送成功!")
        else:
            print("郵件傳送失敗!")

def roll_call_total(schoolnum_l,score_l,account,smtp):
    for i in range(len(schoolnum_l)):
        from_addr=account
        to_addr=schoolnum_l[i]+'@mail.nuk.edu.tw'

        s='點名累積總分數: '+score_l[i]+'分'
        mime=MIMEText(s, "plain", "utf-8")
        mime["Subject"]='點名累積總分'

        msg=mime.as_string()
        status=smtp.sendmail(from_addr, to_addr, msg)
        if status=={}:
            print("郵件傳送成功!")
        else:
            print("郵件傳送失敗!")

def shutdown(smtp):
    smtp.quit()
    



