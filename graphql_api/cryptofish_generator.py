from itertools import product
import random, string
import sqlite3

opt = input("Do you want to generate a new database? (y/n):")
if opt == 'n':
    exit()


connection = sqlite3.connect("cryptofish.db", check_same_thread=False)

planet = [1, 2, 3, 4, 5, 6, 7]
status = ['hungry', 'sleepy', 'bored', 'playful', 'grumpy', 'lonely', 'happy']
size = ['small', 'medium', 'large', 'giant', 'tiny', 'colossal', 'molecular']

combinations = list(product(planet, status, size))

combinations_dict = {}

for i, combination in enumerate(combinations):
    combinations_dict[i+1] = {
        'id': i+1,
        'name' : ''.join(random.choices("".join(random.choices(string.ascii_lowercase, k=7)), k=5)),
        'planet': combination[0],
        'status': combination[1],
        'size': combination[2],
        'cost': round(i*random.randint(1,69)*random.random(), 2),
        'owner': random.randint(1,36) if i < len(combinations)//1.2 else 'NULL',
    }

# shuffle the ids  
values = list(combinations_dict.values())
random.shuffle(values)
shuffled_dict = {k: v for k, v in zip(combinations_dict.keys(), values)}

queries = []
queries.append('DROP TABLE IF EXISTS cryptofish;')
queries.append('DROP TABLE IF EXISTS planet;')
queries.append('DROP TABLE IF EXISTS user;')
queries.append('CREATE TABLE cryptofish (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, planet_id INTEGER NOT NULL, status TEXT NOT NULL, size TEXT NOT NULL, cost INTEGER NOT NULL, owner_id INTEGER);')
queries.append('CREATE TABLE planet (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, type TEXT NOT NULL);')
queries.append('CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL);')
queries.append('INSERT INTO planet (name, type) VALUES ("earth-420", "terrestrial");')
queries.append('INSERT INTO planet (name, type) VALUES ("ilab-2", "ocean");')
queries.append('INSERT INTO planet (name, type) VALUES ("welsenus", "gas giant");')
queries.append('INSERT INTO planet (name, type) VALUES ("chrsitorus", "ice giant");')
queries.append('INSERT INTO planet (name, type) VALUES ("x-212", "neptunian");')
queries.append('INSERT INTO planet (name, type) VALUES ("mars-54", "puffy");')
queries.append('INSERT INTO planet (name, type) VALUES ("kaku-z", "protoplanet");')


str_format = 'INSERT INTO cryptofish VALUES ({id}, "{name}", {planet}, "{status}", "{size}", {cost}, {owner});'
for i in range(1, len(shuffled_dict)+1):
    queries.append(str_format.format(**shuffled_dict[i]))
    # print(str_format.format(**shuffled_dict[i]))

first_names = ["eber", "welsen", "sarah", "dylan", "jessica","timmy", "joseph", "nathan", "kimberly", "joshua", "christine", "ryan", "amanda", "chris", "ashley", "brandon", "brittany", "jennifer", "ryan", "james", "rachel", "melissa", "joseph", "daniel", "jose", "emily", "kevin", "matthew", "michael", "brian", "lauren", "amanda", "derek", "jennifer", "stephanie", "andrew"]
last_names = ["christer", "evan", "alvandi", "smith", "paul", "nakamura", "bob", "chad", "donna", "jackson", "maggie", "oliver", "randy", "patricia", "barbara", "steven", "karen", "jacob", "cameron", "kelly", "lucas", "elizabeth", "peter", "debra", "tracy", "victor", "tony", "jason", "gabriel", "julie", "julian", "carlos", "philip", "frank", "gina", "kyle"]
str_format_user = 'INSERT INTO user VALUES ({id}, "{name}", "{email}");'
for i in range(1, 37):
    queries.append(str_format_user.format(id=i, name=first_names[i-1] + ' ' +last_names[i-1] , email= last_names[i-1]+'.'+ first_names[i-1] + '@'+''.join(random.choices(string.ascii_lowercase, k=6))+'.com'))
    # print(str_format_user.format(id=i, name=first_names[i-1] + ' ' +last_names[i-1] , email= last_names[i-1]+'.'+ first_names[i-1] + '@'+''.join(random.choices(string.ascii_lowercase, k=6))+'.com')) 

for query in queries:
    connection.execute(query)

connection.commit()
connection.close()