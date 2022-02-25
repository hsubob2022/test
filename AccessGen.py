import random

from uszipcode import SearchEngine
engine = SearchEngine()

years = [2021,2022]
months = list(range(1, 13))
days = list(range(1, 29))
hours = list(range(9, 15))
minutes = list(range(0, 60))
seconds = list(range(0, 60))

fas = ["John Smith","Mary Shelly","Peter Williams","Nicro Brown", "Jay Miller", "David Lopez"]

actions = ["Name Search","Number Search"]

assets = ["EQ","MF"]

offices = ["101","102","103","104","105","106"]



states = ['NY','NJ','CT']
						
random.seed()

TAB = ","

#file = open("C:\\logs\\search.txt","a")
file = open("search.txt","a")

#file.write("Timestamp"+TAB+"Site"+TAB+"Action"+TAB+"FA"+TAB+"State"+TAB+"ZIP"+TAB+"City"+TAB+"Population"+TAB+"Mid Household Income"+"\n")


for index in range(1000):

	ran_1 = random.randint(0,100)
	ran_2 = random.randint(0,100)
	ran_3 = random.randint(0,100)
	
	t_yy = str(years[ran_1 % len(years)])
	t_MM = str(months[ran_2 % len(months)])
	t_dd = str(days[ran_3 % len(days)])
	t_hh = str(hours[ran_1 % len(hours)])
	t_mm = str(minutes[ran_2 % len(minutes)])
	t_ss = str(seconds[ran_3 % len(seconds)])

	if (t_yy == '2022'):
		t_MM = str(ran_2 % 2 +1)
	
	t_timestamp = str(t_yy)+"-"+t_MM.rjust(2, '0')+"-"+t_dd.rjust(2, '0')+" "+t_hh.rjust(2, '0')+":"+t_mm.rjust(2, '0')+":"+t_ss.rjust(2, '0')
	
	t_asset = assets[ran_1 % len(assets)]
	
	t_no = ran_2 % len(offices)
	
	t_office = offices[t_no]
	
	t_fa = fas[t_no]
	
	if (t_office == '101'):
		t_state = "NY"
	elif (t_office == '102'):
		t_state = "NY"
	elif (t_office == '103'):
		t_state = "NJ"
	elif (t_office == '104'):
		t_state = "NJ"
	elif (t_office == '105'):
		t_state = "CT"
	elif (t_office == '106'):
		t_state = "CT"
	
	
	t_action = actions[ran_1 % len(actions)]
	
		
	file.write(t_timestamp+TAB+t_asset+TAB+t_office+TAB+t_fa+TAB+t_action+TAB+t_state+"\n")



file.close()

