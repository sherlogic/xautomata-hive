from hive.api import ApiManager
from typing import Literal


class TsService(ApiManager):

    def ts_services(self, status: Literal['status', 'value'] = 'status', single_page: bool = False,
                    page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):
        """
        metodo che permette di recuperare la time serie di tutte le metriche. Si puo scegliere se ottenere le metriche di stato o di valore.

        Args:
            status (['status', 'value'], optional): discrimina tra le metriche di stato e di valore. Default to "status".
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
            uuid_service (str, optional): additional filter
            timestamp_start ($date-time, optional): additional filter
            timestamp_end ($date-time, optional): additional filter
            database_timestamp_start ($date-time, optional): additional filter
            database_timestamp_end ($date-time, optional): additional filter
            service_status (str, optional): additional filter (se metrica di stato),
            ranking (int, optional): additional filter (se metrica di stato),
            description (str, optional): additional filter string (se metrica di stato),
            unit (str, optional): additional filter (se metrica di valore)
            value (float, optional): additional filter (se metrica di valore)

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        if 'service_status' in list(params.keys()): params['status'] = params.pop('service_status')
        response = self.execute('GET', path='/ts_service_' + status + "/", single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response

    def ts_services_bulk(self, payload: list, ts_start: str, ts_end: str, status: Literal['status', 'value'] = 'status', single_page: bool = False,
                         page_size: int = 100, warm_start: bool = False, kwargs: dict = None, **params):
        """
        metodo che permette di recuperare la time serie di tutte le metriche. Si puo scegliere se ottenere le metriche di stato o di valore.

        Args:
            payload (list[str], optional): additional filter
            ts_start (str): start time range. MANDATORY.
            ts_end (str): end time range. MANDATORY.
            status (['status', 'value'], optional): discrimina tra le metriche di stato e di valore. Default to "status".
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        params = {'ts_start': ts_start, 'ts_end': ts_end, **params}
        response = self.execute('POST', path='/ts_service_' + status + "/bulk/read/", single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, params=params, **kwargs)
        return response

    def ts_services_bulk_create(self, payload: list, status: Literal['status', 'value'] = 'status', single_page: bool = False,
                                page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):
        """
        metodo che permette di recuperare la time serie di tutte le metriche. Si puo scegliere se ottenere le metriche di stato o di valore.

        Args:
            payload (list[str], optional): additional filter
            status (['status', 'value'], optional): discrimina tra le metriche di stato e di valore. Default to "status".
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Examples:
            uuids: [
                     {
                       "uuid_service": "string",
                       "timestamp": "2023-02-15T10:51:01.662Z",
                       "status": "grey",
                       "ranking": 0,
                       "description": "string",
                       "extended_attributes": [
                         "string"
                       ]
                     }
                   ]

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/ts_service_' + status + "/bulk/create/", single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, params=params, **kwargs)
        return response

    def ts_services_query(self, status: Literal['status', 'value'] = 'status', single_page: bool = False, page_size: int = 5000,
                          warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch all ts services.

        Args:
            status (['status', 'value'], optional): discrimina tra le metriche di stato e di valore. Default to "status".
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
            uuid_parent (str, optional): additional filter
            uuid_customer (str, optional): additional filter
            profile (str, optional): additional filter
            name (str, optional): additional filter
            description (str, optional): additional filter
            service_status (str, optional): additional filter
            timestamp_start (str, optional): additional filter
            timestamp_end (str, optional): additional filter

        Example:
            Per estrarre l'ultimo valore puo essere fatto con la seguente chimata pandas:
                last = pd_caster(spell.ts_services_query(profile=profile_m, statys = 'red', timestamp_start=ts_start.isoformat())).sort_values(by='timestamp', ascending=True).groupby('uuid_service').tail(1)
                in questo modo vengono ricavati i servizzi a partire da ts_start e viene restituito solo l'ultimo valore per servizio

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        if 'service_status' in list(params.keys()): params['status'] = params.pop('service_status')
        response = self.execute('GET', path='/ts_service_' + status + '/query/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response
