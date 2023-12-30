import csv
from decimal import Decimal
from collections import namedtuple

# Define your named tuple
Row = namedtuple('Row', ['SNo', 'clouds_all', 'date', 'day', 'holiday', 'hour', 'month', 'rain_1h', 'snow_1h', 'temp', 'time', 'traffic_volume', 'weather_description', 'weather_main', 'year'])

# Create a list of named tuples
data = [
    Row(SNo=4317, clouds_all=90, date='2013-03-16', day=16, holiday=0, hour=6, month=3, rain_1h=Decimal('0.0'), snow_1h=Decimal('0.0'), temp=Decimal('272.63'), time='06:00:00', traffic_volume=1329, weather_description=17, weather_main=8, year=2013),
    Row(SNo=35262, clouds_all=20, date='2017-07-11', day=11, holiday=0, hour=19, month=7, rain_1h=Decimal('0.0'), snow_1h=Decimal('0.0'), temp=Decimal('302.08'), time='19:00:00', traffic_volume=3367, weather_description=4, weather_main=0, year=2017),
    Row(SNo=25269, clouds_all=90, date='2016-07-27', day=27, holiday=0, hour=2, month=7, rain_1h=Decimal('0.0'), snow_1h=Decimal('0.0'), temp=Decimal('296.32'), time='02:00:00', traffic_volume=341, weather_description=2, weather_main=0, year=2016),
    Row(SNo=39433, clouds_all=90, date='2017-12-03', day=3, holiday=0, hour=11, month=12, rain_1h=Decimal('0.0'), snow_1h=Decimal('0.0'), temp=Decimal('276.57'), time='11:00:00', traffic_volume=4113, weather_description=2, weather_main=0, year=2017),
    Row(SNo=3372, clouds_all=44, date='2013-02-05', day=5, holiday=0, hour=13, month=2, rain_1h=Decimal('0.0'), snow_1h=Decimal('0.0'), temp=Decimal('261.27'), time='13:00:00', traffic_volume=4811, weather_description=0, weather_main=0, year=2013),
    Row(SNo=37032, clouds_all=1, date='2017-09-09', day=9, holiday=0, hour=23, month=9, rain_1h=Decimal('0.0'), snow_1h=Decimal('0.0'), temp=Decimal('291.5'), time='23:00:00', traffic_volume=2026, weather_description=3, weather_main=1, year=2017),
    Row(SNo=14340, clouds_all=90, date='2014-05-15', day=15, holiday=0, hour=4, month=5, rain_1h=Decimal('0.0'), snow_1h=Decimal('0.0'), temp=Decimal('277.82'), time='04:00:00', traffic_volume=823, weather_description=2, weather_main=0, year=2014),
    Row(SNo=18417, clouds_all=1, date='2015-09-19', day=19, holiday=0, hour=16, month=9, rain_1h=Decimal('0.0'), snow_1h=Decimal('0.0'), temp=Decimal('293.29'), time='16:00:00', traffic_volume=4578, weather_description=3, weather_main=1, year=2015),
    Row(SNo=1584, clouds_all=90, date='2012-11-30', day=30, holiday=0, hour=18, month=11, rain_1h=Decimal('0.0'), snow_1h=Decimal('0.0'), temp=Decimal('273.88'), time='18:00:00', traffic_volume=5420, weather_description=2, weather_main=0, year=2012),
    Row(SNo=7034, clouds_all=88, date='2013-06-16', day=16, holiday=0, hour=16, month=6, rain_1h=Decimal('12.19'), snow_1h=Decimal('0.0'), temp=Decimal('293.65'), time='16:00:00', traffic_volume=4271, weather_description=14, weather_main=7, year=2013)
]

# Specify the CSV file path
csv_file_path = 'output.csv'

# Write named tuples to CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write header
    writer.writerow(Row._fields)
    
    # Write data
    for row in data:
        writer.writerow(row)