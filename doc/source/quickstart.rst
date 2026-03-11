Quickstart
==========

Run the application locally
---------------------------

.. code-block:: bash

   python manage.py migrate
   python manage.py runserver

The application is then available at:

.. code-block:: text

   http://127.0.0.1:8000

Run quality checks
------------------

.. code-block:: bash

   flake8 oc_lettings_site lettings profiles
   pydocstyle oc_lettings_site lettings profiles
   pytest --cov=oc_lettings_site --cov=lettings --cov=profiles