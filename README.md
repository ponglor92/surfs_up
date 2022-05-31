# Surfs_up: Module 9 Challenge

## Overview of the Project
### Purpose
-	The purpose of this analysis is to be able to find temperature data for the months June and December, so W. Avy can determine if the surf and ice cream shop business would be sustainable year- round. With the knowledge gained from chapter 9, the two deliverables were successful.
## Results 
### Provide a bulleted list with three major points from the two analysis deliverables. Use images as support where needed.
- Images below are the charts showing June and December:
- 
![june temperture](https://user-images.githubusercontent.com/101531875/171085706-4cdb7dfb-5de0-4dd7-af18-a97af2ad71e1.png)
![dec temperture](https://user-images.githubusercontent.com/101531875/171085721-5e8bcc62-94ce-4c37-aa3a-21e73a021b29.png)


1. Comparing the mean of the temperature from both months, June and December; the mean in June is higher than in December. June had a mean temperature of 75 degree Fahrenheit and December  
2.	Comparing both of the months temperature, there is an 8 degree difference in the minimum of both months. June has a minimum temperature of 64 degree Fahrenheit, and December has a minimum temperature of 56 degree Fahrenheit.
3.	There is a difference in the maximum by 2 degree Fahrenheit. June’s maximum temperature is 85 degree Fahrenheit which is higher than Decembers maximum temperature; 83 degree Fahrenheit. 

## Summary
There is not much of a difference between the June and December temperatures like how there would be differences in some other states in the United States. Some additional queries that I would add to gather more weather data for June and December is the months July and October.

1.	Query for July (summer)
2.	
![July temperture](https://user-images.githubusercontent.com/101531875/171085596-f22dfd40-2f7c-4807-9cb0-e43b2a11d94f.png)

July_temperatures = session.query(Measurement).filter(extract('month', Measurement.date) == 3)
July_temp_list = [temp.tobs for temp in July_temperatures]
July_temp_df = pd.DataFrame(July_temp_list, columns=["July Temps"])
July_temp_df.describe()


2.	Query for October (fall)
3.	
![oct temperture](https://user-images.githubusercontent.com/101531875/171085633-bbb45713-4d1b-49f7-8c23-33c4faf3ef08.png)

October_temperatures = session.query(Measurement).filter(extract('month', Measurement.date) == 9)
October_temp_list = [temp.tobs for temp in October_temperatures]
October_temp_df = pd.DataFrame(October_temp_list, columns=["October Temps"])
October_temp_df.describe()
