def get_data():
    with open('names.txt') as f:
        names = f.read()
        names = names.split()
    return names


if __name__ == '__main__':
    print(get_data())