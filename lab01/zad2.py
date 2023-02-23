def validParameterForBitCount(param):
    if not float(param).is_integer():
        return 'To nie jest liczba całkowita'
    else:
        return int(param).bit_count()


if __name__ == '__main__':
    print(validParameterForBitCount(31.0))