# Construisez une classe Orao dont les attributs d'instances sont la quantite de
# sucre et la quantite de chocolat ainsi que si le biscuit est Rao Compliant.
# L'attribut Rao Compliant doit etre optionnel et vrai par defaut.

# Construisez egalement un classe representant une boite de biscuits Orao. La
# methode fill place un biscuit Orao dans une des rangees.

# Si vous vous sentez braves, construisez un decorateur inject_serum a la
# methode fill. Ce decorateur injectera un serum de compliance et s'assurera que
# le Orao est conforme avant de le placer dans la boite.


def inject_serum(func):
    def func_wrapper(self, row, cookie):
        cookie.rao_compliant = True
        return func(self, row, cookie)
    return func_wrapper


class OraoBox(object):
    rows = [[], [], []]

    @inject_serum
    def fill(self, row, cookie):
        if len(self.rows[row]) > 12:
            self.rows[row].append(cookie)
            return True
        else:
            return False


class Orao(object):

    def __init__(self, sugar_qtt, chocolate_qtt, rao_compliant=True):
        self.sugar_qtt = sugar_qtt
        self.chocolate_qtt = chocolate_qtt
        self.rao_compliant = rao_compliant

    def eat(self):
        self.sugar_qtt = self.sugar_qtt / 2
        self.chocolate_qtt = self.chocolate_qtt / 2


def main():
    cookie = Orao(200.0, 500.0, rao_compliant=False)
    box = OraoBox()
    box.fill(0, cookie)
    # print cookie.rao_compliant


if __name__ == '__main__':
    main()