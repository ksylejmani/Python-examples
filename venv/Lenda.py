class lenda:
    """Ky shembull ka si qellim te gjeneroj kodin e nje lende"""
    kodi_aktual = 100

    def __init__(self):
        lenda.kodi_aktual += 1
        self.kodi = lenda.kodi_aktual

    def merre_kodin(self):
        return self.kodi


if __name__ == '__main__':
    lista_kodeve = []
    for i in range(10):
        lista_kodeve.append(lenda())
    for k in lista_kodeve:
        print(k.merre_kodin(), end=' ')
    print()
