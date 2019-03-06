import logging

logging.basicConfig(level=logging.INFO, # 定义输出到文件的log级别
                    format='%(asctime)s [%(filename)s %(lineno)d ]: %(levelname)s  %(message)s',  # 定义输出log的格式
                    datefmt  = '%Y-%m-%d %A %H:%M:%S', # 时间
                    filename = "./logFilename.txt", # log文件名
                    filemode = 'a',  # 写入模式“w”或“a”

                    )

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("this is a info log")
    logger.info("this is a info log 1")