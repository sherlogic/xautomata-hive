from hive.api import ApiManager


class VirtualDomains(ApiManager):

    def virtual_domains(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path='/virtual_domains/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response