from huawei_lte_api.Client import Client, Device
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.Connection import Connection

connection = AuthorizedConnection('http://admin:admin1@192.168.8.1/')

client = Client(connection) 

try:

    print(client.net.net_mode())
    
    print(client.device.signal())  # Can be accessed without authorization
    print(client.device.information())  # Needs valid authorization, will throw exception if invalid credentials are passed in URL

except Exception as e:
    print('error')
    print(e)

