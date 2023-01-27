import strawberry

from schema import User, CryptoFish
from query import cursor, connection, get_cryptofish_by_id, get_cryptofish, get_user, get_planet, get_total_value

def add_user(name: str, email: str) -> User:
    cursor.execute("INSERT INTO user (name, email) VALUES (?, ?)", (name, email))
    connection.commit()
    return User(id=cursor.lastrowid, name=name, email=email)

def delete_user(user_id: int) -> User:
    all_cryptofish = get_cryptofish()
    for fish in all_cryptofish:
        if fish.owner and fish.owner.id == user_id:
            cursor.execute("UPDATE cryptofish SET owner_id=NULL WHERE id=?", (fish.id,))
    cursor.execute("DELETE FROM user WHERE id=?", (user_id,))
    connection.commit()
    return User(id=user_id, name="", email="")

def update_user(user_id: int, name: str, email: str) -> User:
    cursor.execute("UPDATE user SET name=?, email=? WHERE id=?", (name, email, user_id))
    connection.commit()
    return User(id=user_id, name=name, email=email)

def fish_cryptofish(cryptofish_id: int, user_id: int):
    if get_cryptofish_by_id(cryptofish_id).owner is not None:
        return get_cryptofish_by_id(cryptofish_id)
    cursor.execute("UPDATE cryptofish SET owner_id=? WHERE id=?", (user_id, cryptofish_id))
    connection.commit()
    return get_cryptofish_by_id(cryptofish_id)

def sell_cryptofish(cryptofish_id: int) -> CryptoFish:
    cursor.execute("UPDATE cryptofish SET owner_id=NULL WHERE id=?", (cryptofish_id,))
    connection.commit()
    return get_cryptofish_by_id(cryptofish_id)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self, name: str, email: str) -> User:
        return add_user(name, email)
    
    @strawberry.mutation
    def delete_user(self, user_id: int) -> User:
        return delete_user(user_id)

    @strawberry.mutation
    def update_user(self, user_id: int, name: str, email: str) -> User:
        return update_user(user_id, name, email)

    @strawberry.mutation
    def fish_cryptofish(self, cryptofish_id: int, user_id: int) -> CryptoFish:
        return fish_cryptofish(cryptofish_id, user_id)

    @strawberry.mutation
    def sell_cryptofish(self, cryptofish_id: int) -> CryptoFish:
        return sell_cryptofish(cryptofish_id)

