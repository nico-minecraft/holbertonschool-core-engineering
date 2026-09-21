#!/usr/bin/env python3
"""Module that defines the Animal abstract class and its subclasses.

This module demonstrates the use of Python's abc module to
create an abstract base class that enforces a common interface
on all of its subclasses.
"""
ABC = __import__('abc').ABC
abstractmethod = __import__('abc').abstractmethod


class Animal(ABC):
    """Represent an abstract animal.

    This class defines a common interface for all animals
    through the abstract sound method. Subclasses must provide
    their own concrete implementation of this method.
    """

    @abstractmethod
    def sound(self):
        """Return the sound the animal makes.

        This method is abstract and must be implemented by any
        concrete subclass of Animal.
        """
        pass


class Dog(Animal):
    """Represent a dog, a concrete subclass of Animal."""

    def sound(self):
        """Return the sound a dog makes.

        Returns:
            str: the string "Bark".
        """
        return "Bark"


class Cat(Animal):
    """Represent a cat, a concrete subclass of Animal."""

    def sound(self):
        """Return the sound a cat makes.

        Returns:
            str: the string "Meow".
        """
        return "Meow"
