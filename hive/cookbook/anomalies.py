from hive.api import ApiManager
from hive.api import handling_single_page_methods


class Anomalies(ApiManager):

    def anomalies(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch all anomalies.

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
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False
            date_start (str, optional): data di inizio delle anomalie
            date_end (str, optional): data di fine delle anomalie
            uuid_customer (str, optional): uuid del cliente a cui appartengono le anomalie
            type (str, optional): tipo delle anomalie da recuperare
            value (str, optional): valore delle anomalie da recuperare
            sampling (str, optional): sampling con cui sono stati aggregati i dati delle anomalie (tipicamente numero + intervallo temporale, ex. 7D)

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path='/anomalies/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def anomaly(self, uuid: str, warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch single anomaly.

        Args:
            uuid (str): uuid dell'anomalia da recuperare
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/anomalies/{uuid}', warm_start=warm_start, params=params, **kwargs)
        return response

    def anomalies_create_bulk(self, payload: list, single_page: bool = False, page_size: int = 5000, kwargs: dict = None, **params):
        """
        create anomalies.

        Args:
            payload (list, required): list of anomalies to post
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            best_effort (bool, optional): if true, continues to send anomalies regardless of failing one post. Default to True

        Examples:
            anomalies= [
                    {
                        "date_anomaly_start": "2023-05-31",
                        "date_anomaly": "2023-05-31",
                        "uuid_customer": "string",
                        "type": "string",
                        "value": "string",
                        "sampling": "string",
                        "parameters": {}
                    }
                ]
        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/anomalies/bulk/create/', single_page=single_page,
                                page_size=page_size, params=params, payload=payload, **kwargs)
        return response

    def anomalys_delete(self, uuid: str, kwargs: dict = None):
        """
        delete single anomaly.

        Args:
            uuid: uuid dell'anomalia da eliminare
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/anomalies/{uuid}', **kwargs)
        return response

    def anomalys_post(self, kwargs: dict = None, **payload):
        """
        Post delle anomaly.

        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/anomalies/', payload=payload, **kwargs)
        return response

    def anomalys_bulk(self, groups: list, single_page: bool = False,
                      page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):
        """
        fetch le anomaly in bulk

        Args:
            groups (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            join (bool, optional): Aggiunge le info dei livelli superiori dell'albero. Default to False.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/anomalies/bulk/read/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=groups, params=params, **kwargs)
        return response

    def anomalys_delete_bulk(self, payload: list, single_page: bool = False,
                             page_size: int = 5000, kwargs: dict = None):
        """
        elimina le anomaly in bulk

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/anomalies/bulk/delete/', single_page=single_page, page_size=page_size,
                                payload=payload, **kwargs)
        return response
