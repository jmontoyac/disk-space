#import rabbitFunctions as rabbit
import os
import logging
import logging.handlers as handlers

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    filename='/var/log/bucket.log',
                    filemode='w')


logHandler = handlers.TimedRotatingFileHandler('/var/log/bucket.log',
                                               when='midnight',
                                               interval=1,
                                               backupCount=3)

logger = logging.getLogger('bucket')
logger.addHandler(logHandler)


def createTestData(numberOfFiles):
    lista = []
    for i in range(numberOfFiles):
        dict = {'id': str(i), 'pathfile': '/images/IMG' + str(i) + '.jpg'}
        lista.append(dict)
    #rabbit.publish_to_rabbit('delete_list', lista, 'rabbitmq')
    return lista


def buildCommands():
    myFiles = createTestData(10)
    deleteList = []
    for dict in myFiles:
        deleteFile = {
            'id': dict['id'], 'pathfile': dict['pathfile'], 'command': 'rm ' + dict['pathfile']}
        deleteList.append(deleteFile)
        print(deleteFile['id'] + ':' +
              deleteFile['pathfile'] + deleteFile['command'])


def deleteFiles(myFiles):
    for file in myFiles:
        try:
            print('Removing: ' + file['pathfile'])
            logger.debug('Removing: ' + file['pathfile'])
            # os.remove(file['pathfile'])
        except Exception as e:
            logger.debug('Error during file deletion: ' + str(e))
            print('Error during file deletion: ' + str(e))


# Main
# buildCommands()
f = createTestData(5)
deleteFiles(f)
