import pytest
from project import translate, filemanager, langcodestable


def main():
    test_translate()


def test_translate():
    assert translate("こんにちは兄！") == "Hello brother!"
    assert translate("ela unnaru?") == "How are you?"
    assert translate("hola mundo!") == "Hello World!"


def test_filemanager():
    with pytest.raises(SystemExit):
        filemanager("invalid.txt", None, "en", "ja", False)


def test_langcodestable():
    languages = {
        "English": "en",
    }
    assert (
        f"{langcodestable(languages)}"
        == "+----------+------+\n| Language | Code |\n+----------+------+\n| English  |  en  |\n+----------+------+"
    )


if __name__ == "__main__":
    main()
