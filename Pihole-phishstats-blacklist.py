import requests,time,re,os

def delta_file():
    DELTA_FILE = 'phishstats_delta.txt'
    TS = ''
    TODAY = time.strftime('%Y-%m-%dT%H:%M:%S.000Z',time.localtime())
    if os.path.exists(DELTA_FILE):
        FILE_ = open(DELTA_FILE, 'r+')
        TS = FILE_.readlines()
        FILE_.truncate(0)
        FILE_.write(TODAY)
        FILE_.close()
        print('Updating Delta File with '+str(TODAY))
    else:
        print("Delta File did not exists, creating file: "+DELTA_FILE)
        FILE_ = open(DELTA_FILE, 'w+')
        TS = TODAY
        FILE_.write(TODAY)
        FILE_.close()
    return str(TS[0])

def call_api(TS,PAGE_TRACKER):
        url = 'https://phishstats.info:2096/api/phishing?_size=100&_where=(date,gt,'+TS+')&_p='+str(PAGE_TRACKER)
        RESPONSE = requests.get(url)
        JSON_PAYLOAD = []
        JSON_PAYLOAD = RESPONSE.json()
        return JSON_PAYLOAD

def Fetch_Results(TS):
    Loop_control = True
    page_tracker = 1
    DOMAIN_LIST=[]

    while Loop_control:
        JSON_PAYLOAD = []
        try:
            JSON_PAYLOAD = call_api(TS,page_tracker)
        except:
            Loop_control = False
            print('error in api call, quiting script')
            break

        for OBJ in JSON_PAYLOAD:
            DOMAIN_EXTRACT = re.findall(r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]',OBJ['url'])#extracts domain from url
            DOMAIN_LIST.append(DOMAIN_EXTRACT[0])

        if not len(JSON_PAYLOAD)== 100:
            Loop_control = False
            break

        time.sleep(5)
        page_tracker += 1

    return DOMAIN_LIST

def main():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    TS = delta_file()
    DOMAIN_LIST = list(set(Fetch_Results(TS)))#remove duplicates from list
    print(DOMAIN_LIST)

if __name__ == '__main__':
    main()
