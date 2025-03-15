# L4re.org website source

## How to build

Prepare a Python virtualenv and install all dependencies:

    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt

When returning to an existing environment, just do:

    $ virtualenv venv
    $ . venv/bin/activate

With this, build simply with:

    $ PATH_L4RE_TAG_FILE=/path/to/doxygens/l4re.tag make html

Providing the TAG file is optional.
    
The result can be found in `_build/html/index.html`.

## Readings

reStructuredText Primer: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html


