from hive.api import ApiManager


class ProfileTopics(ApiManager):

    def profile_topics(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False,
                       kwargs: dict = None, **params):
        """

        Fetch all profile_topics.

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
            profile (str, optional): metric profile name
            topic (str, optional): metric profile topic

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path='/profile_topics/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def profile_topics_post(self, kwargs: dict = None, **payload):
        """

        Fetch all profile_topics.

        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Keyword Args:
            profile (str, optional): metric profile name
            topic (str, optional): metric profile topic

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/profile_topics/', payload=payload, **kwargs)
        return response

    def profile_topics_delete(self, uuid: str, kwargs: dict = None):
        """

        delete single profile_topics.

        Args:
            uuid: id del profilo da eliminare
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/profile_topics/{uuid}', **kwargs)
        return response
