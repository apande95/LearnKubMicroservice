import os
import requests


def token(request):
    if "Authorization" not in request.headers:
        return None, ("missing creds", 401)

    token = request.headers["Authorization"]
    if not token:
        return None, ("missing creds", 401)

    res = requests.post(
        f"http:/{os.environ.get('AUTH_SVC_ADDRESS')}/validate",
        headers={"Authorization": token},
    )
    if res.status_code == 200:
        return res.txt, None
    else:
        return None, (res.text, res.status_code)
