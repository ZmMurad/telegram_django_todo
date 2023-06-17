import requests
from config import url_server_port



def return_headers(token):
    return {"Authorization": f"Token {token}"}

def send_token(token):
    result=requests.post(url=url_server_port+"/api/v1/auth/check_token/", headers=return_headers(token))
    result.raise_for_status()
    if result.json()["status"]=="success":
        return True
    return False


def get_does(token):
    result=requests.get(url=url_server_port+"/api/v1/does/",headers=return_headers(token))
    result.raise_for_status()
    return result.json()


def get_do(token,id):
    result=requests.get(url=url_server_port+f"/api/v1/does/{id}",headers=return_headers(token))
    result.raise_for_status()
    return result.json()


def delete_do_f(token,id):
    result=requests.delete(url=url_server_port+f"/api/v1/does/{id}",headers=return_headers(token))
    result.raise_for_status()
    return result.json()

def add_do_f(token, data):
    result=requests.post(url=url_server_port+"/api/v1/does/", headers=return_headers(token), data=data)
    result.raise_for_status()
    return result.json()