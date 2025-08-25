# lib/owner_pet.py

from __future__ import annotations
from typing import List, Optional


class Owner:
    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Owner.name must be a non-empty string")
        self.name = name

    # Return all Pet instances that belong to this owner
    def pets(self) -> List["Pet"]:
        return [p for p in Pet.all if p.owner is self]

    # Attach a Pet to this owner (with type checking)
    def add_pet(self, pet: "Pet") -> None:
        if not isinstance(pet, Pet):
            raise Exception("add_pet expects a Pet instance")
        pet.set_owner(self)

    # Return this owner's pets sorted by name (ascending)
    def get_sorted_pets(self) -> List["Pet"]:
        return sorted(self.pets(), key=lambda p: p.name)

    def __repr__(self) -> str:
        return f"Owner(name={self.name!r})"


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all: List["Pet"] = []

    def __init__(self, name: str, pet_type: str, owner: Optional[Owner] = None):
        # name validation
        if not isinstance(name, str) or not name.strip():
            raise Exception("Pet.name must be a non-empty string")
        self.name = name

        # pet_type validation
        if not isinstance(pet_type, str):
            raise Exception("Pet.pet_type must be a string")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type: {pet_type!r}. Allowed: {Pet.PET_TYPES}")
        self.pet_type = pet_type

        # optional owner validation/assignment
        self.owner: Optional[Owner] = None
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("Pet.owner must be an Owner or None")
            self.owner = owner

        # track all instances
        Pet.all.append(self)

    # helper used by Owner.add_pet (and safe to call directly)
    def set_owner(self, owner: Owner) -> None:
        if not isinstance(owner, Owner):
            raise Exception("set_owner expects an Owner instance")
        self.owner = owner

    def __repr__(self) -> str:
        o = getattr(self.owner, "name", None)
        return f"Pet(name={self.name!r}, type={self.pet_type!r}, owner={o!r})"
