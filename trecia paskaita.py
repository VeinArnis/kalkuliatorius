# Nr1
asd = int(input("Iveskite sveikaji skaiciu: "))
ar_skaicius_teigiamas = True
if asd > 0:
    print(ar_skaicius_teigiamas)
else:
    asd -= 0
    ar_skaicius_teigiamas = False
    print(ar_skaicius_teigiamas)

# Nr2
import datetime

laikas = datetime.datetime.today()
z = datetime.datetime.strftime(laikas, "%Y %m %d, %H:%M:%S")
print(laikas)
print(laikas - datetime.timedelta(days=5))
print(laikas + datetime.timedelta(hours=8))
print(z)

# Nr3
ivesta_data = input("Iveskite data: ")
data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d %H:%M:%S")
skirtumas = (datetime.datetime.now() - data)
print(skirtumas.days / 365)                  # years
print(skirtumas.days * 0.0328549112)         # months
print(skirtumas.days)                        # days
print(skirtumas.total_seconds() / 3600)      # hours
print(skirtumas.days * 1440)                 # minutes
print(skirtumas.total_seconds())             # seconds
