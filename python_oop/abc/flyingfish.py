#!/usr/bin/env python3
"""Module that defines the Fish, Bird, and FlyingFish classes.

This module demonstrates multiple inheritance in Python and how
the method resolution order (MRO) determines which parent's
method is used when a method is not overridden.
"""


class Fish:
    """Represent a fish that lives and swims in water."""

    def swim(self):
        """Print a message describing how the fish swims."""
        print("The fish is swimming")

    def habitat(self):
        """Print a message describing where the fish lives."""
        print("The fish lives in water")


class Bird:
    """Represent a bird that lives and flies in the sky."""

    def fly(self):
        """Print a message describing how the bird flies."""
        print("The bird is flying")

    def habitat(self):
        """Print a message describing where the bird lives."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represent a flying fish, inheriting from Fish and Bird.

    This class overrides the swim, fly, and habitat methods of
    both parent classes to reflect its own unique behavior.
    """

    def fly(self):
        """Print a message describing how the flying fish flies."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print a message describing how the flying fish swims."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print a message describing where the flying fish lives."""
        print("The flying fish lives both in water and the sky!")
