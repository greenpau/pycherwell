Getting Started with Cherwell API Client
========================================

Installation
------------

If necessary, upgrade ``pip``:

.. code:: bash

    python3 -m pip install --upgrade pip setuptools wheel twine

Install with PyPI:

.. code:: bash

    pip3 install pycherwell --user

Install from source:

.. code:: bash

    git clone https://github.com/greenpau/pycherwell.git
    cd pycherwell
    python3 setup.py install --user --record installed_files.txt

If necessary, uninstall ``pycherwell``:

.. code:: bash

    pip3 uninstall pycherwell
    cat installed_files.txt | xargs sudo rm -rf

Configuration Files
-------------------

LDAP Configuration file: ``~/.cherwell/config``:

.. code:: toml

    [default]
    client_id = "5d4f6f1b-f0de-4442-8791-4582816b04de"
    auth_mode = "LDAP"
    username = "MYDOMAIN\myappuser"
    password = "xxxxxx"
    host = "myapp.cherwellondemand.com"
    port = "443"
    protocol = "https"

LOCAL configuration file: ``~/.cherwell/config``:

.. code:: toml

    [default]
    client_id = "5d4f6f1b-f0de-4442-8791-4582816b04de"
    auth_mode = "Internal"
    username = "Cherwell\myappuser"
    password = "xxxxxx"
    host = "myapp.cherwellondemand.com"
    port = "443"
    protocol = "https"

Basic Usage
-----------

The following command checks whether the services is available:

.. code:: bash

    $ cherwell-client --get-service-info --debug

The expected output is:

.. code:: json

    {
        "service_info": {
            "api_version": "9.3.2",
            "csm_culture": "en-US",
            "csm_version": "9.3.2",
            "system_date_time": "2019-11-18 18:14:42.510452+00:00"
        }
    }

The following commands fetches business object summaries. It is a
reference to the IDs for business objects themselves, their fields,
states, etc.

.. code:: bash

    cherwell-client --get-business-object-summaries > business-object-summaries.json
    {
        "business_object_summaries": [
            {
                "bus_ob_id": "fe838f7d1a8d4a748940dba7be76995c",
                "display_name": "Incident",
                "first_rec_id_field": "3910bef5813c421a92e4a68eea109a95",
                "group": false,
                "group_summaries": [],
                "lookup": false,
                "major": true,
                "name": "Incident",
                "rec_id_fields": "f5e8c54b647f48ad81e720132624001e",
                "state_field_id": "cb62a991a2cb4fd98cab26c3519b2d92",
                "states": "Pending,Closed,Reopened,New,In Progress,Resolved,Assigned",
                "supporting": false
            }
        ]
    }

By default, the tool stores the returned business objects in
``~/.cherwell/business_object.json``. Subsequent requests return the
content of that file, unless the invocation includes ``--rebase``
argument.

.. code:: bash

    cherwell-client --get-business-object-summaries --rebase

The following command gives information about Cherwell Incident 1234567:

.. code:: bash

    cherwell-client --get-incident 1234567 --debug --format yaml

