# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'design-patterns'
copyright = '2024, Volleyball Player'
author = 'Volleyball Player'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'sphinx.ext.coverage',
    'sphinx_click',
    'sphinxcontrib.plantuml',
]


always_document_param_types = True

templates_path = ['_templates']

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']

# Install Java
# Install Graphviz
# Download plantuml.jar file from https://sourceforge.net/projects/plantuml/
# Set PLANTUML_JAR, JAVA_HOME and GRAPHVIZ_DOT env variables in .bashrc
plantuml_jar = os.getenv('PLANTUML_JAR')
plantuml = f'java -jar {plantuml_jar}'
