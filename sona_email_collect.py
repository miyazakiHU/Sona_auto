from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ID・パスワード，SonaシステムのURLを定義
ID = "ID"  # IDを入力してください
PASS = "PASS"  # パスワードを入力してください
URL = "https://hup.sona-systems.com/"
DELETE_PATH = "delete_emails.txt"  # 削除するメールアドレスを保存するファイル名を指定してください
REMAIN_PATH = "remain_emails.txt"  # 削除しないメールアドレスが保存されてあるtxtファイルを指定してください
DELETE_CONDITION = ["B17","b17","M19","m19"]  # 削除するアカウントの学生番号の最初の三文字を指定してください
SEARCH_WORD = "b17 m19"  # 検索時に使用する文字列を指定してください

delete_emails = []
remain_emails = []

# 削除しないアカウントのメールアドレスを取得
with open(REMAIN_PATH) as f:
    for s_line in f:
        # 改行コードを取り除く
        remain_emails.append(s_line.rstrip('\n'))

# chromeを起動
driver = webdriver.Chrome()
driver.get(URL)

# IDとパスワードを入力して，ログインボタンをクリック
driver.find_element_by_id("ctl00_ContentPlaceHolder1_userid").send_keys(ID)
driver.find_element_by_id("ctl00_ContentPlaceHolder1_pw").send_keys(PASS)
driver.find_element_by_id("ctl00_ContentPlaceHolder1_default_auth_button").click()

# User Management から View and Edit Users をクリック
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[-1])
driver.get('https://hup.sona-systems.com/admin_view_userlist.aspx')

# 削除するアカウントを検索
driver.find_element_by_id("txtSearch").send_keys(SEARCH_WORD)
driver.find_element_by_id("ctl00_ContentPlaceHolder1_Search").click()

def get_student_number(n):
    driver.find_element_by_id(f"ctl00_ContentPlaceHolder1_repSearchResult_ctl{str(n+1).zfill(2)}_Name").click()
    num = driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtStudentID").get_attribute("value")
    driver.back()
    return num

def get_delete_emails(page, delete_emails):
    for i in range(100):
        try:
            email_temp = driver.find_element_by_id(f"ctl00_ContentPlaceHolder1_repSearchResult_ctl{str(i+1).zfill(2)}_NameHyperLink").text
            student_number = get_student_number(i)
            
            if not(email_temp in remain_emails) and (student_number[0:3] in DELETE_CONDITION):
                delete_emails.append(email_temp)
                print(f"{email_temp}を削除対象リストに追加しました。")
                print(f"学生番号：{student_number}")
                print()

            else:
                print(f"{email_temp}は削除対象外です。")
                print(f"学生番号：{student_number}")
                print()
        except:
            print(f"最終行（{i+1}行）まで来ました。{page+1}ページへ遷移します。")
            try:
                driver.find_element_by_id(f"ctl00_ContentPlaceHolder1_repSearchResult_ctl51_UserPager_rptPages_ctl{str(page+1).zfill(2)}_lnkPage").click()
                return get_delete_emails(page+1,delete_emails)
            except:
                print(f"最終ページ（{page}ページ）まで来ました。結果を出力します。")
                print()
                break

# 関数を実行
get_delete_emails(1,delete_emails)

# 削除するアカウントのEmailを表示
print(delete_emails)

# txtでEmailを出力
with open(DELETE_PATH, mode="w") as f:
    f.write("\n".join(delete_emails))

print(f"以上の結果は{DELETE_PATH}に保存されました。")

# chromeを終了する
driver.quit()
