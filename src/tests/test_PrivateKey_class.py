import unittest, os, importlib
from bitshares_helpers.account import PrivateKey



wifs = [
    '9e303cabec67b6c6cc6d9c255d7741b14ce5461774ae4d62068b37646bacefb6',
    '30bb0c873bfe3a3a8018dd7c2af084c1a4f849b9579016bddcedc4e60352f3b7',
    'a69ba6e8faf5cf7e32a556e9be040ad8d0639358d2017d0748b09b02edef5583',
]


class wif_private_key__property(unittest.TestCase):

    def test_wifs_should_encode_correctly(self):
        for wif in wifs:
            pk = PrivateKey(wif=wif, prefix='BTS')
            self.assertEqual(
                wif,
                pk.wif_private_key,
            )




