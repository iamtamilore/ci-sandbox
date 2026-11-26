"""A tiny application used to produce real failed CI runs.

The import of app.helpers is deliberately broken, so every run of this
workflow fails. That failure is the input Build Doctor works on.
"""

from app.helpers import greet


def main() -> None:
    print(greet("world"))


if __name__ == "__main__":
    main()
