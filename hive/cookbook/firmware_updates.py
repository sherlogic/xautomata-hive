from hive.api import ApiManager, handling_single_page_methods, warning_wrong_parameters


class FirmwareUpdates(ApiManager):
    """Class that handles all the XAutomata firmware_updates APIs"""

    def firmware_updates(self, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Read Firmware Updates

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            site_code (string optional): additional filter - parameter
            uuid_customer (string optional): additional filter - parameter
            uuid_metric (string optional): additional filter - parameter
            site_city (string optional): additional filter - parameter
            site_country (string optional): additional filter - parameter
            site_address (string optional): additional filter - parameter
            site_region (string optional): additional filter - parameter
            site_zip_code (string optional): additional filter - parameter
            site_type (string optional): additional filter - parameter
            site_description (string optional): additional filter - parameter
            site_state_province (string optional): additional filter - parameter
            metric_profile (string optional): additional filter - parameter
            group_name (string optional): additional filter - parameter
            uuid_virtual_domain (string optional): additional filter - parameter
            virtual_domain_name (string optional): additional filter - parameter
            virtual_domain_description (string optional): additional filter - parameter
            object_name (string optional): additional filter - parameter
            model (string optional): additional filter - parameter
            type (string optional): additional filter - parameter
            brand (string optional): additional filter - parameter
            modello_serie (string optional): additional filter - parameter
            marca_modello_serie (string optional): additional filter - parameter
            end_of_life (string optional): additional filter - parameter
            metric_type_name (string optional): additional filter - parameter
            firmware (string optional): additional filter - parameter
            last_firmware_version (string optional): additional filter - parameter
            last_value_description (string optional): additional filter - parameter
            password_created_time (string optional): additional filter - parameter
            password_expiring_date (string optional): additional filter - parameter
            password_warning_threshold (string optional): additional filter - parameter
            password_critical_threshold (string optional): additional filter - parameter
            object_last_check_ts (string optional): additional filter - parameter
            status (string optional): additional filter - parameter
            uuid_downtime (string optional): additional filter - parameter
            downtime_code (string optional): additional filter - parameter
            downtime_description (string optional): additional filter - parameter
            downtime_start (string optional): additional filter - parameter
            downtime_end (string optional): additional filter - parameter
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
        official_params_list = ['sort_by', 'site_code', 'uuid_customer',
            'uuid_metric', 'site_city', 'site_country', 'site_address',
            'site_region', 'site_zip_code', 'site_type', 'site_description',
            'site_state_province', 'metric_profile', 'group_name',
            'uuid_virtual_domain', 'virtual_domain_name',
            'virtual_domain_description', 'object_name', 'model', 'type',
            'brand', 'modello_serie', 'marca_modello_serie', 'end_of_life',
            'metric_type_name', 'firmware', 'last_firmware_version',
            'last_value_description', 'password_created_time',
            'password_expiring_date', 'password_warning_threshold',
            'password_critical_threshold', 'object_last_check_ts', 'status',
            'uuid_downtime', 'downtime_code', 'downtime_description',
            'downtime_start', 'downtime_end', 'date_start', 'date_end',
            'skip', 'limit', 'like', 'join', 'count']
        params.get('sort_by'), params.get('site_code'), params.get(
            'uuid_customer'), params.get('uuid_metric'), params.get('site_city'
            ), params.get('site_country'), params.get('site_address'
            ), params.get('site_region'), params.get('site_zip_code'
            ), params.get('site_type'), params.get('site_description'
            ), params.get('site_state_province'), params.get('metric_profile'
            ), params.get('group_name'), params.get('uuid_virtual_domain'
            ), params.get('virtual_domain_name'), params.get(
            'virtual_domain_description'), params.get('object_name'
            ), params.get('model'), params.get('type'), params.get('brand'
            ), params.get('modello_serie'), params.get('marca_modello_serie'
            ), params.get('end_of_life'), params.get('metric_type_name'
            ), params.get('firmware'), params.get('last_firmware_version'
            ), params.get('last_value_description'), params.get(
            'password_created_time'), params.get('password_expiring_date'
            ), params.get('password_warning_threshold'), params.get(
            'password_critical_threshold'), params.get('object_last_check_ts'
            ), params.get('status'), params.get('uuid_downtime'), params.get(
            'downtime_code'), params.get('downtime_description'), params.get(
            'downtime_start'), params.get('downtime_end'), params.get(
            'date_start'), params.get('date_end'), params.get('skip'
            ), params.get('limit'), params.get('like'), params.get('join'
            ), params.get('count')
        if not self._silence_warning:
            warning_wrong_parameters(self.firmware_updates.__name__, params,
                official_params_list)
        response = self.execute('GET', path=f'/firmware_updates/',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, **kwargs)
        return response

    def firmware_updates_grouped(self, uuid_customer: str,
        warm_start: bool = False, single_page: bool = False,
        page_size: int = 5000, kwargs: dict = None, **params) -> list:
        """Read Firmware Updates Grouped

        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            column (string required): additional filter - parameter
            site_code (string optional): additional filter - parameter
            uuid_metric (string optional): additional filter - parameter
            site_city (string optional): additional filter - parameter
            site_country (string optional): additional filter - parameter
            site_address (string optional): additional filter - parameter
            site_zip_code (string optional): additional filter - parameter
            site_type (string optional): additional filter - parameter
            site_description (string optional): additional filter - parameter
            site_state_province (string optional): additional filter - parameter
            site_region (string optional): additional filter - parameter
            metric_profile (string optional): additional filter - parameter
            group_name (string optional): additional filter - parameter
            uuid_virtual_domain (string optional): additional filter - parameter
            virtual_domain_name (string optional): additional filter - parameter
            virtual_domain_description (string optional): additional filter - parameter
            object_name (string optional): additional filter - parameter
            model (string optional): additional filter - parameter
            type (string optional): additional filter - parameter
            brand (string optional): additional filter - parameter
            modello_serie (string optional): additional filter - parameter
            marca_modello_serie (string optional): additional filter - parameter
            metric_type_name (string optional): additional filter - parameter
            firmware (string optional): additional filter - parameter
            last_firmware_version (string optional): additional filter - parameter
            last_value_description (string optional): additional filter - parameter
            password_created_time (string optional): additional filter - parameter
            password_expiring_date (string optional): additional filter - parameter
            password_warning_threshold (string optional): additional filter - parameter
            password_critical_threshold (string optional): additional filter - parameter
            object_last_check_ts (string optional): additional filter - parameter
            status (string optional): additional filter - parameter
            uuid_downtime (string optional): additional filter - parameter
            downtime_code (string optional): additional filter - parameter
            downtime_description (string optional): additional filter - parameter
            downtime_start (string optional): additional filter - parameter
            downtime_end (string optional): additional filter - parameter
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
        official_params_list = ['column', 'site_code', 'uuid_metric',
            'site_city', 'site_country', 'site_address', 'site_zip_code',
            'site_type', 'site_description', 'site_state_province',
            'site_region', 'metric_profile', 'group_name',
            'uuid_virtual_domain', 'virtual_domain_name',
            'virtual_domain_description', 'object_name', 'model', 'type',
            'brand', 'modello_serie', 'marca_modello_serie',
            'metric_type_name', 'firmware', 'last_firmware_version',
            'last_value_description', 'password_created_time',
            'password_expiring_date', 'password_warning_threshold',
            'password_critical_threshold', 'object_last_check_ts', 'status',
            'uuid_downtime', 'downtime_code', 'downtime_description',
            'downtime_start', 'downtime_end', 'date_start', 'date_end',
            'skip', 'limit', 'like', 'join', 'count']
        params.get('column'), params.get('site_code'), params.get('uuid_metric'
            ), params.get('site_city'), params.get('site_country'), params.get(
            'site_address'), params.get('site_zip_code'), params.get(
            'site_type'), params.get('site_description'), params.get(
            'site_state_province'), params.get('site_region'), params.get(
            'metric_profile'), params.get('group_name'), params.get(
            'uuid_virtual_domain'), params.get('virtual_domain_name'
            ), params.get('virtual_domain_description'), params.get(
            'object_name'), params.get('model'), params.get('type'
            ), params.get('brand'), params.get('modello_serie'), params.get(
            'marca_modello_serie'), params.get('metric_type_name'), params.get(
            'firmware'), params.get('last_firmware_version'), params.get(
            'last_value_description'), params.get('password_created_time'
            ), params.get('password_expiring_date'), params.get(
            'password_warning_threshold'), params.get(
            'password_critical_threshold'), params.get('object_last_check_ts'
            ), params.get('status'), params.get('uuid_downtime'), params.get(
            'downtime_code'), params.get('downtime_description'), params.get(
            'downtime_start'), params.get('downtime_end'), params.get(
            'date_start'), params.get('date_end'), params.get('skip'
            ), params.get('limit'), params.get('like'), params.get('join'
            ), params.get('count')
        if not self._silence_warning:
            warning_wrong_parameters(self.firmware_updates_grouped.__name__,
                params, official_params_list)
        response = self.execute('GET', path=
            f'/firmware_updates/{uuid_customer}/grouped/', single_page=
            single_page, page_size=page_size, warm_start=warm_start, params
            =params, **kwargs)
        return response

    def firmware_updates_planned_maintenances(self,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """Read Planned Maintenances

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            profile (string optional): additional filter - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs.copy(),
            params=params.copy())
        official_params_list = ['profile']
        params.get('profile')
        if not self._silence_warning:
            warning_wrong_parameters(self.
                firmware_updates_planned_maintenances.__name__, params,
                official_params_list)
        response = self.execute('GET', path=
            f'/firmware_updates/planned_maintenances/', warm_start=
            warm_start, params=params, **kwargs)
        return response

    def firmware_updates_password(self, ip: str, port: str,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """Read Password

        Args:
            ip (str, required): ip
            port (str, required): port
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            uuid_metric (string optional): additional filter - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs.copy(),
            params=params.copy())
        official_params_list = ['uuid_metric']
        params.get('uuid_metric')
        if not self._silence_warning:
            warning_wrong_parameters(self.firmware_updates_password.
                __name__, params, official_params_list)
        response = self.execute('GET', path=
            f'/firmware_updates/password/{ip}/{port}/', warm_start=
            warm_start, params=params, **kwargs)
        return response

    def firmware_updates_kpi_iot(self, warm_start: bool = False,
        kwargs: dict = None, **params) -> list:
        """Read Kpi Iot

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            produce_xlsx (boolean optional): additional filter - parameter
            uuid_customer (string optional): additional filter - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs.copy(),
            params=params.copy())
        official_params_list = ['produce_xlsx', 'uuid_customer']
        params.get('produce_xlsx'), params.get('uuid_customer')
        if not self._silence_warning:
            warning_wrong_parameters(self.firmware_updates_kpi_iot.__name__,
                params, official_params_list)
        response = self.execute('GET', path=f'/firmware_updates/kpi_iot/',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def firmware_updates_discovery_status(self, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Read Discovery Status

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            uuid_customer (string optional): additional filter - parameter
            site_type (string optional): additional filter - parameter
            site_code (string optional): additional filter - parameter
            site_address (string optional): additional filter - parameter
            site_zip_code (string optional): additional filter - parameter
            site_city (string optional): additional filter - parameter
            site_country (string optional): additional filter - parameter
            site_description (string optional): additional filter - parameter
            site_state_province (string optional): additional filter - parameter
            site_region (string optional): additional filter - parameter
            uuid_virtual_domain (string optional): additional filter - parameter
            group_name (string optional): additional filter - parameter
            virtual_domain_name (string optional): additional filter - parameter
            virtual_domain_description (string optional): additional filter - parameter
            object_name (string optional): additional filter - parameter
            traffico_attivo (string optional): additional filter - parameter
            ultima_attivita (string optional): additional filter - parameter
            sorgente_presente (string optional): additional filter - parameter
            sorgente (string optional): additional filter - parameter
            null_fields (string optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_params_list = ['sort_by', 'uuid_customer', 'site_type',
            'site_code', 'site_address', 'site_zip_code', 'site_city',
            'site_country', 'site_description', 'site_state_province',
            'site_region', 'uuid_virtual_domain', 'group_name',
            'virtual_domain_name', 'virtual_domain_description',
            'object_name', 'traffico_attivo', 'ultima_attivita',
            'sorgente_presente', 'sorgente', 'null_fields', 'skip', 'limit',
            'like', 'join', 'count']
        params.get('sort_by'), params.get('uuid_customer'), params.get(
            'site_type'), params.get('site_code'), params.get('site_address'
            ), params.get('site_zip_code'), params.get('site_city'
            ), params.get('site_country'), params.get('site_description'
            ), params.get('site_state_province'), params.get('site_region'
            ), params.get('uuid_virtual_domain'), params.get('group_name'
            ), params.get('virtual_domain_name'), params.get(
            'virtual_domain_description'), params.get('object_name'
            ), params.get('traffico_attivo'), params.get('ultima_attivita'
            ), params.get('sorgente_presente'), params.get('sorgente'
            ), params.get('null_fields'), params.get('skip'), params.get(
            'limit'), params.get('like'), params.get('join'), params.get(
            'count')
        if not self._silence_warning:
            warning_wrong_parameters(self.firmware_updates_discovery_status
                .__name__, params, official_params_list)
        response = self.execute('GET', path=
            f'/firmware_updates/discovery_status/', single_page=single_page,
            page_size=page_size, warm_start=warm_start, params=params, **kwargs
            )
        return response
