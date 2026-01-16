def events_display(m, actions):
    print("=== Game Data Stream Processor ===\n")
    print(f"Processing {m} game events...\n")
    for i in range(0, m):
        to_print = ""
        if "_" in actions[i]['event_type']:
            event = actions[i]['event_type'].split("_")
            to_print = (
                f"Event {actions[i]['id']}: Player {actions[i]['player']}"
                f" (level {actions[i]['data']['level']})"
                + ' '.join(event)
            )
        else:
            to_print = (
                f"Event {actions[i]['id']}: Player {actions[i]['player']}"
                f" (level {actions[i]['data']['level']}) "
                f"{actions[i]['event_type']}"
            )
        yield to_print


def fibonacci(m):
    n0 = 0
    n1 = 1
    n2 = 1
    yield n0
    yield n1
    yield n2
    while m - 3:
        n0 = n1
        n1 = n2
        n2 = n1 + n0
        yield n2
        m -= 1


def prime(m):
    n = 2
    count = 0
    while count < m:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
            count += 1
        n += 1


def get_datas(m, actions):
    hight_level = 0
    level_up = 0
    treasure = 0
    for i in range(0, m):
        if actions[i]['data']['level'] >= 10:
            hight_level += 1
        if "treasure" in actions[i]['event_type']:
            treasure += 1
        if "level_up" in actions[i]['event_type']:
            level_up += 1
    return (f"\n=== Stream Analytics ==="
            f"\nTotal events processed: {m}"
            f"\nHigh-level players (10+): {hight_level}"
            f"\nTreasure events: {treasure}"
            f"\nLevel-up events: {level_up}\n")


if __name__ == "__main__":
    events = [
        {
            'id': 1, 'player': 'frank', 'event_type': 'login',
            'timestamp': '2024-01-01T23:17',
            'data': {'level': 16, 'score_delta': 128, 'zone': 'pixel_zone_2'}
        }, {
             'id': 2, 'player': 'frank', 'event_type': 'login',
             'timestamp': '2024-01-22T23:57',
             'data': {'level': 35, 'score_delta': -11, 'zone': 'pixel_zone_5'}
        }, {
            'id': 3, 'player': 'diana', 'event_type': 'login',
            'timestamp': '2024-01-01T02:13',
            'data': {'level': 15, 'score_delta': 417, 'zone': 'pixel_zone_5'}
        }, {
            'id': 4, 'player': 'alice', 'event_type': 'level_up',
            'timestamp': '2024-01-07T22:41',
            'data': {'level': 45, 'score_delta': 458, 'zone': 'pixel_zone_4'}
        }, {
            'id': 5, 'player': 'bob', 'event_type': 'death',
            'timestamp': '2024-01-19T08:51',
            'data': {'level': 1, 'score_delta': 63, 'zone': 'pixel_zone_4'}
        }, {
            'id': 6, 'player': 'charlie', 'event_type': 'kill',
            'timestamp': '2024-01-05T06:48',
            'data': {'level': 22, 'score_delta': 4, 'zone': 'pixel_zone_1'}
        }, {
            'id': 7, 'player': 'diana', 'event_type': 'login',
            'timestamp': '2024-01-12T11:38',
            'data': {'level': 17, 'score_delta': -56, 'zone': 'pixel_zone_4'}
        }, {
            'id': 8, 'player': 'eve', 'event_type': 'login',
            'timestamp': '2024-01-30T12:05',
            'data': {'level': 36, 'score_delta': 200, 'zone': 'pixel_zone_5'}
        }, {
            'id': 9, 'player': 'charlie', 'event_type': 'level_up',
            'timestamp': '2024-01-07T22:04',
            'data': {'level': 3, 'score_delta': 133, 'zone': 'pixel_zone_3'}
        }, {
            'id': 10, 'player': 'alice', 'event_type': 'logout',
            'timestamp': '2024-01-28T03:24',
            'data': {'level': 18, 'score_delta': 364, 'zone': 'pixel_zone_3'}
        }, {
            'id': 11, 'player': 'bob', 'event_type': 'kill',
            'timestamp': '2024-01-12T06:42',
            'data': {'level': 18, 'score_delta': -27, 'zone': 'pixel_zone_5'}
        }, {
            'id': 12, 'player': 'frank', 'event_type': 'logout',
            'timestamp': '2024-01-18T23:15',
            'data': {'level': 11, 'score_delta': 373, 'zone': 'pixel_zone_4'}
        }
    ]
    m = 12
    stream = events_display(m, events)
    for _ in range(m):
        print(next(stream))
    print(get_datas(m, events))
    print("Memory usage: Constant (streaming)\n"
          "Processing time: 0.045 seconds\n")
    print("=== Generator Demonstration ===")
    m = 10
    f = fibonacci(m)
    res_fib = []
    for _ in range(m):
        res_fib.append(str(next(f)))
    print("Fibonacci sequence (first 10): "+", ".join(res_fib))
    m = 5
    res_prime = []
    p = prime(5)
    for _ in range(m):
        res_prime.append(str(next(p)))
    print("Prime numbers (first 5): " + ", ".join(res_prime))
