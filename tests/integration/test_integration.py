import pytest
from src.Register import Register
from src.custom_details import custom_details

@pytest.mark.integration
def test_registers_added_name_in_registry():
    register = Register()
    cd = custom_details()

    register.register_new_register("Donald Obama", cd)

    assert "Donald Obama" in register.registers
    assert "Donald Obama" in cd.registry