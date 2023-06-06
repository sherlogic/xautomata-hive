# Xautomata API
Pacchetto che fornisca una interfaccia semplice per usare le API di Xautomata in python

# Installazione

Delle installazioni presentate qui di seguito si consiglia di usare l'installazione editabile, che appare essere piu stabile
rispetto a quella generica

## Installazione editabile
```
pip install -e git+https://github.com/sherlogic/xautomata-hive.git#egg=Tages[hive]
```

Se si e' interessati ad una specifica versione, bisogna inserire la versione scelta dopo la @, come indicato di seguito
```
pip install -e git+https://github.com/sherlogic/xautomata-hive.git@0.0.1#egg=Tages[modulo]
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