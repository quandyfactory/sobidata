Summary
=======

Download your Social Bicycles (SoBi) route data and save it locally in various formats.

Details
=======

The `sobidata` module allows you to download your [Social Bicycles](https://app.socialbicycles.com) (SoBi) route data via the applications web API and save it locally in a variety of file formats.

The module uses the `requests` library to download collections of routes from the SoBi HTTP REST API using HTTP Basic Authentication, as outlined in the [SoBi API documentation](https://app.socialbicycles.com/developer/).

The route data is paginated, and the method that downloads the data calls itself recursively, incrementing the page with each request until there is no more data.

For each route, the module  makes a follow-up request to the API to look up the bike name, origin hub address and destination hub address. However, it also stores the results of those requests locally so that a subsequent search for the same bike name or hub address retrieves the result from the local cache rather than making a duplicate API request.

As a result, the data includes three datasets: a list of routes, a list of hubs and a list of bikes. The module also makes a list of totals, calculating the total distance in miles, total distance in km, total duration in seconds, total duration in minutes, total duration in hours, total number of distinct bikes, and total number of distinct hubs.

Once the data is downloaded, you can save it locally in a variety of formats: JSON, XML, Excel 2007 or CSV format. Note that the JSON, XML and Excel 2007 formats save all four datasets, but the CSV format only saves the routes dataset.

Installation
============

The sobidata module is [published on the Python Package Index](https://pypi.python.org/pypi/sobidata), so you can install it using `pip` or `easy_install`.

    pip install sobidata
    
Or:

    easy_install sobidata

Alternately, you can download the tarballed installer - `sobidata-[VERSION].tar.gz` - for this package from the [dist](https://github.com/quandyfactory/sobidata/tree/master/dist) directory on github and uncompress it. Then, from a terminal or command window, navigate into the unzipped folder and type the command:

    python setup.py install
    
That should be all you need to do.

Basic Usage
===========

From a Python terminal or script, import the `sobidata` module and create an instance of the Sobi() class.

    >>> import sobidata
    >>> sobi = sobidata.Sobi()

Assign your SoBi username (your email address) and password, as they are used for authentication.

    >>> sobi.username = 'my@email.address'
    >>> sobi.password = 'SecretPassword123'

If you try to get any data from the API without setting a username and password, the module will raise a `ValueError`.

Download Routes Data
--------------------

Call the `get_data()` method to download and process the data.

    >>> sobi.get_data()

It will take a few moments to download all the data. 

Specify a destination path to save the data.

    >>> sobi.path = '/path/to/sobi/download/files'

Save Your Data
--------------

Export and save the data locally.

    >>> sobi.save_data()

If you call `save_data()` without any parameters, it saves the data in JSON format under the filename:

`/path/to/sobi/download/files/sobidata_export.json` 

You can also save in several other formats by specifying the format as an optional argument:

    >>> sobi.save_data('xml') # XML format via dicttoxml module
    >>> sobi.save_data('xlsx') # Excel 2007 format via openpyxl module
    >>> sobi.save_data('csv') # CSV format - only saves routes

Polite Mode
-----------

Under normal functioning, this module makes a series of HTTP requests to the SoBi API with no delay. However, you can enable polite mode by setting `polite` to `True`:

    >>> sobi.polie = True

When you enable polite mode, the module introduces a 0-3 second delay (chosen randomly) between each HTTP request. That way, the load on the SoBi API endpoint is reduced.

Advanced Usage
==============

Access Local Data
-----------------

The local data is stored in a dictionary. If you want to view/manipulate the data further, you can access the dictionary here:

    >>> data = sobi.data
    >>> data.keys()
    ['bikes', 'hubs', 'routes', 'totals']

The `data['bikes']` item is a list of dictionaries with the following keys: `bike_id`, `bike_name`.

The `data['hubs']` item is a list of dictionaries with the following keys: `hub_id', `hub_address`.

The `data['routes']` item is a list of dictionaries with the following keys: `bike_id`, `bike_name`, `distance_km`, `distance_miles`, `duration`, `duration_hh_mm_ss`, `finish_time`, `first_location_address`, `from_hub_address`, `from_hub_id`, `route_id`, `start_time`, `to_hub_address`, `to_hub_id`.

The `data['totals']` is a dictionary with the following keys: `distinct_bikes`, `distinct_hubs`, `total_distance_km`, `total_distance_miles`, `total_duration_hours`, `total_duration_minutes`, `total_duration_seconds`.

Import Data
-----------

If you have previously saved the data in JSON format, you can import it:

    >>> sobi.import_data()

Currently, you can only import data in JSON format.

Make Requests
-------------

You can use `sobidata` to make specific requests against the SoBi API for resource details via the `make_request()` method. The method uses the `requests.get()` method and returns a response object from `requests`.

Currently, the following resources are supported:

* routes - the details for a route
* hubs - the details for a hub
* bikes - the details for a bike
* friends - list of friends (no way to access individuals by id)
* me - returns your own user details

Continuing with our example code, here is how to get the details for the bike with id 917:

    >>> response = sobi.make_request('bikes', 917):
    >>> response.status_code
    200
    >>> obj = response.json()
    >>> obj.keys()
    [u'distance', u'current_position', u'name', u'network_id', u'hub_id', u'id', u'state', u'inside_area', u'address', u'repair_state']
    >>> obj['id']
    917
    >>> obj['state']
    u'available'

And here is how to get the details for the hub with id 552:

    >>> response = sobi.make_request('hubs', 552)
    >>> response.status_code
    200
    >>> obj = response.json()
    >>> obj.keys()
    [u'has_kiosk', u'area_id', u'polygon', u'name', u'distance', u'network_id', u'free_racks', u'inside', u'racks_amount', u'current_bikes', u'available_bikes', u'address', u'middle_point', u'id', u'description']
    obj['id']
    552
    >>> obj['address']
    u'The Chedoke Rail Trail, Hamilton'
    >>> obj['current_bikes']

(Note: this functionality does not currently extend to retrieving all the routes, hubs or bikes from the API, but we plan to introduce this in a future revision.)

Author
======

* Author: Ryan McGreal
* Email: [ryan@quandyfactory.com](mailto:ryan@quandyfactory.com)
* Repository: [http://github.com/quandyfactory/sobidata](http://github.com/quandyfactory/sobidata)

Version
=======

* Version: 0.4.1
* Release Date: 2015-05-08

Revision History
================

Version 0.4.1
-------------

* Release Date: 2015-05-08
* Notes:
    * Updated README to edit formatting, add copyright and licence

Version 0.4
-----------

* Release Date: 2015-05-08
* Notes:
    * Added ability to make specific API requests
    * Added total number of routes to totals dictionary
    * Added 'polite' mode for delayed API calls
    * Added hashbang and docstring
    * Updated README.md

Version 0.3
-----------

* Release Date: 2015-05-06
* Notes:
    * Fixed version in sobidata.py, README.md and setup.py

Version 0.2
-----------

* Release Date: 2015-05-06
* Notes:
    * Dropped and recreated repository.

Version 0.1
-----------

* Release Date: 2015-05-06
* Notes:
    * First commit.
    * Thanks to [parlarjb](https://gist.github.com/parlarjb) for looking at an [early gist](https://gist.github.com/quandyfactory/08125fe3050a563d55c3) and offering some helpful suggestions to clean up the code.

Copyright and Licence
=====================

Copyright &copy; Ryan McGreal, 2015.

Licenced under the [GNU General Public License, version 2](https://www.gnu.org/licenses/gpl-2.0.html).

