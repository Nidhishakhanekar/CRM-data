import logging


class Loggenerator:
    @staticmethod
    def logger():
        logName=logging.getLogger()
        logFile=logging.FileHandler("C:\\Users\\pradi\\OneDrive\\Desktop\\python new file\\cybage\\Log\\log.log")
        Format=logging.Formatter("%(asctime)s:%(funcName)s:%(message)s")
        logFile.setFormatter(Format)
        logName.addHandler(logFile)
        logName.setLevel(logging.INFO)
        return logName
