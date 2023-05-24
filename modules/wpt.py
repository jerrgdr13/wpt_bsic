#!/usr/bin/env python3
import requests
import json

logs = {

}

def create_wpt(test_id):
    try:
        endpoint = f'https://www.webpagetest.org/jsonResult.php?test={test_id}'

        data_wpt = json.dumps(endpoint, indent=2)
        response = requests.get(endpoint)
        dic_wpt = response.json()
        sor_data = {
            'id' : dic_wpt['data']['id'],
            'url' : dic_wpt['data']['url'],
            'lcp' : dic_wpt['data']['average']['firstView']['chromeUserTiming.LargestContentfulPaint'],
            'CLS' : dic_wpt['data']['average']['firstView']['chromeUserTiming.CumulativeLayoutShift'],
            'TBT' : dic_wpt['data']['average']['firstView']['TotalBlockingTime'],
            'SPI' : dic_wpt['data']['average']['firstView']['SpeedIndex'],
            'ttfb' : dic_wpt['data']['average']['firstView']['TTFB'],
            'CMS' : dic_wpt['data']['median']['firstView']['detected']['CMS'],
            'CRM' : dic_wpt['data']['median']['firstView']['detected']['CRM'],
            'ServerOS' : dic_wpt['data']['median']['firstView']['detected']['Operating systems'],
            'Webservers' : dic_wpt['data']['median']['firstView']['detected']['Web servers'],
            'Cloud' : dic_wpt['data']['median']['firstView']['detected']['PaaS']
  
        }
    except Exception as e:
        print(e)
    return sor_data
