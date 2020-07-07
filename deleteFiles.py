import rabbitFunctions as rabbit


def createTestData(numberOfFiles):
    lista = []
    for i in range(numberOfFiles):
        dict = {'id': str(i), 'pathfile': '/images/IMG' + str(i)}
        lista.append(dict)
    rabbit.publish_to_rabbit('delete_list', lista, 'rabbitmq')
