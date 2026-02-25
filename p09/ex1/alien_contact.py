from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum
from typing_extensions import Self


class contact(Enum):
    radio = 1
    visual = 2
    physical = 3
    telepathic = 4


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: contact
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_id(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError('ID do not start with "AC"')
        return self

    @model_validator(mode='after')
    def check_contact_type(self) -> Self:
        if not self.contact_type:
            raise ValueError('Contact type note specified')
        if self.contact_type == contact.physical and not self.is_verified:
            raise ValueError('Physical contact type not verified')
        if self.contact_type == contact.telepathic and self.witness_count < 3:
            raise ValueError('Telepathic type should have at least 3 witness')
        return self

    @model_validator(mode='after')
    def check_signal_strength(self) -> Self:
        if self.signal_strength > 7 and self.message_received is None:
            raise ValueError('Signal strength but no messages')
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 40)

    try:
        alien = AlienContact(
            contact_id="AC-2024-001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=contact.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        print(f"ID: {alien.contact_id}")
        print(f"Type: {alien.contact_type.name}")
        print(f"Location: {alien.location}")
        print(f"Signal: {alien.signal_strength}/10")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witnesses: {alien.witness_count}")
        print(f"Message: '{alien.message_received}'")
    except ValidationError as e:
        print(f"Unexpected Error: {e.json()}")
    print("=" * 40)
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC-999",
            timestamp=datetime.now(),
            location="Paris",
            contact_type=contact.telepathic,
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=2,
            message_received="Mind meld"
        )
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
