import os
import logging
import zipfile
import hashlib

# -----設定部分-----start

FORMAT = '%(asctime)s [%(levelname)s]:%(message)s'
FILE_NAME = 'USJ-DataPack.zip'
ALLOW_LIST = ["pack.mcmeta", "pack.png", "LICENSE", "README.md"]
DIRECTORY = "data"

# -----設定部分-----end


logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logging.info("実行開始")


def write(ziph, root, file):
    ziph.write(os.path.join(root, file))
    logging.info(root+"/" + file)


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        dir = root.encode().decode()
        if (dir.startswith(DIRECTORY, 2)):
            for file in files:
                write(ziph, root, file)
        elif (dir == "."):
            for file in files:
                for allowFile in ALLOW_LIST:
                    if (file == allowFile):
                        write(ziph, root, file)
                        continue


logging.info("zipファイルにしています...")
zipf = zipfile.ZipFile(FILE_NAME, 'w', zipfile.ZIP_DEFLATED)
zipdir('.', zipf)
zipf.close()

logging.info("zipファイルが生成されました")
logging.info("ファイルの場所:\n" + os.path.abspath(FILE_NAME))


with open(FILE_NAME, 'rb') as file:
    logging.info('sha1:  ' + hashlib.sha1(file.read()).hexdigest())

input("Enterキーで、この画面を閉じます")

logging.info("プログラムを終了します")
