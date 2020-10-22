from rcon import Console

console = Console(host='93.186.198.185', password='Rfcd2025', port=27017)
console.command('listgamemodeproperties')
console.close()