import random

from uszipcode import SearchEngine
engine = SearchEngine()

years = [2019,2020,2021]
months = list(range(1, 13))
days = list(range(1, 29))
hours = list(range(9, 15))
minutes = list(range(0, 60))
seconds = list(range(0, 60))

fas = ["John Smith","Mary Shelly","Peter Williams","Nicro Brown", "Jay Miller", "David Lopez", "Jane Davis", "Cathy Jones"]

sites = ["3D","MSO","ETarde","External"]

actions = ["Account Name Search","Account Number Search","UOE megamenu launch","UOE 3D context launch","Trade"]


ny_zips = ["11530","11753","11030","11576","11946","10024","10023","10021","10007","10006"]
nj_zips = ["07010","07020","07050","07078","07097","07632","07024","08540"]
ct_zips = ["06807","06070","06830","06836","06510","06901"]


states = ['NY','NJ','CT']
						
random.seed()

TAB = "\t"

file = open("C:\\logs\\access.txt","a")

file.write("Timestamp"+TAB+"Site"+TAB+"Action"+TAB+"FA"+TAB+"State"+TAB+"ZIP"+TAB+"City"+TAB+"Population"+TAB+"Mid Household Income"+"\n")


for index in range(100):

	ran_1 = random.randint(0,100)
	ran_2 = random.randint(0,100)
	ran_3 = random.randint(0,100)
	ran_qty = random.randint(1000,1000000)
	
	t_yy = str(years[ran_1 % len(years)])
	t_MM = str(months[ran_2 % len(months)])
	t_dd = str(days[ran_3 % len(days)])
	t_hh = str(hours[ran_1 % len(hours)])
	t_mm = str(minutes[ran_2 % len(minutes)])
	t_ss = str(seconds[ran_3 % len(seconds)])
	
	t_fa = fas[ran_2 % len(fas)]
	
	t_timestamp = str(t_yy)+"-"+t_MM.rjust(2, '0')+"-"+t_dd.rjust(2, '0')+" "+t_hh.rjust(2, '0')+":"+t_mm.rjust(2, '0')+":"+t_ss.rjust(2, '0')
	
	t_state = states[ran_2 % len(states)]
	
	if (t_state == 'NY'):
		t_zip = ny_zips[ran_1 % len(ny_zips)]
	elif (t_state == 'NJ'):
		t_zip = nj_zips[ran_2 % len(nj_zips)]
	else:
		t_zip = ct_zips[ran_3 % len(ct_zips)]
		
	t_access = sites[ran_2 % len(sites)]
	
	t_action = actions[ran_3 % len(actions)]
	

	zipcode = engine.by_zipcode(t_zip)

		
	file.write(t_timestamp+TAB+t_access+TAB+t_action+TAB+t_fa+
              TAB+t_state+TAB+t_zip+TAB+zipcode.major_city+TAB+str(zipcode.population)+TAB+str(zipcode.median_household_income)+"\n")



file.close()

