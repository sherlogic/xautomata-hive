from hive.api import ApiManager
from hive.api import handling_single_page_methods


class Metrics(ApiManager):

    def metrics(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None,
                **params):
        """
        Fetch all metrics.

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
            uuid_metric_type (str, optional): additional filter
            name (str, optional): additional filter
            description (str, optional): additional filter
            feedback_for_operator (str, optional): additional filter
            profile (str, optional): additional filter
            status (str, optional): additional filter

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path='/metrics/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def metrics_post(self, kwargs: dict = None, **payload):
        """
        post selected metrics.

        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API


        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/metrics/', payload=payload, **kwargs)
        return response

    def metric(self, uuid: str, warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch single metric.

        Args:
            uuid (str): uuid della metrica da recuperare
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/metrics/{uuid}', warm_start=warm_start, params=params, **kwargs)
        return response

    def metric_put(self, uuid: str, kwargs: dict = None, **payload):
        """
        update selected metric.

        Args:
            uuid (str): uuid della metrica da modificare
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Keyword Args:
            uuid_metric (str, optional): additional filter
            name (str, optional): additional filter
            description (str, optional): additional filter
            feedback_for_operator (str, optional): additional filter
            profile (str, optional): additional filter
            status (str, optional): additional filter
            data_profile (list or dict, optional): data profile
            automata_domain (list or dict, optional): automata domain

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('PUT', path=f'/metrics/{uuid}', payload=payload, **kwargs)
        return response

    def metric_delete(self, uuid: str, kwargs: dict = None):

        """
        delete single metric.

        Args:
            uuid (str): uuid della metrica da eliminare
            kwargs (dict, optional): additional parameters for execute. Default to None..

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/metrics/{uuid}', **kwargs)
        return response

    def metrics_delete_bulk(self, payload: list, single_page: bool = False,
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
        response = self.execute('POST', path='/metrics/bulk/delete/', single_page=single_page, page_size=page_size,
                                payload=payload, **kwargs)
        return response

    def metrics_bulk(self, payload: list, single_page: bool = False,
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
        response = self.execute('POST', path='/metrics/bulk/read/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, **kwargs)
        return response

    def metrics_last_value(self, uuid: str, warm_start: bool = False, kwargs: dict = None, **params):
        """
        Cerca l'ultimo valore della metrics

        Args:
            uuid (str): uuid della metrica da cercare
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/metrics/{uuid}/last_value', warm_start=warm_start, **kwargs)
        return response

    def metrics_services(self, uuid: str, single_page: bool = False, page_size: int = 5000, warm_start: bool = False,
                         kwargs: dict = None, **params):
        """
        Get the services linked with the metric.

        Args:
            uuid (str): uuid metric
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
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False
            not_in (bool, optional): additional filter

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/metrics/{uuid}/services', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def metrics_services_post(self, uuid: str, uuid_service: str, kwargs: dict = None, **payload):
        """
        create link between selected object and selected metrics service.

        Args:
            uuid (str): uuid della metrics
            uuid_service (str): uuid del service
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/metrics/{uuid}/services/{uuid_service}', payload=payload, **kwargs)
        return response

    def metrics_services_delete(self, uuid: str, uuid_service: str, kwargs: dict = None):

        """
        delete service linked with selected metric.

        Args:
            uuid: uuid del metric
            uuid_service: uuid del service da eliminare
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/metrics/{uuid}/services/{uuid_service}', **kwargs)
        return response

    def metrics_downtimes(self, uuid: str, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):

        """
        get the downtimes linked with the metrics.

        Args:
            uuid (str): uuid metric
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: parametri in piu che si vuole passare alla API
        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False
            active_at_timestamp (str, optional): additional filter
            fetch all(bool, optional): additiional filter
        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/metrics/{uuid}/downtimes', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def metrics_downtimes_post(self, uuid: str, uuid_downtime: str, kwargs: dict = None, **payload):
        """
        create link between selected metrics and selected downtime.

        Args:
            uuid (str): uuid della metrics
            uuid_downtime (str): uuid del downtime
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/metrics/{uuid}/downtimes/{uuid_downtime}', payload=payload, **kwargs)
        return response

    def metrics_downtimes_delete(self, uuid: str, uuid_downtime: str, kwargs: dict = None):
        """

        delete service linked with selected metric.

        Args:
            uuid(str): uuid del metric
            uuid_downtime(str): uuid downtime da eliminare
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/metrics/{uuid}/services/{uuid_downtime}', **kwargs)
        return response

    def metrics_dispatchers(self, uuid: str, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):
        """
        metodo che restituisce i dispatchers di una metric

        Args:
            uuid (str): uuid metric
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
            join (bool, optional): additional filter
            not_in (nool, optional): additional filter
        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/metrics/{uuid}/dispatchers', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def metrics_dispatchers_post(self, uuid: str, uuid_dispatcher: str, kwargs: dict = None, **payload):
        """
        create link between selected dispatcher and selected metrics service.
        Args:
            uuid (str, required): uuid della metrics
            uuid_dispatcher (str, required): uuid del service
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API
        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/metrics/{uuid}/dispatchers/{uuid_dispatcher}', payload=payload, **kwargs)
        return response

    def metrics_dispatchers_delete(self, uuid: str, uuid_dispatcher: str, kwargs: dict = None):
        """

        delete dispatcher linked with selected metric.

        Args:
            uuid(str): uuid del metric
            uuid_dispatcher (str): uuid dispatcher da eliminare
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/metrics/{uuid}/dispatchers/{uuid_dispatcher}', **kwargs)
        return response

    def metrics_services_create_bulk(self, payload: list, single_page: bool = False,
                                     page_size: int = 5000,  kwargs: dict = None, **params):
        """
        crea le bulk di metrics_services

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params

        kwargs:
            best_effort (bool, optional): se a True forza a proseguire anche se un elemento genera un errore

        Examples:
                            [
                                {
                                    "uuid_metric": "string",
                                    "uuid_service": "string"
                                }
                            ]

        Returns: list
        """

        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/metrics/bulk/create/services', single_page=single_page, page_size=page_size,
                                payload=payload, params=params, **kwargs)
        return response

    def metrics_read_by_bulk(self, payload: list, single_page: bool = False, page_size: int = 5000,
                             warm_start: bool = False, kwargs: dict = None):
        """
        reads metrics_bulk by code
        Args:
            payload (list[str], optional): additional filter
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Examples:[
                    {
                        "uuid_metric_type": "string",
                        "name": "string"
                    }
                ]

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path="/metrics/bulk/read_by/", single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, **kwargs)
        return response

    def metrics_downtimes_create_bulk(self, payload: list, single_page: bool = False,
                                      page_size: int = 5000,  kwargs: dict = None, **params):
        """
        crea le bulk di metrics_downtime

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params

        kwargs:
            best_effort (bool, optional): se a True forza a proseguire anche se un elemento genera un errore

        Examples:
                    uuids = [
                                {
                                    "uuid_downtime": "string",
                                    "uuid_metric": "string"
                                }
                            ]

        Returns: list
        """

        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/metrics/bulk/create/downtimes', single_page=single_page, page_size=page_size,
                                payload=payload, params=params, **kwargs)
        return response

    def metrics_downtimes_delete_bulk(self, payload: list, single_page: bool = False, page_size: int = 5000, kwargs: dict = None, **params):
        """
        cancella le bulk di metrics_downtimes
        Args:
            payload (list[str], optional): additional filter
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: parametri in piu che si vuole passare alla API
        Examples:[
                    {
                        "uuid_metric_type": "string",
                        "name": "string"
                    }
                ]

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path="/metrics/bulk/delete/downtimes", single_page=single_page, page_size=page_size,
                                payload=payload, params=params, **kwargs)
        return response

    def metrics_services_delete_bulk(self, payload: list, single_page: bool = False, page_size: int = 5000, kwargs: dict = None, **params):
        """
        cancella le bulk di metrics_services
        Args:
            payload (list[str], optional): additional filter
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: parametri in piu che si vuole passare alla API
        Examples:[
                    {
                        "uuid_metric": "string",
                        "uuid_service": "string"
                    }
                ]

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path="/metrics/bulk/delete/services", single_page=single_page, page_size=page_size,
                                payload=payload, params=params, **kwargs)
        return response

    def metrics_create_bulk(self, payload: list, single_page: bool = False,
                            page_size: int = 5000,  kwargs: dict = None, **params):
        """
        crea le bulk di metrics

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params

        kwargs:
            best_effort (bool, optional): se a True forza a proseguire anche se un elemento genera un errore

        Examples:
                    uuids = [
                                {
                                    "uuid_metric_type": "string",
                                    "name": "string",
                                    "description": "string",
                                    "feedback_for_operator": "string",
                                    "profile": "string",
                                    "data_profile": {},
                                    "automata_domain": [
                                    "string"
                                    ],
                                    "status": "s"
                                }
                            ]

        Returns: list
        """

        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/metrics/bulk/create/', single_page=single_page, page_size=page_size,
                                payload=payload, params=params, **kwargs)
        return response
