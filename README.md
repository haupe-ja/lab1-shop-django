# Projekt 1: Sklep internetowy (Django)

Prosta aplikacja webowa sklepu internetowego stworzona w frameworku Django. Projekt został przygotowany w celach edukacyjnych i zawiera wstępnie skonfigurowaną bazę danych SQLite z przykładowymi produktami.

## Wymagania wstępne
Aby uruchomić projekt lokalnie, upewnij się, że masz zainstalowane w systemie:
* [Python 3]
* [Git]

## Instrukcja uruchomienia lokalnego

Postępuj zgodnie z poniższymi instrukcjami w terminalu/wierszu poleceń, aby pobrać i uruchomić aplikację na swoim komputerze.

### 1. Pobranie repozytorium
Sklonuj repozytorium na swój dysk lokalny i przejdź do utworzonego folderu.
```bash
git clone [https://github.com/haupe-ja/lab1-shop-django.git](https://github.com/haupe-ja/lab1-shop-django.git)
cd lab1-shop-django
```

### 2. Utworzenie środowiska wirtualnego
Utwórz wirtualne środowisko o nazwie venv.
```bash
python3 -m venv venv
```

### 3. Aktywacja środowiska wirtualnego
Uruchom środowisko w zależności od Twojego systemu operacyjnego.

**Windows (Wiersz poleceń / PowerShell):**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 4. Instalacja wymaganych bibliotek
Gdy środowisko jest aktywne, zainstaluj wszystkie pakiety niezbędne do działania aplikacji.
```bash
pip install -r requirements.txt
```

### 5. Aktualizacja bazy danych
Projekt zawiera już plik bazy danych db.sqlite3 z dodanymi kategoriami i produktami. Mimo to, zalecane jest wykonanie migracji w celu upewnienia się, że struktura jest aktualna.
```bash
python manage.py migrate
```

### 6. Uruchomienie serwera deweloperskiego
Odpal lokalny serwer testowy Django.
```bash
python manage.py runserver
```