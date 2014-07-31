Gonalytics (tracker)
=============

Gonalytic is a open source web analytics application. It consists of:
- tracker: https://github.com/piotrkowalczuk/gonalytics-tracker
- tracking script: https://github.com/piotrkowalczuk/gonalytics-tracking-script
- dashboard (this repository)

Installation
------------
1. Create virtual environment: `virtualenv venv`
2. Activate virtual environement: `. venv/bin/activate`
3. Install dependencies: `pip install -r requirements/dev.pip`
4. Create settings file: `cp application/gonalytics/settings.py.dist application/gonalytics/settings.py`
5. Update settings. Db credentials etc.
6. Init database schema: `python application/manage.py syncdb`
7. Install frontend dependencies: `python application/manage.py bower install`
8. Run an application: `python application/manage.py runserver 127.0.0.1:8000`

Dependencies
------------
- MySQL/PostgreSQL
