import SourceQuery


server = SourceQuery.SourceQuery('93.186.198.185')
print(server.get_info()['Ping'])
print(server.get_info()['Hostname'])
print(server.get_info()['Password'])
print(server.get_info()['GameDesc'])
print(server.get_info()['Players'])
print(server.get_info()['MaxPlayers'])
print(server.get_info()['Map'])
print(server.get_info()['Secure'])
print(server.get_info()['GamePort'])
print(server.get_info()['SteamID'])
print(server.get_info()['Tags'])
print(server.get_players())
print(server.get_rules())
