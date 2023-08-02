from hive.api import ApiManager


class TreeHierarchy(ApiManager):

    def tree_hierarchy_metrics(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False,
                               kwargs: dict = None, **params):
        """

        Fetch all last_statuses.

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
            extract_valueless_metrics (bool, optional): Se True vengono inserite nella risposta anche le metriche che non hanno mai avuto un valore nelle time series. Default to False.
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

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path='/tree_hierarchy/metrics', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def tree_hierarchy_metric_types(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False,
                                    kwargs: dict = None, **params):
        """

        Fetch all last_statuses.

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
            extract_valueless_metrics (bool, optional): Se True vengono inserite nella risposta anche le metriche che non hanno mai avuto un valore nelle time series. Default to False.
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
            uuid_object (str, optional): additional filter
            object_name (str, optional): additional filter
            object_status (str, optional): additional filter
            object_profile (str, optional): additional filter
            uuid_metric_type (str, optional): additional filter
            metric_type_name (str, optional): additional filter
            metric_type_status (str, optional): additional filter

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path='/tree_hierarchy/metric_types', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def tree_hierarchy_objects(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False,
                               kwargs: dict = None, **params):
        """

        Fetch all last_statuses.

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
            extract_valueless_metrics (bool, optional): Se True vengono inserite nella risposta anche le metriche che non hanno mai avuto un valore nelle time series. Default to False.
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
            uuid_object (str, optional): additional filter
            object_name (str, optional): additional filter
            object_status (str, optional): additional filter
            object_profile (str, optional): additional filter


        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path='/tree_hierarchy/objects', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def tree_hierarchy_groups(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False,
                              kwargs: dict = None, **params):
        """

        Fetch all last_statuses.

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
            extract_valueless_metrics (bool, optional): Se True vengono inserite nella risposta anche le metriche che non hanno mai avuto un valore nelle time series. Default to False.
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

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path='/tree_hierarchy/groups', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response