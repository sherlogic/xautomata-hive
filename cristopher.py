# import requests
# import json
# import pandas as pd

# _url = "https://dev-qa.sherlogic.com/api/v0/customers/"

# _params = {'skip': 0,
#            'limit': 100,
#            'like': True,
#            'join': False,
#            'count': False}

# user, password = 'tester', '12345678aA!'

# def authenticate():
#     """
#     Metodo che compie l'autenticazione e ottiene il token per la sessione
#     """
#     auth_date = {"grant_type": "password", "username": user, "password": password}
#     _response = requests.post(f'https://dev-qa.sherlogic.com/api/v0/login/access-token', data=auth_date)
#     return json.loads(_response.content.decode('utf-8'))['access_token']

# authentication = {'Authorization': f'Bearer {authenticate()}'}
# response = requests.get(url=_url, params=_params, headers=authentication)

# df = pd.DataFrame(json.loads(response.content.decode('utf-8')))

# print(df)

from hive.api import XautomataApi
import pandas as pd

root = 'https://dev-qa.sherlogic.com/api/v0/'
user = 'tester'
pasw = '12345678aA!'

xa = XautomataApi(root=root, user=user, password=pasw)

# params = {'limit': 10, 'code': 'DEMO'}
# res = xa.execute(mode='GET', path='/customers/', params=params)

# uuid = res[0]['uuid']
# params = {'limit': 10, 'status': 'A'}
# res = xa.execute(mode='GET', path=f'/customers/{uuid}/groups', params=params)

# print(pd.DataFrame(res))

# uuid = res[0]['uuid']
# params = {'limit': 10}
# res = xa.execute(mode='GET', path=f'/groups/{uuid}/objects', params=params)

# print(pd.DataFrame(res))

# res = xa.customers(limit=10, company_name='gargallo')
# uuid = res[0]['uuid']

# res = xa.customers_groups(uuid=uuid, limit=10, status='A')
# uuid = res[0]['uuid']

# res = xa.groups_objects(uuid=uuid, limit=10)
# print(pd.DataFrame(res))

res = xa.customers(limit=10, company_name='gargallo')
uuid = res[0]['uuid']

res = xa.customers_groups(uuid=uuid, limit=10, status='A')
uuid = res[0]['uuid']

print(pd.DataFrame(res))
 
# res = xa.groups_objects(uuid=uuid, limit=10)

# res = xa.customers(limit=10, company_name='gargallo')
# uuid = res[0]['uuid']

# res = xa.customers_groups(name="DEMO7044", limit=10, status='A')
# uuid = res[0]['uuid']

# res = xa.groups_objects(uuid=uuid, limit=10)

# print(pd.DataFrame(res))