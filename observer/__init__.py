# -*- coding: utf-8 -*-

"""

Simple implementation of the Observer pattern.

Copyright (C) 2009 Florian Léger


License
=======
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see U{http://www.gnu.org/licenses/}.


Example
=======
    >>> def myObserver(observable, *args, **kwargs):
    ...     print("Observable has changed: value=%s." %(kwargs["value"]))
    ...
    >>> class MyObservable(Observable):
    ...     def __init__(self):
    ...         Observable.__init__(self)
    ...         self.__value=None
    ...
    ...     def __getValue(self):
    ...         return self.__value
    ...
    ...     def __setValue(self, value):
    ...         self.__value=value
    ...         self._setChanged()
    ...         self.notifyObservers(value=self.value)
    ...
    ...     value=property(fset=__setValue, fget=__getValue)
    >>> myObservable=MyObservable()
    >>> myObservable.addObservers(myObserver)
    >>> print(myObservable.countObservers())
    1
    >>> myObservable.value=42
    Observable has changed: value=42.
    >>> myObservable.deleteObservers(myObserver)
    >>> print(myObservable.countObservers())
    0
    >>> myObservable.value="Stay quiet"
"""

__author__="Florian Léger"
__license__="GPLv3"
__version__="1.0.1"
__date__="15/09/2009"
__copyright__="2009 Florian Léger"
__url__="http://asi.insa-rouen.fr/etudiants/~fleger"

class Observable(object):
    """
    An Observable object.

    @note: Observers are callables.
    """

    def __init__(self):
        """
        Creates a new instance of Observable.
        """
        self.__observers=set()
        self.__hasChanged=False

    @property
    def hasChanged(self):
        """
        true if the Observable has changed, or false.
        """
        return self.__hasChanged

    def addObservers(self, *observers):
        """
        Add one or more Observers.

        @param observers:   The Observers to add.
        """
        self.__observers|=set(observers)

    def _clearChanged(self):
        """
        Clear the hasChanged flag.
        """
        self.__changed=False

    def countObservers(self):
        """
        Count how many observers observe thisn Observable.
        @return:        The number of observers attached to this Observable.
        @rtype:         int
        """
        return len(self.__observers)

    def deleteObservers(self, *observers):
        """
        Delete one or more Observers.

        @param observers:   The Observers to delete.
        """
        self.__observers-=set(observers)

    def notifyObservers(self, *args, **kwargs):
        """
        Notify all the Observers that the Observable has changed.

        The Observable must have changed (using the _setChanged method) for this method to take effect.
        The hasChanged flag is automatically cleared at the end of this method.

        @param args:        Arguments to pass to the observers.
        @param kwargs:      Named arguments to pass to the observers.
        """
        if self.hasChanged:
            [observer(self, *args, **kwargs) for observer in self.__observers]
            self._clearChanged()

    def _setChanged(self):
        """
        Set the hasChanged flag.
        """
        self.__hasChanged=True

if __name__=="__main__":
    # Regression tests
    import doctest
    doctest.testmod()