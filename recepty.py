class Tag:
    def __init__(self, label) -> None:
        self.label = label

    def __str__(self) -> str:
        return self.label

class Course:
    def __init__(self, label) -> None:
        self.label = label

    def __str__(self) -> str:
        return self.label

class Unit:
    def __init__(self, label) -> None:
        self.label = label

    def __str__(self) -> str:
        return self.label

class Receipt:
    def __init__(self, label: str, course: Course) -> None:
        self.label = label
        self.course = course
        self.tags = []
        self.ing = {}

    def add_tag(self, tag):
        self.tags.append(tag)

    def add_ing(self, ing, amount):
        self.ing[ing.label] = [ing, amount]
        ing.add_receipt(self)

    def __str__(self) -> str:
        r = ''
        for k, v in self.ing.items():
            r += f'{v[1]}[{v[0].unit.label}] {v[0]}, '
        
        return f'{self.label} - potrebujeme {r}'

class Ingredience:
    def __init__(self, label, unit: Unit) -> None:
        self.label = label
        self.unit = unit
        self.receipts = []

    def __str__(self) -> str:
        return self.label

    def add_receipt(self, receipt: Receipt):
        self.receipts.append(receipt)

    def print_all_receipts(self):
        r = f'{self.label} je potreba pro: '
        for item in self.receipts:
            r += item.label + ', '

        return r

c_breakfast = Course('snidane')
c_lunch = Course('obed')
c_dinner = Course('vecere')

t_vege = Tag('vege')

u_kg = Unit('kg')
u_l = Unit('l')
u_pcs = Unit('ks')

rice = Ingredience('ryze', u_kg)
milk = Ingredience('mleko', u_l)
butter = Ingredience('maslo', u_kg)

ryzak = Receipt('nakyp', c_lunch)
ryzak.add_ing(rice, 0.2)
ryzak.add_ing(milk, 0.4)
ryzak.add_ing(butter, 0.04)

print(ryzak)


krupicna_kase = Receipt('krupicna kase', c_breakfast)
krupicna_kase.add_ing(milk, 0.4)
krupicna_kase.add_ing(butter, 0.04)

print(krupicna_kase)

print(milk.print_all_receipts())
