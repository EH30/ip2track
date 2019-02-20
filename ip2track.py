import os
import sys
import geoip2.database

if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")
elif sys.platform == "darwin":
    os.system("clear")
else:
    print ("Unknown System")


user_ip = raw_input("\033[1;32mIP: \033[1;m")
geo_tracker = geoip2.database.Reader("GeoLite2-City_20190212/GeoLite2-City.mmdb")

coder = geo_tracker.city(user_ip)

country = coder.country.name
iso_code = coder.country.iso_code
city = coder.city.name
postal_code = coder.postal.code
latitude = coder.location.latitude
longitude = coder.location.longitude


info = """\033[1;32m
country: {0}
country code: {1}
city: {2}
postal code: {3}
latitude: {4}
longitude: {5}\033[1;m
""".format(country, iso_code, city, postal_code, latitude, longitude)


print (info)
geo_tracker.close()
