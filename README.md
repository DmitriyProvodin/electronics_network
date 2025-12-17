## Electronics Network API

### Технологии
- Python 3.8+
- Django 3+
- Django REST Framework
- PostgreSQL

### Запуск проекта

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
