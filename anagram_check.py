from nose.tools import assert_equal


def anagram(s1, s2):
    array1 = []
    array2 = []
    for each in s1:
        if not each.isspace():
            array1.append(each.lower())

    for each in s2:
        if not each.isspace():
            array2.append(each.lower())

    array1.sort()
    array2.sort()

    return array1 == array2


def anagram2(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)


def anagram3(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    count = {}
    for each in s1:
        if each in count:
            count[each] += 1
        else:
            count[each] = 1

    for each in s2:
        if each in count:
            count[each] -= 1
        else:
            count[each] = 1

    for k in count:
        if count[k] > 0:
            return False
        else:
            return True


class AnagramTest(object):
    @staticmethod
    def test(sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('ABC', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('AAbbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print "ALL TEST CASES PASSED"


# Run Tests
t = AnagramTest()
t.test(anagram)
t.test(anagram2)
t.test(anagram3)
