import requests, time, re


def main():

    TS = '2021-05-19T12:00:00.000Z'
    Loop_control = True
    page_tracker = 1


    while Loop_control:
        url = 'https://phishstats.info:2096/api/phishing?_size=100&_where=(date,gt,'+TS+')&_p='+str(page_tracker)
        RESPONSE = requests.get(url)
        JSON_PAYLOAD = []
        JSON_PAYLOAD = RESPONSE.json()
        page_tracker += 1

        for dictionary in JSON_PAYLOAD:
            test = re.findall(r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]',dictionary['url'])
            print(dictionary['url'])
            print(test[0])

        if not len(JSON_PAYLOAD)== 100:
            Loop_control = False
            break
        time.sleep(5)


if __name__ == '__main__':
    main()
