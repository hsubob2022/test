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

securities = ["Equity","Fixed Income", "Mutual Funds"]

b_s = ["Buy","Sell"]

eq_tickers = ["AAPL","MS","C","GOOG","COST","BAC"]
fi_tickers = ["^IRX","^FVX","^TNX","^TYX"]
mf_tickers = ["AAAAX","AAATX","ASRAX","CALCI","MMKBX"]

ny_zips = ["11530","11753","11030","11576","11946","10024","10023","10021","10007","10006"]
nj_zips = ["07010","07020","07050","07078","07097","07632","07024","08540"]
ct_zips = ["06807","06070","06830","06836","06510","06901"]


states = ['NY','NJ','CT']
						
random.seed()

TAB = ","

file = open("C:\\logs\\trades.txt","a")

file.write("Timestamp"+TAB+"Buy/Sell"+TAB+"Quantity"+TAB+"Ticker"+TAB+"Asset Class"+TAB+"FA"+TAB+"State"+TAB+"ZIP"+TAB+"City"+TAB+"Population"+TAB+"Mid Household Income"+"\n")


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
	
	
	t_timestamp = str(t_yy)+"-"+t_MM.rjust(2, '0')+"-"+t_dd.rjust(2, '0')+" "+t_hh.rjust(2, '0')+":"+t_mm.rjust(2, '0')+":"+t_ss.rjust(2, '0')
	
	t_state = states[ran_2 % len(states)]
	
	if (t_state == 'NY'):
		t_zip = ny_zips[ran_1 % len(ny_zips)]
	elif (t_state == 'NJ'):
		t_zip = nj_zips[ran_2 % len(nj_zips)]
	else:
		t_zip = ct_zips[ran_3 % len(ct_zips)]
		
	t_fa = fas[ran_2 % len(fas)]
	
	t_security = securities[ran_3 % len(securities)]
	
	if (t_security == 'Equity'):
		t_tciker = eq_tickers[ran_1 % len(eq_tickers)]
	elif (t_security == 'Fixed Income'):
		t_tciker = fi_tickers[ran_2 % len(fi_tickers)]
	else:
		t_tciker = mf_tickers[ran_3 % len(mf_tickers)]
		
	t_buy_sell= b_s[ran_1 % len(b_s)]
	
	t_qty = str(ran_qty)

	zipcode = engine.by_zipcode(t_zip)

		
	file.write(t_timestamp+TAB+t_buy_sell+TAB+t_qty+TAB+t_tciker+TAB+t_security+TAB+t_fa+
              TAB+t_state+TAB+t_zip+TAB+zipcode.major_city+TAB+str(zipcode.population)+TAB+str(zipcode.median_household_income)+"\n")



file.close()

