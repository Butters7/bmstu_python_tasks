import hashlib

class AuthentificationSystem:
    def __init__(self, filename):
        self.filename = filename

    
    def add_new_user(self, username, password):
        with open(self.filename, 'a') as file:
            secret_password = hashlib.sha512(password.encode('utf-8')).hexdigest()
            file.write(f'{username}:{secret_password}\n')

    def auth(self, username, password):
        with open(self.filename, 'r') as file:
            for object in file:
                current_username, current_password = object.strip().split(':')
                hash_password = hashlib.sha512(password.encode('utf-8')).hexdigest()
                if username == current_username and hash_password == current_password:
                    return True
        return False
    
    def change_password(self, username, old_password, new_password):
        with open(self.filename, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for object in lines:
                current_username, current_password = object.strip().split(':')
                if username == current_username:
                    hash_old_password = hashlib.sha512(old_password.encode('utf-8')).hexdigest()
                    if hash_old_password == current_password:
                        hash_new_password = hashlib.sha512(new_password.encode('utf-8')).hexdigest()
                        file.write(f'{username}:{hash_new_password}\n')
                        return True
                file.write(object)
            file.truncate()
        return False


auth = AuthentificationSystem('db.txt')
auth.add_new_user('bones', 'qwerty123')

is_auth = auth.auth('bones', 'qwerty123')
print(is_auth)

is_not_auth = auth.auth('mgk', 'sha512')
print(is_not_auth)

can_change = auth.change_password('bones', 'qwerty123', 'qwerty1337')
print(can_change)
