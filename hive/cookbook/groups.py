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

    def groups_post(self, kwargs: dict = None, **payload):
        """
        post selected groups.

        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Keyword Args:
            uuid_parent (str, optionsl): uuid della parent
            uuid_site (str, required): uuid del site
            uuid_virtual_domain (str, required): additional filter
            name (str): additional filter, required
            description (str, optional): additional filter
            type (str): additional filter, required
            automata_domain (list, optional): additional filter
            status (str): additional filter, required

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/groups/', payload=payload, **kwargs)
        return response

    def group(self, uuid: str, warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch single metric.

        Args:
            uuid (str): uuid del gruppo da recuperare
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: parametri in piu che si vuole passare alla API

        Keyword Args:
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/groups/{uuid}', warm_start=warm_start, params=params, **kwargs)
        return response

    def groups_put(self, uuid: str, kwargs: dict = None, **payload):
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

    def groups_delete(self, uuid: str, kwargs: dict = None):

        """
        delete single group.

        Args:
            uuid: uuid del group da eliminare
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/groups/{uuid}', **kwargs)
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
            like (bool,optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True.
            profile (str,optional): additional filter
            sort_by (str,optional): additional filter
            join (bool,optional): additional filter

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/groups/{uuid}/objects', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def groups_object_post(self, uuid: str, uuid_object: str, kwargs: dict = None):

        """
        create link between selected group and selected object.

        Args:
            uuid (str): uuid della group
            uuid_object (str): uuid della object
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/groups/{uuid}/objects/{uuid_object}', **kwargs)
        return response

    def groups_object_delete(self, uuid: str, uuid_object: str, kwargs: dict = None):
        """
        delete link between selected group and selected object.

        Args:
            uuid (str): uuid della group
            uuid_object (str): uuid della object
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/groups/{uuid}/objects/{uuid_object}', **kwargs)
        return response

    def groups_user(self, uuid: str, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):

        """
        get the user linked with a group.

        Args:
            uuid (str): uuid group
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: parametri in piu che si vuole passare alla API

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False
            not_in (str,optional) additional filter.
            like (bool,optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True.

        Returns: list

        """

        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/groups/{uuid}/users', single_page=single_page, page_size=page_size, params=params,
                                warm_start=warm_start, **kwargs)

        return response

    def groups_users_post(self, kwargs: dict = None, uuid=str, name=str):

        """
        post selected groups_users.

        Args:
            uuid: uuid della group
            name (str): additional filter, required
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list

        """

        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/groups/{uuid}/users/{name}', **kwargs)
        return response

    def groups_users_delete(self, uuid: str, name: str, kwargs: dict = None):

        """
        delete selected groups_users.

        Args:
            uuid (str): uuid della group
            name (str): additional filter
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Keyword Args:
            name (str): additional filter, required

        Returns: list
        """

        if kwargs is None: kwargs = dict()

        response = self.execute('DELETE', path=f'/groups/{uuid}/users/{name}', **kwargs)

        return response

    def groups_downtime(self, uuid: str, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):

        """
        get the downtimes linked with a group.

        Args:
            uuid (str, required): uuid del group
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: parametri in piu che si vuole passare alla API

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False
            active_at_timestamp (str, optional): additional filter
            not_in (bool, optional): additional filter

        Returns: list

        """

        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/groups/{uuid}/downtimes', single_page=single_page, page_size=page_size, params=params,
                                warm_start=warm_start, **kwargs)

        return response

    def groups_downtimes_post(self, uuid: str, uuid_downtime: str, kwargs: dict = None):

        """

        create link between selected object and selected downtime.

        Args:
            uuid (str, required): uuid della group
            uuid_downtime (str, required): uuid del downtime
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/groups/{uuid}/downtimes/{uuid_downtime}',  **kwargs)
        return response

    def groups_downtimes_delete(self, uuid: str, uuid_downtime: str, kwargs: dict = None):

        """
        remove downtime linked with the group.

        Args:
            uuid (str, required): uuid della group
            uuid_downtime (str, required): uuid del downtime
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/groups/{uuid}/downtimes/{uuid_downtime}', **kwargs)
        return response

    def groups_dispatchers(self, uuid: str, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):

        """
        metodo che restituisce i dispatchers di un group

        Args:
            uuid (str, required): uuid della group
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
            join (bool, optional): additional filter
            not_in (nool, optional): additional filter
            active_at_timestamp (str, optional): additional filter

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/groups/{uuid}/dispatchers', single_page=single_page, page_size=page_size, params=params,
                                warm_start=warm_start, **kwargs)
        return response

    def groups_dispatchers_post(self, uuid: str, uuid_dispatcher: str, kwargs: dict = None):

        """
        create link between selected group and selected dispatcher.
        Args:
            uuid (str, required): uuid della group
            uuid_dispatcher (str, required): uuid della dispatcher
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """

        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/groups/{uuid}/dispatchers/{uuid_dispatcher}', **kwargs)

        return response

    def groups_dispatchers_delete(self, uuid: str, uuid_dispatcher: str, kwargs: dict = None):

        """
        delete dispatcher linked with the group.

        Args:
            uuid (str, required): uuid della group
            uuid_dispatcher (str, required): uuid del dispatcher
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/groups/{uuid}/dispatchers/{uuid_dispatcher}', **kwargs)
        return response

    def groups_delete_bulk(self, payload: list, single_page: bool = False,
                           page_size: int = 5000, kwargs: dict = None):
        """
        elimina i groups in bulk

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
        fetch i groups in bulk

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
        elimina la lista tra groups e object in bulk

        Args:
            payload (list[dict], optional): List dict to create.
            best_effort (bool, optional): se a True forza a proseguire anche se un elemento genera un errore
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
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
        response = self.execute('POST', path='/groups/bulk/create/objects', single_page=single_page, page_size=page_size,
                                payload=payload, params={'best_effort': best_effort}, **kwargs)
        return response

    def groups_objects_delete_bulk(self, payload: list, single_page: bool = False,
                                   page_size: int = 5000, kwargs: dict = None):
        """
        elimina i groups in bulk

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
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
                                payload=payload, **kwargs)
        return response

    def groups_downtimes_create_bulk(self, payload: list, single_page: bool = False,
                                     page_size: int = 5000,  kwargs: dict = None, **params):
        """
        crea le bulk di groups_downtime
        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params

        kwargs:
            best_effort (bool, optional): se a True forza a proseguire anche se un elemento genera un errore

        Examples:[
                    {
                        "uuid_downtime": "string",
                        "uuid_group": "string"
                    }
                ]

        Returns: list
        """

        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/groups/bulk/create/downtimes', single_page=single_page, page_size=page_size,
                                payload=payload, params=params, **kwargs)
        return response

    def groups_downtimes_delete_bulk(self, payload: list, single_page: bool = False, page_size: int = 5000, kwargs: dict = None):
        """
        cancella le bulk di groups_downtimes
        Args:
            payload (list[str], optional): additional filter
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Examples:
            payload = [payload
                    {
                        "uuid_downtime": "string",
                        "uuid_group": "string"
                    }
                ]

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path="/groups/bulk/delete/downtimes", single_page=single_page, page_size=page_size,
                                payload=payload, **kwargs)
        return response

    def groups_users_create_bulk(self, payload: list, single_page: bool = False,
                                 page_size: int = 5000,  kwargs: dict = None, **params):
        """
        crea le bulk di groups_users
        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params

        kwargs:
            best_effort (bool, optional): se a True forza a proseguire anche se un elemento genera un errore

        Examples:[
                    {
                    "username": "string",
                    "uuid_group": "string"
                    }
                ]

        Returns: list
        """

        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/groups/bulk/create/users', single_page=single_page, page_size=page_size,
                                payload=payload, params=params, **kwargs)
        return response

    def groups_users_delete_bulk(self, payload: list, single_page: bool = False, page_size: int = 5000, kwargs: dict = None, **params):
        """
        cancella le bulk di groups_users
        Args:
            payload (list[str], optional): additional filter
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: parametri in piu che si vuole passare alla API
        Examples:
            payload = [
                    {
                    "username": "string",
                    "uuid_group": "string"
                    }
                ]

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path="/users/bulk/delete/downtimes", single_page=single_page, page_size=page_size,
                                payload=payload, params=params, **kwargs)
        return response

    def groups_read_by_bulk(self, payload: list, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None):
        """
        reads groups_bulk by code
        Args:
            payload (list[str], optional): additional filter
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Examples:[
                    {
                        "uuid_site": "string",
                        "uuid_virtual_domain": "string",
                        "name": "string"
                    }
                ]
        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path="/groups/bulk/read_by/", single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, **kwargs)
        return response

    def groups_create_bulk(self, payload: list, single_page: bool = False,
                           page_size: int = 5000,  kwargs: dict = None, **params):
        """
        crea le bulk di groups

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params

        kwargs:
            best_effort (bool, optional): se a True forza a proseguire anche se un elemento genera un errore

        Examples:[
                    {
                        "uuid_parent": "string",
                        "uuid_site": "string",
                        "uuid_virtual_domain": "string",
                        "type": "string",
                        "name": "string",
                        "description": "string",
                        "automata_domain":[
                            "string"
                        ]
                        "status": "s"
                    }
                ]

        Returns: list
        """

        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/groups/bulk/create/', single_page=single_page, page_size=page_size,
                                payload=payload, params=params, **kwargs)
        return response