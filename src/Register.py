class Register:
    def __init__(self):
        self.registers = []

    def register_new_register(self, name, cd):
        self.registers.append(name)
        cd.add_name_in_registry(name)