from hive.api import ApiManager, handling_single_page_methods


class TsServiceValue(ApiManager):
    """Class that handles all the XAutomata ts_service_value APIs"""

    def ts_service_value(self, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Read Value Services
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            null_fields (string optional): additional filter - parameter
            uuid_service (string optional): additional filter - parameter
            timestamp_start (string optional): additional filter - parameter
            timestamp_end (string optional): additional filter - parameter
            database_timestamp_start (string optional): additional filter - parameter
            database_timestamp_end (string optional): additional filter - parameter
            unit (string optional): additional filter - parameter
            value (number optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/ts_service_value/',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, **kwargs)
        return response

    def ts_service_value_create(self, kwargs: dict = None, **payload) -> list:
        """Create Timeseries Service Value
        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            uuid_service (string required): additional filter - payload
            timestamp (string required): additional filter - payload
            unit (string required): additional filter - payload
            value (number required): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/ts_service_value/', payload
            =payload, **kwargs)
        return response

    def ts_service_value_delete(self, uuid_service: str,
        kwargs: dict = None, **params) -> list:
        """Delete Timeseries Service Value
        Args:
            uuid_service (str, required): uuid_service
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            ts_start (string required): additional filter - parameter
            ts_end (string required): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('DELETE', path=
            f'/ts_service_value/{uuid_service}/', params=params, **kwargs)
        return response

    def ts_service_value_query(self, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Read Services
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            null_fields (string optional): additional filter - parameter
            uuid_parent (string optional): additional filter - parameter
            uuid_customer (string optional): additional filter - parameter
            profile (string optional): additional filter - parameter
            name (string optional): additional filter - parameter
            description (string optional): additional filter - parameter
            status (string optional): additional filter - parameter
            ts_timestamp_start (string optional): additional filter - parameter
            ts_timestamp_end (string optional): additional filter - parameter
            ts_unit (string optional): additional filter - parameter
            ts_value (number optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/ts_service_value/query/',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, **kwargs)
        return response

    def ts_service_value_bulk(self, payload: list, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Read Status Metrics
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            ts_start (string required): additional filter - parameter
            ts_end (string required): additional filter - parameter
        Examples:
            payload = 
          [
            "uuid": "str", required
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=
            f'/ts_service_value/bulk/read/', single_page=single_page,
            page_size=page_size, warm_start=warm_start, params=params,
            payload=payload, **kwargs)
        return response

    def ts_service_value_create_bulk(self, payload: list,
        single_page: bool = False, page_size: int = 5000, kwargs: dict = None
        ) -> list:
        """Bulk Create Ts Service Value
        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Examples:
            payload = 
          [
           {
            "uuid_service": "string", required
            "timestamp": "string", required
            "unit": "string", required
            "value": "number", required
           }
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=
            f'/ts_service_value/bulk/create/', single_page=single_page,
            page_size=page_size, payload=payload, **kwargs)
        return response

    def ts_service_value_delete_bulk(self, payload: list,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Bulk Delete Ts Service Value
        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            ts_start (string required): additional filter - parameter
            ts_end (string required): additional filter - parameter
        Examples:
            payload = 
          [
            "uuid": "str", required
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('DELETE', path=
            f'/ts_service_value/bulk/delete/', single_page=single_page,
            page_size=page_size, params=params, payload=payload, **kwargs)
        return response