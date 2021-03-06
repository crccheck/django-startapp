Django Start App
================

This is a boilerplate template for starting a standalong Django app. It comes
with these amazing features:

* a non-functional setup.py
* example project for development that's Heroku-ready
* a testing app for your app built into the example project
* APL2 license

Instructions for once you get started:

Setup
-----

::

    pip install -r requirements.txt


Using Postgresql instead of Sqlite as your database::

    export DATABASE_URL='postgres:///{{ project_name }}'



Deploying to Heroku
-------------------

Create a new app and give it a database::

    $ heroku apps:create
    $ heroku addons:add heroku-postgresql:dev
    $ heroku config:set DJANGO_SETTINGS_MODULE=example_project.settings

Promote the database to ``DATABASE_URL`` (this should happen automatically)::

    $ heroku config | grep HEROKU_POSTGRESQL
    HEROKU_POSTGRESQL_RED_URL: postgres://user3123:passkja83kd8@ec2-117-21-174-214.compute-1.amazonaws.com:6212/db982398
    $ heroku pg:promote RED

Install the pgbackups addon::

    $ heroku addons:add pgbackups

Migrate data from your local Postgresql to Heroku (https://devcenter.heroku.com/articles/heroku-postgres-import-export)::

    $ pg_dump -Fc --no-acl --no-owner {{ project_name }} > {{ project_name }}.dump

Upload ``{{ project_name }}.dump`` someplace on the Internets and pull it into Heroku::

    $ heroku pgbackups:restore DATABASE http://example.com/{{ project_name }}.dump
