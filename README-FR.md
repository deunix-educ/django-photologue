# django-photoloque
Il s'agit d'un fork de l'application Django [django-photoloque](https://github.com/richardbarran/django-photologue)
une puissante application de gestion d'images et de galerie

Ajout de django-resized et django-axes
w3.css comme feuille de style css.

## Installation

        tar xzfv django-photologue-main.zip
        or
        git clone git@github.com:deunix-educ/django-photologue.git
        cd django-photologue
        chmod +x etc/bin/*.sh
        chmod +x gallery/manage.py

- Installer les packages système 

        sudo apt update
        sudo apt -y install build-essential openssl git pkg-config redis supervisor
        sudo apt -y install python3-dev python3-pip python3-venv libmariadb-dev libpq-dev
        sudo cp /etc/supervisor/supervisord.conf /etc/supervisor/supervisord.conf.old 
        sudo cat >> /etc/supervisor/supervisord.conf << EOF [inet_http_server] port=*:9001 username=root password=toor EOF 
        
- configurer le serveur : exemple de configuration dans etc/conf 
            
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

        