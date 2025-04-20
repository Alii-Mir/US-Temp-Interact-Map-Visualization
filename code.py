import csv
import folium

def main():
    # Create a map using the us-states.json file
    us_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

    # Add a tile layer to the map
    folium.TileLayer('Mapbox Bright', attr='Mapbox Bright').add_to(us_map)

    # Open the CSV
    with open("C:\\Users\\mahdi\\Desktop\\IBM Gen AI Exercise\\states.csv") as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=",")

        # Skip the header row
        next(csv_reader)

        # Loop through the data
        for col in csv_reader:
            # Get the data for each state
            lat = float(col[0])
            lon = float(col[1])
            temp = float(col[2])

            # Print the temperature value for debugging
            print(temp)

            # Add a circle marker for each state
            folium.CircleMarker(location=[lat, lon], radius=10, popup=str(temp)+"°F", fill_color=get_color(temp), color="grey", fill_opacity=0.7).add_to(us_map)

    # Save the map
    us_map.save("us_map.html")

def get_color(temp):
    # Use a conditional statement to set the marker color
    if temp < 50:
        return "green"

    elif temp < 60:
        return "orange"

    else:
        return "red"

if __name__ == "__main__":

    main()