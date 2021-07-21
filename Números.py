#%%
import re


class Número:
    def __init__(self, número):
        self.padrão = "([0-9]{2})?([0-9]{2})?([0-9])?([0-9]{4})([0-9]{4})"
        if self.número_é_válido(número):
            self._número = número
        else:
            raise ValueError("NÚMERO INVÁLIDO!")

    def número_é_válido(self, número):
        return re.findall(self.padrão, número)

    def __str__(self):
        return self.número_formatado()

    def número_formatado(self):
        resultado = re.search(self.padrão, self._número)
        tamanho_resultado = len(resultado.group())
        if tamanho_resultado == 13:
            return f"+{resultado.group(1)}({resultado.group(2)}){resultado.group(3)}{resultado.group(4)}-{resultado.group(5)}"
        elif tamanho_resultado == 11:
            return f"+55({resultado.group(1)}){resultado.group(3)}{resultado.group(4)}-{resultado.group(5)}"
        elif tamanho_resultado == 9:
            return f"+55(73){resultado.group(3)}{resultado.group(4)}-{resultado.group(5)}"
        elif tamanho_resultado == 8:
            return f"+55(73)9{resultado.group(4)}-{resultado.group(5)}"
