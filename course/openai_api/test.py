from configs import conf


def main():
    print(conf.get("api_key"))


if __name__ == "__main__":
    main()
