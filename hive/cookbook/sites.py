from hive.api import ApiManager
from hive.api import handling_single_page_methods


class Sites(ApiManager):

    def sites(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None,
              **params):
        """
        Fetch all metrics.

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
            extract_severity (bool, optional): Se True nella risposta e' anche presente la severita, Default to False.
            uuid_customer (str, optional): additional filter
            type (str, optional): additional filter
            code (str, optional): additional filter
            description (str, optional): additional filter
            address (str, optional): additional filter
            zip_code (str, optional): additional filter
            city (str, optional): additional filter
            country (str, optional): additional filter
            notes (str, optional): additional filter
            state_province (str, optional): additional filter
            status (str, optional): additional filter
            filter_group_types (str, optional): additional filter

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path='/sites/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def site(self, uuid: str, warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch single metric.

        Args:
            uuid (str): uuid della metrica da recuperare
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Keyword Args:
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/sites/{uuid}', warm_start=warm_start, params=params, **kwargs)
        return response

    def sites_groups(self, uuid: str, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None,
                     **params):
        """
        Fetch all groups linked with site.

        Args:
            uuid (str, required): uuid del sito
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
        response = self.execute('GET', path=f'/sites/{uuid}/groups', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def site_put(self, uuid: str, geocode: bool = False, kwargs: dict = None, **payload):
        """
        update selected metric.

        Args:
            uuid (str): uuid della metrica da modificare
            geocode (bool, optional): additional filter
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Keyword Args:
            uuid_customer (str, optional): additional filter
            type (str, optional): additional filter
            code (str, optional): additional filter
            description (str, optional): additional filter
            address (str, optional): additional filter
            zip_code (str, optional): additional filter
            city (list or dict, optional): data profile
            country (list or dict, optional): data profile
            notes (list or dict, optional): data profile
            state_province (list or dict, optional): data profile
            status (list or dict, optional): data profile

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('PUT', path=f'/sites/{uuid}', payload=payload, params={'geocode': geocode}, **kwargs)  # todo da verificare se funziona
        return response

    def site_delete(self, uuid: str, kwargs: dict = None):
        """

        delete single metric.

        Args:
            uuid: id del metric da eliminare
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/sites/{uuid}', **kwargs)
        return response
    def sites_contacts(self, uuid: str, single_page: bool = False, page_size: int = 5000, warm_start: bool = False,

                         kwargs: dict = None, **params):

        """

        Get the services linked with the sites_contacts.




        Args:

            uuid (str, required): uuid contacts

            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.

            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.

            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.

            kwargs (dict, optional): additional parameters for execute. Default to None.

            **params: additional parameters for the API

            type (str, required): Body

        Keyword Args:

            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            like (bool, optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True.
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False
            not_in (bool, optional): additional filter

        Returns: list
        """

        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/sites/{uuid}/contacts', single_page=single_page, page_size=page_size, warm_start=warm_start, params=params, **kwargs)
        return response

    def sites_contacts_post(self, uuid: str, uuid_contact: str, kwargs: dict = None, **payload):

        """
        create link between selected site and selected contact.

        Args:
            uuid (str, required): uuid
            uuid_contact (str, required): uuid del contact
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API
        Keywords Args: 
            type (str, required): additional filter
        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/sites/{uuid}/contacts/{uuid_contact}', payload=payload, **kwargs)
        return response

    def sites_contacts_delete(self, kwargs: dict = None, uuid=str, uuid_contact=str):

        """
        delete selected sites_contact.

        Args:
            uuid (str, required): uuid
            uuid_contact (str, required): uuid del contact
            kwargs (dict, optional): additional parameters for execute. Default to None.
           
        Returns: list

        """

        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'//sites/{uuid}/contacts/{uuid_contact}', **kwargs)
        return response
    
    def sites_coordinates(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None,
               **params):
        """
        metodo che restituisce le coordinate

        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: parametri in piu che si vuole passare alla API

        Keyword Args:
            uuid_site (str, optional): additional filter
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            sort_by (str, optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "".
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False
           
        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/sites/coordinates/', single_page=single_page, page_size=page_size, params=params,
                                warm_start=warm_start, **kwargs)
        return response

    def sites_coordinates_delete(self, uuid: str, kwargs: dict = None):
        """

        delete coordinate.

        Args:
            uuid: id del object da eliminare
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/objects/{uuid}', **kwargs)
        return response

    def sites_delete_bulk(self, sites: list, single_page: bool = False,
                          page_size: int = 5000, warm_start: bool = False, kwargs: dict = None):
        """
        elimina le metriche in bulk

        Args:
            sites (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/sites/bulk/delete/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=sites, **kwargs)
        return response

    def sites_read_bulk(self, sites: list, single_page: bool = False,
                        page_size: int = 5000, warm_start: bool = False, kwargs: dict = None):
        """
        elimina le metriche in bulk

        Args:
            sites (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/sites/bulk/read/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=sites, **kwargs)
        return response
    
    def sites_contacts(self, uuid: str, single_page: bool = False, page_size: int = 5000, warm_start: bool = False,
                         kwargs: dict = None, **params):
        """
        Get the services linked with the sites_contacts.

        Args:
            uuid (str, required): uuid contacts
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API
            type (str, required): Body
        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            like (bool, optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True.
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False
            not_in (bool, optional): additional filter

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/sites/{uuid}/contacts', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response
    
    def sites_contacts_post(self, uuid: str, uuid_contact: str, kwargs: dict = None, **payload):

        """
        create link between selected group and selected object.
        Args:
            uuid (str, required): uuid 
            uuid_contact (str, required): uuid del contact
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API
        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/sites/{uuid}/contacts/{uuid_contact}', payload=payload, **kwargs)
        return response 
     
    def sites_contacts_delete(self, kwargs: dict = None, uuid=str, uuid_contact=str, **payload):
        """
        delete selected groups_users.
        Args:
            uuid (str, required): uuid
            uuid_contact (str, required): uuid del contact
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API 
        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'//sites/{uuid}/contacts/{uuid_contact}', payload=payload, **kwargs)
        return response 

    def sites_coordinates_post(self, kwargs: dict = None, **payload):
        """
        metodo che restituisce le coordinate di un sito
        Args:
        longitude(str, required)
        latitude(str, required)
        uuid_site(str, required)
        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/sites/coordinates/',payload=payload, **kwargs)
        return response
    