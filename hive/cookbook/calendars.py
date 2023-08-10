from hive.api import ApiManager, handling_single_page_methods


class Calendars(ApiManager):
    """Class that handles all the XAutomata calendars APIs"""

    def calendars(self, warm_start: bool = False, single_page: bool = False,
        page_size: int = 5000, kwargs: dict = None, **params) -> list:
        """Read Calendars
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            null_fields (string optional): additional filter - parameter
            name (string optional): additional filter - parameter
            local_public_holidays (boolean optional): additional filter - parameter
            mon_int1_start (string optional): additional filter - parameter
            mon_int1_end (string optional): additional filter - parameter
            mon_int2_start (string optional): additional filter - parameter
            mon_int2_end (string optional): additional filter - parameter
            tue_int1_start (string optional): additional filter - parameter
            tue_int1_end (string optional): additional filter - parameter
            tue_int2_start (string optional): additional filter - parameter
            tue_int2_end (string optional): additional filter - parameter
            wed_int1_start (string optional): additional filter - parameter
            wed_int1_end (string optional): additional filter - parameter
            wed_int2_start (string optional): additional filter - parameter
            wed_int2_end (string optional): additional filter - parameter
            thu_int1_start (string optional): additional filter - parameter
            thu_int1_end (string optional): additional filter - parameter
            thu_int2_start (string optional): additional filter - parameter
            thu_int2_end (string optional): additional filter - parameter
            fri_int1_start (string optional): additional filter - parameter
            fri_int1_end (string optional): additional filter - parameter
            fri_int2_start (string optional): additional filter - parameter
            fri_int2_end (string optional): additional filter - parameter
            sat_int1_start (string optional): additional filter - parameter
            sat_int1_end (string optional): additional filter - parameter
            sat_int2_start (string optional): additional filter - parameter
            sat_int2_end (string optional): additional filter - parameter
            sun_int1_start (string optional): additional filter - parameter
            sun_int1_end (string optional): additional filter - parameter
            sun_int2_start (string optional): additional filter - parameter
            sun_int2_end (string optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/calendars/', single_page=
            single_page, page_size=page_size, warm_start=warm_start, params
            =params, **kwargs)
        return response

    def calendars_create(self, kwargs: dict = None, **payload) -> list:
        """Create Calendar
        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            name (string required): additional filter - payload
            local_public_holidays (boolean required): additional filter - payload
            mon_int1_start (string optional): additional filter - payload
            mon_int1_end (string optional): additional filter - payload
            mon_int2_start (string optional): additional filter - payload
            mon_int2_end (string optional): additional filter - payload
            tue_int1_start (string optional): additional filter - payload
            tue_int1_end (string optional): additional filter - payload
            tue_int2_start (string optional): additional filter - payload
            tue_int2_end (string optional): additional filter - payload
            wed_int1_start (string optional): additional filter - payload
            wed_int1_end (string optional): additional filter - payload
            wed_int2_start (string optional): additional filter - payload
            wed_int2_end (string optional): additional filter - payload
            thu_int1_start (string optional): additional filter - payload
            thu_int1_end (string optional): additional filter - payload
            thu_int2_start (string optional): additional filter - payload
            thu_int2_end (string optional): additional filter - payload
            fri_int1_start (string optional): additional filter - payload
            fri_int1_end (string optional): additional filter - payload
            fri_int2_start (string optional): additional filter - payload
            fri_int2_end (string optional): additional filter - payload
            sat_int1_start (string optional): additional filter - payload
            sat_int1_end (string optional): additional filter - payload
            sat_int2_start (string optional): additional filter - payload
            sat_int2_end (string optional): additional filter - payload
            sun_int1_start (string optional): additional filter - payload
            sun_int1_end (string optional): additional filter - payload
            sun_int2_start (string optional): additional filter - payload
            sun_int2_end (string optional): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/calendars/', payload=
            payload, **kwargs)
        return response

    def calendar(self, uuid: str, warm_start: bool = False, kwargs: dict = None
        ) -> list:
        """Read Calendar
        Args:
            uuid (str, required): uuid
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/calendars/{uuid}',
            warm_start=warm_start, **kwargs)
        return response

    def calendars_put(self, uuid: str, kwargs: dict = None, **payload) -> list:
        """Update Calendar
        Args:
            uuid (str, required): uuid
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            name (string optional): additional filter - payload
            local_public_holidays (boolean optional): additional filter - payload
            mon_int1_start (string optional): additional filter - payload
            mon_int1_end (string optional): additional filter - payload
            mon_int2_start (string optional): additional filter - payload
            mon_int2_end (string optional): additional filter - payload
            tue_int1_start (string optional): additional filter - payload
            tue_int1_end (string optional): additional filter - payload
            tue_int2_start (string optional): additional filter - payload
            tue_int2_end (string optional): additional filter - payload
            wed_int1_start (string optional): additional filter - payload
            wed_int1_end (string optional): additional filter - payload
            wed_int2_start (string optional): additional filter - payload
            wed_int2_end (string optional): additional filter - payload
            thu_int1_start (string optional): additional filter - payload
            thu_int1_end (string optional): additional filter - payload
            thu_int2_start (string optional): additional filter - payload
            thu_int2_end (string optional): additional filter - payload
            fri_int1_start (string optional): additional filter - payload
            fri_int1_end (string optional): additional filter - payload
            fri_int2_start (string optional): additional filter - payload
            fri_int2_end (string optional): additional filter - payload
            sat_int1_start (string optional): additional filter - payload
            sat_int1_end (string optional): additional filter - payload
            sat_int2_start (string optional): additional filter - payload
            sat_int2_end (string optional): additional filter - payload
            sun_int1_start (string optional): additional filter - payload
            sun_int1_end (string optional): additional filter - payload
            sun_int2_start (string optional): additional filter - payload
            sun_int2_end (string optional): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('PUT', path=f'/calendars/{uuid}', payload=
            payload, **kwargs)
        return response

    def calendars_delete(self, uuid: str, kwargs: dict = None) -> list:
        """Delete Calendar
        Args:
            uuid (str, required): uuid
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('DELETE', path=f'/calendars/{uuid}', **kwargs)
        return response

    def calendars_bulk(self, payload: list, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Bulk Read Calendars
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
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
        Examples:
            payload = 
          [
            "uuid": "str", required
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/calendars/bulk/read/',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, payload=payload, **kwargs)
        return response

    def calendars_create_bulk(self, payload: list,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Bulk Create Calendars
        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            best_effort (boolean optional): additional filter - parameter
        Examples:
            payload = 
          [
           {
            "name": "string", required
            "local_public_holidays": "boolean", required
            "mon_int1_start": "string", optional
            "mon_int1_end": "string", optional
            "mon_int2_start": "string", optional
            "mon_int2_end": "string", optional
            "tue_int1_start": "string", optional
            "tue_int1_end": "string", optional
            "tue_int2_start": "string", optional
            "tue_int2_end": "string", optional
            "wed_int1_start": "string", optional
            "wed_int1_end": "string", optional
            "wed_int2_start": "string", optional
            "wed_int2_end": "string", optional
            "thu_int1_start": "string", optional
            "thu_int1_end": "string", optional
            "thu_int2_start": "string", optional
            "thu_int2_end": "string", optional
            "fri_int1_start": "string", optional
            "fri_int1_end": "string", optional
            "fri_int2_start": "string", optional
            "fri_int2_end": "string", optional
            "sat_int1_start": "string", optional
            "sat_int1_end": "string", optional
            "sat_int2_start": "string", optional
            "sat_int2_end": "string", optional
            "sun_int1_start": "string", optional
            "sun_int1_end": "string", optional
            "sun_int2_start": "string", optional
            "sun_int2_end": "string", optional
           }
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/calendars/bulk/create/',
            single_page=single_page, page_size=page_size, params=params,
            payload=payload, **kwargs)
        return response

    def calendars_delete_bulk(self, payload: list,
        single_page: bool = False, page_size: int = 5000, kwargs: dict = None
        ) -> list:
        """Bulk Delete Calendars
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
            "uuid": "str", required
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/calendars/bulk/delete/',
            single_page=single_page, page_size=page_size, payload=payload,
            **kwargs)
        return response
