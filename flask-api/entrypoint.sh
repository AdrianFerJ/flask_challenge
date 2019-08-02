echo "Waiting for mysql..."

while ! nc -z comments-db 3306; do
  sleep 0.1
done

echo "MySQL started"

python manage.py run -h 0.0.0.0