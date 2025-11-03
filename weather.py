# Weather Severity Project (Auto Test Version)

data_lines = [
    "0.2 25",
    "1.0 35",
    "4.5 45",
    "-1.0"
]

# Initialize totals and counter
total_rain = 0.0
total_wind = 0.0
count = 0
index = 0

# Read first input
rain_wind = data_lines[index].strip().split()
rain = float(rain_wind[0])

# Sentinel-controlled loop
while rain != -1.0:
    wind = float(rain_wind[1])
    total_rain += rain
    total_wind += wind
    count += 1
    index += 1
    rain_wind = data_lines[index].strip().split()
    rain = float(rain_wind[0])

# Output results
if count > 0:
    avg_rain = total_rain / count
    avg_wind = total_wind / count
    weather_severity = (avg_rain * 10) + avg_wind
    print(f"The average rain is {avg_rain:.1f} inches")
    print(f"The average wind is {avg_wind:.1f} mph")
    print(f"The weather severity for these {count} readings is: {weather_severity:.1f}")
else:
    print("No data entered.")
