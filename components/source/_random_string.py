def get_random_string(length):
    import random
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    global result_str
    result_str = ''.join(random.choice(letters) for i in range(length))