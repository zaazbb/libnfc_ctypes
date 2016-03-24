libnfc_ctypes
===========

This is libnfc python ctypes bindings, it should support python2 and python3.

I can not find a python3 version libnfc library under raspberry pi, so i write this codes for it.
  
It should work under other platform only need replace the libzbar path.  

It only test under Raspbian (raspberry pi) now.


Usage
-----

- Install (on raspberry pi)  
    - install libnfc:
    
        see https://github.com/nfc-tools/libnfc  
    
    - install libnfc_ctypes::

        git clone https://github.com/zaazbb/libnfc_ctypes
        cd libnfc_ctypes
        sudo python3 setup.py install  

- Example (on raspberry pi)  
    - run the example script.
  
todo
----

Add all libnfc function bindings.

Contact
-------

by jf.  

zaazbb <zaazbb@163.com>
