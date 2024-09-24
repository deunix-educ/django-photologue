# django-photoloque
This is a fork of django application [django-photoloque](https://github.com/richardbarran/django-photologue) 
a powerful image management and gallery application

Added django-resized and django-axes

## Installation

        tar xzfv django-photologue-main.zip
        or
        git clone git@github.com:deunix-educ/django-photologue.git
        cd django-photologue
        chmod +x etc/bin/*.sh
        chmod +x gallery/manage.py

- Install system packages 

        sudo apt update
        sudo apt -y install build-essential openssl git pkg-config redis supervisor
        sudo apt -y install python3-dev python3-pip python3-venv libmariadb-dev libpq-dev
        sudo cp /etc/supervisor/supervisord.conf /etc/supervisor/supervisord.conf.old 
        sudo cat >> /etc/supervisor/supervisord.conf << EOF [inet_http_server] port=*:9001 username=root password=toor EOF 
        
- configure server: Configuration example in etc/conf 
            
        # django-photologue: Adapt etc/conf/gallery_service.conf
            sudo cp etc/conf/gallery_service.conf /etc/supervisor/conf.d/
            sudo supervisorctl reread

        # Edit and Configure Environment Variables gallery/.env-example
            cp gallery/.env-example gallery/.env

        # Create the python environment (.venv)
            etc/bin/venv-install.sh etc/install/requirements.txt

        # application
            cd gallery
            ./manage.py makemigrations
            ./manage.py migrate
            ./manage.py initapp
            ./manage.py collectstatic
            sudo supervisorctl update

        