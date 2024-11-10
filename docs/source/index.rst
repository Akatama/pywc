.. pywc documentation master file, created by
   sphinx-quickstart on Sat Nov  9 22:37:51 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pywc's documentation!
================================

Quickstart
----------

1. Install dependencies

    $ pip install pywc

2. Run uptimer

   $ python -m pywc test.txt


Quickstart for Devs
-------------------
1. Create a virtual environment

    $ python -m venv venv

2. Activate the environment

    $ source /venv/bin/activate

3. Download the Developer dependencies

    $ pip install -e '.[test]'

CLI commands
------------

.. click:: pywc.cli:cli
    :prog: pywc


Useful links
------------

.. toctree::
   :maxdepth: 2
