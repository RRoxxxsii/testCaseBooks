<a href='https://likesoft.notion.site/Python-c476609af7fe48e586cd7bafd639ea1e'><h1>Тестовое задание - книжный сервис</h1></a>
<hr>
<h4></h4>
<h2>Технологии:</h2>

`django-rest-framework`, `celery`, `redis`, `pytest`, `flake8`, `isort` 
<p>Версия Python: 3.11</p>
<p>СУБД: MySQL</p>

<hr>
<h3>Запуск: </h3>
<ul>
<li>

`git clone https://github.com/RRoxxxsii/testCaseBooks.git`

</li>

<li>

создать файл `.env` в корне проекта*

</li>

<li>

`docker compose up --build`

</li>

</ul>

<h4>*Содержимое `.env` файла</h4>

```
MYSQL_HOST=db
MYSQL_USER=root
MYSQL_PASSWORD=secret
MYSQL_ROOT_PASSWORD=secret
MYSQL_DATABASE=books
MYSQL_PORT=3306
```

<hr>
<h4>Запуск тестов</h4>

`pytest tests/`

<hr>

<h4>Эндпоинты:</h4>

`api/v1/accounts/` - создание пользователя
`api/v1/books/` - удаление/получение(cписка или по `id`)/редактирование/создание книг

<hr>
<p>установка фикстур:</p>

<ul>
<li>

`docker exec -it <имя django контейнера> /bin/bash`
</li>

<li>

`python manage.py loaddata fixture.json`
</li>

</ul>

<p>вход в админ-панель (после загрузки данных из фикстуры в ДБ):</p>
Имя пользователя: root
<br>
Пароль: 1234
