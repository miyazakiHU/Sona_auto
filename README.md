# ソナシステムのアカウント承認・削除を自動で行うプログラムです。

## 【動作確認環境】
・Python：3.8.3  
・Selenium：3.141.0  
・Google Chrome：89.0.4389.90（Official Build） （64 ビット）  

## 【前準備】
1.Python3をインストールして，Seleniumをpipでインストールしてください。  
2.全てのファイル（delete_emails.txt・remain_emails.txt・sona_auto_approve.py・sona_auto_delete.py・sona_email_collect.py）を同じフォルダーにダウンロードしてください。※フォルダー名と場所は任意で構いません。  
3.Google Chromeをインストールして，そのバージョンに対応するChromedriverを「2」で作成したフォルダにダウンロードして下さい。  

## 【使い方】  
A.アカウントを削除したい  
⇒アカウントのメールアドレスが分かっている⇒A1，メールアドレスが分からない⇒A2  
B.アカウントを承認したい  
⇒承認申請が出されている全てのアカウントを承認したい⇒B1，一部のアカウントのみを承認したい。⇒申し訳ございません。そのような機能は実装しておりません。  

### 【A1：sona_auto_delete.pyを使用します】  
1.削除したいアカウントのメールアドレスをdelete_emails.txtに入力してください。  
2.sona_auto_delete.pyの6行目と7行目にソナの管理者アカウントのIDとパスワードを入力してください。  
3.sona_auto_delete.pyを実行してください。※最終確認が行われますので，表示内容に問題がなければ"y"を入力しEnterキーを押してください。それ以外の入力があった場合，アカウント削除は行われません。  

### 【A2：sona_email_collect.pyとsona_auto_delete.pyを使用します】  
1.sona_email_collect.pyの6行目と7行目にソナの管理者アカウントのIDとパスワードを入力してください。  
2.sona_email_collect.pyの11行目に削除するアカウントの学生番号の最初の三文字を指定してください。また，12行目にアカウント検索時のキーワードを入力してください。  
3.「2」で指定した学生番号を持つアカウントに削除したくないアカウントが含まれる場合は，remain_emails.txtにそのアカウントのメールアドレスを入力してください。  
4.sona_email_collect.pyを実行してください。（delete_emails.txtが生成され，その中に削除対象のアカウントのメールアドレスが保存されます。）  
5.sona_auto_delete.pyの6行目と7行目にソナの管理者アカウントのIDとパスワードを入力し，sona_auto_delete.pyを実行してください。  

### 【B1：sona_auto_approve.pyを使用します】  
1.sona_auto_approve.pyの9行目に承認するアカウントの総数を入力してください。※推奨最大値は50です。それ以上はエラーが発生する可能性があります。  
2.sona_auto_approve.pyの6行目と7行目にソナの管理者アカウントのIDとパスワードを入力してください。  
3.sona_auto_approve.pyを実行してください。  
※51以上のアカウントを承認したい場合は何度もsona_auto_approve.pyを実行してください。  

2022/10/31 実験参加者のメールアドレスを抽出するコードを追記
【使い方】
1. sonaシステムの「時間枠」をクリック⇒「2022-10-15 23:00」みたいなやつをクリックして、参加者のメールアドレスが表示されるページに移動する。
2. ページのソースを表示する（WindowsだとCtrl+U）
3. Ctrl+Aでソースを全選択して、選択部分を「sona.html」として保存する。
　※例えば、メモ帳を開いて中身をCtrl+Vでペーストして、「名前を付けて保存」で「sona.html」を指定する。
4. 3で作成した「sona.html」と同じディレクトリ（以下、作業ディレクトリ）に「extract_emails_from_sona.py」をダウンロードする。
5. コマンドプロンプト等で作業ディレクトリに移動し、「extract_emails_from_sona.py」を実行する。
6. 作業ディレクトリに「extracted_emails.txt」が生成され、その中に参加者のメールアドレス一覧がある。
※beautifulsoup4のインストールが必要

