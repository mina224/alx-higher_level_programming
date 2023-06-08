#!/usr/bin/python3
# (4-hidden_discovery.py)

"""prints all the names defined by the compiled module hidden_4.pyc"""

if __name__ == "__main__":
    import hidden_4
    for j in dir(hidden_4):
        if not j.startswith("__"):
            print("{:s}".format(j))
