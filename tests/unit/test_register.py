
import pytest
from src.Register import Register


@pytest.mark.Unit
def test_add_name_in_registry(mocker):
  register = Register()
  name = "Jesus"
  cd = mocker.Mock()
  register.register_new_register(name,cd)

  assert "Jesus" in register.registers