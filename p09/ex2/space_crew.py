from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from enum import Enum
from typing_extensions import Self
from datetime import datetime


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Rank.cadet
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: Optional[bool] = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: Optional[str] = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_id_validator(self) -> Self:
        if self.mission_id[:1] != 'M':
            raise ValueError("mission_id should start with 'M'")
        return self

    @model_validator(mode="after")
    def crew_validator(self) -> Self:
        commander = 0
        for member in self.crew:
            if member.rank in [Rank.commander, Rank.captain]:
                commander += 1
        if commander <= 0:
            raise ValueError("Mission must have at least one Commander "
                             "or Captain")
        return self

    @model_validator(mode="after")
    def long_mission(self) -> Self:
        if self.duration_days > 365:
            experienced = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced += 1
            if experienced < len(self.crew) / 2:
                raise ValueError("Long mission must have at least 50% of "
                                 "experienced crew")
        return self

    @model_validator(mode="after")
    def active_validator(self) -> Self:
        for member in self.crew:
            if not member.is_active:
                raise ValueError("Mission must have all crew active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    try:
        # ======================= CREW GENERATION ======================= #
        member1 = CrewMember(
            member_id="EQ102-5",
            name="Clara",
            rank=Rank.commander,
            age=29,
            specialization="pilot",
            years_experience=6,
            is_active=True
        )
        member2 = CrewMember(
            member_id="EQ102-6",
            name="Chloé",
            rank=Rank.commander,
            age=29,
            specialization="pilot",
            years_experience=2,
            is_active=True
        )
        member3 = CrewMember(
            member_id="EQ102-7",
            name="Roger",
            rank=Rank.cadet,
            age=29,
            specialization="pilot",
            years_experience=4,
            is_active=True
        )
        print("Member1:")
        print(f"Type: {member1.name}")
        print(f"years: {member1.years_experience}")
        print(f"active: {member1.is_active}")
        print("\nMember2:")
        print(f"Type: {member2.name}")
        print(f"years: {member2.years_experience}")
        print(f"active: {member2.is_active}")
        print("\nMember3:")
        print(f"Type: {member3.name}")
        print(f"years: {member3.years_experience}")
        print(f"active: {member3.is_active}")

        # ======================= VALID MISSION ======================= #
        sm1 = SpaceMission(
            mission_id="M-echo-123",
            mission_name="Echo2000",
            destination="Echo-planet",
            launch_date=datetime(2020, 5, 17),
            duration_days=364,
            crew=[member1, member2, member3],
            budget_million=200.0
        )
        print("\nValid mission created:")
        print(f"Mission: {sm1.mission_name}")
        print(f"ID: {sm1.mission_id}")
        print(f"Destination: {sm1.destination}")
        print(f"Duration: {sm1.duration_days}")
        print(f"Budget: {sm1.budget_million}M")
        print(f"Crew size: {len(sm1.crew)}")
        for mem in sm1.crew:
            print(f"- {mem.name} ({mem.rank}) - {mem.specialization}")
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg']}")

        # ======================= INVALID MISSION ======================= #
    try:
        print("\nDetails of the Invalid mission:")
        sm2 = SpaceMission(
            mission_id="-echo-123",
            mission_name="Echo2000",
            destination="Echo-planet",
            launch_date=datetime(2020, 5, 17),
            duration_days=364,
            crew=[member1, member2, member3],
            budget_million=200.0
        )
        print(f"mission id: {sm2.mission_id}")
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg']}")
        # ======================= INVALID MISSION ======================= #
    try:
        print("\nDetails of the Invalid mission:")
        sm3 = SpaceMission(
            mission_id="M-echo-123",
            mission_name="Echo2000",
            destination="Echo-planet",
            launch_date=datetime(2020, 5, 17),
            duration_days=3000,
            crew=[member1, member2, member3],
            budget_million=200.0
        )
        print(f"mission id: {sm3.mission_id}")
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg']}")

        # ======================= INVALID MISSION ======================= #
    try:
        print("\nDetails of the Invalid mission:")
        sm3 = SpaceMission(
            mission_id="M-echo-123",
            mission_name="Echo2000",
            destination="Echo-planet",
            launch_date=datetime(2020, 5, 17),
            duration_days=300,
            crew=[member3],
            budget_million=200.0
        )
        print(f"mission id: {sm3.mission_id}")
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg']}")

        # ======================= INVALID MISSION ======================= #
    member4 = CrewMember(
            member_id="EQ102-7",
            name="Roger",
            rank=Rank.cadet,
            age=29,
            specialization="pilot",
            years_experience=4,
            is_active=False
        )
    try:
        print("\nDetails of the Invalid mission:")
        sm3 = SpaceMission(
            mission_id="M-echo-123",
            mission_name="Echo2000",
            destination="Echo-planet",
            launch_date=datetime(2020, 5, 17),
            duration_days=300,
            crew=[member1, member4],
            budget_million=200.0
        )
        print(f"mission id: {sm3.mission_id}")
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg']}")


if __name__ == "__main__":
    main()
