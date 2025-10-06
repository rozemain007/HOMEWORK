from adress import Adress
from mailing import Mailing

my_mail = Mailing(Adress("12345","Москва", "Московская", "15", "15"), Adress("12475", "Пермь", "Пермская","13", "11"), 1500, "POST1245")


print(f"Отправление {my_mail.track} из {my_mail.from_address.index},{my_mail.from_address.city},{my_mail.from_address.street},{my_mail.from_address.house} - {my_mail.from_address.apartament} в {my_mail.to_address.index},{my_mail.to_address.city},{my_mail.to_address.street},{my_mail.to_address.house}-{my_mail.to_address.apartament}. Стоимость {my_mail.cost} рублей ")