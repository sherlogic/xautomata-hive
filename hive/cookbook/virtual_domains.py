from hive.api import ApiManager


class VirtualDomains(ApiManager):

    def virtual_domains(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path='/virtual_domains/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def virtual_domains_groups(self, uuid: str, kwargs: dict = None, **params):
        """
        get the groups linked with the object.

        Args:
            uuid (str): uuid della object
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/virtual_domains/{uuid}/groups', params=params, **kwargs)
        return response