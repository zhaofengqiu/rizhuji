import re
import time
import requests
from bs4 import BeautifulSoup
from util import write,post
from config import SMTPPASSWD,EMAIL,PRODUCT,STOPTIME
SENDER = FROMADDR = EMAIL
while True:
    msg=''
    ans = requests.get("https://rizhuji.com/cart.php?gid=8")
    
    soup = BeautifulSoup(ans.text,'html.parser')
    for product_id in PRODUCT:
        res = soup.find_all(attrs={'id':product_id})
        if len(res)>0:
            datatxt = res[0].get_text()
            if '可用' in datatxt:
                    msg = msg+'\n========================================\n\n'+datatxt
    if msg!='':
        emailText = write(msg,FROMADDR,SENDER)
        post(emailText,FROMADDR,SENDER,SMTPPASSWD)
    time.sleep(STOPTIME)