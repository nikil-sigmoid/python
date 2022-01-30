def car_info(manufacturer, model_name, **other_information):
    car = {
        'manufacturer': manufacturer,
        'model_name': model_name,
        'misc_info': other_information
    }
    return car


car_details = car_info('tesla', 's', color='white', type='sedan', vehicle_power='battery')

print(f"Manufacturer: {car_details['manufacturer']}")
print(f"Model_name: {car_details['model_name']}")
for k,v in car_details['misc_info'].items():
    print(f"{k}: {v}")
# print(f"Car Color: {car_details['misc_info']['color']}")
# print(f"Car Type: {car_details['misc_info']['type']}")
# print(f"Vehicle Power: {car_details['misc_info']['vehicle_power']}")
