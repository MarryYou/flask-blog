from hashlib import md5

def create_md5(pwd,salt):
    md5_obj = md5()
    md5_obj.update((pwd+salt).encode('utf-8'))
    return md5_obj.hexdigest()

def create_salt(username):
    salt_obj = md5()
    salt_obj.update(username.encode('utf-8'))
    return salt_obj.hexdigest()    