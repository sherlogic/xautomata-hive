from hive.api import ApiManager
from hive.api import handling_single_page_methods


class TsCostManagement(ApiManager):

    def ts_cost_management(self, single_page: bool = False, page_size: int = 5000,
                           warm_start: bool = False, kwargs: dict = None, **params):
        """
        metodo che permette di recuperare i costi per le anomalie.

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
            uuid_metric (str, optional): additional filter
            date_start ($date-time, optional): additional filter
            date_end ($date-time, optional): additional filter
            cloud_provider (str, optional): additional filter
            resource_location (str, optional): additional filter
            subscription_type (str, optional): additional filter
            subscription_id (str, optional): additional filter
            family (str, optional): additional filter
            category (str, optional): additional filter
            subcategory (str, optional): additional filter
            object (str, optional): additional filter
            metric (str, optional): additional filter
            resource_group (str, optional): additional filter
            reservation_name (str, optional): additional filter
            publisher_name (str, optional): additional filter
            local_currency (str, optional): additional filter
            provider_currency (str, optional): additional filter

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/ts_cost_management/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_uuid(self, uuid: str, single_page: bool = False, page_size: int = 5000,
                                warm_start: bool = False, kwargs: dict = None, **params):
        """
        metodo che permette di recuperare i costi per le anomalie.

        Args:
            uuid (str): uuid_metric.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            date ($date-time): additional filter. Mandatory.
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            like (bool, optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True.
            sort_by (str, optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "".
            null_fileds (str, optional): Stringa separata da virgole di campi di cui si vuole rimuovere, o imporre, un valore nullo nel result set. Esempio "campo:nullable". Default to "".

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/ts_cost_management/{uuid}', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_ccm_by_date(self, uuid: str, warm_start: bool = False, kwargs: dict = None, **params):
        """
        metodo che permette di recuperare i costi per le anomalie.

        Args:
            uuid (str): uuid del customer di cui si vuole scaricare i costi
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            date_start ($date-time, optional): additional filter
            date_end ($date-time, optional): additional filter
            interval (Literal['day', 'week', 'month', 'year'], optional): sampling window. Default to day.

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/ts_cost_management/ccm_by_date/{uuid}', warm_start=warm_start,
                                params=params, **kwargs)
        return response

    def ts_cost_management_anomalies(self, warm_start: bool = False, kwargs: dict = None, **params):
        """
        metodo che permette di recuperare i costi per le anomalie.

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            date_start ($date-time, optional): additional filter
            date_end ($date-time, optional): additional filter

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path='/ts_cost_management/anomalies/', warm_start=warm_start,
                                params=params, **kwargs)
        return response

    def ts_cost_management_anomalies_geo(self, warm_start: bool = False, kwargs: dict = None, **params):
        """
        metodo che permette di recuperare i costi per le anomalie geografiche.

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            date_start ($date-time, optional): additional filter
            date_end ($date-time, optional): additional filter

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path='/ts_cost_management/anomalies_geo/', warm_start=warm_start, params=params,
                                **kwargs)
        return response
