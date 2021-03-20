from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ID・パスワード，SonaシステムのURLを定義
ID = "ID"  # IDを入力してください
PASS = "PASS"  # パスワードを入力してください
URL = "https://hup.sona-systems.com/"
PATH = "delete_emails.txt"  # メールアドレスが保存されてあるtxtファイルを指定してください

Email_list = []
error_list = []

# 削除したいアカウントのメールアドレスを取得
with open(PATH) as f:
    for s_line in f:
        # 改行コードを取り除く
        Email_list.append(s_line.rstrip('\n'))

# 最終確認
print(Email_list)
print()
if (input("以上のメールアドレスに対してアカウント削除を実行します。よろしいですか？(y/n)") != "y"):
    print("作業を中断しました。アカウントは削除されていません。")
    exit()

# chromeを起動
driver = webdriver.Chrome()
driver.get(URL)

# IDとパスワードを入力して，ログインボタンをクリック
driver.find_element_by_id("ctl00_ContentPlaceHolder1_userid").send_keys(ID)
driver.find_element_by_id("ctl00_ContentPlaceHolder1_pw").send_keys(PASS)
driver.find_element_by_id("ctl00_ContentPlaceHolder1_default_auth_button").click()


def delete_account(email, e_list):
    # User Management から View and Edit Users をクリック
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get('https://hup.sona-systems.com/admin_view_userlist.aspx')

    # 削除するアカウントを検索
    driver.find_element_by_id("txtSearch").send_keys(email)
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_Search").click()

    try:
        # Delete Userボタンをクリック
        driver.find_element_by_id("ctl00_ContentPlaceHolder1_repSearchResult_ctl01_DeleteHyperLink").click()

        # アカウントを削除する (Yes, Deleteをクリックしたときに動作するJavascriptを実行する)
        driver.execute_script('WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions("ctl00$ContentPlaceHolder1$ctl03", "", true, "", "", false, true))')

        print(f"{email} は正常に削除されました。")


    # 削除できなかったアカウントを取得
    except:
        e_list.append(email)
        print(f"{email} は削除されませんでした。")

    #タブを閉じる
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# 削除を実行
for email in Email_list:
    delete_account(email, error_list)

# chromeを終了する
driver.quit()

# 削除できなかったアカウントのメールアドレスを取得
if (error_list != []):
    print("以下のメールアドレスに対応するアカウントの削除に失敗しました。")
    print(error_list)

else:
    print("全ての作業は正常に終了しました。")