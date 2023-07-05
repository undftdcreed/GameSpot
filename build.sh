pip install -r deps.txt

python manage.py collectstatic --noinput

python manage.py migrate