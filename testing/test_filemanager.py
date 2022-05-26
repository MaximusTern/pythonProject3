from new_function.filemanager import filenames


def test_filenames():
    assert filenames() == ['tests.py', 'test_filemanager.py', 'test_file_curator_function.py', 'test_file_manager.py']



