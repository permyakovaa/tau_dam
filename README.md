# Tau Digigtal Assets Management system

## To run website in Docker:
1. Create .env file and setup database connection parameters
```bash
cp atube/.env.template atube/.env
nano atube/.env
```

2. Create docker network to connect app container and mysql contrainer
```bash
docker network create websitenetwork
```

3. Setup mysql server container (don't forget to change YOUR_PASSWORD)
```bash
docker run --name mysql-container --network websitenetwork -e MYSQL_ROOT_PASSWORD=YOUR_PASSWORD -e MYSQL_DATABASE=tau_dam -d mysql:latest
```

4. Connect to mysql docker image
```bash
docker exec -it mysql-container bash
```

5. Connect to mysql
```bash
mysql -u root -p
```

6. Execute mysql queries (don't forget to change YOUR_PASSWORD)
```bash
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'YOUR_PASSWORD';
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'YOUR_PASSWORD';
flush privileges;
```

7. Build website container
```bash
docker build -t tau_dam .
```

8. Run website container
```bash
docker run -d --network websitenetwork -p 8000:8000 tau_dam
```

9. Connect to app docker container
```bash
docker exec -it tau_dam bash
```

10. Execute migrations
```bash
python3 manage.py migrate
```

11. Add superuser
```bash
python3 manage.py createsuperuser
```