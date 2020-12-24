import requests

try:
    var = "21432142131dasdad"
    register = f'http://www.isrt.info/version/register.php?clientid={var}'
    register_post = requests.post(register)
except Exception:
    pass