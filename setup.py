from setuptools import find_packages, setup

version = '1.0'

# version go
urllib3 = 'urllib3==1.26.13'
tqdm = 'tqdm==4.64.1'
requests = 'requests==2.28.1'
# version end

# start
requires_dict = {
'hive': [tqdm, urllib3, requests],
'hive.api': [urllib3, tqdm, requests],
'hive.cookbook': [urllib3, tqdm, requests],
'hive.cookbook.analytics': [tqdm, urllib3, requests],
'hive.cookbook.anomalies': [tqdm, urllib3, requests],
'hive.cookbook.customers': [tqdm, urllib3, requests],
'hive.cookbook.external_tickets': [tqdm, urllib3, requests],
'hive.cookbook.groups': [tqdm, urllib3, requests],
'hive.cookbook.ingest': [tqdm, urllib3, requests],
'hive.cookbook.last_status': [tqdm, urllib3, requests],
'hive.cookbook.metric_types': [tqdm, urllib3, requests],
'hive.cookbook.metrics': [tqdm, urllib3, requests],
'hive.cookbook.objects': [tqdm, urllib3, requests],
'hive.cookbook.probes': [tqdm, urllib3, requests],
'hive.cookbook.profile_topics': [tqdm, urllib3, requests],
'hive.cookbook.services': [tqdm, urllib3, requests],
'hive.cookbook.sites': [tqdm, urllib3, requests],
'hive.cookbook.ts_cost_management': [tqdm, urllib3, requests],
'hive.cookbook.ts_metric': [tqdm, urllib3, requests],
'hive.cookbook.ts_service': [tqdm, urllib3, requests],
'hive.cookbook.users': [tqdm, urllib3, requests],
'hive.cookbook.virtual_domains': [tqdm, urllib3, requests],
'hive.cookbook.webhooks': [tqdm, urllib3, requests],
'hive.cookbook.widget_groups': [tqdm, urllib3, requests],
'hive.decorators': [],
'hive.exceptions': [],
}
# stop

setup(
    name='hive',
    version=version,
    packages=find_packages(include=['hive']),
    license='',
    author='Enrico Ferro - Andrea Jacassi',
    author_email='',
    description='',
    url="https://github.com/sherlogic/xautomata-hive.git",
    extras_require=requires_dict,
    install_requires=[],
)
