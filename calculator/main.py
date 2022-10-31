import controller as c
import logging as log

# если хотим, чтобы логи выводились в консоль
log.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=log.INFO)


c.run(log)