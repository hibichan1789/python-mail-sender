# Gmail Sender CLI
Python と Dockerを使ってコマンドラインからGmailを送信するツール  



# 以下のように.envファイルの作成をしてください
GMAIL_PASS はgoogleのアカウント→セキュリティとログイン→2段階認証プロセス→アプリパスワードから発行可能  
GMAIL_USER=your-email@gmail.com  
GMAIL_PASS=xxxx-xxxx-xxxx-xxxx  


# ビルドと実行
docker compose build  
docker compose run --rm app --to "recipient@example.com" --subject "テスト" --body "Dockerから送信！"  

# ライブラリを追加した場合
docker compose buildをし直す  

# 追加した機能
環境変数から取得 os.environ.get("")  
メール送信機能の追加  
MIMETextの使用  
smtplib.SMTP_SSLで送信の実装  
# 今回のエラー修正



# 今回の勉強内容
DockerfileのENTRYPOINT["python", "main.py"]は固定コマンドになる  
docker-compose run はdocker-compose.ymlを探す→build: . カレントディレクトリにあるDockerfileを使うということ  
run --rm　は一度実行した後に即座にコンテナが消える  
docker compose up -d --buildはAPIなどの常駐型  
.envは .gitignore, .dockerignoreに必ず入れる(情報が漏洩するから) 
logの導入をした。logファイルは履歴が汚れるし、ログに個人情報が入っていた場合漏洩する可能性があるから.gitignoreに追加する  
shift + Enter or 半角スペース2個で.mdファイルは改行  
["%X"]はdocker内だと標準時になるらしい  

# 今日勉強したコマンド、ショートカット
ctrl + p ファイルを開けれる  
ctrl + w 現在のファイルを閉じる  
ctrl + tab ファイルを切り替えれる  
ctrl + 1 vscodeのコードにカーソルをフォーカス  
ctrl + ` ターミナルにカーソルをフォーカス  
ctrl + [ インデントを下げる  
ctrl + ] インデントする　インデントはpythonでは必須級！  
ni ファイル名 ファイルを作成  

