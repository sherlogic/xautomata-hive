from hive.api import XautomataApi
import pandas as pd

root = 'https://dev-qa.sherlogic.com/api/v0/'
user = 'tester'
pasw = '12345678aA!'
#uuid = '00cf20e6-ae55-4787-a7bc-71528a95028b'
_params = {'skip': 0,
           'limit': 100,
           'like': True,
           'join': False
           }

xa = XautomataApi(root=root,user=user,password=pasw)

# res = xa.customers(limit=5, company_name = 'piave motori')
# uuid = res[0]['uuid']

#res = xa.site(uuid='63923066-a0a3-4829-b6dd-4b64892ce23d', limit = 10)

res = xa.customers(uuid='801b5d2f-05c6-489a-8d7e-ce5eb836b9de')
# res = xa.sites(uuid_customer=uuid, limit = 30)

# res = xa.groups_objects(uuid=uuid, limit=5)
# uuid = res[#]['uuid']

# res = xa.metric_type(uuid=uuid, limit=5)
# uuid = res[0]['uuid']


print(pd.DataFrame(res))