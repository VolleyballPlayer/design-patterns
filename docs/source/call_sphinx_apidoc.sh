# source this script to create the API documentation of modules
# working directory must be root of repository

SPHINX_APIDOC_OPTIONS=members,show-inheritance sphinx-apidoc -o docs/source/technical_documentation/autodoc -f \
src/designpatterns