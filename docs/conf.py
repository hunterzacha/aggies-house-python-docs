# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('../flask_app'))
sys.path.insert(0, os.path.abspath('../database_temp'))
sys.path.insert(0, os.path.abspath('../testusers'))
sys.path.insert(0, os.path.abspath('../run'))
sys.path.insert(0, os.path.abspath('../test_data'))

project = "Aggie's House"
copyright = "2024, Hunter Zacha, Michelle Nguyen, Navya Mittal, Harini Kumar"
author = "Hunter Zacha, Michelle Nguyen, Navya Mittal, Harini Kumar"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_static_path = ['_static']
