from hive.api import ApiManager


class Users(ApiManager):

    def users(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None,
              **params):
        """
        Fetch all Users data.

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
            join (bool, optional): Se True restituisce i legami con l'albero.
            like (bool, optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True.
            sort_by (str, optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "".
            null_fileds (str, optional): Stringa separata da virgole di campi di cui si vuole rimuovere, o imporre, un valore nullo nel result set. Esempio "campo:nullable". Default to "".
            name (str, optional): additional filter
            active (str, optional): additional filter
            email (str, optional): additional filter
            phone (str, optional): additional filter
            uuid_acl_override (str, optional): additional filter

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path='/users/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def users_customers(self, name: str, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None,
                        **params):
        """
        Fetch all Users data.

        Args:
            name (str): customer name.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            not_in (bool, optional): additional parameters.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/users/{name}/customers', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def users_create(self, kwargs: dict = None, **payload):
        """
        Register new user

        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Keyword Args:
            name (str, mandatory): additional filter
            active (bool, mandatory): additional filter
            email (str, mandatory): additional filter
            phone (str, mandatory): additional filter
            acl (dict, mandatory): additional filter
            uuid_acl_override (str, optional): additional filter

        Returns: list
        """

        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/users/', payload=payload, **kwargs)
        return response

    def users_customers_create(self, user_name: str, uuid_customer: str, kwargs: dict = None):
        """
        creare i link user customer

        Args:
            user_name
            uuid_customer
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/users/{user_name}/customers/{uuid_customer}', **kwargs)
        return response

    def users_customers_delete(self, user_name: str, uuid_customer: str, kwargs: dict = None):
        """
        creare i link user customer

        Args:
            user_name
            uuid_customer
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/users/{user_name}/customers/{uuid_customer}', **kwargs)
        return response

    def users_widgetgroups_create(self, user_name: str, uuid_widget_groups: str, kwargs: dict = None):
        """
        creare i link user uuid_widget_groups

        Args:
            user_name
            uuid_widget_groups
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/users/{user_name}/widget_groups/{uuid_widget_groups}', **kwargs)
        return response

    def users_customers_create_bulk(self, payload: list,  best_effort: bool = True, single_page: bool = False,
                                    page_size: int = 5000, kwargs: dict = None):
        """
        creare i link user customer in bulk

        Args:
            payload (list[dict], optional): List dict to create.
            best_effort (bool, optional): se a True forza a proseguire anche se un elemento genera un errore
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Example:
            payload = [
                              {
                                "username": "string",
                                "uuid_customer": "string"
                              }
                            ]

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/users/bulk/create/customers', single_page=single_page, page_size=page_size,
                                payload=payload, params={'best_effort': best_effort}, **kwargs)
        return response

    def users_customers_delete_bulk(self, payload: list, single_page: bool = False,
                                    page_size: int = 5000, kwargs: dict = None):
        """
        creare i link user customer in bulk

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Example:
            payload = [
                              {
                                "username": "string",
                                "uuid_customer": "string"
                              }
                            ]

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/users/bulk/delete/customers', single_page=single_page, page_size=page_size,
                                payload=payload, **kwargs)
        return response