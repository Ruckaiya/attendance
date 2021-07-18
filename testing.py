# import random
# import string

# def generate_key(length):
#     return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# print(generate_key(20))


import datetime
add_time = datetime.timedelta(minutes=2)
print(datetime.datetime.now() )
print(datetime.datetime.now() + add_time)
print(add_time)
print(add_time.days)