from hive.api import ApiManager, handling_single_page_methods


class TsCostManagement(ApiManager):
    """Class that handles all the XAutomata ts_cost_management APIs"""

    def ts_cost_management(self, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Read Costs
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            null_fields (string optional): additional filter - parameter
            uuid_metric (string optional): additional filter - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
            cloud_provider (string optional): additional filter - parameter
            resource_location (string optional): additional filter - parameter
            subscription_type (string optional): additional filter - parameter
            subscription_id (string optional): additional filter - parameter
            subscription_name (string optional): additional filter - parameter
            family (string optional): additional filter - parameter
            category (string optional): additional filter - parameter
            subcategory (string optional): additional filter - parameter
            object (string optional): additional filter - parameter
            metric (string optional): additional filter - parameter
            unit (string optional): additional filter - parameter
            resource_group (string optional): additional filter - parameter
            reservation_name (string optional): additional filter - parameter
            publisher_name (string optional): additional filter - parameter
            local_currency (string optional): additional filter - parameter
            provider_currency (string optional): additional filter - parameter
            uuid_customer (string optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/ts_cost_management/',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_create(self, kwargs: dict = None, **payload
        ) -> list:
        """Create Cost Multi
        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            uuid_metric (string required): additional filter - payload
            date (string required): additional filter - payload
            cloud_provider (string required): additional filter - payload
            resource_location (string required): additional filter - payload
            subscription_type (string optional): additional filter - payload
            subscription_id (string required): additional filter - payload
            subscription_name (string optional): additional filter - payload
            family (string required): additional filter - payload
            category (string required): additional filter - payload
            subcategory (string required): additional filter - payload
            object (string required): additional filter - payload
            metric (string required): additional filter - payload
            unit (string required): additional filter - payload
            qnt (number optional): additional filter - payload
            local_currency (string required): additional filter - payload
            unit_cost (number required): additional filter - payload
            total_cost (number required): additional filter - payload
            unit_revenue (number required): additional filter - payload
            total_revenue (number required): additional filter - payload
            provider_currency (string required): additional filter - payload
            unit_cost_pc (number required): additional filter - payload
            total_cost_pc (number required): additional filter - payload
            unit_revenue_pc (number required): additional filter - payload
            total_revenue_pc (number required): additional filter - payload
            cumulative_qnt (number required): additional filter - payload
            cumulative_unit_cost (number required): additional filter - payload
            cumulative_total_cost (number required): additional filter - payload
            cumulative_unit_revenue (number required): additional filter - payload
            cumulative_total_revenue (number required): additional filter - payload
            resource_group (string required): additional filter - payload
            reservation_name (string required): additional filter - payload
            publisher_name (string required): additional filter - payload
            tenant_id (string optional): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/ts_cost_management/',
            payload=payload, **kwargs)
        return response

    def ts_cost_management_grouped(self, uuid_customer: str,
        warm_start: bool = False, single_page: bool = False,
        page_size: int = 5000, kwargs: dict = None, **params) -> list:
        """Query Group By Date
        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
            cloud_provider (string optional): additional filter - parameter
            resource_group (string optional): additional filter - parameter
            resource_location (string optional): additional filter - parameter
            category (string optional): additional filter - parameter
            subscription (string optional): additional filter - parameter
            subscription_type (string optional): additional filter - parameter
            interval (None optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=
            f'/ts_cost_management/grouped/{uuid_customer}', single_page=
            single_page, page_size=page_size, warm_start=warm_start, params
            =params, **kwargs)
        return response

    def ts_cost_management_uuid_metric(self, uuid_metric: str,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """Read Cost
        Args:
            uuid_metric (str, required): uuid_metric
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            date (string required): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/ts_cost_management/{uuid_metric}', warm_start=warm_start,
            params=params, **kwargs)
        return response

    def ts_cost_management_ccm_by_date(self, uuid_customer: str,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """Query Group By Cloud Provider Subscription Type Resource Group
        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
            interval (None optional): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/ts_cost_management/ccm_by_date/{uuid_customer}', warm_start=
            warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_ccm_by_subscription_type(self,
        uuid_customer: str, warm_start: bool = False, kwargs: dict = None,
        **params) -> list:
        """Query Group By Cloud Provider Subscription Type
        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/ts_cost_management/ccm_by_subscription_type/{uuid_customer}',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_ccm_by_category(self, uuid_customer: str,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """Query Group By Category
        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/ts_cost_management/ccm_by_category/{uuid_customer}',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_ccm_by_resource_location(self,
        uuid_customer: str, warm_start: bool = False, kwargs: dict = None,
        **params) -> list:
        """Query Group By Resource Location
        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/ts_cost_management/ccm_by_resource_location/{uuid_customer}',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_ccm_by_resource_group(self, uuid_customer: str,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """Query Group By Resource Group
        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/ts_cost_management/ccm_by_resource_group/{uuid_customer}',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_ccm_by_subscription(self, uuid_customer: str,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """Query Group By Subscription
        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/ts_cost_management/ccm_by_subscription/{uuid_customer}',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_anomalies(self, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Query Anomalies
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=
            f'/ts_cost_management/anomalies/', single_page=single_page,
            page_size=page_size, warm_start=warm_start, params=params, **kwargs
            )
        return response

    def ts_cost_management_anomaly_selector(self, warm_start: bool = False,
        kwargs: dict = None, **params) -> list:
        """Query Anomaly Selector
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
            sampling (None optional): additional filter - parameter
            uuid_customer (string required): additional filter - parameter
            cloud_provider (string required): additional filter - parameter
            description (string required): additional filter - parameter
            family (string required): additional filter - parameter
            category (string required): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/ts_cost_management/anomaly_selector/', warm_start=warm_start,
            params=params, **kwargs)
        return response

    def ts_cost_management_anomaly_selector_geo(self,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """Query Anomaly Selector Geo
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
            sampling (None optional): additional filter - parameter
            uuid_customer (string required): additional filter - parameter
            cloud_provider (string required): additional filter - parameter
            description (string required): additional filter - parameter
            resource_location (string required): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/ts_cost_management/anomaly_selector_geo/', warm_start=
            warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_anomalies_geo(self, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Query Anomalies Geo
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=
            f'/ts_cost_management/anomalies_geo/', single_page=single_page,
            page_size=page_size, warm_start=warm_start, params=params, **kwargs
            )
        return response

    def ts_cost_management_billing(self, warm_start: bool = False,
        kwargs: dict = None, **params) -> list:
        """Query Billing
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string required): additional filter - parameter
            date_end (string required): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=f'/ts_cost_management/billing/',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_az_customer_data(self, warm_start: bool = False,
        kwargs: dict = None, **params) -> list:
        """Az Customer Data
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string required): additional filter - parameter
            date_end (string required): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/ts_cost_management/az_customer_data/', warm_start=warm_start,
            params=params, **kwargs)
        return response

    def ts_cost_management_az_customer_data_probe_uuid(self,
        probe_uuid: str, warm_start: bool = False, kwargs: dict = None, **
        params) -> list:
        """Az Customer Data Single
        Args:
            probe_uuid (str, required): probe_uuid
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string required): additional filter - parameter
            date_end (string required): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/ts_cost_management/az_customer_data/{probe_uuid}',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_az_customer_data_delete(self, probe_uuid: str,
        kwargs: dict = None, **params) -> list:
        """Az Customer Data Single
        Args:
            probe_uuid (str, required): probe_uuid
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            date_start (string required): additional filter - parameter
            date_end (string required): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('DELETE', path=
            f'/ts_cost_management/az_customer_data/{probe_uuid}', params=
            params, **kwargs)
        return response

    def ts_cost_management_last_cumulative_values(self,
        subscription_id: str, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Query Last Cumulative Values
        Args:
            subscription_id (str, required): subscription_id
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            until (string required): additional filter - parameter
            category (string required): additional filter - parameter
            subcategory (string required): additional filter - parameter
            metric (string required): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=
            f'/ts_cost_management/last_cumulative_values/{subscription_id}',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_probe_delete(self, uuid_probe: str,
        kwargs: dict = None, **params) -> list:
        """Delete By Uuid Probe And Date Range
        Args:
            uuid_probe (str, required): uuid_probe
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            tenant_id (string optional): additional filter - parameter
            date_start (string required): additional filter - parameter
            date_end (string required): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('DELETE', path=
            f'/ts_cost_management/probe/{uuid_probe}/', params=params, **kwargs
            )
        return response
