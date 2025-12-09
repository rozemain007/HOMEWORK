import pytest
import requests
import json

base_url = "https://yougile.com/api-v2"
token = "trlDCL-3VXCpd6Jnpdw3TuUmRK29rIpyR8nat-h2tWyOI01Br6Pb9yYZ1y2-vdpp"


def test_create_company_positive():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    info = {
        "title": "New_company_SkyPro"
    }
    resp = requests.post(base_url+"/projects", json=info, headers=headers)
    assert resp.status_code == 201
    id_comp = resp.json()["id"]
    return id_comp


def test_create_company_negative():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    info = {
        "title": ""
    }
    resp = requests.post(base_url+"/projects", json=info, headers=headers)
    assert resp.status_code == 400


def test_change_company_positive():
    id_company = test_create_company_positive()
    info = {
        "title": "New_name"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    resp = requests.put(base_url+'/projects/'+id_company, json=info, headers=headers)
    assert resp.status_code == 200
    assert id_company == resp.json()["id"]




def test_change_company_negative():
    id_company = test_create_company_positive()
    info = {
        "title": ""
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    resp = requests.put(base_url+'/projects/'+id_company, json=info, headers=headers)
    assert resp.status_code == 400



def test_take_id_positive():
    id_company = test_create_company_positive()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    resp = requests.get(base_url+'/projects/'+id_company, headers=headers)
    assert resp.status_code == 200
    assert resp.json()["id"] == id_company


def test_take_id_negative():
    id_company = test_create_company_positive()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    resp = requests.get(base_url+'/projects/'+id_company, )
    assert resp.status_code == 401


