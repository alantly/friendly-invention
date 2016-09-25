def odd_or_even(x):
    return (x & 1) == 0

def nth_bit_set(x,n):
    return x & (1 << n)

def set_nth_bit(x,n):
    return x | (1 << n)

def unset_nth_bit(x,n):
    return x & ~(1 << n)

def toggle_nth_bit(x,n):
    return x ^ (1 << n)

def turn_off_rightmost_one(x):
    return x & (x - 1)

def propogate_rightmost_one(x):
    return x | (x - 1)

def isolate_rightmost_one(x):
    return x & (-x)

def isolate_rightmost_zero(x):
    return ~x & (x+1)

def turn_on_rightmost_zero(x):
    return x | (x + 1)
