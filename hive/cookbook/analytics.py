from hive.api import ApiManager
from hive.api import handling_single_page_methods


class Analytics(ApiManager):

    def analytics(self, uuid: str, warm_start: bool = False, kwargs: dict = None, **params):
        """
        metodo che permette di recuperare la time serie di tutte le metriche. Si puo scegliere se ottenere le metriche di stato o di valore.

        Args:
            uuid (list): lista delle metriche di cui si vuole ottenere la time series.
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
            date_start ($date-time, optional): additional filter
            date_end ($date-time, optional): additional filter
            metric_profile (str, optional): additional filter
            metric_name (str, optional): additional filter

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/analytics/{uuid}', warm_start=warm_start, params=params, **kwargs)
        return response
