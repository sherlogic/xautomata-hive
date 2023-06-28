from hive.api import ApiManager
from hive.api import handling_single_page_methods


class MetricTypes(ApiManager):

    def metric_types(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None,
                **params):
        """
        metodo che restituisce tutti i metric_types

        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: parametri in piu che si vuole passare alla API

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            like (bool, optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True.
            sort_by (str, optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "".
            null_fileds (str, optional): Stringa separata da virgole di campi di cui si vuole rimuovere, o imporre, un valore nullo nel result set. Esempio "campo:nullable". Default to "".
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False
            extract_severity (bool, optional): Se True nella risposta e' anche presente la severita, Default to False.
            uuid_object (str, optional): additional filter
            name (str, optional): additional filter
            description (str, optional): additional filter
            feedback_for_operator (str, optional): additional filter
            profile (str, optional): additional filter
            status (str, optional): additional filter

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/metric_types/', single_page=single_page, page_size=page_size, params=params,
                                warm_start=warm_start, **kwargs)
        return response

    def metric_types_post(self, kwargs: dict = None, **payload):
        """
        post selected metric_types.

        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API


        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/metric_types/', payload=payload, **kwargs)
        return response

    def metric_type(self, uuid: str, warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch single metric_type.

        Args:
            uuid (str): uuid del metric_type da recuperare
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Keyword Args:
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/metric_types/{uuid}', warm_start=warm_start, params=params, **kwargs)
        return response

    def metric_type_metrics(self, uuid: str, single_page: bool = False, page_size: int = 5000, warm_start: bool = False,
                            kwargs: dict = None,
                            **params):
        """
        metodo che restituisce le metrics del metric type inserito

        Args:
            uuid (str, required): uuid della metric_type da cercare
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: parametri in piu che si vuole passare alla API

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            like (bool, optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True.
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False
            not_in (bool,optional): additional filter

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/metric_types/{uuid}/metrics', single_page=single_page,
                                page_size=page_size, params=params,
                                warm_start=warm_start, **kwargs)
        return response

    def metric_type_put(self, uuid: str, kwargs: dict = None, **payload):
        """
        update selected metric_type.

        Args:
            uuid (str): uuid della metric_type da modificare
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Keyword Args:
            uuid_object (str, optional): additional filter
            name (str, optional): additional filter
            description (str, optional): additional filter
            feedback_for_operator (dict, optional): additional filter
            profile (str, optional): additional filter
            data_profile (dict, optional): additional filter
            automata_domain (list or dict, optional): automata domain
            status (str, optional): additional filter

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('PUT', path=f'/metric_types/{uuid}', payload=payload, **kwargs)
        return response

    def metric_type_delete(self, uuid: str, kwargs: dict = None):
        """

        delete single metric_type.

        Args:
            uuid: id del metric_type da eliminare
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/metric_types/{uuid}', **kwargs)
        return response

    def metric_types_delete_bulk(self, payload: list, single_page: bool = False,
                                 page_size: int = 5000, kwargs: dict = None):
        """
        elimina le metriche in bulk

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/metric_types/bulk/delete/', single_page=single_page, page_size=page_size,
                                payload=payload, **kwargs)
        return response

    def metric_types_bulk(self, payload: list, single_page: bool = False,
                               page_size: int = 5000, warm_start: bool = False, kwargs: dict = None):
        """
        fetch le metriche in bulk

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/metric_types/bulk/read/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, **kwargs)
        return response