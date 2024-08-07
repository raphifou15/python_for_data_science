import time
import datetime
import calendar

# renvoie le temps actuel en secondes depuis le début de l'époque (epoch),
# qui est le 1er janvier 1970 à minuit UTC
seconds = time.time()

# Formate le nombre de secondes en notation scientifique avec
# deux chiffres après la virgule
science = "{:.2e}".format(seconds)

# Formate la valeur de seconds avec des séparateurs de milliers et 4 chiffres
# après la virgule
secondesFr = f"{seconds:,.4f}"
str = (
    f"Seconds since January 1, 1970: {secondesFr}"
    f"or {science} in scientific notation"
)

# Convertit le nombre de secondes écoulées depuis l'époque Unix
# en un objet datetime
date_time = datetime.datetime.fromtimestamp(seconds)
month_number = date_time.month
day_number = date_time.day
year_number = date_time.year

# recupere le nom du mois
month_name = calendar.month_name[month_number]
str2 = f"{month_name} {day_number} {year_number}"

print(str)
print(str2)


# print(time.ctime(seconds))
