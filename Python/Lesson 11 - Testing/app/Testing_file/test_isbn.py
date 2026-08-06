from isbn import validate_isbn


def test_validate_isbn():
    result = validate_isbn("978-1-4028-9462-6")

    assert result == True


    