from app.password.password import Password
from app.requeriments.additions.additions import Additions
import re


class UpperCaseLetters(Additions):
    def __init__(self, password: Password):
        super().__init__(password)

    def _get_number_of_uppercase_letters(self):
        contador = 0
        lista = re.findall('[A-Z]+', self._password)
        for dado in lista:
            contador += len(dado)
        return contador
