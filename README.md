# NY-motor-collisions

I worked on NYC Motor Vehicle Collisions dataset comprising 1.4 million rows and spanning 2013-2016. I obtained this data from [NYC Open Data api.](https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95)

## Tools used:

1- Pandas (for data munging & cleaning)

2- Plotly (for drawing graphs in Jupyter notebook + dashboard)

3- Dash (creating a dashboard based on the analysis performed)

4- Folium (creating maps to display collision trends in NY boroughs)

I built a dashboard displaying information about number of injuries/per capita injuries along with the breakdown of injury type in NY boroughs motor collisions for 2013-2016. I looked at daily/monthly trends in collisions as well as street intersections which had the highest number of collisions occurring at them. 

## Workflow:

1- Cleaned, filled out missing values from the data and stored it as a CSV

2- Using Pandas, I performed data analysis on the cleaned data 

3- Using Dash, I showcased my results using a dashboard

4- Using Folium, I drew a map to show data related to collisions on street intersections

## Technical challenges:

1- Filling out missing borough data: With the data provided, I had more collisions which had ‘Longitude’ and ‘Latitude’ data for collision site as compared to the borough name in which that collision that took place. 
Using ‘Longitude’ and ‘Latitude’ data for these collisions, I filled the missing borough locations for collisions which did not have the borough name but had ‘Longitude’ and ‘Latitude’ data available for them. This was done by computing the distance of collision location from each of the five boroughs and finding which borough had the minimum distance from the collision location. 

2- Removing anomalous data: Multiple entries had ‘Longitude’ and ‘Latitude’ data which didn’t conform with NYC boroughs longitude/latitude data. I removed these anomalous rows from the dataset.

3- Challenges with building dashboard:

i- I learned how to use Dash to design dashboards. Since Dash incorporates a lot of Javascript, HTML in its code, there were a lot of things to learn in terms of the layout and display of the dashboard.

ii- I was interested in plotting the top 5 street intersections where the highest number of collisions took place. I struggled a bit to find the right library to plot a map which included the streetview with markers highlighting the locations of interest.
In my quest to find the right library, I was introduced to GeoPandas. I found out that GeoPandas could perform the job of highlighting the latitudes/longitudes of interest but couldn’t show the underlying streetview map. 
I was introduced to Folium, a Javascript library used to construct graphs. This allowed me to tinker with Open Street Maps. 

The next roadblock I hit was related to displaying Folium maps on the dashboard: I found a very helpful Medium article through which I learned about using Iframe which is an html element that lets you integrate any webpage in an html document. Since Dash relies on HTML for its front end display I used Dash’s Iframe component to display Folium maps after saving them in html format. 

## Results:

1- From 2013-2016, Brooklyn accounted for the highest number of injuries. However, Manhattan accounted for the highest number of per capita injuries (total number of injuries/total borough population)

2- Motorist injuries accounted for the highest number of injuries across all years. 

3- Monthly distribution of collisions: Winter conditions do not cause more collisions as observed by data from 2013-2016. In 2013 and 2014, the highest number of collisions occurred in May and June respectively. 
Daily distribution of collisions: Highest number of collisions occurred on Friday from 2013-2016.

4- Using Folium, I plotted the street intersections where the highest number of collisions took place. 

## Next steps:

1- I want to build a dashboard that automatically updates everyday to display the latest data available on the NYC Open Data api.

2- I want to study the traffic collision patterns in other metropolitan areas of the world to find similarities and differences between them.
