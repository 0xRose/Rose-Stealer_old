def get_random_string(length):
    import random
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
