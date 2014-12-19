# Configuration files for the server

### gunicorn.conf
This is the configuration file for Gunicorn. It binds Gunicorn workers to Django and puts them under Supervisor's control. There should be a symlink to it, located in /etc/supervisor/conf.d/

### nginx.conf
This is the configuration file for the Nginx server. It basically maps port 80 to the Django/Gunicorn port 8000 as well as serves up the static files. There should be a symlink to it, located in /etc/nginx/sites-enabled/

### requirements.txt
This is the file that contains the names and versions of python packages to be used to install them via pip into a virtual environment.
    
    pip install -r requirements.txt