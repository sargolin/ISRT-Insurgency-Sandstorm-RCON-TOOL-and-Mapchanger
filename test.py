
test = {'Coop_b': 'true', 'CustomRules_b': 'false', 'Day_b': 'true', 'GameMode_s': 'Checkpoint', 'MatchServer_b': 'false', 'ModList_s': '98145,109375,95897', 'Mods_b': 'true', 'Mutated_b': 'true', 'Mutators_s': 'NoRestrictedArea', 'Night_b': 'false', 'OfficialRuleset_b': 'false', 'PlrC_i': '0', 'PlrM_i': '6', 
'Pwd_b': 'false', 'RankedServer_b': 'true', 'S': '523', 'Versus_b': 'false'}

mutator = test.get('ModList_s')

if mutator:
        print("existing")
else:
        print("Not existing")
