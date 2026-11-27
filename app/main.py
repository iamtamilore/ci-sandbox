"""A tiny application with a realistic missing standard-library import."""


def main() -> None:
    print(Path("greeting.txt").read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    main()
