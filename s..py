import os, sys, time, smtplib
import time
from time import sleep
E = '\x1b[1;34m'
G = '\x1b[1;35m'
S = '\x1b[1;33m'
email = 'uinitnlayton@gmail.com'
password = 'jryb xhci ixvy zpjh'
victim = 'abuse@telegram.org'
victim2 = 'abuse@telegram.org'
victim3 = 'abuse@telegram.org'
victim4 = 'abuse@telegram.org'
victim5 = 'abuse@telegram.org'
victim6 = 'abuse@telegram.org'
victim7 = 'abuse@telegram.org'
sub = 'My channel was suspended due to an error. There is no violating content. Please be careful Telegram'
number = int(input(" [?] Amount: "))
class SMTP():
    def __init__(self):
        self.email = email
        self.password = password
        self.email = email
        self.password = password
        self.victim = victim
        self.message = f"""Subject : {sub}\n

Hello Telegram, I would like to inform you that my channel was suspended by mistake. I did not publish pornographic content. Please pay attention and review the information. My channel was suspended due to the use of some celebrities by bad people. Please lift the ban on my channel. Thank you and your efforts. I will attach a link to my channel below.

Channel link:  https://t.me/+WOJka2g0ARI4ZTJk

Channel ID: 1951570669
        """
        self.number = number

    def verify(self):

        server1 = smtplib.SMTP("smtp.gmail.com", 587)
        server1.ehlo()
        server1.starttls()

        try:
            server1.login(self.email, self.password)
        except smtplib.SMTPAuthenticationError:
            print('''
 [!] The email or password is wrong''')
            time.sleep(0)
            exit()

        SMTP().main()

    def main(self):
        if len(sys.argv) < 2:
            
            sys.stdout.write(f'''
            
        [!] Connected as: {self.email}
        [!] Victim: {self.victim}
        [!] Message: {self.message}  
        [!] Amount: {self.number}
        
        ''')

        option = input('''
 [?] Spam email? [y/n]: ''')
        if option == 'y':
            SMTP().spam()
            os.system("python main.py")
        if option == 'n':
            os.system("python main.py")
        else:
            print(''' 
 [!] Invalid option''')
            time.sleep(2)
            SMTP().main()
        
    def spam(self):
        time.sleep(0)
        server2 = smtplib.SMTP("smtp.gmail.com", 587)
        server2.ehlo()
        server2.starttls()
        server2.login(self.email, self.password)
        i = 0
        while i < self.number:
            i+=1
            sleep(2)
            server2.sendmail(self.email,[victim2,self.victim,victim3,victim4,
          victim5,victim6,victim7],self.message)
            if i == 1: 
                print(('\033[1;35m"  [S.L.R] ''%d salar_1+1=52-b : salar ')%(i))
            else:
                print(('\033[1;35m"  [S.L.R] ''%d salar_1+1=52-b : salar ')%(i))
            sys.stdout.flush()
        print('''
 [!] Process finished''')
        time.sleep(2)
            
if __name__ == '__main__':
    SMTP().verify()
