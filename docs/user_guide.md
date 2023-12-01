# Manuale d'uso

La libreria *hive* è stata pensata per facilitare l'interazione con le API di XAutomata.
Di seguito si trova un esempio dove viene chiesta la lista dei customers con codice DEMO, e si chiede di ottere il 
risultato paginato di 50 elementi per volta. Il risultato ottenuto (ricompattato in un unica lista) vine poi
usato per estrarre lo uuid del primo customer per chiedere tutti i siti attivi di quel customer scelto.

L'uso di questa libreria garantisce una serie di feature aggiuntive automatiche, gestite dietro le quinte, di cui l'operatore non deve preoccuparsi:
- warmstart: gestione di una cache locale per non rifare piu volte la stessa chiamata se non serve.
- ratelimiter: vengono limitate le chiamate massime al minuto che si possono fare, garantendo l'impossibilita di dare fastidio al server inavvertitamente.
- riautenticazione: se l'autenticazione usata scade per il troppo tempo passato, viene gestita in automatico la riatuenticazione.
- paginazione: le chiamate troppo grandi vengono suddivise in automatico in sottochiamate per non chiedere tutto assieme.
- richiamate: se una chiamata fallisce vengono fatti una serie di tentativi prima di restituire un errore.

**Ogni metodo usato restituisce sempre una lista di elementi.**

Le API trovate sullo swagger del proprio ambiente XAUTOMATA sono chiamabili in maniera semplificata come metodi della
libreria *XautomataAPI*. In alternativa si puo usare una metodologia piu simile alla libreria *request* che richiede l'url
dell'API. Di seguito i due tipi di approccio.

## API come metodi

```python
from hive.api import XautomataApi

root = ''
passw = ''
user = ''

xa = XautomataApi(root=root, user=user, password=passw)

customers = xa.customers(code='DEMO', like=True, page_size=50)

uuid_c = customers[0]['uuid']

sites = xa.sites(uuid_customer=uuid_c, status='A')
```

Si puo vedere come le chiamate alle API hanno la stessa terminologie trovata sullo swagger
cosi come tutti i parametri di filtro evidenziati dentro lo swagger.
Suddetti filtri vengono selezionati semplicemente aggiungendo la chiave:valore nel metodo scelto.
In aggiunta ai filtri degli specifici endpoint sono presenti in aggiunta:
- single_page: XautomataApi pagina sempre la chiamata, ma se impostato a single_page=True, la paginazione viene inibita
- page_size: paginando in automatico, è sempre presente un valore di elementi per pagina. Importante ricordare che il risultato non viene restituito paginato ma sempre ricompattato in una unica risposta.
- warm_start: per le chiamate in lettura è sempre possibile attivare la modalita warmstart che crea una hard cache locale, salvado la risposta in un file. Ogni volta che viene rifatta la stessa chiamata con gli stessi parametri (se in modalita warm_start), il risultato viene preso dal file locale invece che fare la chiamata al server.
- kwargs: questa chiave prevede di ricevere un dizionario e sono valori vengono passati direttamente a *request*. Utile sono a chi sa cosa sta facendo e vuole un comportamento di request diverso dal default.

L'uso di ogni API è specializzato ai parametri specifici di quel API, per avere un dettaglio dei parametri usabili si puo consultare sia il docstring di ogni metodo,
che contiene il dettaglio dei parametri usabili, cosi come lo swagger stesso. Ogni parametro presente nello swagger è riportato un modo speculare nei parametri di XautomataApi.

Nelle situazioni in cui viene richiesto un corpo delle API sotto forma di una lista di oggetti, la lista deve essere fornita per intero, come nell'esempio che segue:

```python
from hive.api import XautomataApi
xa = XautomataApi(root='root', user='user', password='passw')

lista_uuid = ['uuid1', 'uuid2', 'uuid3']

customers = xa.sites_bulk(payload=lista_uuid)
```

### chiamate in modalita multi
E' anche possibile iterare un metodo sopra una lista di chiavi con il metodo multi built-in.
Questo metodo esegue un semplice for su ogni chiave della lista che si vuole investigare, ma a differenza di un ciclo normale, gestisce l'eventuale paginazione e warm_start come fosse un unica chiamata, rendendo il tutto piu efficiente.
Un esempio di uso e' il seguente:

```python
from hive.api import XautomataApi
xa = XautomataApi(root='root', user='user', password='passw')

lista_uuid = ['uuid1', 'uuid2', 'uuid3']

uuid_objects_w_probes = xa.multi_method(method=xa.metric, name_to_cicle='uuid',
                                        multi_uuid=lista_uuid, warm_start=True)
```
In questo esempio vengono chiesti gli uuid di piu metriche in un ciclo che chiama l'API **metric** per ciascun uuid.
In casi dove il risultato puo essere ottenuto anche con un metodo bulk, il metodo bulk e' preferibile sia per performance che rapidita di esecuzione.

### chiamate in modalita get_post
Questo metodo permette di chiamare un endpoint in forma di GET, se si riceve una risposta ma il contenuto e' parzialmente diverso da quello usato viene fatta automaticamente una PUT, mentre se non e' presente viene eseguita automaticamente una POST.
Esistono due versioni di questo metodo, una versione singola **get_post** ed una versione bulk **get_post_bulk**.
La versione bulk permette di fornire una lista di elementi da verificare tutti assieme.

L'uso e' mostrato nell'esempio sottostante

