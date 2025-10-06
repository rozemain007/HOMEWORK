from smartphone import Smartphone

catalog = [
    Smartphone("Samsung","S24Ultra", "+798588785549" ),
    Smartphone("Honor", "X^c", "+79171478899"),
    Smartphone("Huawei", "nova 13i", "+79878889997"),
    Smartphone("Xiaomi", "Redmi A5", "+79875566778"),
    Smartphone("FRBBY", "4/128", "+79174747337")
]

for smartphone in catalog:
    print(f"{smartphone.brand}-{smartphone.model}.{smartphone.number_phone}")