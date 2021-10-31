from bitsharesbase.account import PrivateKey as BTSPrivateKey


__all__ = [
    'PrivateKey',
]


class PrivateKey(BTSPrivateKey):
    """
    A wrapper around a Bitshares private key, which adds convenience properties.
    """

    @property
    def wif_private_key(self):
        """
        Returns the private key as a "wif key" (a HEX string).

        :return: A "wif key".
        :rtype: str
        """
        return self.private_key_as_hex

    @property
    def private_key_as_hex(self):
        """
        Returns a private key as a HEX string.

        :return: The private key converted to a HEX string.
        :rtype: str
        """
        return self.__repr__()
