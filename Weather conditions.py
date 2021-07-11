# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#### Import package
!pip install wwo-hist
from wwo_hist import retrieve_hist_data
#### Set working directory to store output csv file(s)

import os
os.chdir("/Users/rochipodesta/Desktop/maestría/Herramientas/semana 3/parte1-py")


#### Example code
frequency=24
start_date = '1-JAN-2015'
end_date = '31-DEC-2015'
api_key = '26098d8245194cc7842233300211206'
location_list = ['20625', '20650', '20688', '20744', '20871', '21040', '21042', '21158', '21204', '21240', '21505', '21606', '21638', '21639', '21643', '21651', '21701', '21740', '21801', '21811', '21853', '21914']

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)
