class Computer:
    def __init__(self, brand):
        self.brand = brand
        self.__os = None
    def __install_os(self , os_name):
        self.__os = os_name
    def install_os(self, os_name):
        self.__install_os(os_name)


computer = Computer("Dell")
computer.install_os(os_name="Windows 8.1")
print(computer._Computer__os)

