import pytest
import requests
import json
from Employee import Employer, Company
from Data import *
from faker import Faker


fake = Faker()


employer = Employer()
company = Company()




def test_authorization(get_token):
    token = get_token
    assert token is not None
    assert isinstance(token, str)




def test_getcompany_id():
    company_id = company.last_active_company_id()
    assert company_id is not None
    assert str(company_id).isdigit()




def test_add_employer(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
    "id": 0,
    "firstName": "string",
    "lastName": "string",
    "middleName": "string",
    "companyId": 0,
    "email": "string",
    "url": "string",
    "phone": "string",
    "birthdate": "2024-06-29T17:27:03.698Z",
    "isActive": 'true'
    }
    new_employer_id = (employer.add_new(token, body_employer))['id']
    assert new_employer_id is not None
    assert str(new_employer_id).isdigit()


    info = employer.get_into(new_employer_id)
    assert info.json()['id'] == new_employer_id
    assert info.status_code == 200




def test_add_employer_without_token():
    com_id = company.last_active_company_id()
    token = ""
    body_employer = {
        "id": 0,
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "middleName": "string",
        "companyId": com_id,
        "email": fake.email(),
        "url": "string",
        "phone": "string",
        "birthdate": "2024-06-29T17:27:03.698Z",
        "isActive": 'true'
    }
    new_employer = employer.add_new(token, body_employer)
    assert new_employer['message'] == 'Unauthorized'




def test_add_employer_without_body(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {}
    new_employer = employer.add_new(token, body_employer)
    assert new_employer['message'] == 'Internal server error'




def test_get_employer():
    com_id = company.last_active_company_id()
    list_employers = employer.get_list(com_id)
    assert isinstance(list_employers, list)




def test_get_list_employers_missing_company_id():
    try:
        employer.get_list()
    except TypeError as e:
        assert str (e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"




def test_get_list_employer_invalid_company_id():
    try:
        employer.get_list('')
    except TypeError as e:
        assert str(e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"




def test_get_info_new_employers_missing_employer_id():
    try:
        employer.get_into()
    except TypeError as e:
        assert str(e) == "Employer.get_into() missing 1 required positional argument: 'employee_id'"




def test_change_employer_info(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
        "id": 0,
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "middleName": "string",
        "companyId": com_id,
        "email": fake.email(),
        "url": "string",
        "phone": "string",
        "birthdate": "2024-06-29T17:27:03.698Z",
        "isActive": 'true'
    }
    just_employer = employer.add_new(token, body_employer)
    id = just_employer['id']
    body_change_employer = {
        "lastName": "Novikov",
        "email": "test2@mail.ru",
        "url": "string",
        "phone": "string",
        "isActive": 'true'
    }
    employer_changed = employer.change_info(token, id, body_change_employer)
    assert employer_changed.status_code == 200
    assert id == employer_changed.json()['id']
    assert (employer_changed.json()['email']) == body_change_employer.get('email')




def test_employers_missing_id_and_token():
    try:
        employer.change_info()
    except TypeError as e:
        assert str (e) == "Employer.change_info() missing 3 required positional arguments: 'token', 'employee_id', and 'body'"