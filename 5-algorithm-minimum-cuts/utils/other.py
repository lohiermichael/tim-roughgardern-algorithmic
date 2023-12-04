def name_str(val, local_vars):
    for key, value in local_vars.items():
        if val == value:
            return key


if __name__ == "__main__":
    h = 1
    print(name_str(h, local_vars=locals()))
