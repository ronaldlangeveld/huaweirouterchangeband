from huawei_lte_api.Client import Client, Device
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.Connection import Connection

connection = AuthorizedConnection('http://admin:admin1@192.168.8.1/')

client = Client(connection) # This just simplifies access to separate API groups, you can use device = Device(connection) if you want
# lteband = 20000000000 #default 7FFFFFFFFFFFFFFF

    # ('b1', 'FDD', '2100', '1'),
    # ('b2', 'FDD', '1900', '2'),
    # ('b3', 'FDD', '1800', '4'),
    # ('b4', 'FDD', '1700', '8'),
    # ('b5', 'FDD', '850', '10'),
    # ('b6', 'FDD', '800', '20'),
    # ('b7', 'FDD', '2600', '40'),
    # ('b8', 'FDD', '900', '80'),
    # ('b19', 'FDD', '850', '40000'),
    # ('b20', 'FDD', '800', '80000'),
    # ('b26', 'FDD', '850', '2000000'),
    # ('b28', 'FDD', '700', '8000000'),
    # ('b32', 'FDD', '1500', '80000000'),
    # ('b38', 'TDD', '2600', '2000000000'),
    # ('b40', 'TDD', '2300', '8000000000'),
    # ('b41', 'TDD', '2500', '10000000000'),

try:
    
    lteband = 40
    networkband = "3FFFFFFF"
    networkmode = "03"
    setBand = client.net.set_net_mode(lteband=lteband, networkband=networkband, networkmode=networkmode)
    setBand
    print('success')

except Exception as e:
    print('error')
    print(e)

