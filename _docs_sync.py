"""Allinea la documentazione mkdocs a quello che c'e' in ``hive/cookbook/``.

Per ogni modulo ``hive/cookbook/<nome>.py``:
  * crea ``docs/hive.cookbook.<nome>.md`` se manca (contenuto: ``::: hive.cookbook.<nome>``)
  * aggiunge la voce nel blocco ``cookbook:`` del ``nav`` di ``mkdocs.yml``
e rimuove pagine e voci di nav dei moduli che non esistono piu'.

Solo stdlib, idempotente. Lanciato dalla action prima di ``mkdocs gh-deploy`` cosi' la build non
si rompe quando i generatori aggiungono o potano file del cookbook.

Uso:  python _docs_sync.py          # applica
      python _docs_sync.py --check  # exit 1 se la documentazione non e' allineata (non scrive)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COOKBOOK = ROOT / 'hive' / 'cookbook'
DOCS = ROOT / 'docs'
MKDOCS = ROOT / 'mkdocs.yml'
PREFIX = 'hive.cookbook.'

# intestazione del blocco da riscrivere; il blocco finisce alla prima riga vuota successiva
NAV_HEADER = re.compile(r'^(?P<indent> *)- cookbook:\s*$', re.M)


def sync(check: bool = False) -> bool:
    """Ritorna True se era gia' tutto allineato."""
    modules = sorted(p.stem for p in COOKBOOK.glob('*.py') if p.stem != '__init__')
    changes = []

    # --- pagine docs/*.md
    wanted = {f'{PREFIX}{m}.md': f'::: {PREFIX}{m}' for m in modules}
    for existing in sorted(DOCS.glob(f'{PREFIX}*.md')):
        if existing.name not in wanted:
            changes.append(f'rimossa {existing.name}')
            if not check:
                existing.unlink()
    for name, content in wanted.items():
        path = DOCS / name
        if not path.exists():
            changes.append(f'creata {name}')
            if not check:
                path.write_text(content, encoding='utf-8', newline='')

    # --- nav di mkdocs.yml
    text = MKDOCS.read_text(encoding='utf-8')
    match = NAV_HEADER.search(text)
    if match is None:
        raise RuntimeError("blocco '- cookbook:' non trovato nel nav di mkdocs.yml")
    item_indent = match.group('indent') + '  '
    end = text.find('\n\n', match.end())
    if end == -1:
        end = len(text)
    new_items = ''.join(f'\n{item_indent}- {m}: {PREFIX}{m}' for m in modules)
    new_text = text[:match.end()] + new_items + text[end:]
    if new_text != text:
        changes.append('aggiornato nav in mkdocs.yml')
        if not check:
            MKDOCS.write_text(new_text, encoding='utf-8', newline='')

    for change in changes:
        print(change)
    if not changes:
        print('documentazione gia allineata')
    return not changes


if __name__ == '__main__':
    aligned = sync(check='--check' in sys.argv)
    sys.exit(0 if aligned or '--check' not in sys.argv else 1)
