from hashlib import sha256  # https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py


def create_hash(p):         # https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py       
    pw_bytestring = p.encode()
    return sha256(pw_bytestring).hexdigest()


password_hash = '401f83e57ce50aaa8d46d44f0303e10133188f618d616f25a36d8d90e7b50ece'
comments = []


# print(password_hash)


def print_comments():
    print("Previously entered comments")
    for i in range(len(comments)):
       print(str(i + 1) + "." + comments[i])


while True:
    comment = input("Enter your comment:")
    password = input("Enter your password:")
    new_hash_password = create_hash(password)
    # print(new_hash_password)
    if new_hash_password == password_hash:
        comments.append(comment)
        print_comments()
    else:
        print("I am sorry I can't let you do that")
