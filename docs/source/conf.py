# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Django Modules Import ---------------------------------------------------
import os
import sys

import django

# Add the absolute path to the directory that contains 'manage.py'
# From docs/source/, go up one level to docs/, then up another to pronto_npc_backend/
sys.path.insert(0, os.path.abspath("../../"))

# Add the absolute path to the directory containing your project's settings.py
# This is usually the inner project directory, named the same as your project.
# From docs/source/, go up to pronto_npc_backend/, then into pronto_npc_backend/
sys.path.insert(0, os.path.abspath("../pronto_npc_backend"))

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pronto_npc_backend.settings")
django.setup()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pronto_npc_backend.settings")
django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Pronto NPC Backed"
copyright = "2025, CMC Services - Cash Myers"
author = "Cash Myers"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # Recommended for more flexible docstring parsing
    "sphinx.ext.viewcode",  # Adds links to the source code
    "sphinx_rtd_theme",  # If you want the Read the Docs theme
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
