import hashlib
def creathash(str):
    hash1=hashlib.md5()
    hash1.update(str)
    return int(hash1.hexdigest(),16)
