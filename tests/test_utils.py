from mkgen.utils import flat


def test_flat():

    ll = [[1, 2, 3], [4, 5], [6]]

    assert flat(ll) == [1, 2, 3, 4, 5, 6]
