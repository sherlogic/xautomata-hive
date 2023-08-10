from hive.api import ApiManager, handling_single_page_methods


class Login(ApiManager):
    """Class that handles all the XAutomata login APIs"""

    def login_access_token_create(self, params: dict = False,
        kwargs: dict = None, **payload) -> list:
        """Login Access Token Oauth2
        Args:
            params (dict, optional): additional parameters for the API.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            value_refresh_token (None optional): additional filter - parameter
            refresh (string optional): additional filter - parameter
            grant_type (string optional): additional filter - payload
            username (string required): additional filter - payload
            password (string required): additional filter - payload
            scope (string optional): additional filter - payload
            client_id (string optional): additional filter - payload
            client_secret (string optional): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/login/access-token', params
            =params, payload=payload, **kwargs)
        return response

    def login_refresh_create(self, kwargs: dict = None, **params) -> list:
        """Refresh Token
        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            refresh (string optional): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/login/refresh', params=
            params, **kwargs)
        return response

    def login_refresh_invalidate_create(self, kwargs: dict = None, **params
        ) -> list:
        """Invalidate Token
        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            refresh (string optional): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/login/refresh/invalidate',
            params=params, **kwargs)
        return response

    def login_refresh_invalidate_user_create(self, kwargs: dict = None, **
        params) -> list:
        """Invalidate User Tokens
        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            username (string required): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=
            f'/login/refresh/invalidate_user', params=params, **kwargs)
        return response

    def login_refresh_invalidate_tokens_create(self, kwargs: dict = None
        ) -> list:
        """Invalidate User Tokens
        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=
            f'/login/refresh/invalidate_tokens', **kwargs)
        return response

    def login_current_user(self, warm_start: bool = False, kwargs: dict = None
        ) -> list:
        """Get Current User
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/login/current_user',
            warm_start=warm_start, **kwargs)
        return response

    def login_current_user_put(self, kwargs: dict = None, **payload) -> list:
        """Update User
        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            phone (string optional): additional filter - payload
            password (string optional): additional filter - payload
            email (string optional): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('PUT', path=f'/login/current_user', payload
            =payload, **kwargs)
        return response

    def login_current_user_image(self, warm_start: bool = False,
        kwargs: dict = None) -> list:
        """Get Image
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/login/current_user/image',
            warm_start=warm_start, **kwargs)
        return response

    def login_current_user_image_put(self, kwargs: dict = None, **payload
        ) -> list:
        """Update Image
        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            image (string required): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('PUT', path=f'/login/current_user/image',
            payload=payload, **kwargs)
        return response
