from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)
    try:
        sta = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )
        print("Valid station created:")
        print(f"ID: {sta.station_id}")
        print(f"Name: {sta.name}")
        print(f"Crew: {sta.crew_size} people")
        print(f"Power: {sta.power_level}%")
        print(f"Oxygen: {sta.oxygen_level}%")
        print(f"Status: {'Operational' if sta.is_operational else 'Offline'}")
    except ValidationError as e:
        print(f"Unexpected Error: {e}")
    print("=" * 40)

    print("Expected validation error:")
    try:
        insta = SpaceStation(
            station_id="DEATHSTAR",
            name="Overcrowded Station",
            crew_size=50,
            power_level=10.0,
            oxygen_level=10.0,
            last_maintenance=datetime.now()
        )
        print("Valid station created:")
        print(f"ID: {insta.station_id}")
        print(f"Name: {insta.name}")
        print(f"Crew: {insta.crew_size} people")
        print(f"Power: {insta.power_level}%")
        print(f"Oxygen: {insta.oxygen_level}%")
        print("Status: "
              f"{'Operational' if insta.is_operational else 'Offline'}")
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
