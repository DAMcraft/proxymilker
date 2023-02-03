# Scrapes socks5 proxies from https://proxygenerator.azura.best/
import os.path
import time
import grequests

repeat_forever = True


class OutOfStock(Exception):
    pass


def get_all_proxies() -> list[tuple[str, int]]:
    request = grequests.map([grequests.get('https://proxygenerator.azura.best/')])[0]
    if request.status_code == 400:
        raise OutOfStock('Out of stock')
    tmp_ip, tmp_port = (request.json()['proxy']).split(':')
    proxies: list[tuple[str, int]] = [(tmp_ip, int(tmp_port))]

    amount = request.json()['remaining-proxies']
    amount = int(amount)

    requests = (grequests.get('https://proxygenerator.azura.best/') for _ in range(amount))
    requests = grequests.map(requests)
    for response in requests:
        if response.status_code == 400:
            break
        tmp_ip, tmp_port = (response.json()['proxy']).split(':')
        proxies.append((tmp_ip, int(tmp_port)))
    return proxies


if not os.path.isfile('proxies.txt'):
    with open('proxies.txt', 'w') as f:
        f.write('')

try:
    all_proxies = get_all_proxies()
    with open('proxies.txt', 'a') as f:
        for ip, port in all_proxies:
            f.write(f'{ip}:{port}\n')
    print(f"Found {len(all_proxies)} new proxies")
except OutOfStock:
    print("Out of stock")

while repeat_forever:
    time.sleep(60)
    try:
        all_proxies = get_all_proxies()
        with open('proxies.txt', 'a') as f:
            for ip, port in all_proxies:
                f.write(f'{ip}:{port}\n')
        print(f"Found {len(all_proxies)} new proxies")
        time.sleep(60)
    except OutOfStock:
        print("Out of stock")
        time.sleep(60)
        continue
    except Exception as e:
        print("An error occurred")
        print(e)
        time.sleep(60)
        continue


# Write a readme for github
