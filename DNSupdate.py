import sys
import logging
import requests

def updateIP(username="", password="", currentIP=""):
    #setup logging
    logging.basicConfig(level = logging.INFO)
    logger = logging.getLogger(__name__)

    handler = logging.FileHandler('DNSupdate.log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    #api calls
    logger.info('Posting IP update')

    url = 'https://domains.google.com/nic/update'
    data = {'hostname': 'flowersync.com', 'myip': currentIP}

    post_response = requests.post(url, data, auth = (username, password))

    logger.info('Posted request with a response of {}'.format(post_response.text))

if __name__ == '__main__':
    updateIP(username = sys.argv[1], password = sys.argv[2], currentIP = sys.argv[3])
