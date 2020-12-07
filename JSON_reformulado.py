import json
import os


"""
Considere colocar o JSONStorage em um arquivo separado e importar
"""

class JSONStorage:
    def __init__(self, filename):
        self.data = None
        self.filename = filename
        self.load()

    def load(self):
        with open("inventario_json.json", "r") as arq_json:
            self.data = json.load(arq_json)

    def save(self):
        with open("inventario_json.json", "w") as arq_json:
            json.dump(self.data, arq_json)

"""
Considere colocar as bases/pai em um outro arquivo
"""

class OptionBase:
    option_label = None
    option_description = None

    @classmethod
    def action(cls):
        pass

class MenuNavigation:
    def __init__(self):
        self.option_not_found = "Opção não encontrada"
        self.exit_option = "3"  # considere sair com uma letra como "S" ou "Q"
        self.exit_label = "Para sair"
        self._options = {}

    def register_option(self, option):
        self._options[option.option_label] = option

    def show_options(self):
        print("Digite:")
        for option in self._options:
            print(f"< {self._options[option].option_label} > {self._options[option].option_description}")
        print(f"< {self.exit_option} > {self.exit_label}")

        option = input()
        return option

    def call_option(self, option):
        sel_option = self._options[option]
        sel_option.action()


    def run(self):
        while True:
            option = self.show_options()
            if option == self.exit_option:
                break
            try:
                self.call_option(option)
            except KeyError:
                print(self.option_not_found)

"""
Seu programa pincipal -> main.py
"""
json_storage = JSONStorage("inventario_json.json")


class RegisterOption(OptionBase):
    option_label = "1"
    option_description = "para registrar ativo"

    @classmethod
    def action(cls):
        resp = "S"
        while resp == "S":
            json_storage.data[input("Digite o número patrimonial:\n")] = [
                input("Digite a data da última atualização:\n"),
                input("Digite a descrição:\n"),
                input("Digite o departamento:\n")]
            resp = input("Digite <S> para continuar ou <N> para sair\n").upper()

        json_storage.save()
        print("JSON gerado!!!!")


class ShowItemsOption(OptionBase):
    option_label = "2"
    option_description = "para exibir ativos armazenados"

    @classmethod
    def action(cls):
        for chave, dado in json_storage.data.items():
            print(f"Data.........:{dado[0]}")
            print(f"Descrição....: {dado[1]}")
            print(f"Departamento.: {dado[2]}")


if __name__ == "__main__":
    main_menu = MenuNavigation()
    main_menu.register_option(RegisterOption)
    main_menu.register_option(ShowItemsOption)
    main_menu.run()

