
from files_manager_function import dir, catal

def test_dir():
    assert dir() == ['.git', '.idea', 'bithday.py', 'files_manager.py', 'myfunctions.py', 'sdf', 'testing', 'use_function.py', 'venv', 'viktorina.py', '__pycache__']


def test_catal():
    assert catal() == ['.git', '.idea', 'bithday.py', 'files_manager.py', 'files_manager_function.py', 'myfunctions.py', 'sdf', 'testing', 'use_function.py', 'venv', 'viktorina.py', '__pycache__']