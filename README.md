Django mongodb sample application

### Install app

###### *Install Python packages*

virtualenv

If not already installed, grab a copy from the Cheeseshop:

<pre>pip install virtualenv</pre>

To set up a virtual environment for your project, use

<pre>virtualenv myproject</pre>

To join the environment, use (in Bash):

<pre>source myproject/bin/activate</pre>

Django-nonrel

<pre>pip install git+https://github.com/django-nonrel/django@nonrel-1.5</pre>

djangotoolbox

<pre>pip install git+https://github.com/django-nonrel/djangotoolbox</pre>

Django MongoDB Engine

You should use the latest Git revision.

<pre>pip install git+https://github.com/django-nonrel/mongodb-engine</pre>

<pre>pip install restframework</pre>

### Run an app

###### *Run Server*

./manage.py syncdb

./manage.py runserver 

You can see the port number in command prompt after sucessfull run

You can change the settings in settings.py file
