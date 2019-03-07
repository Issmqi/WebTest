import logging
import rootpath
class Log():

    def __init__(self):
        logPath = rootpath.get_rootpath() + r'\result\log\running.log'
        self.logger = logging.getLogger('WebTest')
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')
        # 使用FileHandler输出到文件
        fh = logging.FileHandler(logPath,encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        # 使用StreamHandler输出到屏幕
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(formatter)
        # 添加两个Handler
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)


    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

def main():
    logyyx = Log()
    logyyx.debug('一个debug信息cces')
    logyyx.info('一个info信息')
    logyyx.warn('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.critical('一个致命critical信息')


if __name__ == '__main__':
    main()

