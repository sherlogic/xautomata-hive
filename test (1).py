from hive.api import XautomataApi
import pandas as pd

root = 'https://dev-qa.sherlogic.com/api/v0/'
user = 'tester'
pasw = '12345678aA!'

xa = XautomataApi(root=root, user=user, password=pasw)

params = {'limit': 10, 'code': 'DEMO'}
res = xa.execute(mode='GET', path='/customers/', params=params)

uuid = res[0]['uuid']
params = {'limit': 10, 'status': 'A'}
res = xa.execute(mode='GET', path=f'/customers/{uuid}/groups', params=params)

uuid = res[0]['uuid']
params = {'limit': 10}
res = xa.execute(mode='GET', path=f'/groups/{uuid}/objects', params=params)
print(pd.DataFrame(res))


res = xa.customers(limit=10, code='DEMO')
uuid = res[0]['uuid']


res = xa.customers_groups(uuid=uuid, limit=10, status='A')
uuid = res[0]['uuid']

res = xa.groups_objects(uuid=uuid, limit=10)
print(pd.DataFrame(res))