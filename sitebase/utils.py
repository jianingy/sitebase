class tag_memoize(object):

    def __init__(self, tag):

        self.tag = tag
        self.cache = {}

    def __call__(self, f):

        def decorated_function(*args):
            try:
                return self.cache[self.tag]
            except KeyError:
                val = f(*args)
                self.cache[self.tag] = val
                return val

        return decorated_function
