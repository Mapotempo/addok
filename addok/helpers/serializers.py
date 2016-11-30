import zlib
import marshal


class Compressed:

    @classmethod
    def dumps(cls, data):
        return zlib.compress(marshal.dumps(data))

    @classmethod
    def loads(cls, data):
        return marshal.loads(zlib.decompress(data))
