# Shoppie - Django website
    A Shopping website with django

[Click To See django admin: Shoppie](https://vivekskecher.pythonanywhere.com/admin)

##### Login for DjangoAdmin
##### User :vivek
##### password :weareheros


### =======version used=======

###### python -> 3.5.4
###### django -> 2.1
###### pip    -> 18.0
###### virtualenv->16.0.0

### =======Frist of all create environment======
```shell
cmd -> pip intall virtualenv
cmd -> virtalenv envname
cmd -> cd envname
cmd -> cd scripts
cmd -> activate
```

### =======Now Create A Django project and app======
```shell
cmd -> django-admin startproject projectname
cmd -> django-admin startapp appname
cmd -> python manage.py runserver 
```

### =======Link mysql database=======
```sql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'throughdjango',
        'USER': 'root',
        'PASSWORD': '12345',
    }
}
```

### =======Link Installed app=========
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Home',
]
```

### ========Check For correct connection======
```shell
(env1) A:\College Project\Django project\shopie>python manage.py shell
Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.db import connection
>>> c=connection.cursor()
>>> //if no error means connect successfully
```

### ========create models or work with model.py=======
```python
class User(models.Model):           //User changed into table name as Home_User
    Loginas = models.CharField()    //loginas changed in column and char is input type
    Uname = models.CharField()      //Uname changed in column and char is input type
    Password = models.CharField()   //Password changed in column and char is input type
    Email = modles.CharField()      //Email changed in column and char is input type
```

### =======install sqlclient=============

`cmd ->pip install pymysql`
`cmd ->pip install --only-binary :all: mysqlclient`
`cmd ->python manage.py check`


### =========migrations of code=========
```shell
for converting or creating or make changes in databases we need to make the migrations using commands
(env1) A:\College Project\Django project\shopie>python manage.py makemigratations
(env1) A:\College Project\Django project\shopie>python manage.py migrate
```

### =========Create SuperUser===============
`cmd -> python manage.py createsuperuser`
