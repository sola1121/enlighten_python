import hashlib

def md5(info):
    md = hashlib.md5()
    md.update(info.encode("utf8"))
    return md.hexdigest()
