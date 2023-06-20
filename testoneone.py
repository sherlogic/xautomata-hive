from hive.api import XautomataApi
import pandas as pd

root = 'https://dev-qa.sherlogic.com/api/v0/'
user = 'tester'
pasw = '12345678aA!'

xa = XautomataApi(root=root,user=user,password=pasw)

# res=xa.objects_groups(uuid='77e3aa14-3f1a-46e7-973d-b9da4284eed2')
# res=xa.site(uuid='3b80f1ca-26a4-407b-a5ce-5654bf5c46be')
#res=xa.customers(uuid='00cf20e6-ae55-4787-a7bc-71528a95028b')
#res=xa.object_downtimes(uuid='77e3aa14-3f1a-46e7-973d-b9da4284eed2')
#res=xa.objects_dispatchers(uuid='736b35a2-31b4-4395-9fa0-e4bce3467fdb')
#res=xa.metrics_last_value(uuid='2c955832-c150-4715-b78d-10e37718f291')
#res=xa.metrics_dispatchers(uuid="23ff93cc-5793-4382-b3d7-193ed1c05eb7")
#res=xa.metrics_downtimes(uuid="23ff93cc-5793-4382-b3d7-193ed1c05eb7")
#res=xa.metric_type_metrics(uuid="f6faf967-4dd9-4eb4-8105-46a60560b6e3")
#res=xa.metric_type_downtime(uuid="f6faf967-4dd9-4eb4-8105-46a60560b6e3")
#res=xa.metric_type_dispatchers(uuid="23908e09-d666-4051-918b-71809c14dc09")
print(pd.DataFrame(res))




# aggiuta = 'testo in piu'
# testo = f'ciao{aggiuta}'

# print(testo)




