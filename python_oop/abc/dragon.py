#!/usr/bin/env python3
"""Module that defines the SwimMixin, FlyMixin, and Dragon classes.

This module demonstrates the use of mixins to compose behaviors
in a class in a modular fashion, without relying on a deep or
rigid inheritance hierarchy.
"""


class SwimMixin:
    """Provide swimming behavior to any class that uses it."""

    def swim(self):
        """Print a message describing the creature swimming."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior to any class that uses it."""

    def fly(self):
        """Print a message describing the creature flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon that can both swim and fly.

    Composes the SwimMixin and FlyMixin classes to gain
    swimming and flying behavior, and adds its own unique
    roaring behavior.
    """

    def roar(self):
        """Print a message describing the dragon roaring."""
        print("The dragon roars!")
