from hive.api import ApiManager


class Webhooks(ApiManager):

    def webhooks(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):

        """
        Fetch all webhooks.

        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            like (bool, optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True.
            sort_by (str, optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "".
            null_fileds (str, optional): Stringa separata da virgole di campi di cui si vuole rimuovere, o imporre, un valore nullo nel result set. Esempio "campo:nullable". Default to "".
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False
            extract_severity (bool, optional): Se True nella risposta e' anche presente la severita, Default to False.
            webhook_type (str, optional): additional filter
            uuid_probe (str, optional): additional filter

        Returns: list

        """

        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path='/webkooks/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def webhook(self, uuid: str, warm_start: bool = False, kwargs: dict = None):

        """
        Fetch all webhooks.

        Args:
            uuid (str): uuid del webhook da recuperare
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Returns: list

        """

        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/webkooks/{uuid}', warm_start=warm_start, **kwargs)
        return response

    def webhook_put(self, uuid: str, auth_token: str, uuid_probe: str, kwargs: dict = None, **payload):
        
        """
        update selected metric.

        Args:
            uuid (str): uuid del webhook da modificare
            uuid_probe (str): auth token del webhook da modificare
            auth_token (str): uuid della probe da modificare
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('PUT', path=f'/webhooks/{uuid}', auth_token=auth_token, uuid_probe=uuid_probe, payload=payload, **kwargs)
        return response