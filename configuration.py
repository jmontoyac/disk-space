import configparser

bucketsList = []
bucketData = {}

config = configparser.ConfigParser()
config.read('/bucket_config/config.ini')
sections = config.sections()

# Read configuration file and load data in list 'bucketData'


def loadConfiguration():
    i = 0
    try:
        for section in sections:
            print('Section: ' + section)
            print('ID: ' + config[section]['ID'])
            print('TYPE: ' + config[section]['TYPE'])
            print('STATE: ' + config[section]['STATE'])
            print('PATH: ' + config[section]['PATH'])
            print('Valor de i: ' + str(i))
            bucketData[i] = {
                'ID': config[section]['ID'],
                'TYPE': config[section]['TYPE'],
                'STATE': config[section]['STATE'],
                'PATH': config[section]['PATH']
            }
            i = i + 1
    except Exception as e:
        print('Error in config file, section ' + section + ': ' + str(e))


def getActiveBucket():
    for section in sections:
        if (config[section]['STATE'] == 'ACTIVE'):
            print('Found active bucket  with ID: ' +
                  str(config[section]['ID']))
            bucketData = {
                'ID': config[section]['ID'],
                'TYPE': config[section]['TYPE'],
                'STATE': config[section]['STATE'],
                'PATH': config[section]['PATH']
            }
            return bucketData


# Main
loadConfiguration()
getActiveBucket()
