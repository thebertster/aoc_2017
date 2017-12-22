class Registers(dict):
    """Registers class.

    Works like a dict with a default value of 0,
    but only for keys that start with an alpha character.

    Accessing a key that does not start with an alpha returns
    an integer representation of the key.
    """

    def __getitem__(self, key):
        """Register/value access.

        Return register contents if key is alpha (default 0).
        Return key as value otherwise.
        """
        return (self.setdefault(key, 0)
                if key[0].isalpha()
                else int(key))
