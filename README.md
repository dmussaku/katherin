# Setting up dev environment with Vagrant and Docker

## 0. Install Vagrant and VirtualBox.

## 1. Clone project and go to project directory `cd katherin`

## 2. Create vagrant machine - `vagrant up`. This will also install Docker engine inside vagrant machine.

## 3. SSH to vagratn - `vagrant ssh`

## 4. Pull PostgreSQL image from official repository:
```
docker pull postgres:9.6
```

## 5. Create data-container from postgres:9.6 image for persisting database data.
```
docker create --name "postgres-data" -v /var/lib/postgresql/data postgres:9.6
```

## 6. Build project environment container
```
docker build backend/Dockerfile amir/katherin_env
```

## 7. Start postgres container
```
docker run -d --name postgres -e POSTGRES_PASSWORD=katherin -e POSTGRES_DB=katherin -e POSTGRES_USER=katherin postgres:9.6
```

## 8. Start project env container
```
docker run -it -p 8080:8080 --name katherin -v /www/katherin:/www/katherin --link postgres:postgres amir/katherin_env /bin/bash
```

## 9. Run application inside container and go to browser `localhost:8080` to check if port forwarding works correctly.
```
python3 manage.py runserver 0.0.0.0:8080 --settings=settings.dev
```

# Run tests

## 1. Create another postgres container for running tests
```
docker run -d --name postgres-for-tests -e POSTGRES_PASSWORD=katherin -e POSTGRES_DB=katherin -e POSTGRES_USER=katherin postgres:9.6
```

## 2. Run tests
```
docker run --rm -it --name katherin-tests -v /www/katherin:/www/katherin -v /www/katherin/run_tests.sh:/www/run_tests.sh --link postgres-for-tests:postgres-for-tests amir/katherin_env /www/run_tests.sh
```
