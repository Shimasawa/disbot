import json
with open("databox/token.json","r") as f:
    token_json = json.load(f)
TOKEN = token_json["TOKEN"]
print(TOKEN)