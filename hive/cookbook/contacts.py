from hive.api import ApiManager, handling_single_page_methods


class Contacts(ApiManager):
    """Class that handles all the XAutomata contacts APIs"""

    def contacts(self, warm_start: bool = False, single_page: bool = False,
        page_size: int = 5000, kwargs: dict = None, **params) -> list:
        """Read Contacts
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            null_fields (string optional): additional filter - parameter
            type (string optional): additional filter - parameter
            name (string optional): additional filter - parameter
            surname (string optional): additional filter - parameter
            qualification (string optional): additional filter - parameter
            company (string optional): additional filter - parameter
            department (string optional): additional filter - parameter
            principal_email (string optional): additional filter - parameter
            secondary_email (string optional): additional filter - parameter
            principal_mobile_number (string optional): additional filter - parameter
            secondary_mobile_number (string optional): additional filter - parameter
            phone_number (string optional): additional filter - parameter
            birthday (string optional): additional filter - parameter
            notes (string optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/contacts/', single_page=
            single_page, page_size=page_size, warm_start=warm_start, params
            =params, **kwargs)
        return response

    def contacts_create(self, kwargs: dict = None, **payload) -> list:
        """Create Contact
        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            type (string optional): additional filter - payload
            name (string required): additional filter - payload
            surname (string required): additional filter - payload
            qualification (string optional): additional filter - payload
            company (string optional): additional filter - payload
            department (string optional): additional filter - payload
            principal_email (string optional): additional filter - payload
            secondary_email (string optional): additional filter - payload
            principal_mobile_number (string optional): additional filter - payload
            secondary_mobile_number (string optional): additional filter - payload
            phone_number (string optional): additional filter - payload
            birthday (string optional): additional filter - payload
            notes (string optional): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/contacts/', payload=payload,
            **kwargs)
        return response

    def contact(self, uuid: str, warm_start: bool = False, kwargs: dict = None
        ) -> list:
        """Read Contact
        Args:
            uuid (str, required): uuid
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/contacts/{uuid}', warm_start
            =warm_start, **kwargs)
        return response

    def contacts_put(self, uuid: str, kwargs: dict = None, **payload) -> list:
        """Update Contact
        Args:
            uuid (str, required): uuid
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            type (string optional): additional filter - payload
            name (string optional): additional filter - payload
            surname (string optional): additional filter - payload
            qualification (string optional): additional filter - payload
            company (string optional): additional filter - payload
            department (string optional): additional filter - payload
            principal_email (string optional): additional filter - payload
            secondary_email (string optional): additional filter - payload
            principal_mobile_number (string optional): additional filter - payload
            secondary_mobile_number (string optional): additional filter - payload
            phone_number (string optional): additional filter - payload
            birthday (string optional): additional filter - payload
            notes (string optional): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('PUT', path=f'/contacts/{uuid}', payload=
            payload, **kwargs)
        return response

    def contacts_delete(self, uuid: str, kwargs: dict = None) -> list:
        """Delete Contact
        Args:
            uuid (str, required): uuid
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('DELETE', path=f'/contacts/{uuid}', **kwargs)
        return response

    def contacts_sites(self, uuid: str, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """List Sites
        Args:
            uuid (str, required): uuid
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            not_in (boolean optional): additional filter - parameter
            type (string optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/contacts/{uuid}/sites',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, **kwargs)
        return response

    def contacts_sites_put(self, uuid: str, uuid_site: str,
        kwargs: dict = None, **payload) -> list:
        """Update Site
        Args:
            uuid (str, required): uuid
            uuid_site (str, required): uuid_site
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            type (string required): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('PUT', path=
            f'/contacts/{uuid}/sites/{uuid_site}', payload=payload, **kwargs)
        return response

    def contacts_sites_create(self, uuid: str, uuid_site: str,
        kwargs: dict = None, **payload) -> list:
        """Add Site
        Args:
            uuid (str, required): uuid
            uuid_site (str, required): uuid_site
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            type (string required): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=
            f'/contacts/{uuid}/sites/{uuid_site}', payload=payload, **kwargs)
        return response

    def contacts_sites_delete(self, uuid: str, uuid_site: str,
        kwargs: dict = None) -> list:
        """Remove Site
        Args:
            uuid (str, required): uuid
            uuid_site (str, required): uuid_site
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('DELETE', path=
            f'/contacts/{uuid}/sites/{uuid_site}', **kwargs)
        return response

    def contacts_customers(self, uuid: str, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """List Customers
        Args:
            uuid (str, required): uuid
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            not_in (boolean optional): additional filter - parameter
            type (string optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/contacts/{uuid}/customers',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, **kwargs)
        return response

    def contacts_customers_put(self, uuid: str, uuid_customer: str,
        kwargs: dict = None, **payload) -> list:
        """Update Customer
        Args:
            uuid (str, required): uuid
            uuid_customer (str, required): uuid_customer
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            type (string required): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('PUT', path=
            f'/contacts/{uuid}/customers/{uuid_customer}', payload=payload,
            **kwargs)
        return response

    def contacts_customers_create(self, uuid: str, uuid_customer: str,
        kwargs: dict = None, **payload) -> list:
        """Add Customer
        Args:
            uuid (str, required): uuid
            uuid_customer (str, required): uuid_customer
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            type (string required): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=
            f'/contacts/{uuid}/customers/{uuid_customer}', payload=payload,
            **kwargs)
        return response

    def contacts_customers_delete(self, uuid: str, uuid_customer: str,
        kwargs: dict = None) -> list:
        """Remove Customer
        Args:
            uuid (str, required): uuid
            uuid_customer (str, required): uuid_customer
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('DELETE', path=
            f'/contacts/{uuid}/customers/{uuid_customer}', **kwargs)
        return response

    def contacts_dispatchers(self, uuid: str, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """List Dispatchers
        Args:
            uuid (str, required): uuid
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            not_in (boolean optional): additional filter - parameter
            send_email (boolean optional): additional filter - parameter
            role_email (string optional): additional filter - parameter
            send_sms (boolean optional): additional filter - parameter
            active_at_timestamp (string optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/contacts/{uuid}/dispatchers',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, **kwargs)
        return response

    def contacts_dispatchers_put(self, uuid: str, uuid_dispatcher: str,
        kwargs: dict = None, **payload) -> list:
        """Update Dispatcher
        Args:
            uuid (str, required): uuid
            uuid_dispatcher (str, required): uuid_dispatcher
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            send_email (boolean optional): additional filter - payload
            role_email (None optional): additional filter - payload
            send_sms (boolean optional): additional filter - payload
            endpoint (array object optional): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('PUT', path=
            f'/contacts/{uuid}/dispatchers/{uuid_dispatcher}', payload=
            payload, **kwargs)
        return response

    def contacts_dispatchers_create(self, uuid: str, uuid_dispatcher: str,
        kwargs: dict = None, **payload) -> list:
        """Add Dispatcher
        Args:
            uuid (str, required): uuid
            uuid_dispatcher (str, required): uuid_dispatcher
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            send_email (boolean required): additional filter - payload
            role_email (None optional): additional filter - payload
            send_sms (boolean required): additional filter - payload
            endpoint (array object optional): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=
            f'/contacts/{uuid}/dispatchers/{uuid_dispatcher}', payload=
            payload, **kwargs)
        return response

    def contacts_dispatchers_delete(self, uuid: str, uuid_dispatcher: str,
        kwargs: dict = None) -> list:
        """Delete Dispatcher
        Args:
            uuid (str, required): uuid
            uuid_dispatcher (str, required): uuid_dispatcher
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('DELETE', path=
            f'/contacts/{uuid}/dispatchers/{uuid_dispatcher}', **kwargs)
        return response

    def contacts_bulk(self, payload: list, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Bulk Read 
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
        Examples:
            payload = 
          [
            "uuid": "str", required
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/contacts/bulk/read/',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, payload=payload, **kwargs)
        return response

    def contacts_create_bulk(self, payload: list, single_page: bool = False,
        page_size: int = 5000, kwargs: dict = None, **params) -> list:
        """Bulk Create Contacts
        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            best_effort (boolean optional): additional filter - parameter
        Examples:
            payload = 
          [
           {
            "type": "string", optional
            "name": "string", required
            "surname": "string", required
            "qualification": "string", optional
            "company": "string", optional
            "department": "string", optional
            "principal_email": "string", optional
            "secondary_email": "string", optional
            "principal_mobile_number": "string", optional
            "secondary_mobile_number": "string", optional
            "phone_number": "string", optional
            "birthday": "string", optional
            "notes": "string", optional
           }
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/contacts/bulk/create/',
            single_page=single_page, page_size=page_size, params=params,
            payload=payload, **kwargs)
        return response

    def contacts_delete_bulk(self, payload: list, single_page: bool = False,
        page_size: int = 5000, kwargs: dict = None) -> list:
        """Bulk Delete Contacts
        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Examples:
            payload = 
          [
            "uuid": "str", required
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/contacts/bulk/delete/',
            single_page=single_page, page_size=page_size, payload=payload,
            **kwargs)
        return response

    def contacts_customers_create_bulk(self, payload: list,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Bulk Link Customers
        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            best_effort (boolean optional): additional filter - parameter
        Examples:
            payload = 
          [
           {
            "uuid_contact": "string", required
            "uuid_customer": "string", required
            "type": "string", optional
           }
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=
            f'/contacts/bulk/create/customers', single_page=single_page,
            page_size=page_size, params=params, payload=payload, **kwargs)
        return response

    def contacts_customers_delete_bulk(self, payload: list,
        single_page: bool = False, page_size: int = 5000, kwargs: dict = None
        ) -> list:
        """Bulk Unlink Customers
        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Examples:
            payload = 
          [
           {
            "uuid_contact": "string", required
            "uuid_customer": "string", required
           }
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=
            f'/contacts/bulk/delete/customers', single_page=single_page,
            page_size=page_size, payload=payload, **kwargs)
        return response

    def contacts_dispatchers_create_bulk(self, payload: list,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Bulk Link Dispatchers
        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            best_effort (boolean optional): additional filter - parameter
        Examples:
            payload = 
          [
           {
            "uuid_contact": "string", required
            "uuid_dispatcher": "string", required
            "send_email": "boolean", optional
            "role_email": "None", optional
            "send_sms": "boolean", optional
            "endpoint": "array object", optional
           }
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=
            f'/contacts/bulk/create/dispatchers', single_page=single_page,
            page_size=page_size, params=params, payload=payload, **kwargs)
        return response

    def contacts_dispatchers_delete_bulk(self, payload: list,
        single_page: bool = False, page_size: int = 5000, kwargs: dict = None
        ) -> list:
        """Bulk Unlink Dispatchers
        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Examples:
            payload = 
          [
           {
            "uuid_contact": "string", required
            "uuid_dispatcher": "string", required
           }
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=
            f'/contacts/bulk/delete/dispatchers', single_page=single_page,
            page_size=page_size, payload=payload, **kwargs)
        return response

    def contacts_sites_create_bulk(self, payload: list,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Bulk Link Sites
        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            best_effort (boolean optional): additional filter - parameter
        Examples:
            payload = 
          [
           {
            "uuid_contact": "string", required
            "uuid_site": "string", required
            "type": "string", optional
           }
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/contacts/bulk/create/sites',
            single_page=single_page, page_size=page_size, params=params,
            payload=payload, **kwargs)
        return response

    def contacts_sites_delete_bulk(self, payload: list,
        single_page: bool = False, page_size: int = 5000, kwargs: dict = None
        ) -> list:
        """Bulk Unlink Sites
        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Examples:
            payload = 
          [
           {
            "uuid_contact": "string", required
            "uuid_site": "string", required
           }
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/contacts/bulk/delete/sites',
            single_page=single_page, page_size=page_size, payload=payload,
            **kwargs)
        return response
