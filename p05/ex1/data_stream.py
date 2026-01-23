from typing import Any, List, Dict, Optional, Union
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        if "SENSOR" in self.stream_id:
            self.stream_type = "Environmental Data"
        elif "TRANS" in self.stream_id:
            self.stream_type = "Financial Data"
        elif "EVENT" in self.stream_id:
            self.stream_type = "System Events"
        self.count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return False

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"id": self.stream_id, "processed": self.processed_count}


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        if super().filter_data(data_batch, float):
            return "Invalid Type Data"
        self.count += (len(data_batch))
        return (f"Sensor analysis: {len(data_batch)} readings processed, "
                f"avg temp: {data_batch[0]}")


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        if super().filter_data(data_batch, float):
            return "Invalid Type Data"
        self.count += (len(data_batch))
        data_sum = sum(data_batch)
        if data_sum > 0:
            n = "+"
        else:
            n = "-"
        return (f"Transaction analysis: {len(data_batch)} operations, net flow"
                f":{n}{data_sum}")


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        if super().filter_data(data_batch, str):
            return "Invalid Type Data"
        self.count += (len(data_batch))
        c = 0
        for d in data_batch:
            if d == "Error" or d == "error":
                c += 1
        p = ""
        if c > 1:
            p = "s"
        return (f"Event analysis: {len(data_batch)} events, "
                f"{c} error{p} detected")


class StreamProcessor():
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream):
        if isinstance(stream, DataStream):
            self.streams.append(stream)
        else:
            print("Erreur : Type de flux invalide")

    def process_all(self, data_lst: List[Any]):
        i = 0
        for stream in self.streams:
            if isinstance(stream, SensorStream):
                print(f"Processing event batch: {data_lst[i]}")
            elif isinstance(stream, TransactionStream):
                print(f"Processing event batch: {data_lst[i]}")
            elif isinstance(stream, EventStream):
                print(f"Processing event batch: {data_lst[i]}")
            print(stream.process_batch(data_lst[i]))
            i += 1


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    streams = [
        SensorStream("SENSOR_001"),
        TransactionStream("TRANS_001"),
        EventStream("EVENT_001")
    ]
    lst = [
        [22.5, 65, 1013],
        [100, -150, 75],
        ["login", "error", "logout"]
    ]
    print("Initializing Sensor Stream...")
    processor = StreamProcessor()
    for s in streams:
        processor.add_stream(s)
    processor.process_all(lst)
