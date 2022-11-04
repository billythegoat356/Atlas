import random
from base64 import b64encode
from zlib import compress


# https://github.com/CSM-BlueRed

# <3





def _encrypt(stream: bytes) -> tuple[bytes, bytes]:
    key = bytes(random.choices(range(255 + 1), k = len(stream)))
    return bytes(kc ^ sc for kc, sc in zip(key, stream)), key


def encrypt(content):

    crypted, key = _encrypt(content)
    readable_key = b64encode(compress(key)).decode()

    crypt_my_repl_class = r'''
class CryptMyRepl:
    key = key
    stream = stream
'''[1:-1]

    script = [
        r'''# Made with https://github.com/billythegoat356/Atlas\n\n# <3\n\n\n'''
        r'''import os, base64, zlib''',
        r'''key: bytes = zlib.decompress(base64.b64decode(os.getenv('ENCRYPTION_KEY').encode()))''',
        r'''stream: bytes = zlib.decompress({!r})'''.format(compress(crypted)) + '\n',
        crypt_my_repl_class,
        r'''exec(bytes(kc ^ sc for kc, sc in zip(key, stream)), {'CryptMyReplClass': CryptMyRepl})'''
    ]

    script = '\n'.join(script)


    return script, readable_key