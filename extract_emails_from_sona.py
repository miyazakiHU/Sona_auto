from bs4 import BeautifulSoup

FILE_PATH = 'sona.html'
OUTPUT_FILE_NAME = "extracted_emails.txt"

soup = BeautifulSoup(open(FILE_PATH,encoding="utf-8"), 'html.parser')

email_list = []

# 100個以上メールアドレスがある場合は知らん
for i in range(1,100):
    element = soup.find(id=f"ctl00_ContentPlaceHolder1_repSignUps_ctl{str(i).zfill(2)}_HyperLinkEmail")
    
    if element is None: break
    else:
        email_list.append(element.text[1:-1])


with open(OUTPUT_FILE_NAME, 'w') as f:
    for email in email_list:
        f.write(f"{email}\n")

