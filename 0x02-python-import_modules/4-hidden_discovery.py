#!/usr/bin/python3
if __name__ == "__main__":
    # Importing the compiled python file
    import hidden_4

    # Looping through all the names inside hidden_4 python file
    for name in dir(hidden_4):
        if name[:2] != "__":
            print("{:s}".format(name))
