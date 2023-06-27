from hive.api import ApiManager
from hive.api import handling_single_page_methods


class Groups(ApiManager):

    def groups(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None,
               **params):
        """
        metodo che restituisce tutti i groups

        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: parametri in piu che si vuole passare alla API

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            like (bool, optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True.
            sort_by (str, optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "".
            null_fileds (str, optional): Stringa separata da virgole di campi di cui si vuole rimuovere, o imporre, un valore nullo nel result set. Esempio "campo:nullable". Default to "".
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False
            extract_severity (bool, optional): Se True nella risposta e' anche presente la severita, Default to False.
            uuid_parent (str, optional): additional filter
            uuid_site (str, optional): additional filter
            uuid_virtual_domain (str, optional): additional filter
            type (str, optional): additional filter
            name (str, optional): additional filter
            description (str, optional): additional filter
            status (str, optional): additional filter

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/groups/', single_page=single_page, page_size=page_size, params=params,
                                warm_start=warm_start, **kwargs)
        return response

    def group(self, uuid: str, warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch single metric.

        Args:
            uuid (str): uuid del gruppo da recuperare
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Keyword Args:
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/groups/{uuid}', warm_start=warm_start, params=params, **kwargs)
        return response

    def groups_objects(self, uuid: str, single_page: bool = False, page_size: int = 5000, warm_start: bool = False,
                       kwargs: dict = None, **params):
        """
        Fetch all objects related to a certain group, referenced by its UUID

        Args:
            uuid (str): uuid di un gruppo di cui si vuole sapere quali oggetti possiede
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            extract_severity (bool, optional): Se True nella risposta e' anche presente la severita, Default to False.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/groups/{uuid}/objects', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def group_put(self, uuid: str, kwargs: dict = None, **payload):
        """
        update selected group.

        Args:
            uuid (str): uuid della group da modificare
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Keyword Args:
            uuid_parent (str, optional): additional filter
            uuid_site (str, optional): additional filter
            uuid_virtual_domain (str, optional): additional filter
            type (str, optional): additional filter
            name (str, optional): additional filter
            description (str, optional): additional filter
            automata_domain (list or dict, optional): automata domain
            status (str, optional): additional filter

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('PUT', path=f'/groups/{uuid}', payload=payload, **kwargs)
        return response

    def group_delete(self, uuid: str, kwargs: dict = None):
        """

        delete single group.

        Args:
            uuid: id del group da eliminare
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/groups/{uuid}', **kwargs)
        return response

    def groups_delete_bulk(self, payload: list, single_page: bool = False,
                           page_size: int = 5000, kwargs: dict = None):
        """
        elimina le metriche in bulk

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/groups/bulk/delete/', single_page=single_page, page_size=page_size,
                                payload=payload, **kwargs)
        return response

    def groups_bulk(self, payload: list, single_page: bool = False,
                    page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):
        """
        fetch le metriche in bulk

        Args:
            payload (list[dict], optional): List dict to create.
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
        response = self.execute('POST', path='/groups/bulk/read/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, params=params, **kwargs)
        return response

    def groups_objects_create_bulk(self, payload: list, best_effort: bool = True, single_page: bool = False,
                                   page_size: int = 5000, kwargs: dict = None):
        """
        elimina le metriche in bulk

        Args:
            payload (list[dict], optional): List dict to create.
            best_effort (bool, optional): se a True forza a proseguire anche se un elemento genera un errore
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Examples:
            uuids = [
                      {
                        "uuid_group": "string",
                        "uuid_object": "string"
                      }
                    ]

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/groups/bulk/create/objects', single_page=single_page, page_size=page_size,
                                payload=payload, params={'best_effort': best_effort}, **kwargs)
        return response

    def groups_objects_delete_bulk(self, payload: list, single_page: bool = False,
                                   page_size: int = 5000, warm_start: bool = False, kwargs: dict = None):
        """
        elimina le metriche in bulk

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Examples:
            objects_groups = [
                              {
                                "uuid_group": "string",
                                "uuid_object": "string"
                              }
                            ]

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/groups/bulk/delete/objects', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, **kwargs)
        return response