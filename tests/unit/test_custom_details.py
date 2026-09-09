import pytest
from src.custom_details import custom_details


@pytest.mark.Unit
def test_add_name_in_registry():

    cd = custom_details()

    cd.add_name_in_registry("Jens von laxnacke")

    assert "Jens von laxnacke" in cd.registry