import strawberry
from schema import User, Planet, CryptoFish, Portfolio
import sqlite3

connection = sqlite3.connect("cryptofish.db", check_same_thread=False)
cursor = connection.cursor()


def get_users() -> list[User]:
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()
    all_users = []
    for user in users:
        all_users.append(User(id=user[0], name=user[1], email=user[2]))
    return all_users

def get_user(user_id : int) -> User:
    cursor.execute("SELECT * FROM user WHERE id=?", (user_id,))
    user = cursor.fetchone()
    return User(id=user[0], name=user[1], email=user[2])

def get_planets() -> list[Planet]:
    cursor.execute("SELECT * FROM planet")
    planets = cursor.fetchall()
    all_planets = []
    for planet in planets:
        all_planets.append(Planet(id=planet[0], name=planet[1], type=planet[2]))
    return all_planets

def get_planet(planet_id : int) -> Planet:
    cursor.execute("SELECT * FROM planet WHERE id=?", (planet_id,))
    planet = cursor.fetchone()
    return Planet(id=planet[0], name=planet[1], type=planet[2])

def get_cryptofish() -> list[CryptoFish]:
    cursor.execute("SELECT * FROM cryptofish")
    cryptofish = cursor.fetchall()
    all_cryptofish = []
    for fish in cryptofish:
        all_cryptofish.append(CryptoFish(id=fish[0], name=fish[1], planet=get_planet(fish[2]), status=fish[3], size=fish[4], cost=fish[5], owner=get_user(fish[6]) if fish[6] else None))
    return all_cryptofish


def get_cryptofish_by_id(cryptofish_id : int) -> CryptoFish:
    cursor.execute("SELECT * FROM cryptofish WHERE id=?", (cryptofish_id,))
    fish = cursor.fetchone()
    return CryptoFish(id=fish[0], name=fish[1], planet=get_planet(fish[2]), status=fish[3], size=fish[4], cost=fish[5], owner=get_user(fish[6]) if fish[6] else None)

def get_total_value(cryptofishs: list[CryptoFish]) -> float:
    total_value = 0
    for fish in cryptofishs:
        total_value += fish.cost
    return round(total_value,2)

def get_portfolio(user_id : int) -> Portfolio:
    cursor.execute("SELECT * FROM cryptofish WHERE owner_id=?", (user_id,))
    cryptofish = cursor.fetchall()
    all_cryptofish = []
    for fish in cryptofish:
        all_cryptofish.append(CryptoFish(id=fish[0], name=fish[1], planet=get_planet(fish[2]), status=fish[3], size=fish[4], cost=fish[5], owner=get_user(fish[6])))
    return Portfolio(user=get_user(user_id), cryptofish=all_cryptofish, total_value=get_total_value(all_cryptofish))

@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> list[User]:
        return get_users()
    
    @strawberry.field
    def user(self, user_id: strawberry.ID) -> User:
        return get_user(user_id)
    
    @strawberry.field
    def planets(self) -> list[Planet]:
        return get_planets()
    
    @strawberry.field
    def planet(self, planet_id: strawberry.ID) -> Planet:
        return get_planet(planet_id)
    
    @strawberry.field
    def cryptofish(self) -> list[CryptoFish]:
        return get_cryptofish()
    
    @strawberry.field
    def cryptofish_by_id(self, cryptofish_id: strawberry.ID) -> CryptoFish:
        return get_cryptofish_by_id(cryptofish_id)
    
    @strawberry.field
    def portfolio(self, user_id: strawberry.ID) -> Portfolio:
        return get_portfolio(user_id)
