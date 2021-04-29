Role Name
=========

This role automates the process of installing the neccesary Cache client Python libraries to allow connection to a Cache database via M Gateway's connection service.

Requirements
------------

It is assumed that Cache is to be installed somewhere on the network to allow testing.

It is also assumed that that the Service integration gateway is also installed (see https://github.com/RamSailopal/cache-node-server for details of installation)

Role Variables
--------------

hst - The address of the Intersystems Cache server

[ Default - localhost ]


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      role: cache-python-mg
      hst: cacheserver 
      ...

Further Information
-------------------

The github repo relating to the library being installed:

https://github.com/chrisemunt/mg_python

License
-------

BSD

Author Information
------------------

Raman Sailopal
