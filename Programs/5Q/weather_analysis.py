weather_data = [
    {"date": "2024-08-01", "max_temp": 31, "min_temp": 22, "humidity": 60},
    {"date": "2024-08-02", "max_temp": 30, "min_temp": 21, "humidity": 58},
    {"date": "2024-08-03", "max_temp": 29, "min_temp": 20, "humidity": 65},
    {"date": "2024-08-04", "max_temp": 32, "min_temp": 23, "humidity": 63},
    {"date": "2024-08-05", "max_temp": 33, "min_temp": 24, "humidity": 67},
    {"date": "2024-08-06", "max_temp": 34, "min_temp": 25, "humidity": 70},
    {"date": "2024-08-07", "max_temp": 35, "min_temp": 26, "humidity": 72},
    {"date": "2024-08-08", "max_temp": 36, "min_temp": 27, "humidity": 74},
    {"date": "2024-08-09", "max_temp": 37, "min_temp": 28, "humidity": 75},
    {"date": "2024-08-10", "max_temp": 38, "min_temp": 29, "humidity": 77},
]

def find_highest_and_lowest_temperatures(data):
    highest_temp = max(data, key=lambda x: x["max_temp"])
    lowest_temp = min(data, key=lambda x: x["min_temp"])
    return highest_temp["max_temp"], lowest_temp["min_temp"]

def count_days_above_30(data):
    count = sum(1 for day in data if day["max_temp"] > 30)
    return count

def compute_average_humidity(data):
    total_humidity = sum(day["humidity"] for day in data)
    average_humidity = total_humidity / len(data)
    return average_humidity

highest_temp, lowest_temp = find_highest_and_lowest_temperatures(weather_data)
print(f"Highest temperature recorded: {highest_temp}°C")
print(f"Lowest temperature recorded: {lowest_temp}°C")

days_above_30 = count_days_above_30(weather_data)
print(f"Number of days with temperatures above 30°C: {days_above_30}")

average_humidity = compute_average_humidity(weather_data)
print(f"Average humidity: {average_humidity:.2f}%")
