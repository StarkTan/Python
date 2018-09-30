import logging
logging.basicConfig(
                level=logging.DEBUG,
                format='%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='logging1.log',
                filemode='w')
logging.info('logging1')
logging.basicConfig(
                level=logging.DEBUG,
                format='%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='logging2.log',
                filemode='w')
logging.info('logging2')