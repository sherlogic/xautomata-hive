from setuptools import find_packages, setup

version = '1.0'

urllib3 = 'urllib3==1.26.13'
tqdm = 'tqdm==4.64.1'
requests = 'requests==2.28.1'

# start
requires_dict = {
'hive': [urllib3, requests, tqdm],
'hive.api': [tqdm, requests, urllib3],
'hive.cookbook': [tqdm, requests, urllib3],
'hive.cookbook.analytics': [urllib3, requests, tqdm],
'hive.cookbook.customers': [urllib3, requests, tqdm],
'hive.cookbook.external_tickets': [urllib3, requests, tqdm],
'hive.cookbook.groups': [urllib3, requests, tqdm],
'hive.cookbook.ingest': [urllib3, requests, tqdm],
'hive.cookbook.last_status': [urllib3, requests, tqdm],
'hive.cookbook.metric_types': [urllib3, requests, tqdm],
'hive.cookbook.metrics': [urllib3, requests, tqdm],
'hive.cookbook.objects': [urllib3, requests, tqdm],
'hive.cookbook.probes': [urllib3, requests, tqdm],
'hive.cookbook.profile_topics': [urllib3, requests, tqdm],
'hive.cookbook.services': [urllib3, requests, tqdm],
'hive.cookbook.sites': [urllib3, requests, tqdm],
'hive.cookbook.ts_cost_management': [urllib3, requests, tqdm],
'hive.cookbook.ts_metric': [urllib3, requests, tqdm],
'hive.cookbook.ts_service': [urllib3, requests, tqdm],
'hive.cookbook.virtual_domains': [urllib3, requests, tqdm],
'hive.cookbook.webhooks': [urllib3, requests, tqdm],
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
