def sum_digits_rec(n):
    return n % 10 + (sum_digits_rec(n // 10) if n >= 10 else 0)
