import random
from uszipcode import SearchEngine

engine = SearchEngine()

years = [2021,2022]
months = list(range(1, 13))
days = list(range(1, 29))
hours = list(range(9, 15))
minutes = list(range(0, 60))
seconds = list(range(0, 60))


securities = ["Equity", "Mutual Funds","Options","Fixed Income","UIT"]

reasons = ["Trade blocked by Lydia as security is held below the line (e.g. MS securities, ineligible ETFs or restricted securities)",
"FA/CSA registration process not refreshed real time",
"An approved PEPE exception exists for this trade (please provide exception #)",
"System outage",
"Security symbol is invalid / not applicable / new (and therefore blocked at order entry)",
"Account opened today (and therefore blocked at order entry)",
"Account Red Flagged for escheatment. Security sold to cover a cash debit",
"Trade blocked by CGA portal (e.g. MS securities)",
"Solicited Inverse or Leveraged ETF trade in an employee or employee related account"
]


random.seed()

TAB = "$"

#file = open("C:\\logs\\trades.txt","a")
file = open("reasons.txt","a")


for index in range(1000):

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
	
	if (t_yy == '2022'):
		t_MM = str(ran_2 % 2 +1)
	
	
	t_timestamp = str(t_yy)+"-"+t_MM.rjust(2, '0')+"-"+t_dd.rjust(2, '0')+" "+t_hh.rjust(2, '0')+":"+t_mm.rjust(2, '0')+":"+t_ss.rjust(2, '0')

	
	t_security = securities[ran_1 % len(securities)]
	
	t_reason = reasons[ran_3 % len(reasons)]
	
	
	file.write(t_timestamp+TAB+t_security+TAB+t_reason+"\n")



file.close()

