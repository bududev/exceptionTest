# Dependencies
<p>
    <ul>
        <li>
            redis - pip install redis
        </li>
        <li>
            celery - pip install celery
        </li>
    </ul>
</p>

#How to run
Execute 'redis-server' </br>
Execute 'python manage.py runserver' on other shell </br>
Execute 'celery worker -A exceptioinTest --loglevel=debug --concurrency=4' on another shell </br>
Fetch 'http://localhost:8000/exception/' to occur exception.
Fetch 'http://localhost:8000/list/' to get exceptions.