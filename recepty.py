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
        
        tt = ', '.join([tag.label for tag in self.tags])

        return f'{self.label} patri do: {tt} - potrebujeme {r}'

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
        r = ', '.join(it.label for it in self.receipts)
        return f'{self.label} je potreba pro: {r}'

c_breakfast = Course('snidane')
c_lunch = Course('obed')
c_dinner = Course('vecere')

t_vegetarian = Tag('vegetarianske')
t_sweet = Tag('sladky pokrm')

u_kg = Unit('kg')
u_l = Unit('l')
u_pcs = Unit('ks')
u_g = Unit('g')

rice = Ingredience('ryze', u_kg)
milk = Ingredience('mleko', u_l)
butter = Ingredience('maslo', u_kg)
apple = Ingredience('jablko', u_kg)
sugar_crystal = Ingredience('cukr krystal', u_kg)
semolina = Ingredience('krupice', u_kg)
salt = Ingredience('sul', u_g)
egg = Ingredience('vejce', u_pcs)
roll = Ingredience('rohlik', u_pcs)
cinnamon = Ingredience('skorice', u_g)


ryzak = Receipt('nakyp', c_lunch)
ryzak.add_ing(rice, 0.5)
ryzak.add_ing(milk, 1)
ryzak.add_ing(butter, 0.02)
ryzak.add_ing(apple, 0.5)
ryzak.add_ing(sugar_crystal, 0.2)
ryzak.add_tag(t_vegetarian)
ryzak.add_tag(t_sweet)

zemlbaba = Receipt('zemlovka', c_lunch)
zemlbaba.add_ing(milk, 1.5)
zemlbaba.add_ing(roll, 10)
zemlbaba.add_ing(sugar_crystal, 0.6)
zemlbaba.add_ing(cinnamon, 5)
zemlbaba.add_ing(egg, 2)
zemlbaba.add_ing(butter, 0.02)
zemlbaba.add_ing(apple, 2)
zemlbaba.add_tag(t_vegetarian)
zemlbaba.add_tag(t_sweet)

krupicna_kase = Receipt('krupicna kase', c_breakfast)
krupicna_kase.add_ing(milk, 0.5)
krupicna_kase.add_ing(butter, 0.04)
krupicna_kase.add_ing(semolina,0.02)
krupicna_kase.add_ing(salt, 3)
krupicna_kase.add_tag(t_vegetarian)
krupicna_kase.add_tag(t_sweet)

print(krupicna_kase)
print(ryzak)
print(zemlbaba)
print(milk.print_all_receipts())
