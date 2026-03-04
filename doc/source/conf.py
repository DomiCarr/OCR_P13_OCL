# doc/source/conf.py
#
# Configuration file for the Sphinx documentation builder.

import os
import sys
import django

sys.path.insert(0, os.path.abspath("../.."))

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "oc_lettings_site.settings",
)

django.setup()

# -- Project information -----------------------------------------------------

project = "OCL"
copyright = "2026, OCR"
author = "OCR"
release = "1.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]