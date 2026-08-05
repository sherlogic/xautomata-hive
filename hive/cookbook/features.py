from hive.api import ApiManager, handling_single_page_methods, warning_wrong_parameters


class Features(ApiManager):
    """Class that handles all the XAutomata features APIs"""

    def features(self, warm_start: bool = False, kwargs: dict = None, **headers
        ) -> list:
        """Get Api Features Settings

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **headers: additional HTTP headers required by the API.

        Keyword Args:
            user-agent (string optional): additional filter - header

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_headers_list = ['user-agent']
        headers.get('user-agent')
        if not self._silence_warning:
            warning_wrong_parameters(self.features.__name__, headers,
                official_headers_list)
        response = self.execute('GET', path=f'/features/', warm_start=
            warm_start, headers=headers, **kwargs)
        return response
