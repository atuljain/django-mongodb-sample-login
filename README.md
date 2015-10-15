Django mongodb sample application

### Install app

###### *Install Python packages*

virtualenv

If not already installed, grab a copy from the Cheeseshop:

pip install virtualenv

To set up a virtual environment for your project, use

virtualenv myproject

To join the environment, use (in Bash):

source myproject/bin/activate

Django-nonrel

pip install git+https://github.com/django-nonrel/django@nonrel-1.5

djangotoolbox

pip install git+https://github.com/django-nonrel/djangotoolbox

Django MongoDB Engine

You should use the latest Git revision.

pip install git+https://github.com/django-nonrel/mongodb-engine

pip install restframework

### Run an app

###### *Run Server*

./manage.py syncdb

./manage.py runserver 

You can see the port number in command prompt after sucessfull run

You can change the settings in settings.py file
