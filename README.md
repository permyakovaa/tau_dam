# Tau Digigtal Assets Management system

## To run website in Docker:
1. Run docker compose
```bash
docker compose up --build
```

2. Connect to app docker container
```bash
docker exec -it tau_dam bash
```

3. Execute migrations
```bash
python3 manage.py migrate
```

4. Add superuser
```bash
python3 manage.py createsuperuser
```