import random
import time
import datetime
import string

root_path = "/home/daserk/Desktop/python3/arac_servis/"

dummy_name = root_path + "dummyDataSet" + time.strftime("%Y-%m-%d_%H-%M-%S")+ ".csv"

header = "tarih,plaka,marka,model,uretim_tarihi,km,parca_fiyat,iscilik_fiyat"

markalar = ["FORD","VOLKSWAGEN","VOLVO","MERCEDES","FIAT"]

#markalar.append("MAZDA")
modeller = { "FIAT":["EGEA","LINEA","SPIDER","FIORINO","DOBLO","MAREA","ALBEA"],
            "MERCEDES":["E200","C180","S600","S350","E250","A180"],
            "VOLKSWAGEN":["PASSAT","JETTA","GOLF","SCIROCCO","PHOETON","POLO"],
            "FORD":["FOCUS","MONDEO","KA","FIESTA","KUGA","ESCORT"],
            "VOLVO":["S40","S60","XC90","V40","V60","S90"]
            }

dizi = []
random.randint(2000,2019)

dosya = open(dummy_name,"w", encoding="UTF-8")
dosya.write(header+"\n")
for x in range(24000):
    marka = random.choice(markalar)
    model = random.choice(modeller[marka])
    #uretim_tari59hi=random.randint59(2000,2020)
    rplaka = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    plaka = random.randint(1,81)
    km = random.randint(1000,200000)
    parca_fiyat = random.randint(50,10000)
    iscilik_fiyat = random.randint(250,2000)
    start_date = datetime.date(2010, 1, 1)
    end_date = datetime.date(datetime.datetime.now().year,datetime.datetime.now().month, datetime.datetime.now().day)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    uretim_tarihi = random.randint(2000,random_date.year)
    #if(uretim_tarihi > random_date.year):
    #    uretim_tarihi = random.randint(2000,random_date.year)

    dosya.write(str(random_date)+"," + str(rplaka) + ","+str(marka)+","+str(model)+","+\
                str(uretim_tarihi)+ "," +str(km)+"," +str(parca_fiyat)+"," + \
                str(iscilik_fiyat) +  "\n")
dosya.close()