```python
from hive.api import XautomataApi
xa = XautomataApi(root='root', user='user', password='passw')

newgroup = {
    "uuid_site": '000',
    "uuid_virtual_domain": '000',
    "type": 'IT',
    "name": 'name',
    "description": "description group",
    "status": "A"
}

getgroup = {
    "uuid_site": '000',
    "uuid_virtual_domain": '000',
    "name": 'name'
}

uuid, get_count, post_count, put_count = xa.get_post(url_get='/groups/', get_params=getgroup, post_params=newgroup)
```

Il modo migliore di usare i parametri della get e' usando solo quelli obligatori lasciando quelli optionali nella post, cosi se avviene un cambiamento dei parametri optionali l'oggetto viene ugualmente trovato.
Se la post avviene su un url diverso, puo essere usata la chiave *url_post*. Se l'api in scrittura chiede dei parametri aggiuntivi (come il site per la geolocalizzazione), questi possono essere aggiunti con la chiave **add_post_params**.

Nella risposta del metodo viene dato l'uuid dell'elemento e un valore intero che dice se l'uuid e' stato ottenuto con una GET, PUT o POST.

La versione bulk deve essere scritta come segue:

```python
from hive.api import XautomataApi
xa = XautomataApi(root='root', user='user', password='passw')

groups = [
    {
        "uuid_site": '000',
        "uuid_virtual_domain": '000',
        "type": 'IT',
        "name": 'name0',
        "description": "description group0",
        "status": "A"
    },
    {
        "uuid_site": '111',
        "uuid_virtual_domain": '111',
        "type": 'TLC',
        "name": 'name1',
        "description": "description group1",
        "status": "A"
    }
]

uuid, get_count, post_count, put_count = xa.spell.get_post_bulk(url_get="groups", post_params=groups)
```

La versione bulk e' piu diretta e semplica da usare. Puo essere dato il solo url della get se la post usa lo stesso nome.
Si usano solo i parametri della post, e' il metodo internamente che nella get opera con i soli parametri obligatori.
Se necessario possono essere aggiunti parametri alle API con le chiavi **add_get_params** e **add_post_params**.
La risposta e' una lista di uuid restituita nello stesso ordine degli elementi dati in ingresso.
I conteggi di get, put e post sono il numero totale di quanti ne sono avvenuti.

## Uso della documentazione delle API

Su questo sito di documentazione e' anche presente la documentazione dettagliata di ogni metodo creato.
La documentazione e' stata scritta con delle linee guida:
- le chiavi **payload** e **params** sono usate come contenitori di piu parametri. I parametri usabili tramite queste due chiavi sono descritti nella sezione **Kyeword Args**. Ciascun parametro porta alla fine della sua descrizione la parola **payload** o **params** per aiutare a distinguere a quale chiave appartiene.
- se un metodo e' di write, delete o update, sara esplicitato nel nome del metodo stesso. Mentre se il metodo e' di sola lettura, non sara espicitato nulla nel nome.
- tutti i metodi bulk richiedono la costruzione di una lista con dei dizionari dentro e in tutti i casi questo oggetto va dentro a **payload** indipendetemente se e' GET, POST, DELETE
- Non esistono metodi bulk PUT
- Gli schema dei dati che si possono mettere dentro al **payload** viene riportato negli **Examples**
- Se un metodo ha piu di uno schema dei dati che si possono inviare, le chiavi appartenenti ai diversi schema hanno un postilla numerica che rappresenta lo schema di appartenenza: *uuid_1, name_1, uuid_2, status_2* - in questo esempio lo schema 1 contiene uuid e name, mentre lo schema 2 contiene uuid e status
- Se sono presenti sia **payload** che **params** solo uno dei due sara nella versione kwargs (esempio **params), l'altro dovra essere scritto come oggetto unico non scomponibile, con la tipologia indicata nella documentazione, tipicamente o *dizionario* o *lista*

## API come url

In alternativa e' possibile usare XautomataApi tramite l'url dell'endpoint. La differenza chiave sul passare tramite
questo approccio e' che si possono chiamare anche API non ancora implemetate in modalita metodi, o manipolare in modo piu
diretto cosa viene passato alla chiamata. Resta ugualmente preferibile usare XautomataApi rispetto a *request*
perche anche tramite la chiamta url vengono mantenute le proprieta di paginazione, cache, riautenticazione etc.

Qui di seguito si puo vedere la chiamata fatta per ottenere i clienti con codice 'DEMO' in modalita url.

```python
from hive.api import XautomataApi
xa = XautomataApi(root='root', user='user', password='passw')

params = {'code': 'DEMO',
          'like': True}

customers = xa.execute(mode='GET', path='/customers/', params=params, page_size=50)
```

a differenza della modalita per metodi, in questo caso i parametri devono essere inseriti all'interno di un dizionario
che viene passato a **params** se si sta fornendo un parametri, e a **payload** se si sta fornendo un *corpo* (tipicamente
usato per le post)

## tips and tricks

esiste un parametri privato *_get_only* che se forzato a True impedisce di usare API di POST/PUT/DELETE. Fatta eccezione
delle bulk e query dove vengono inibite solo le chiamtate che andrebbero ad apportare modifiche al db

```python
from hive.api import XautomataApi
xa = XautomataApi(root='root', user='user', password='passw')
xa._get_only = True
```

con il parametro privato *_timeout_retry* si possono impostare un numero di retry per le situazioni in cui si fallisca le
request in caso di timeout, e il tempo tra un retry e quello successivo e' impostabile con *_timeout_sleep_time*.

con il parametro privato *_timeout_get_session_retry* si possono impostare un numero di retry per la libreria request su errori
noti, e il tempo tra un retry e quello successivo e' impostabile con una formula basata sul valore  *_timeout_get_session_backoff_factor*.
Di default *_timeout_get_session_retry* = 5 e *_timeout_get_session_backoff_factor* = 5.
