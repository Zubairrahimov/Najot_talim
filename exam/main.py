import json
import uuid
from typing import List, Dict
from contextlib import contextmanager

class CarStorage:
    def __init__(self, filename: str):
        self.filename = filename
        self.data = self._load_data()

    def _load_data(self) -> Dict:
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent =4)

    def add_car(self, car: Dict):
        car_id = str(uuid.uuid4())[:8]
        self.data[car_id] = car
        self._save_data()
        return car_id

    def update_car(self, car_id: str, key: str, value: str):
        if car_id in self.data:
            self.data[car_id][key] = value
            self._save_data()
        else:
            print("Vehicle Not Found")

    def delete_car(self, car_id: str):
        if car_id in self.data:
            del self.data[car_id]
            self._save_data()
        else:
            print("Vehicle Not Found")

    def list_cars(self):
        for car_id, car_info in self.data.items():
            print(f"{car_id}. {car_info['brand']} {car_info['model']} {car_info['year']}")

    def search_cars(self, brand: str, model: str, year: str) -> List[Dict]:
        results = []
        for car_id, car_info in self.data.items():
            if (
                car_info['brand'] == brand
                and car_info['model'] == model
                and car_info['year'] == year
            ):
                results.append(car_info)
        return results

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._save_data()

def main():
    with CarStorage('car_storage.json') as storage:
        while True:
            print("Menu:")
            print("1. Add new car")
            print("2. Change car information")
            print("3. Delete car")
            print("4. List cars")
            print("5. Search cars")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                brand = input("Brand: ")
                model = input("Model: ")
                position = input("Position: ")
                color = input("Color: ")
                year = input("Year: ")
                fuel_type = input("Fuel type: ")
                mileage = input("Mileage: ")
                transmission = input("Transmission: ")
                car_id = storage.add_car({
                    'brand': brand,
                    'model': model,
                    'position': position,
                    'color': color,
                    'year': year,
                    'fuel_type': fuel_type,
                    'mileage': mileage,
                    'transmission': transmission
                })
                print(f"New car added with ID: {car_id}")

            elif choice == '2':
                car_id = input("Enter car ID: ")
                key = input("Enter property to change: ")
                value = input(f"Enter new {key}: ")
                storage.update_car(car_id, key, value)

            elif choice == '3':
                car_id = input("Enter car ID: ")
                storage.delete_car(car_id)

            elif choice == '4':
                storage.list_cars()

            elif choice == '5':
                brand = input("Enter brand: ")
                model = input("Enter model: ")
                year = input("Enter year: ")
                results = storage.search_cars(brand, model, year)
                if results:
                    print("Search results:")
                    for result in results:
                        print(result)
                else:
                    print("No matching cars found.")

            elif choice == '6':
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
