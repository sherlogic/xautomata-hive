# Installazione

Delle installazioni presentate qui di seguito si consiglia di usare l'installazione editabile, che appare essere piu stabile
rispetto a quella generica

## Installazione editabile
```
pip install -e git+https://github.com/sherlogic/xautomata-hive.git#egg=hive[hive]
```

Se si e' interessati ad una specifica versione, bisogna inserire la versione scelta dopo la @, come indicato di seguito
```
pip install -e git+https://github.com/sherlogic/xautomata-hive.git@0.0.1#egg=hive[modulo]
```

in alternativa si puo scaricare il source code dalla release desiderata e pip installare il source code direttamente
```
pip install -e Source_code.tar.gz[modulo]
```

in alternativa si puo clonare la rep e pip installare la libreria dalla cartella locale
```
pip install -e ./xautomata-hive[modulo]
```
## Installazione generica
Per l'installazione generica basta rimuovere il **-e** dalla riga di comando, sconsigliato perche meno stabile con la tipologia di setup di questo pacchetto

## gestione dei moduli

come si vede dalle chiamte elencate sopra, al fondo degli url delle chiamte pip viene sempre aggiunto un
elemento tra due parentesi quadre **[modulo]**. Questo e' un metodo con cui vengono gestite le dipendenze specifiche per ogni uso.
In fase di installazione della libreria e' sempre possibile chiedere di installare le dipendenze dei soli file o cartelle usati.
Per fare cio basta inserire nello spazio **modulo** il percorso del pacchetto o del file interessato.
Di seguito un esempio di installazione di hive per una situazione in cui si e' interessati all'uso di un solo file e una cartella della libreria.

```
pip install -e ./xautomata-hive[hive.cookbook,hive.decorators]
```
L'esempio non ha necessariamente senso, ma se fatto verrebbero installate solo le librerie necessarie per 
usare tutti gli script nella cartella cookbook e quelli nel file decorators.

**Se si vogliono ottenere tutte le dipendeze disonga inserire [hive], non mettere nulla non installa dipendenze**