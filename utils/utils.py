import hashlib
import time


def gen_unique_id():
    return hashlib.md5((time.time_ns()).to_bytes(16, 'big')).hexdigest()[:7]
