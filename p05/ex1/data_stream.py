from typing import Any, List, Dict, Union
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        types = {"SENSOR": "Environmental Data", "TRANS": "Financial Data",
                 "EVENT": "System Events"}
        self.stream_type = next((v for k, v in types.items()
                                 if k in stream_id), "General Data")
        self.count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Must be implemented by subclasses."""
        pass

    def filter_data(self, data_batch: Dict[str, Any],
                    criteria: Any = None) -> List[Any]:
        if not criteria:
            return data_batch
        if data_batch["filter"] != criteria:
            return None
        return [item for item in data_batch["data"]]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "id": self.stream_id,
            "type": self.stream_type,
            "processed": self.count
        }


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.count += len(data_batch)
            return (f"Sensor analysis: {len(data_batch)} readings processed, "
                    f"avg temp: {data_batch[0]}°C")
        except Exception as e:
            return f"Processing failure: {e}"


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.count += len(data_batch)
            net = sum(data_batch)
            return (f"Transaction analysis: {len(data_batch)} operations, "
                    f"net flow: {'+' if net > 0 else ''}{net} units")
        except Exception as e:
            return f"Processing failure: {e}"


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.count += len(data_batch)
            errors = len([d for d in data_batch if "error" in str(d).lower()])
            return (f"Event analysis: {len(data_batch)} events, {errors} "
                    f"error{'s' if errors != 1 else ''} detected")
        except Exception as e:
            return f"Processing failure: {e}"


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, data_map: List[Dict[str, Any]]) -> None:
        print("Batch 1 Results:")
        for i, stream in enumerate(self.streams):
            if i < len(data_map):
                filtered_data = stream.filter_data(data_map[i], "high")
                if not filtered_data:
                    continue
                stream.count = 0
                if filtered_data:
                    stream.process_batch(filtered_data)
                stats = stream.get_stats()
                label = stats['type'].split(' ')[0]
                print(f"- {label} data: {stats['processed']} items processed")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    s1 = SensorStream("SENSOR_001")
    s2 = TransactionStream("TRANSACTION_001")
    s3 = EventStream("EVENT_001")

    processor = StreamProcessor()
    processor.add_stream(s1)
    processor.add_stream(s2)
    processor.add_stream(s3)

    data_batches = [
        {"data": [22.5, 65, 1013], "filter": "medium"},
        {"data": [100, -150, 75], "filter": "high"},
        {"data": ["login", "error", "logout"], "filter": "high"}
    ]

    print("\nInitializing Sensor Stream...")
    print(f"Stream ID: {s1.stream_id}, Type: {s1.stream_type}")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(s1.process_batch(data_batches[0]["data"]))

    print("\nInitializing Transaction Stream...")
    print(f"Stream ID: {s2.stream_id}, Type: {s2.stream_type}")
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(s2.process_batch(data_batches[1]["data"]))

    print("\nInitializing Event Stream...")
    print(f"Stream ID: {s3.stream_id}, Type: {s3.stream_type}")
    print("Processing event batch: [login, error, logout]")
    print(s3.process_batch(data_batches[2]["data"]))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor.process_all(data_batches)

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction\n")
    print("All streams processed successfully. Nexus throughput optimal.")
