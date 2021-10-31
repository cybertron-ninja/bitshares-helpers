import os


__all__ = [
    'TESTS_ROOT',
    'SRC_ROOT',
    'PACKAGE_ROOT',
]


TESTS_ROOT = os.path.dirname(__file__)
SRC_ROOT = os.path.join(
    os.path.dirname(TESTS_ROOT),
    'src'
)
PACKAGE_ROOT = os.path.join(
    SRC_ROOT,
    'bitshares_helpers',
)

