Image Uploads
=============

An example of a project using django-ajax-uploader and django-crispy-forms for image uploads.

To try out this project, download the code into your virtual environment, create local_settings.py with your database settings, install the required third parties:

If you don't have pip:

    easy_install pip

Then install the missing required modules:

    pip install Django
    pip install south
    pip install django-ajax-uploader==0.3
    pip install django-crispy-forms==1.4.0

Finally create the database and run server

    python manage.py syncdb --migrate
    python manage.py runserver