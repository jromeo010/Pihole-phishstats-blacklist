import requests, time


def main():

    TS = '2021-05-10T12:00:00.000Z'
    Loop_control = True
    page_tracker = 1


    while Loop_control:
        url = 'https://phishstats.info:2096/api/phishing?_where=(date,gt,'+TS+')&_p='+str(page_tracker)+'&_size=100'
        RESPONSE = requests.get(url)
        JSON_PAYLOAD = []
        JSON_PAYLOAD = RESPONSE.json()
        page_tracker += 1

        for dictionary in JSON_PAYLOAD:
            print(dictionary['url'])


        if not len(JSON_PAYLOAD)== 100:
            Loop_control = False
            break
        time.sleep(5)


if __name__ == '__main__':
    main()
