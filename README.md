# test

NewTrades_CL 
| extend fields = split(RawData,",")
| extend timestamp = todatetime(fields[0])
| extend buysell = tostring(fields[1])
| extend quantity = toint(fields[2])
| extend ticker = tostring(fields[3])
| extend class = tostring(fields[4])
| extend fa = tostring(fields[5])
| extend state = tostring(fields[6])
| extend zip = tostring(fields[7])
| extend city = tostring(fields[8])
| extend population = toint(fields[9])
| extend household_income = toint(fields[10])
