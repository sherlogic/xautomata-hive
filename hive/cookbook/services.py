from hive.api import ApiManager
from hive.api import handling_single_page_methods


class Services(ApiManager):

    def services(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None,
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
            uuid_parent (str, optional): additional filter
            uuid_customer (str, optional): additional filter
            name (str, optional): additional filter
            description (str, optional): additional filter
            profile (str, optional): additional filter
            status (str, optional): additional filter

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path='/services/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def service(self, uuid: str, warm_start: bool = False, kwargs: dict = None, **params):
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
        response = self.execute('GET', path=f'/services/{uuid}', warm_start=warm_start, params=params, **kwargs)
        return response

    def services_put(self, uuid: str, kwargs: dict = None, **payload):
        """
        update selected metric.

        Args:
            uuid (str): uuid della metrica da modificare
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Keyword Args:
            uuid_parent (str, optional): additional filter
            uuid_customer (str, optional): additional filter
            name (str, optional): additional filter
            description (str, optional): additional filter
            profile (str, optional): additional filter
            status (str, optional): additional filter

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('PUT', path=f'/services/{uuid}', payload=payload, **kwargs)
        return response

    def services_post(self, kwargs: dict = None, **payload):
        """
        update selected metric.

        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Keyword Args:
            uuid_customer (str): additional filter, required
            name (str): additional filter, required, required
            description (str): additional filter, required
            profile (str): additional filter, required
            status (str): additional filter, required
            uuid_parent (str, optional): additional filter
            automata_domain (list, optional): additional filter
            rule (list, optional): additional filter

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/services/', payload=payload, **kwargs)
        return response

    def services_delete(self, uuid: str, kwargs: dict = None):
        """

        delete single metric.

        Args:
            uuid: id del metric da eliminare
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/services/{uuid}', **kwargs)
        return response

    def services_query(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):
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
            uuid_customer (str, optional): additional filter
            customer_code (str, optional): additional filter
            customer_status (str, optional): additional filter
            uuid_site (str, optional): additional filter
            site_code (str, optional): additional filter
            site_address (str, optional): additional filter
            site_description (str, optional): additional filter
            site_zip_code (str, optional): additional filter
            site_city (str, optional): additional filter
            site_country (str, optional): additional filter
            site_state_province (str, optional): additional filter
            site_status (str, optional): additional filter
            uuid_group (str, optional): additional filter
            group_name (str, optional): additional filter
            group_status (str, optional): additional filter
            group_type (str, optional): additional filter
            uuid_object (str, optional): additional filter
            object_name (str, optional): additional filter
            object_status (str, optional): additional filter
            object_profile (str, optional): additional filter
            uuid_metric_type (str, optional): additional filter
            metric_type_name (str, optional): additional filter
            metric_type_status (str, optional): additional filter
            uuid_metric (str, optional): additional filter
            metric_name (str, optional): additional filter
            metric_status (str, optional): additional filter
            metric_profile (str, optional): additional filter
            service_uuid_parent (str, optional): additional filter
            uuid_service (str, optional): additional filter
            service_profile (str, optional): additional filter
            service_name (str, optional): additional filter
            service_description (str, optional): additional filter
            service_status (str, optional): additional filter

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/services/query/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def services_query_bulk(self, warm_start: bool = False, single_page: bool = False,
                            page_size: int = 5000, payload: dict = None, kwargs: dict = None, **params):
        """
        metodo che permette di recuperare la posizione nell'albero di tutti i servizzi.

        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            payload (dict, optional): dizionario con dentro le liste delle chiavi di cui si vuole avere la bulk read.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            like (bool, optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True.
            sort_by (str, optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "".
            null_fileds (str, optional): Stringa separata da virgole di campi di cui si vuole rimuovere, o imporre, un valore nullo nel result set. Esempio "campo:nullable". Default to "".

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/services/query/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, params=params, **kwargs)
        return response

    def services_bulk_create(self, payload: list, single_page: bool = False,
                             page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):
        """
        metodo che permette di recuperare la time serie di tutte le metriche. Si puo scegliere se ottenere le metriche di stato o di valore.

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Keyword Args:
            best_effort (str, optional): Default to True.

        Examples:
            services: [{"uuid_parent": "string",
                        "uuid_customer": "string",
                        "profile": "string",
                        "name": "string",
                        "description": "string",
                        "automata_domain": [
                          "string"
                        ],
                        "rule": [
                          "string"
                        ],
                        "status": "s"
                      },
                      ...
                    ]

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/services/bulk/create/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, params=params, **kwargs)
        return response

    def services_metrics_bulk_create(self, payload: list, single_page: bool = False,
                                     page_size: int = 5000, kwargs: dict = None, **params):
        """
        metodo che permette di legare una metrica a un servizio, in modo bulk.

        Args:
            payload (list[dict], optional): additional filter
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Keyword Args:
            best_effort (str, optional): Default to True.

        Examples:
            payload: [
                    {
                      "uuid_metric": "string",
                      "uuid_service": "string"
                    }, ...
                  ]

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/services/bulk/create/metrics', single_page=single_page, page_size=page_size,
                                payload=payload, params=params, **kwargs)
        return response

    def services_metrics_bulk_delete(self, payload: list, single_page: bool = False,
                                     page_size: int = 5000, kwargs: dict = None, **params):
        """
        metodo che permette di legare una metrica a un servizio, in modo bulk.

        Args:
            payload (list[dict], optional): additional filter
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Keyword Args:
            best_effort (str, optional): Default to True.

        Examples:
            payload: [
                    {
                      "uuid_metric": "string",
                      "uuid_service": "string"
                    }, ...
                  ]

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/services/bulk/delete/metrics', single_page=single_page, page_size=page_size,
                                payload=payload, params=params, **kwargs)
        return response

    def services_metrics(self, uuid: str, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch link service metric.

        Args:
            uuid (str): uuid della servizio da recuperare
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/services/{uuid}/metrics', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def services_metrics_delete(self, uuid: str, uuid_metric: str, kwargs: dict = None):
        """

        delete link service metric.

        Args:
            uuid: id del servizio
            uuid_metric: id della metrica
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/services/{uuid}/metrics/{uuid_metric}', **kwargs)
        return response

    def services_metrics_bulk_read_by(self, payload: list, single_page: bool = False,
                                      page_size: int = 5000, warm_start: bool = False,
                                      kwargs: dict = None):
        """
        metodo fetch di un servizio tramite i suoi valori univoci, in modo bulk.

        Args:
            payload (list[dict], optional): additional filter
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Examples:
            payload: [
                      {
                        "uuid_customer": "string",
                        "profile": "string",
                        "name": "string"
                      }
                    ]

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/services/bulk/read_by/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, **kwargs)
        return response