Lateral bicycle dynamics model
==============================

This code is intended to simulate the coupled dynamics of bicycles using a modified version of the lateral bicycle model
to account for the repelling interaction between them. 

***Last modified version 12/04/2016***

Lateral bicycle model - Python library for bicycle dynamics
===========================================================

Microsimulator solving for the free-space dynamics of bicycles using a so-called "Lateral bicycle
Model" based on the article [Helbing & Molnar Phys. Rev. E 51, 4282 (1995)]. 

- Includes pedestrian dynamics by solving time-dependent "Social Force Model" equations.

Installation
============

Requirements:

- Git
- Python and Numpy, Scipy, Matplotlib dependencies

The following instructions are for a Unix-like environment without 
root privileges.

In a terminal,

```sh
mkdir BicycleModel
cd BicycleModel
git clone https://github.com/UCLGuichard/BicycleModel
```

This gets the code. Now let's run it.

```sh
cd BicycleModel/src
python bicycle.py
```

If all went well, you should now have a test case running.

***BicycleModel has been developed and tested under Windows and Eclipse IDE with Python 2.7 and Anaconda interpreters.***

Usage
-----

Testing
-------

Example
-------

Getting help
------------

License
=======

See LICENSE file for more details.

Citation
========

See CITATION file for more details.

Version
=======

1.0 (in progress)

History
=======

BicycleModel is derived from numerous literature around vehicle models.

Acknowledgements
================

- Whoever involved in this project.

Contact
=======

[Roland Guichard] - <roland.guichard@ts.catapult.org.uk>


