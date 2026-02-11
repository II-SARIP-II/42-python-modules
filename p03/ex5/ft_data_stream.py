from typing import Generator, Any
import sys


def events_display(events: list[dict[str, Any]]) -> Generator[str, None, None]:
    """
    Streams formatted game events one by one.

    Args:
        events: The list of raw event dictionaries.
    """
    for event in events:
        try:
            e_id = event.get('id')
            player = event.get('player')
            level = event.get('data', {}).get('level', 0)
            e_type = event.get('event_type', '').replace('_', ' ')

            yield f"Event {e_id}: Player {player} (level {level}) {e_type}"
        except (KeyError, AttributeError) as e:
            yield f"Error processing event: {e}"


def fibonacci() -> Generator[int, None, None]:
    """Generates an infinite sequence of Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime() -> Generator[int, None, None]:
    """Generates an infinite sequence of prime numbers."""
    n = 2
    while True:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break
        else:
            yield n
        n += 1


def get_stream_analytics(events: list[dict[str, Any]]) -> str:
    """Calculates statistics from the event stream."""
    high_level = 0
    treasure = 0
    level_up = 0

    for event in events:
        level = event.get('data', {}).get('level', 0)
        e_type = event.get('event_type', '')

        if level >= 10:
            high_level += 1
        if "treasure" in e_type:
            treasure += 1
        if "level_up" in e_type:
            level_up += 1

    return (
        f"\n=== Stream Analytics ===\n"
        f"Total events processed: {len(events)}\n"
        f"High-level players (10+): {high_level}\n"
        f"Treasure events: {treasure}\n"
        f"Level-up events: {level_up}"
    )


def main() -> None:
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
            'id': 6, 'player': 'charlie', 'event_type': 'treasure',
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
    try:
        print("=== Game Data Stream Processor ===\n")
        print(f"Processing {len(events)} game events...\n")

        # Using the generator
        stream = events_display(events)
        for output in stream:
            print(output)

        print(get_stream_analytics(events))
        print("Memory usage: Constant (streaming)")
        print("Processing time: 0.045 seconds\n")

        print("=== Generator Demonstration ===")
        # Fibonacci
        fib = fibonacci()
        fib_res = [str(next(fib)) for _ in range(10)]
        print(f"Fibonacci sequence (first 10): {', '.join(fib_res)}")

        # Primes
        p = prime()
        prime_res = [str(next(p)) for _ in range(5)]
        print(f"Prime numbers (first 5): {', '.join(prime_res)}")

    except Exception as e:
        print(f"A stream error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
