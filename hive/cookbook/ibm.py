from hive.api import ApiManager, handling_single_page_methods, warning_wrong_parameters


class Ibm(ApiManager):
    """Class that handles all the XAutomata ibm APIs"""

    def ibm_login(self, warm_start: bool = False, kwargs: dict = None) -> list:
        """Ibm Login

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/ibm/login', warm_start=
            warm_start, **kwargs)
        return response

    def ibm_callback(self, warm_start: bool = False, kwargs: dict = None
        ) -> list:
        """Ibm Callback

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/ibm/callback', warm_start=
            warm_start, **kwargs)
        return response
