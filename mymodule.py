def make_album(artist_name,albumtitle,number_of_tracks=""):
    """ This function takes two mandatory argument
    artist_name,
    albumtitle,
    number_of_tracks
    
    it will return the dictionary  whose keys will be
    artist name
    album title
    
    whose value will be arguments provided by the user during function call.
    
    
    
    """
    album_dic={"artist name : ":artist_name,"album title : ":albumtitle}
    if number_of_tracks:
        album_dic["number of tracks"]=number_of_tracks
   
    return album_dic    





def square_of_a_number(num):
    
    square = num**2   # local variable
    print(f"The sqaure of {num} is {square} which is a local variable")
    
    
def meter_to_km(distance_in_meters):
    distance_in_km= distance_in_meters/1000
    return distance_in_km
    