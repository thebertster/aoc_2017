class CircularList(list):
    """Represents a circular list."""

    def __init__(self, *args):
        """Initialise the circular list.

        Args:
            initial_list (list): An initial individual value or a list.
        """
        list.__init__(self, *args)

    def __getitem__(self, given):
        """Return a circular slice.

        Args:
            given: A slice or single value to return.
        Returns:
            The slice, wrapping as appropriate.
        """

        if isinstance(given, slice):
            start = given.start if given.start else 0
            stop = given.stop if given.stop else start + len(self)
            step = given.step if given.step else 1
            return_slice = [list.__getitem__(self, i % len(self))
                            for i in range(start, stop, step)]
            return return_slice

        return list.__getitem__(self, given)

    def replace(self, start, replacement):
        """Replace part of the list with another list.

        Args:
            start: Index from which to replace.
            replacement: List or value to replace.
        """
        if isinstance(replacement, list):
            for i, element in enumerate(replacement):
                self[(start + i) % len(self)] = element
        else:
            self[start] = replacement
