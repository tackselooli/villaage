def test_property_str(property_fixture):
    """Test the property model string representation"""
    assert property_fixture.__str__() == f"{property_fixture.title}"
