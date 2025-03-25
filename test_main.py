from main import add, main
import pytest

def test_add():
    assert add([]) == 0
    assert add(["1"]) == 1
    assert add(["1", "2", "3"]) == 6

def test_main(capsys):
    main(['main.py'])
    main(['main.py', '1'])
    main(['main.py', '1', '2', '3'])
    cap = capsys.readouterr()
    assert cap.out == '0\n1\n6\n'

