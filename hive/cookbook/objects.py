from hive.api import ApiManager
from hive.api import handling_single_page_methods


class Objects(ApiManager):

    def objects(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None,
                **params):
        """
        metodo che restituisce tutti i objects

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
            extract_severity (bool, optional): Se True nella risposta e' anche presente la severita, Default to False.
            name (str, optional): additional filter
            description (str, optional): additional filter
            feedback_for_operator (str, optional): additional filter
            profile (str, optional): additional filter
            status (str, optional): additional filter

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/objects/', single_page=single_page, page_size=page_size, params=params,
                                warm_start=warm_start, **kwargs)
        return response

    def object(self, uuid: str, warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch single metric.

        Args:
            uuid (str): uuid del gruppo da recuperare
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/objects/{uuid}', warm_start=warm_start, params=params, **kwargs)
        return response

    def objects_metric_types(self, uuid: str, single_page: bool = False, page_size: int = 5000,
                             warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch all metric_types related to a certain object, referenced by its UUID

        Args:
            uuid (str): uuid di un oggetto di cui si vuole sapere quali metric_type possiede
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/objects/{uuid}/metric_types', single_page=single_page,
                                page_size=page_size, warm_start=warm_start, params=params, **kwargs)
        return response

    def objects_groups(self, uuid: str, kwargs: dict = None, **params):
        """
        get the groups linked with the object.

        Args:
            uuid (str): uuid della object
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False
            not_in (bool, optional)

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/objects/{uuid}/groups', params=params, **kwargs)
        return response

    def objects_groups_post(self, uuid: str, uuid_group: str, kwargs: dict = None, **payload):
        """
        create link between selected object and selected group.

        Args:
            uuid (str): uuid della object
            uuid_group (str): uuid della group
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/objects/{uuid}/groups/{uuid_group}', payload=payload, **kwargs)
        return response

    def objects_groups_delete(self, uuid: str, uuid_group: str, kwargs: dict = None):
        """
        delete link between selected object and selected group.

        Args:
            uuid (str): uuid della object
            uuid_group (str): uuid della group
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/objects/{uuid}/groups/{uuid_group}', **kwargs)
        return response

    def objects_probes(self, uuid: str, kwargs: dict = None, **payload):
        """
        get the probes linked with the object.

        Args:
            uuid (str): uuid della object
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/objects/{uuid}/probes', payload=payload, **kwargs)
        return response

    def objects_probes_post(self, uuid: str, uuid_probe: str, kwargs: dict = None, **payload):
        """
        create link between selected object and selected probe.

        Args:
            uuid (str): uuid della object
            uuid_probe (str): uuid della group
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/objects/{uuid}/probes/{uuid_probe}', payload=payload, **kwargs)
        return response

    def objects_probes_delete(self, uuid: str, uuid_probe: str, kwargs: dict = None, **payload):
        """
        delete link between selected object and selected group.

        Args:
            uuid (str): uuid della object
            uuid_probe (str): uuid della group
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/objects/{uuid}/probes/{uuid_probe}', payload=payload, **kwargs)
        return response

    def object_put(self, uuid: str, kwargs: dict = None, **payload):
        """
        update selected object.

        Args:
            uuid (str): uuid della object da modificare
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Keyword Args:
            name (str, optional): additional filter
            description (str, optional): additional filter
            feedback_for_operator (str, optional): additional filter
            ip_cidr (dict, optional): additional filter
            profile (str, optional): additional filter
            data_profile (dict, optional): additional filter
            automata_domain (list or dict, optional): automata domain
            status (str, optional): additional filter

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('PUT', path=f'/objects/{uuid}', payload=payload, **kwargs)
        return response

    def object_delete(self, uuid: str, kwargs: dict = None):
        """

        delete single object.

        Args:
            uuid: id del object da eliminare
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/objects/{uuid}', **kwargs)
        return response

    def objects_bulk(self, payload: list, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):
        """
        metodo che permette di recuperare la time serie di tutte le metriche. Si puo scegliere se ottenere le metriche di stato o di valore.

        Args:
            payload (list[str], optional): additional filter
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: parametri in piu che si vuole passare alla API

        Keyword Args:
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path="/objects/bulk/read/", single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, params=params, **kwargs)
        return response

    def objects_delete_bulk(self, payload: list, single_page: bool = False,
                            page_size: int = 5000, warm_start: bool = False, kwargs: dict = None):
        """
        elimina le metriche in bulk

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path='/objects/bulk/delete/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, **kwargs)
        return response

    def objects_groups_delete_bulk(self, payload: list, single_page: bool = False,
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
        response = self.execute('DELETE', path='/objects/bulk/delete/groups', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, **kwargs)
        return response

    def objects_groups_create_bulk(self, payload: list, single_page: bool = False,
                                   page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):
        """
        create le metriche in bulk

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: parametri in piu che si vuole passare alla API

        Keyword Args:
            best_effort (bool, optional): additional filter. Default to True

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
        response = self.execute('POST', path='/objects/bulk/create/groups', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, params=params, **kwargs)
        return response
