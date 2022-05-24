from  new_function.filemanager import filenames, author_info

def test_filenames():
    assert filenames() == ['tests.py', 'test_file_curator_function.py', 'test_file_manager.py']

def test_author_info():
    assert author_info() == 'Leonid Orlov'
