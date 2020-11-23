import bin.SourceQuery as sq


server = sq.SourceQuery('127.0.0.1', 27131)
# print(server.get_info()['Ping'])
# print(server.get_info()['Hostname'])
# print(server.get_info()['Password'])
# print(server.get_info()['GameDesc'])
# print(server.get_info()['Players'])
# print(server.get_info()['MaxPlayers'])
# print(server.get_info()['Map'])
# print(server.get_info()['Secure'])
# print(server.get_info()['GamePort'])
# print(server.get_info()['SteamID'])
# print(server.get_info()['Tags'])
print(server.get_players())
for player in server.get_players():
    print("{id:<2} {Name:<35} {Frags:<5} {PrettyTime}".format(**player))
# print(server.get_rules())
