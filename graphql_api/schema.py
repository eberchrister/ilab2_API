import strawberry

@strawberry.type
class Planet:
    id: strawberry.ID
    name: str
    type: str

@strawberry.type
class User:
    id: strawberry.ID
    name: str
    email: str

@strawberry.type
class CryptoFish:
    id: strawberry.ID
    name: str
    planet: Planet
    status: str
    size: str
    cost: float
    owner: User | None

@strawberry.type
class Portfolio:
    user: User
    cryptofish: list[CryptoFish]
    total_value: float