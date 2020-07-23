from uszipcode import Zipcode
from uszipcode import SearchEngine

# define helper function for converting GPS coordinates (latitude, longitude) to Zip Code


def gps_to_zip(lat, lon):
    '''
    Takes in parameters of latitude and longitude coordinates and converts to Zip Code
    '''
    try:
        search = SearchEngine(simple_zipcode=True)
        find_zip = search.by_coordinates(lat, lon)
        zip_dict = find_zip[0].to_dict()
        return zip_dict['zipcode']
    except IndexError:
        return None
