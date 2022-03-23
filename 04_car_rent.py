class Car:
    def __init__(self,licence_plate, model, kms):
        self.licence_plate = licence_plate
        self.model = model
        self.kms = kms
        self.is_avaliable = True

    def rent(self):
        if self.is_avaliable:
            self.is_avaliable = False
            return "Potvrzuji zapůjčení vozidla"
        else:
            return "Vozidlo není k dispozici"
    
    def return_car(self, kms_new, rental_period):
        self.is_avaliable = True
        self.kms = kms_new
        if rental_period < 7:
            price = 400 * rental_period   
        else:
            price = 300 * rental_period
        return f'cena za pujceni je {price}'

    def get_info(self):
        return f'{self.licence_plate} - {self.model} - {self.kms}'
    
    def __str__(self):
        return self.get_info()
  
peugeot = Car('4A2 3020','Peugeot 403 Cabrio', 47534)
oktavka = Car('1P3 4747', 'Škoda Octavia', 41253)

while True:
    user_choice = input('Jakou znacku auta si preje zvolit, Škoda nebo Peugeot? ')
    if user_choice.lower() == 'škoda' or user_choice.lower() == 'skoda':
        user_choice = oktavka
        break
    elif user_choice.lower() == 'peugeot': 
        user_choice = peugeot
        break
    else:
        print('Takove auto nemame, vyberte si prosim Škoda nebo Peugeot')



print(str(user_choice))
print(user_choice.rent())
print(user_choice.return_car(50000,4))
print(user_choice.get_info())
print(user_choice.rent())
print(user_choice.rent())
print(user_choice.return_car(55000,8))
print(user_choice.get_info())