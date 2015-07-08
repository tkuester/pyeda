PyEDA aims to provide EDA tools written in Python, and to link to other relevant projects.


The first subproject is kipy (Python tools for KiCAD).  Not really documented at all yet, but you can download kipy via subversion:

svn checkout http://pyeda.googlecode.com/svn/trunk/kipy kipy

kipy is basically a library designed for easy use from other programs, but the kipy/tools directory contains scripts which can do the following:

  * Round-trip (read and write) Kicad .pro, .sch, and .lib files
  * Parse the .sch and .lib files and do additional rules checking
  * Output the netlist in a format suitable for use with ExpressPCB
  * Dump pin to net information for any reference designator

Kipy works under Linux and Windows and currently requires Python 2.5 or 2.6, as well as a KiCAD installation.