from argparse import ArgumentParser
import logging
from logging import FileHandler
from datetime import date
import os
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
    logger = logging.getLogger()
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

    #ここで定義した引数の解析をする
    args = parser.parse_args()

if __name__ == "__main__":
    main()