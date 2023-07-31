import sys
import importlib


def main():
    argv_len = len(sys.argv)
    if argv_len < 3:
        return

    import_module = ""
    for i in range(1, len(sys.argv)):
        import_module += sys.argv[i] + "."
    import_module = import_module.strip("\.")

    module = importlib.import_module(import_module)
    module.run()


if __name__ == "__main__":
    main()
