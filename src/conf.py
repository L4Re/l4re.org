# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os

project = 'L4Re Operating System Framework'
copyright = ': This page is licensed under CC-BY-SA 4.0'
author = 'L4Re project members and individual contributors'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinxcontrib.doxylink',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.plantuml',
    'sphinx.ext.todo',
    'sphinx_togglebutton',
    'sphinx_inline_tabs',
    'sphinx_copybutton',
]

templates_path = ['../_templates']
exclude_patterns = ['venv', '_build', 'Thumbs.db', '.DS_Store', 'README.md']

highlight_language = "none"

todo_include_todos = False

# -- Intersphinx links -------------------------------------------------------

intersphinx_mapping = {
    'bob' : ('https://bob-build-tool.readthedocs.io/en/latest/', None),
}

# -- Doxygen links -----------------------------------------------------------
doxylink = {
    'l4re': (os.getenv("PATH_L4RE_TAG_FILE") or "", 'https://l4re.org/doc/'),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['../_static']
html_last_updated_fmt = "%Y-%m-%d"
html_css_files = ["css/custom.css", "css/asciinema-player.css"]
html_logo = "https://l4re.org/gfx/L4Re_rgb_logo_quadratisch.png"
#html_baseurl = "src"

#html_theme_options = {
#   "logo": {
#      "image_light": "_static/L4Re_logo_quer.svg",
#      "image_dark": "_static/L4Re_logo_quer_invertiert.svg",
#   }
#}
