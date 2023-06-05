from setuptools import find_packages, setup

version = '1.0'

urllib3 = 'urllib3==1.26.13'
tqdm = 'tqdm==4.64.1'
requests = 'requests==2.28.1'

# start
requires_dict = {
'hive': [tqdm, requests, urllib3],
'hive.api': [requests, urllib3, tqdm],
'hive.cookbook': [requests, tqdm, urllib3],
'hive.cookbook.analytics': [tqdm, requests, urllib3],
'hive.cookbook.customers': [tqdm, requests, urllib3],
'hive.cookbook.external_tickets': [tqdm, requests, urllib3],
'hive.cookbook.groups': [tqdm, requests, urllib3],
'hive.cookbook.ingest': [tqdm, requests, urllib3],
'hive.cookbook.last_status': [tqdm, requests, urllib3],
'hive.cookbook.metric_types': [tqdm, requests, urllib3],
'hive.cookbook.metrics': [tqdm, requests, urllib3],
'hive.cookbook.objects': [tqdm, requests, urllib3],
'hive.cookbook.probes': [tqdm, requests, urllib3],
'hive.cookbook.profile_topics': [tqdm, requests, urllib3],
'hive.cookbook.services': [tqdm, requests, urllib3],
'hive.cookbook.sites': [tqdm, requests, urllib3],
'hive.cookbook.ts_cost_management': [tqdm, requests, urllib3],
'hive.cookbook.ts_metric': [tqdm, requests, urllib3],
'hive.cookbook.ts_service': [tqdm, requests, urllib3],
'hive.cookbook.users': [tqdm, requests, urllib3],
'hive.cookbook.virtual_domains': [tqdm, requests, urllib3],
'hive.cookbook.webhooks': [tqdm, requests, urllib3],
'hive.cookbook.widget_groups': [tqdm, requests, urllib3],
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
