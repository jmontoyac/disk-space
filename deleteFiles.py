#import rabbitFunctions as rabbit
import os
import insLogger
import rabbitFunctions as rabbit

logger = insLogger.logging.getLogger('bucketController')
logger.addHandler(insLogger.logHandler)


def createTestData(numberOfFiles):
    lista = []
    for i in range(numberOfFiles):
        dict = {'id': str(i), 'pathfile': '/images/IMG' + str(i) + '.jpg'}
        lista.append(dict)
    rabbit.publish_to_rabbit('delete_list', lista, 'rabbitmq')
    # return lista


def deleteFiles(myFiles):
    response = []
    for file in myFiles:
        try:
            # os.remove(file['pathfile'])
            print('Deleting: ' + file['pathfile'] + ' SUCCESS')
            logger.debug('Deleting: ' + file['pathfile'] + ' SUCCESS')
            operationResult = {'id': file['id'], 'result': 'SUCCESS'}
        except Exception as e:
            logger.error('Error during file deletion for ID: ' +
                         file['id'] + ' ' + str(e))
            print('Error during file deletion: ' + str(e))
            operationResult = {'id': file['id'], 'result': 'FAILED'}
        response.append(operationResult)
    rabbit.publish_to_rabbit('delete_result', response, 'rabbitmq')


# Main
# buildCommands()
# f = createTestData(5)
# deleteFiles(f)
