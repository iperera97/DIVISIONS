# DIVISIONS

#### Sri Lanka is divided into 9 provinces, which are further subdivided into 25 Districtss. Districts are further subdivided into Municipalities, of which are sorted into three categories. Each municipality is divided into Wards and wards into Grama Niladhari divisions.
#

#### we can view / filter and add the provinces, districts and cities

- front end - react and redux
- back end - django, restframework and sqlite3

### backend development
```
    pipenv shell  # activate virtualenvironment
    pipenv sync  # install all packages from lock file
    python manage.py runserver  # running on port 8000
```

### fronend development
```
    npm install
    npm run dev  # running devserver on port 3000
    npm run build  # build project with production environment
```


### development with new database
```
    # migrate tables in database
    python manage.py migrate

    # load json data to database
    python manage.py loaddata fixtures/newdumps/province.json
    python manage.py loaddata fixtures/newdumps/district.json
    python manage.py loaddata fixtures/newdumps/city.json

    # create superuser for adminpanel login
    python manage.py createsuperuser 
```