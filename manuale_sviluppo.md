# sviluppo nuovo endpoint
nel caso dovessero essere implementati nuovi api, qui sotto viene presentata una piccola guida con esempi per le diverse possibilita di codice.
La prima cosa da fare è locare il file corretto su cui aggiungere il nuovo API: nella cartella **coockbook** sono presenti tanti file quante le diverse categorie di API su XAutomata,
se la categorie è gia presente si deve lavorare li dentro, se non è presente deve essere aggiunto nuovo.

Se viene aggiunto nuovo deve essere anche posto tra le classi *Parent* della classe **XautomataApi** nel file *hive.api*.

### simple get
```python
    def new_api(self, single_page: bool = False, page_size: int = 5000, warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch data.

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

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('GET', path='/new_api/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, params=params, **kwargs)
        return response
```

come si vede da questo esempio per una get, si deve inserire il path parziale, e gli altri parametri single_path, page_size, warm_start. Tutti i parametri specifici
di questo endpoint vengono raccolti dentro **params**

esiste una alternativa, per quegli endpoint che non posseggono skip e limit nei loro parametri, queste API non possono essere paginate.
In queste situazioni si deve scrivere il metodo in maniera leggermente diversa.

Il primo passaggio è inserire il seguente import:


```python
from hive.api import handling_single_page_methods
```

e di seguito il metodo che tiene il considerazione il fatto che non su puo paginare

```python
    def new_api(self, uuid: str, warm_start: bool = False, kwargs: dict = None, **params):
        """
        Fetch single element.

        Args:
            uuid (str): uuid dell'elemento da recuperare
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Keyword Args:
            join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)
        response = self.execute('GET', path=f'/new_api/{uuid}', warm_start=warm_start, params=params, **kwargs)
        return response
```

Come si vede, sono stati rimossi i riferimenti a single_page e page_size, oltre ad aver introdotto **handling_single_page_methods**.
Questa funzione garantisce che non vengano passati erroneamente parametri legati alla paginazione.

Piccola nota, l'**uuid** del secondo esempio viene passato direttamente dentro l'url perche è cosi che l'API se lo aspetta.

### simple post

```python
    def new_api_post(self, kwargs: dict = None, **payload):
        """
        update new element.

        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Keyword Args:
            name (str): additional filter, required, required
            description (str): additional filter, required
            status (str): additional filter, required

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path=f'/new_api/', payload=payload, **kwargs)
        return response
```

A differenza della get, la post porta in modo espicito nel nome del metodo la parola post.
Non vengono inserite le chiavi di single_page, page_size e warm_start che non verrebbero usati.
Cio' che prima veniva passato dentro ai **params** ora viene inserito nei **payload**.
Esattamente come per le get, anche qui le chiavi del payload devono essere riportate nel docstring perche nel **payload**
vengono raccolti tutti i filtri specifici dello specifico endpoint.

### simple put

```python
    def new_api_put(self, uuid: str, kwargs: dict = None, **payload):
        """
        update selected element.

        Args:
            uuid (str): uuid della metrica da modificare
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API

        Keyword Args:
            description (str, optional): additional filter
            status (list or dict, optional): data profile

        Returns: list

        """
        if kwargs is None: kwargs = dict()
        response = self.execute('PUT', path=f'/new_api/{uuid}', payload=payload, **kwargs)
        return response
```

Le put prendono la stessa forma delle post, qui sopra si vede un esempio dove viene richiesto un parametro da inserire dentro all'url e dei parametri
specifici di quel endpoint che vengono contenuti dentro al **payload**

### simple delete

```python
    def new_api_delete(self, uuid: str, kwargs: dict = None):
        """

        delete single element.

        Args:
            uuid: id del metric da eliminare
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('DELETE', path=f'/new_api/{uuid}', **kwargs)
        return response
```

anche la delete prende una forma molto simile alla post, viene indicato delete nel nome del metodo
e dentro la **execute**. La delete di solito non porta con se nessun params o payload, ma dipende dal
endpoint specifico, cosi come non devono essere inseriti i riferimenti a single_page e page_size e warm_start.

### bulk (read, create, delete)

Alcune API portano nel nome la dicitura bulk, queste chiamate devono essere gestite diversamente.
Come prima differenza fundamentale, questa API richiede una lista di elementi con cui interagire, non uno per volta.
Tale lista di elementi viene fornita in una vera e propria lista python nel corpo della richiesta.
Queste chiamate possono sempre essere paginate. Mentre il **warmstart** è possibile essere usato solo per le *read*.
L'intero contenuto della lista da passare alla chiamata viene passato al payload di execute, ma viene fornito senza scompattarlo.
*Non esiste una modalita bulk per le update/put.*

**Tutte le bulk indipendente dal fatto che sono read, create o delete devono essere inserite come POST nella execute** 

```python
    def new_api_bulk(self, payload: list, single_page: bool = False,
                     page_size: int = 5000, warm_start: bool = False, kwargs: dict = None):
        """
        fetch gli elementi in bulk

        Args:
            payload (list[dict], optional): List dict uuids.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/new_api/bulk/read/', single_page=single_page, page_size=page_size,
                                warm_start=warm_start, payload=payload, **kwargs)
        return response
```

come per gli altri metodi, la read non porta nel nome del metodo la parola *read*, mentre per le create e delete, viene
riportato nel nome del metodo, come mostrato di seguito. 

```python
    def new_api_delete_bulk(self, payload: list, single_page: bool = False,
                            page_size: int = 5000, kwargs: dict = None):
        """
        elimina gli elementi in bulk

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/new_api/bulk/delete/', single_page=single_page, page_size=page_size,
                                payload=payload, **kwargs)
        return response
```

la create, potrebbe portare una costruzione del contenuto della lista piu complesso, se viene chiesto uno schema piu complesso, questo deve essere 
riportato come esempio nel docstring.

```python
    def new_api_create_bulk(self, payload: list, single_page: bool = False,
                            page_size: int = 5000, kwargs: dict = None):
        """
        crea gli elementi in bulk

        Args:
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Examples:
            uuids = [
            {'name': 'name1, 'status': 'status1'},
            {'name': 'name2, 'status': 'status2'},
            {'name': 'name3, 'status': 'status3'}
            ]

        Returns: list
        """
        if kwargs is None: kwargs = dict()
        response = self.execute('POST', path='/new_api/bulk/create/', single_page=single_page, page_size=page_size,
                                payload=payload, **kwargs)
        return response
```