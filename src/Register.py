class Register:
    def __init__(self):
        self.registers = []


    def register_new_register(self, member, cd):
        self.registers.append(member)
        cd.add_name_in_registry(member)