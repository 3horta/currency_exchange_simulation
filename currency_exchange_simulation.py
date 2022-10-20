from locale import currency
import statistics
import pandas as pd
import random
import datetime

latest_values= {"USD":[], "EUR": [], "MLC":[]}

class currency_exchange_simulation():
    
    
    

    def __init__(self, sim_range):
        self.external_agent=0
        self.sim_range= sim_range
        #random.seed(42)
        
        # Opening JSON files with the data
        import json
        with open("eltoquedataEUR1000.json") as euro_file, open("eltoquedataMLC1000.json") as mlc_file, open("eltoquedataUSD1000.json") as usd_file:
            euro_data = json.load(euro_file)
            mlc_data = json.load(mlc_file)
            usd_data = json.load(usd_file)
            self.data={"EUR": euro_data, "USD": usd_data, "MLC": mlc_data}
        self.latest_days_fluctuation= {"EUR": self.compute_diff("EUR"), "USD": self.compute_diff("USD"), "MLC": self.compute_diff("MLC")}
        self.run()
        
    def compute_diff(self,currency):
        median_values= mean_values= []
        for item in self.data[currency][len(self.data[currency])-1:len(self.data[currency])-1-8:-1]:
            mean_values.append(item["avg"])
            median_values.append(item["median"])
        mean_diff= []
        median_diff=[]

        for i in range (len(mean_values)-1):
            mean_diff.append(mean_values[i]- mean_values[i+1])
            median_diff.append(median_values[i]- median_values[i+1])
        
       
        return mean_diff,median_diff

    def run(self):
        
        #current_price={"EUR": euro_data, "USD": usd_data, "MLC": mlc_data}
        """ today_date= datetime.date.today()
        last_date=[datetime.datetime.strptime(self.data["EUR"][len(self.data["EUR"])-1]["last"]["date"] , '%Y-%m-%d %H:%M:%S').date,
                    datetime.datetime.strptime(self.data["USD"][len(self.data["USD"])-1]["last"]["date"] , '%Y-%m-%d %H:%M:%S').date,
                    datetime.datetime.strptime(self.data["MLC"][len(self.data["MLC"])-1]["last"]["date"] , '%Y-%m-%d %H:%M:%S').date]
        date_offset= {"EUR": today_date - last_date[0] , "USD": today_date - last_date[1], "MLC": today_date - last_date[2]} """
        date_offset= {"EUR": 0 , "USD": 0, "MLC": 0}
        for item in self.latest_days_fluctuation:
            currency_price= int(self.data[item][len(self.data[item])-1]["median"])
            
            #Choosing mean as tendency. Change the statician to change behavior of the system
            tendency_factor= statistics.mean(self.latest_days_fluctuation[item][0])

            random_factor= random.randint(-5,5)


            for i in range(self.sim_range + date_offset[item]):
                count_values= random.randint(100,600)
                offers= []
                for  k in range(count_values):
                    offer= currency_price + tendency_factor + random_factor  
                    offers.append(offer)
                #Choosing mean as currency price. Change the statician to change behavior of the system
                currency_price = statistics.mean(offers)
            
            print("% s : % s" % (item, currency_price))

                    

sim= currency_exchange_simulation(1)   
