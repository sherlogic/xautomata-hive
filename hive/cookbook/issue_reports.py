from hive.api import ApiManager, handling_single_page_methods, warning_wrong_parameters


class IssueReports(ApiManager):
    """Class that handles all the XAutomata issue_reports APIs"""

    def issue_reports(self, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Read Issue Reports

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            null_fields (string optional): additional filter - parameter
            url (string optional): additional filter - parameter
            username (string optional): additional filter - parameter
            issue_type (string optional): additional filter - parameter
            subject (string optional): additional filter - parameter
            file_name (string optional): additional filter - parameter
            file_type (string optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_params_list = ['sort_by', 'null_fields', 'url', 'username',
            'issue_type', 'subject', 'file_name', 'file_type', 'skip',
            'limit', 'like', 'join', 'count']
        params.get('sort_by'), params.get('null_fields'), params.get('url'
            ), params.get('username'), params.get('issue_type'), params.get(
            'subject'), params.get('file_name'), params.get('file_type'
            ), params.get('skip'), params.get('limit'), params.get('like'
            ), params.get('join'), params.get('count')
        if not self._silence_warning:
            warning_wrong_parameters(self.issue_reports.__name__, params,
                official_params_list)
        response = self.execute('GET', path=f'/issue_reports/', single_page
            =single_page, page_size=page_size, warm_start=warm_start,
            params=params, **kwargs)
        return response

    def issue_reports_create(self, params: dict = False,
        kwargs: dict = None, **payload) -> list:
        """Create Issue Report

        Args:
            params (dict, optional): additional parameters for the API.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.

        Keyword Args:
            url (string required): additional filter - parameter
            issue_type (string required): additional filter - parameter
            subject (string required): additional filter - parameter
            message (string required): additional filter - parameter
            file (string optional): additional filter - payload

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_payload_list = ['file']
        payload.get('file')
        if not self._silence_warning:
            warning_wrong_parameters(self.issue_reports_create.__name__,
                payload, official_payload_list)
        response = self.execute('POST', path=f'/issue_reports/', params=
            params, payload=payload, **kwargs)
        return response

    def issue_report(self, uuid: str, warm_start: bool = False,
        kwargs: dict = None, **params) -> list:
        """Read Issue Report

        Args:
            uuid (str, required): uuid
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs.copy(),
            params=params.copy())
        official_params_list = ['join']
        params.get('join')
        if not self._silence_warning:
            warning_wrong_parameters(self.issue_report.__name__, params,
                official_params_list)
        response = self.execute('GET', path=f'/issue_reports/{uuid}',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def issue_reports_put(self, uuid: str, kwargs: dict = None, **payload
        ) -> list:
        """Update Issue Report

        Args:
            uuid (str, required): uuid
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.

        Keyword Args:
            url (string optional): additional filter - payload
            issue_type (string optional): additional filter - payload
            subject (string optional): additional filter - payload
            message (string optional): additional filter - payload

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_payload_list = ['url', 'issue_type', 'subject', 'message']
        payload.get('url'), payload.get('issue_type'), payload.get('subject'
            ), payload.get('message')
        if not self._silence_warning:
            warning_wrong_parameters(self.issue_reports_put.__name__,
                payload, official_payload_list)
        response = self.execute('PUT', path=f'/issue_reports/{uuid}',
            payload=payload, **kwargs)
        return response

    def issue_reports_delete(self, uuid: str, kwargs: dict = None) -> list:
        """Delete Issue Report

        Args:
            uuid (str, required): uuid
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('DELETE', path=f'/issue_reports/{uuid}', **
            kwargs)
        return response

    def issue_reports_download(self, uuid: str, warm_start: bool = False,
        kwargs: dict = None) -> list:
        """Download Issue Report File

        Args:
            uuid (str, required): uuid
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=
            f'/issue_reports/{uuid}/download', warm_start=warm_start, **kwargs)
        return response
