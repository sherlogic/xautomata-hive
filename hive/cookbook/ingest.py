from hive.api import ApiManager


class Ingest(ApiManager):

    def metric_ingest(self, payload: list, single_page: bool = False, page_size: int = 5000,
                      warm_start: bool = False, kwargs: dict = None):
        """
        metodo che permette di inviare in blocco una serie di metriche. Si puo scegliere se inviare metriche di stato o di valore.

        Args:
            payload (list[dict], optional): List dict to send.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Examples:
            metrics: [
                      {
                        "uuid_metric": "string",
                        "uuid_probe": "string",
                        "timestamp": 0,
                        "object_type": "metric",
                        "extended_attributes": "{}",
                        "value": "string",
                        "unit": "string",
                        "description": "string",
                        "status": "string",
                        "ranking": 0
                      },
                      {
                        "uuid_metric": "string",
                        "uuid_probe": "string",
                        "timestamp": 0,
                        "object_type": "metric",
                        "extended_attributes": "{}",
                        "status": "grey",
                        "ranking": 0,
                        "description": "string"
                      },
                      {
                        "uuid_metric": "string",
                        "uuid_probe": "string",
                        "timestamp": 0,
                        "object_type": "metric",
                        "extended_attributes": "string",
                        "description": ""
                      },
                      {
                        "uuid_metric": "string",
                        "uuid_probe": "string",
                        "timestamp": 0,
                        "object_type": "metric",
                        "unit": "string",
                        "value": 0
                      }
                    ]

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/metric_ingest/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, **kwargs)
        return response

    def probes_log_ingest(self, uuid_probe: str, payload: list, single_page: bool = False, page_size: int = 5000,
                          warm_start: bool = False, kwargs: dict = None):

        """
        metodo che permette di inviare in blocco i log di una probe

        Args:
            uuid_probe  (str): uuid della probe a cui appartengono i log
            payload (list[str]): list of strings to sent
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Examples:
            body: [
                    "string"
                  ]

        Returns: list

        """

        params = {'uuid_probe': uuid_probe}

        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/probes_log_ingest/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, params=params, **kwargs)
        return response
