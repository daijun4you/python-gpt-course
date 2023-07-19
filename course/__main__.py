import sys
import importlib


def main():
    if len(sys.argv) < 3:
        return

    module = importlib.import_module(sys.argv[1] + "." + sys.argv[2])
    module.main()


if __name__ == "__main__":
    main()
