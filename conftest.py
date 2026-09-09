import pytest
from src.custom_details import custom_details
from src.Register import Register

@pytest.fixture
def test_register():
    return Register()