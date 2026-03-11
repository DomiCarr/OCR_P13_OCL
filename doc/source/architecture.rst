Architecture
============

Project structure
-----------------

The project is based on one Django project and two Django applications:

- ``oc_lettings_site``: main Django project
- ``lettings``: lettings application
- ``profiles``: profiles application

Main responsibilities
---------------------

- ``oc_lettings_site`` contains global configuration, root URLs and general views
- ``lettings`` contains models, views and URLs related to lettings
- ``profiles`` contains models, views and URLs related to user profiles

Tests
-----

Tests are organized by application and cover:

- models
- views
- URLs