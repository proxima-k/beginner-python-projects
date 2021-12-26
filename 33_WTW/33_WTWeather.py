# https://github.com/jorgegonzalez/beginner-projects#whats-the-weather
# Finished on 18 Apr 2020

import requests, json, webbrowser, datetime

# Requesting
api_key = 'xxx'
city_name = 'xxx'
r = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}', params={'units' : 'metric'})
json_formatted_str = json.dumps(r.json(), indent=2)

# Writing the html file for weathers
html_file = open('wtweather.html', 'w')
declaration = '''<!DOCTYPE html>
<html>
<head>
<title>Weather Forecast</title>
<link href="style.css" style="text/css" rel="stylesheet">
</style>
</head>
<body>
'''
html_file.write(declaration)
html_file.write(f'  <h1>< {r.json()["city"]["name"]}\'s Weather ></h1>\n')
html_file.write('  <h2>- A 5 day / 3 hour forecast -</h2>\n')
html_file.write('  <table>\n    <tr>\n')

# Writing Table headings for first row
html_file.write('<td></td>\n')
date_list = []
for p in r.json()['list']:
    year, month, day = map(int, p['dt_txt'].split()[0].split('-'))
    date = datetime.date(year, month, day)
    if str(date) not in date_list:
        day_name = date.strftime('%A')
        html_file.write(f"    <th>{p['dt_txt'].split()[0]}<br>{day_name}</th>\n")
        date_list.append(str(date))

# Writing each row
for i in range(0, 24, 3):
    # Writing the time -----------------------------|
    html_file.write('<tr>\n')
    hour = str(i)
    if len(hour) < 2:
        hour = "0" + hour
    tri_hourly_str = hour + ":00:00"
    html_file.write(f'<th>{tri_hourly_str}</th>\n')

    # Finding the periods in specific time ---------| Reason: To solve the table problem
    p_obj_list = []
    weather_obj = None
    for d in date_list:
        for p in r.json()['list']:
            if p['dt_txt'].split()[0] == d:
                if p['dt_txt'].split()[1] == tri_hourly_str:
                    weather_obj = p
                    break
                else:
                    weather_obj = None
        # time_dict[tri_hourly_str].append(weather_obj)
        p_obj_list.append(weather_obj)

    # Writing the weather for specific time ---------|
    for p_obj in p_obj_list:
        if p_obj == None:
            html_file.write('<td class="none">No data found</td>\n')
        else:
            html_file.write('<td>')
            html_file.write(f'  <p class="weather">Weather: {p_obj["weather"][0]["main"]}</p>\n')
            html_file.write(f'  <p class="temp">Temperature: {p_obj["main"]["temp"]}</p>\n')
            html_file.write(f'  <p>- High: {p_obj["main"]["temp_max"]}</p>\n')
            html_file.write(f'  <p>- Low: {p_obj["main"]["temp_min"]}</p>\n')
            html_file.write('</td>')

    html_file.write('</tr>\n')

closing = '''    </tr>
  </table>
</body>
</html>'''
html_file.write(closing)
html_file.close()

webbrowser.open_new_tab('wtweather.html')
