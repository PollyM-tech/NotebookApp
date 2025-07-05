## Notebook App

## Models
- category (id, name, created_at)
- entry (id,note, user_id created_at, updated_at, deleted_at)
- user (id, full_name, email_address, password, created_at, updated_at)
- Task (id, name, status, created_at)

- install two packges pipenv install flask-sqlalchemy flask-migrate
- how to get possible commands flask db --help

- init migrations files with flask db migrate -m " "
- apply our migration with flask db upgrade 

