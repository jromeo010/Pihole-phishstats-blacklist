import requests, time, re


def call_api(TS,PAGE_TRACKER):
        url = 'https://phishstats.info:2096/api/phishing?_size=100&_where=(date,gt,'+TS+')&_p='+str(PAGE_TRACKER)
        RESPONSE = requests.get(url)
        JSON_PAYLOAD = []
        JSON_PAYLOAD = RESPONSE.json()
        return JSON_PAYLOAD


def main():

    TS = '2021-06-02T20:40:21.000Z'
    Loop_control = True
    page_tracker = 1

    TODAY = time.strftime('%Y-%m-%dT%H:%M:%S.000Z',time.localtime())
    DOMAIN_LIST=[]

    while Loop_control:
        JSON_PAYLOAD = []
        try:
            JSON_PAYLOAD = call_api(TS,page_tracker)
        except:
            Loop_control = False
            print('error in api call, quiting script')
            break
        page_tracker += 1


        for OBJ in JSON_PAYLOAD:
            DOMAIN_EXTRACT = re.findall(r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]',OBJ['url'])#extracts domain from url
            DOMAIN_LIST.append(DOMAIN_EXTRACT[0])

        if not len(JSON_PAYLOAD)== 100:
            Loop_control = False
            break
        time.sleep(5)

    DOMAIN_LIST = list(set(DOMAIN_LIST))#remove duplicates from list


if __name__ == '__main__':
    main()
