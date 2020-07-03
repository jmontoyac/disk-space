import configparser

bucketsList = []
bucketData = {}

config = configparser.ConfigParser()
config.read('config.ini')


# Read configuration file and load data in list 'bucketData'
def loadConfiguration():
    sections = config.sections()
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


# Main
loadConfiguration()
