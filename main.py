from argparse import ArgumentParser
import logging
from logging import FileHandler
from datetime import date
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart#拡張用
def main():
    log_dirname = "logs"
    os.makedirs(log_dirname, exist_ok=True)
    today = date.today()
    formatted_date = today.strftime("%Y%m%d")
    logfile_name = f"{formatted_date}_mail_sender.log"
    logfile_path = os.path.join(log_dirname, logfile_name)
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s ",
        datefmt="[%X]",
        handlers=[FileHandler(filename=logfile_path)]
    )
    logger = logging.getLogger(__name__)#__name__現在のモジュール名
    parser = ArgumentParser(description="Gmailを飛ばす用")
    parser.add_argument(
        "--to",
        required=True,
        type=str,
    )
    parser.add_argument(
        "--subject",
        required=False,
        type=str,
        default="No Subject"
    )
    parser.add_argument(
        "--body",
        required=False,
        type=str,
        default="Hello from Python"
    )

    logger.info("引数の解析を開始します")
    args = parser.parse_args()
    logger.info("引数の解析が終了しました")

    logger.info("環境変数の取得をします")
    user = os.environ.get("GMAIL_USER")
    password = os.environ.get("GMAIL_PASS")
    if not user or not password:
        logger.error("GMAIL_USER or GMAIL_PASS is not set in environment variables.")
        return
    msg = MIMEText(args.body)#本文
    msg["Subject"] = args.subject
    msg["From"] = user
    msg["To"] = args.to

    logger.info("メールを送信します")
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(user, password)
            server.send_message(msg)
        logger.info("メールの送信に成功")
    except Exception as e:
        logger.error(f"メールの送信に失敗しました: {e}")

if __name__ == "__main__":
    main()