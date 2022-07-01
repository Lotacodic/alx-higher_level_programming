#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)  # dir() returns the list of names a module defines
    for x in names:
        if x[:2] != "__":
            print(x)
