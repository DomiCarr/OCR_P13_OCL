Deployment
==========

Docker
------

The application can be built and run with Docker.

.. code-block:: bash

   docker build -t oc-lettings .
   docker run --env-file .env -p 8000:8000 oc-lettings

CI/CD pipeline
--------------

The project uses GitHub Actions to:

- run quality checks
- run tests
- build the Docker image
- push the image to Docker Hub
- deploy the application to the OVH VPS

Production deployment
---------------------

The application is deployed on an OVH VPS.

Deployment is triggered automatically by the CI/CD pipeline after a push to the main branch.