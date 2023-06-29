from hive.api import ApiManager
from hive.api import handling_single_page_methods


class Customers(ApiManager):

    def customers(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None,
                  **params):
        """
        Fetch all customers data.

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
            type (str, optional): additional filter
            code (str, optional): additional filter
            company_name (str, optional): additional filter
            address (str, optional): additional filter
            zip_code (str, optional): additional filter
            city (str, optional): additional filter
            country (str, optional): additional filter
            notes (str, optional): additional filter
            vat_id (str, optional): additional filter
            currency (str, optional): additional filter
            state_province (str, optional): additional filter
            status (str, optional): additional filter

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path='/customers/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def customers_groups(self, uuid: str, single_page: bool = False, page_size: int = 5000, warm_start: bool = False,
                         kwargs: dict = None, **params):
        """
        Fetch all groups related to a certain customer, referenced by its UUID

        Args:
            uuid (str): uuid del customer di cui si vuole sapere quali gruppi possiede
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters to the API

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            like (bool, optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True.
            sort_by (str, optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "".
            null_fileds (str, optional): Stringa separata da virgole di campi di cui si vuole rimuovere, o imporre, un valore nullo nel result set. Esempio "campo:nullable". Default to "".
            uuid_parent (str, optional): additional filter
            uuid_site (str, optional): additional filter
            uuid_virtual_domain (str, optional): additional filter
            type (str, optional): additional filter
            name (str, optional): additional filter
            description (str, optional): additional filter
            status (str, optional): additional filter

        Returns: List
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/customers/{uuid}/groups', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def customer_networks(self, uuid: str, warm_start: bool = False, kwargs: dict = None, **params):
        """
        metodo che restituisce tutte gli oggetti di uno specifico cliente che sono legati a una rete network, con il data_profile e gli extended_attributes di ogni oggetto e l'indirizzo della rete.
        Questa API non e' paginabile momentaneamente.

        Args:
            uuid (str): uuid del customer di cui si vuole sapere quali gruppi possiede
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
            uuid_object (str, optional): additional filter
            country (str, optional): additional filter
            city (str, optional): additional filter
            address (str, optional): additional filter
            zip_code (str, optional): additional filter
            status (str, optional): additional filter
            description (str, optional): additional filter

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/customers/networks/{uuid}', warm_start=warm_start, params=params,
                                **kwargs)
        return response

    def customers_post(self, kwargs: dict = None, **payload):
        """
        post selected customer.

        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Keyword Args:
            code (str): additional filter, required, required
            company_name (str): additional filter, required
            address (str): additional filter, required
            zip_code (str): additional filter, required
            city (str): additional filter, required
            country (str): additional filter, required
            status (str): additional filter, required
            notes (str, optional): additional filter
            vat_id (str, optional): additional filter
            currency (str, optional): additional filter
            state_province (str, optional): additional filter
            type (str, optional): additional filter

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/customers/', payload=payload, **kwargs)
        return response

    def customers_delete_bulk(self, payload: list, single_page: bool = False,
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
        response = self.execute('DELETE', path='/customers/bulk/delete/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, **kwargs)
        return response

    def customers_bulk(self, payload: list, single_page: bool = False,
                       page_size: int = 5000, warm_start: bool = False, kwargs: dict = None):
        """
        fetch customers bulk

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/customers/bulk/read/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, **kwargs)
        return response

    def customer(self, payload: str, warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch single customer.

        Args:
            payload (str): uuid della metrica da recuperare
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/customers/{payload}', warm_start=warm_start, params=params, **kwargs)
        return response

    def customers_put(self, uuid: str, kwargs: dict = None, **payload):
        """
        update selected customer.

        Args:
            uuid (str): uuid della metrica da modificare
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Keyword Args:
            name (str, optional): additional filter
            description (str, optional): additional filter
            feedback_for_operator (str, optional): additional filter
            profile (str, optional): additional filter
            status (str, optional): additional filter
            data_profile (list or dict, optional): data profile
            automata_domain (list or dict, optional): automata domain

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('PUT', path=f'/customers/{uuid}', payload=payload, **kwargs)
        return response

    def customers_delete(self, uuid: str, kwargs: dict = None):

        """
        delete single customer.

        Args:
            uuid (str): uuid della metrica da eliminare
            kwargs (dict, optional): additional parameters for execute. Default to None..

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/customers/{uuid}', **kwargs)
        return response
