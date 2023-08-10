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