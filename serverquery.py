import query

server = query.Query('93.186.198.185', 27016)
print(server.ping())
print(server.info())
print(server.players())
print(server.rules())