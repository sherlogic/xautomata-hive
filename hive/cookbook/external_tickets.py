from hive.api import ApiManager
from hive.api import handling_single_page_methods
from typing import Literal


class ExternalTickets(ApiManager):

    def external_tickets(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False,
                         kwargs: dict = None, **params):
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path='/external_tickets/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def external_tickets_post(self, kwargs: dict = None, **payload):
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/external_tickets/', payload=payload, **kwargs)
        return response

    def external_tickets_update(self, uuid: str, kwargs: dict = None, **payload):
        if kwargs is None: kwargs = dict()
        response = self.execute('PUT', path=f'/external_tickets/{uuid}', payload=payload, **kwargs)
        return response

    def external_tickets_bulk(self, payload: list, single_page: bool = False, page_size: int = 5000, warm_start: bool = False,
                              kwargs: dict = None):
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/external_tickets/bulk/read/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, **kwargs)
        return response

    def external_tickets_create_bulk(self, payload: list, single_page: bool = False, page_size: int = 5000, kwargs: dict = None):
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/external_tickets/bulk/create/', single_page=single_page, page_size=page_size,
                                payload=payload, **kwargs)
        return response

    def external_tickets_by_date(self, uuid: str, warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch tickets by data for a customer.

        Args:
            uuid (str): uuid client
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            date_start (date): data di partenza. MANDATORY.
            date_end (date): data di fine MANDATORY.

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/external_tickets/ticket_by_date/{uuid}', warm_start=warm_start, params=params, **kwargs)
        return response

    def external_tickets_by_sla(self, uuid:str, ticket_type: Literal['resolution', 'taking_charge'],
                                                    warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch tickets by sla for a customer.

        Args:
            uuid (str): uuid customer
            ticket_type (Literal['resolution', 'taking_charge']): tipo di ticket.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            date_start (date): data di partenza. MANDATORY.
            date_end (date): data di fine MANDATORY.

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/external_tickets/ticket_by_sla/{ticket_type}/{uuid}', warm_start=warm_start, params=params, **kwargs)
        return response

    def external_tickets_by_params(self, uuid: str, ticket_type: Literal['type', 'mode', 'severity', 'responsibility', 'organization'],
                                                    warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch tickets by params for a privat selection of customers.

        Args:
            uuid (str): uuid customer.
            ticket_type (Literal['type', 'mode', 'severity', 'responsibility', 'organization']): tipo di ticket.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            date_start (date): data di partenza. MANDATORY.
            date_end (date): data di fine MANDATORY.

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/external_tickets/ticket_by_params/{ticket_type}/{uuid}', warm_start=warm_start, params=params, **kwargs)
        return response

    def external_tickets_by_date_customers_filtering(self, warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch tickets by data for a privat selection of customers.

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            date_start (date): data di partenza. MANDATORY.
            date_end (date): data di fine MANDATORY.

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path='/external_tickets/ticket_by_date/customers_filtering/', warm_start=warm_start, params=params, **kwargs)
        return response

    def external_tickets_by_sla_customers_filtering(self, ticket_type: Literal['resolution', 'taking_charge'],
                                                    warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch tickets by sla for a privat selection of customers.

        Args:
            ticket_type (Literal['resolution', 'taking_charge']): tipo di ticket.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            date_start (date): data di partenza. MANDATORY.
            date_end (date): data di fine MANDATORY.

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/external_tickets/ticket_by_sla/customers_filtering/{ticket_type}/', warm_start=warm_start, params=params, **kwargs)
        return response

    def external_tickets_by_params_customers_filtering(self, ticket_type: Literal['type', 'mode', 'severity', 'responsibility', 'organization'],
                                                    warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch tickets by params for a privat selection of customers.

        Args:
            ticket_type (Literal['type', 'mode', 'severity', 'responsibility', 'organization']): tipo di ticket.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Keyword Args:
            date_start (date): data di partenza. MANDATORY.
            date_end (date): data di fine MANDATORY.

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/external_tickets/ticket_by_params/customers_filtering/{ticket_type}/', warm_start=warm_start, params=params, **kwargs)
        return response
