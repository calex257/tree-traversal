import tree

copacel = tree.Tree()
copacel.add(5)
copacel.add(2)
copacel.add(0)
copacel.add(3)
copacel.add(4)
copacel.add(1)
copacel.add(6)
copacel.add(8)
copacel.add(7)


def test_find_1():
    assert copacel._find(2, copacel.getRoot()) is not None

def test_find_2():
    assert copacel._find(100, copacel.getRoot()) is None