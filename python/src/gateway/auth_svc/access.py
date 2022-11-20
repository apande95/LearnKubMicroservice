import os
import requests


def login(request):
    auth = request.authorization
    if not auth:
        return None, ("missing creds", 401)

    basicAuth = (auth.username, auth.password)

    res = requests.post(
        f"http:/{os.environ.get('AUTH_SVC_ADDRESS')}/login",
        auth=basicAuth,
    )
    if res.status_code == 200:
        return res.txt, None
    else:
        return None, (res.text, res.status_code)
