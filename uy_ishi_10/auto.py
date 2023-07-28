# AVTO ombori
import json
import os


class Avto:
    FUEL_TYPES = ("gasoline", "gas", "disiel")
    TRANSMISSION = ("Automatic", "Manual", "Robot")

    brand = ""
    model = ""
    positon = ""
    color = ""
    year = ""
    fuel_type = ""
    milage = ""
    transmission = ""

    def __init__(self):
        pass

    def set_brand(self):
        brand = input("Brandni kiriting: ")
        self.brand = brand

    def set_model(self):
        model = input("modelni kiriting: ")
        self.model = model

    def set_positon(self):
        positon = input("positonni kiriting: ")
        self.positon = positon

    def set_color(self):
        color = input("colorni kiriting: ")
        self.color = color

    def set_year(self):
        year = input("yearni kiriting: ")
        self.year = year

    def set_fuel_type(self):
        fuel_type = input("fuel_typeni kiriting: (gasoline, gas, disiel) ")
        # if fuel_type not in self.FUEL_TYPES:
        #     print("Bunday fuel_type mavjud emas")
        #     self.set_fuel_type()
        self.fuel_type = fuel_type

    def set_milage(self):
        milage = input("milageni kiriting: ")
        self.milage = milage

    def set_transmission(self):
        transmission = input("transmissionni kiriting: (Automatic, Manual,Robot) ")
        # if transmission not in self.TRANSMISSION:
        #     print("Bunday transmission mavjud emas")
        #     self.set_transmission()
        self.transmission = transmission

    def save_auto(self):
        last_id = self.get_last_id() + 1
        with open(f"autos/{last_id}.json", "w") as file:
            auto = {
                "brand": self.brand,
                "model": self.model,
                "positon": self.positon,
                "color": self.color,
                "year": self.year,
                "fuel_type": self.fuel_type,
                "milage": self.milage,
                "transmission": self.transmission,
            }
            json.dump(auto, file)
    def list(self):
        dir_list = os.listdir("autos/")
        for i in range(1 , len(dir_list) + 1):
            with open(f"autos/{i}.json", "r") as file:
                l = json.load(file)
            print(f"N{i}{l}")

    def delete(self):
        try:
            s = int(input(" ID kiriting : "))
            with open(f"autos/{s}.json", "r") as file:
                l = json.load(file)
            l= {}
                    
            with open(f"autos/{s}.json" ,  "w") as filew:
                json.dump(l, filew)
            print(f"N{s} deleted")
        except ValueError:
            print("Id topilmadi koroche")
            self.delete()

    def get_last_id(self):
        dir_list = os.listdir("autos/")
        numbers = [0]
        for dir in dir_list:
            if dir.endswith(".json") and dir.split(".")[0].isdigit():
                numbers.append(int(dir.split(".")[0]))
        return max(numbers)
    import json

def change_json_file(file_path, key_to_change, new_value):
    with open(file_path, 'r') as file:
        data = json.load(file)

    data[key_to_change] = new_value

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def change():
    road = input('Please enter the file name that you want to change : ')
    file_path = f'C:/Najot_talim/uy_ishi_10/autos/{road}'
    with open(file_path, 'r') as file:
        current_data = json.load(file)
        print("Current Data in the JSON file:")
        print(json.dumps(current_data, indent=4))
    key_to_change = input("Enter the key you want to change: ")
    new_value = input(f"Enter the new value for '{key_to_change}': ")

    change_json_file(file_path, key_to_change, new_value)


    with open(file_path, 'r') as file:
        updated_data = json.load(file)
        print("\nUpdated Data in the JSON file:")
        print(json.dumps(updated_data, indent=4))



while True:
    command = input("Kommandani kiriting: ")

    if command == "/change":
        change()

    if command == "/delete":
        avto = Avto()
        avto.delete()
    if command == "/exit":
        break
    if command == "/list":
        avto = Avto()
        avto.list()
    if command == "/new":
        avto = Avto()
        avto.set_brand()
        avto.set_model()
        avto.set_positon()
        avto.set_color()
        avto.set_year()
        avto.set_fuel_type()
        avto.set_milage()
        avto.set_transmission()

        avto.save_auto()
