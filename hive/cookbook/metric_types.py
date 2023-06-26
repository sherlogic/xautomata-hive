from hive.api import ApiManager
from hive.api import handling_single_page_methods


class MetricTypes(ApiManager):

    def metric_types(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None,
                **params):
        """
        metodo che restituisce tutti i metric_types

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
            uuid_object (str, optional): additional filter
            name (str, optional): additional filter
            description (str, optional): additional filter
            feedback_for_operator (str, optional): additional filter
            profile (str, optional): additional filter
            status (str, optional): additional filter

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/metric_types/', single_page=single_page, page_size=page_size, params=params,
                                warm_start=warm_start, **kwargs)
        return response
    def metric_types_post(self, kwargs: dict = None, **payload):
        """
        post selected metric_types.

        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API


        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/metric_types/', payload=payload, **kwargs)
        return response


    def metric_type(self, uuid: str, warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch single metric_type.

        Args:
            uuid (str, required): uuid del metric_type da recuperare
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/metric_types/{uuid}', warm_start=warm_start, params=params, **kwargs)
        return response

    def metrics_type_delete(self, uuid: str, kwargs: dict = None):
        """
<<<<<<< HEAD
        delete single metric type.

        Args:
            uuid(str): uuid della metric type da eliminare
            kwargs (dict): additional parameters for execute. Default to None.
=======
        delete single object.

        Args:
            uuid(str, required): id del object da eliminare
            kwargs (dict, optional): additional parameters for execute. Default to None.
>>>>>>> 5470321ff30def63dcbc59dd78ae4dfd2f293a95
        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/metric_types/{uuid}', **kwargs)
        return response

    
    def metrics_types_post(self, kwargs: dict = None, **payload):
        """
        post selected metrics.

        Args:
<<<<<<< HEAD
            uuid metric (str, required): string <uuid4> (Uuid Object)
=======
            uuid object (str, required): string <uuid4> (Uuid Object)
>>>>>>> 5470321ff30def63dcbc59dd78ae4dfd2f293a95
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API
            status(str, required): string (Status) <= 1 characters
        Keyword Args:
            name (str, required): string (Name) <= 255 characters
            profile(str, required): string (Profile) <= 64 characters
            description(str, optional): additional filter    <= 255 characters
            feedback_for_operator(str, optional): additional filter  <= 255 characters
            data_profile(str, optional): additional filter
            automata_domain(str, optional): additional filter
            profile(str, required): 
        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/metric_types/', payload=payload, **kwargs)
        return response
    
    
    def metric_type_metrics(self, uuid:str ,single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None,
                **params):
        """
        metodo che restituisce le metrics del metric type inserito

        Args:
            uuid (str, required): uuid della metric_type da cercare
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
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False
            not_in (bool,optional): additional filter
            
        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/metric_types/{uuid}/metrics', single_page=single_page, page_size=page_size, params=params,
                                warm_start=warm_start, **kwargs)
        return response
    
    def metric_type_downtime(self, uuid: str, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):
        """ get the downtimes linked with a metric type.

        Args:
<<<<<<< HEAD
            uuid (str, required): uuid del metric type 
=======
            uuid (str, required): uuid del metric da cercare
>>>>>>> 5470321ff30def63dcbc59dd78ae4dfd2f293a95
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
        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/metric_types/{uuid}/downtimes', single_page=single_page, page_size=page_size, params=params,
                                warm_start=warm_start, **kwargs)
        return response
    def metric_types_downtimes_post(self, uuid: str, uuid_downtime: str, kwargs: dict = None):

        """

        create link between selected metrics_type and selected downtime.

        Args:

            uuid (str): uuid della metrics

            uuid_downtime (str): uuid del downtime

            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list

        """

        if kwargs is None: kwargs = dict()

        response = self.execute('POST', path=f'/metrics_types/{uuid}/downtimes/{uuid_downtime}', **kwargs)
        return response


    def metrics_type_downtimes_delete(self, uuid: str, uuid_downtime: str, kwargs: dict = None):
        """
        delete selected dispatcher and selected metric_type service.
        Args:
            uuid (str): uuid della metrics
            uuid_downtime (str): uuid del downtime
            kwargs (dict, optional): additional parameters for execute. Default to None.
        
        Returns: list
        
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/metric_types/{uuid}/downtimes/{uuid_downtime}', payload=payload, **kwargs)
        return response



    def metric_type_put(self, uuid: str, kwargs: dict = None, **payload):
        """
        update selected metric_type.

        Args:
            uuid (str): uuid della metric_type da modificare
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Keyword Args:
            uuid_object (str, optional): additional filter
            name (str, optional): additional filter
            description (str, optional): additional filter
            feedback_for_operator (dict, optional): additional filter
            profile (str, optional): additional filter
            data_profile (dict, optional): additional filter
            automata_domain (list or dict, optional): automata domain
            status (str, optional): additional filter

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('PUT', path=f'/metric_types/{uuid}', payload=payload, **kwargs)
        return response

    def metric_type_dispatchers(self, uuid: str, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):
        """ metodo che restituisce i dispatchers di una metric type
        Args:
            uuid (str, required): uuid della dispatcher da cercare
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
<<<<<<< HEAD
        
=======
>>>>>>> 5470321ff30def63dcbc59dd78ae4dfd2f293a95
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path=f'/metric_types/{uuid}/dispatchers', single_page=single_page, page_size=page_size, params=params,warm_start=warm_start, **kwargs)
        return response
   
   
    def metrics_type_dispatchers_delete(self, uuid: str, uuid_dispatcher: str, kwargs: dict = None):
        """
        delete selected dispatcher from the selected metric_type service.
        Args:
            uuid (str, required): uuid della metrics_type
            uuid_service (str, required): uuid del service
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API
        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/metric_types/{uuid}/dispatchers/{uuid_dispatcher}',**kwargs)
        return response
   
   
    def metrics_type_dispatchers_post(self, uuid: str, uuid_dispatcher: str, kwargs: dict = None):
        """
        create link between selected dispatcher and selected metric_type service.
        Args:
            uuid (str): uuid della metrics
            uuid_dispatcher (str): uuid della dispatcher
            kwargs (dict, optional): additional parameters for execute. Default to None.
    
        Returns: list
        
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/metric_types/{uuid}/dispatchers/{uuid_dispatcher}', **kwargs)
        return response
   
   
    def metric_type_delete(self, uuid: str, kwargs: dict = None):
        """

        create link between selected dispatcher and selected metric_type.

        Args:

            uuid (str): uuid della metrics

            uuid_service (str): uuid del service

            kwargs (dict, optional): additional parameters for execute. Default to None.

            **payload: additional parameters for the API

        Returns: list

        """

        if kwargs is None: kwargs = dict()

        response = self.execute('POST', path=f'/metric_types/{uuid}/dispatchers/{uuid_dispatcher}', payload=payload, **kwargs)

        return response
   
    def metric_types_delete_bulk(self, metric_types: list, single_page: bool = False,
                                 page_size: int = 5000, warm_start: bool = False, kwargs: dict = None):
        """
        elimina le metriche in bulk

        Args:
            metric_types (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path='/metric_types/bulk/delete/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=metric_types, **kwargs)
        return response

    def metric_types_read_bulk(self, metric_types: list, single_page: bool = False,
                               page_size: int = 5000, warm_start: bool = False, kwargs: dict = None):
        """
        fetch le metriche in bulk

        Args:
            metric_types (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/metric_types/bulk/read/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=metric_types, **kwargs)
        return response

 

    def metrics_type_downtimes_delete(self, uuid: str, uuid_downtime: str, kwargs: dict = None, **payload):

        """

        delete selected dispatcher linked with the metric_type.

        Args:

            uuid (str, required): uuid della metric_type

            uuid_dispatcher (str, required): uuid del downtime
            kwargs (dict, optional): additional parameters for execute. Default to None.

            **payload: additional parameters for the API

        Returns: list

        """

        if kwargs is None: kwargs = dict()

        response = self.execute('DELETE', path=f'/metric_types/{uuid}/downtimes/{uuid_downtime}', payload=payload, **kwargs)

        return response
    
    def metric_type_dispatchers_delete(self, uuid: str, uuid_dispatcher: str, kwargs: dict = None, **payload):

        """

        delete selected dispatcher linked with the metric  type.

        Args:

            uuid (str, required): uuid della metric type

            uuid_dispatcher (str, required): uuid del dispatcher

            kwargs (dict, optional): additional parameters for execute. Default to None.

            **payload: additional parameters for the API

        Returns: list

        """

        if kwargs is None: kwargs = dict()

        response = self.execute('DELETE', path=f'/metric_types/{uuid}/dispatchers/{uuid_dispatcher}', payload=payload, **kwargs)

        return response