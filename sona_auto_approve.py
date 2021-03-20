from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ID・パスワード，SonaシステムのURLを定義
ID = "ID"  # IDを入力してください
PASS = "PASSWORD"  # パスワードを入力してください
URL = "https://hup.sona-systems.com/"
NUM_OF_APPROVE = 10

# chromeを起動
driver = webdriver.Chrome()
driver.get(URL)

# IDとパスワードを入力して，ログインボタンをクリック
driver.find_element_by_id("ctl00_ContentPlaceHolder1_userid").send_keys(ID)
driver.find_element_by_id("ctl00_ContentPlaceHolder1_pw").send_keys(PASS)
driver.find_element_by_id("ctl00_ContentPlaceHolder1_default_auth_button").click()


def approve_account(num_of_approve):
    # Over View から Participants Needing Approval をクリック
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get("https://hup.sona-systems.com/admin_pending_approvals.aspx")

    # ActionとしてApproveをクリック(全員分)
    for i in range(num_of_approve):
        driver.find_element_by_id(f"ctl00_ContentPlaceHolder1_repParticipants_ctl{str(i).zfill(2)}_Approve").click()

    # Process Changesをクリック
    driver.find_element_by_id(f"ctl00_ContentPlaceHolder1_Submit").click()

# 関数を実行
approve_account(num_of_approve = NUM_OF_APPROVE)

# chromeを終了する
driver.quit()
