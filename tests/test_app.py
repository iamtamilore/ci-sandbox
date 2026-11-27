from app.main import main


def test_greet(capsys) -> None:
    main()
    assert capsys.readouterr().out.strip() == "hello world"
