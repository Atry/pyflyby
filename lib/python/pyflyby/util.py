
from __future__ import absolute_import, division, with_statement

class cached_attribute(object):
    '''Computes attribute value and caches it in instance.

    Example:
        class MyClass(object):
            @cached_attribute
            def myMethod(self):
                # ...
    Use "del inst.myMethod" to clear cache.'''
    # http://code.activestate.com/recipes/276643/

    def __init__(self, method, name=None):
        self.method = method
        self.name = name or method.__name__

    def __get__(self, inst, cls):
        if inst is None:
            return self
        result = self.method(inst)
        setattr(inst, self.name, result)
        return result

def stable_unique(items):
    """
    Return a copy of C{items} without duplicates.  The order of other items is
    unchanged.

      >>> stable_unique([1,4,6,4,6,5,7])
      [1, 4, 6, 5, 7]
    """
    result = []
    seen = set()
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result

def longest_common_prefix(items1, items2):
    """
    Return the longest common prefix.

      >>> longest_common_prefix("abcde", "abcxy")
      'abc'

    @rtype:
      C{type(items1)}
    """
    n = 0
    for x1, x2 in zip(items1, items2):
        if x1 != x2:
            break
        n += 1
    return items1[:n]


Inf = float('Inf')
