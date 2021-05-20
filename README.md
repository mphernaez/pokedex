# pokedex

pokedex/ <br />
├─ pokedex/ <br />
├─ pokedex_webapp/ <br />
├─ README.md <br />

# istallation guide
- pokedex (api)
1. pip install -r requirements.txt
2. python manage.py migrate
3. python manage.py init_pokemon 151
4. python manage.py createsuperuser
5. python manage.py runserver 127.0.0.1:8080


- pokedex_webapp (website)
1. pip install -r requirements.txt
2. python manage.py runserver


# management commands
1. init_pokemon {{ number }}
- all pokemon from 1 to {{ number }} will be imported
- this may take a while because all sprites of pokemon will be downloaded
