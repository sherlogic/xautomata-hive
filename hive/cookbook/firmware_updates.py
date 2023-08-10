from hive.api import ApiManager, handling_single_page_methods


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
            code (string optional): additional filter - parameter
            uuid_customer (string optional): additional filter - parameter
            uuid_metric (string optional): additional filter - parameter
            model (string optional): additional filter - parameter
            type (string optional): additional filter - parameter
            firmware (string optional): additional filter - parameter
            status (None optional): additional filter - parameter
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
        response = self.execute('GET', path=f'/firmware_updates/',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, **kwargs)
        return response

    def firmware_updates_grouped(self, uuid_customer: str,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """Read Firmware Updates Grouped
        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            column (None required): additional filter - parameter
            code (string optional): additional filter - parameter
            uuid_metric (string optional): additional filter - parameter
            model (string optional): additional filter - parameter
            type (string optional): additional filter - parameter
            firmware (string optional): additional filter - parameter
            status (None optional): additional filter - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/firmware_updates/{uuid_customer}/grouped/', warm_start=
            warm_start, params=params, **kwargs)
        return response
