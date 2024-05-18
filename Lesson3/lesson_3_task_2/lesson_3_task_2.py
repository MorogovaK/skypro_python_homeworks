from smartpfone import Smartpfone

catalog = []
phone1 = Smartpfone('Xiaomi','12 Lite', '+79634852345')
phone2 = Smartpfone('Apple','iPhone 15 Pro Max', '+79124567899')
phone3 = Smartpfone('Samsung','Galaxy A34', '+79194561234')
phone4 = Smartpfone('HONOR','X9b', '+79519201234')
phone5 = Smartpfone('OPPO','Reno 11', '+79091236784')

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.phone_number}')