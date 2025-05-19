### Essential Python Modules – Study Repo Format

## 1️⃣ Module: math
"""
✅ Most Used & Essential Functions:
1. math.sqrt(x)        -> Square root
2. math.pow(x, y)      -> Power of x^y
3. math.floor(x)       -> Round down
4. math.ceil(x)        -> Round up
5. math.factorial(x)   -> Factorial of a number
6. math.pi             -> Constant value of pi (π)
7. math.log(x, base)   -> Logarithm of x with given base

Use case: Scientific calculations, formulas, games, ML math
Usage: import math
"""

import math
print("Square root of 25:", math.sqrt(25))
print("2^3:", math.pow(2, 3))
print("Floor of 3.9:", math.floor(3.9))
print("Ceil of 3.1:", math.ceil(3.1))
print("Factorial of 4:", math.factorial(4))
print("Value of pi:", math.pi)
print("Log base 10 of 100:", math.log(100, 10))

# Exercises
# 1. Area of circle
def area_of_circle(radius): return math.pi * math.pow(radius, 2)
# 2. Round up/down
def round_values(num): return math.floor(num), math.ceil(num)
# 3. Factorial
def get_factorial(n): return math.factorial(n)
# 4. Logarithm
def custom_log(x, base): return math.log(x, base)
# 5. Power
def power(x, y): return math.pow(x, y)


## 2️⃣ Module: random
"""
✅ Most Used & Essential Functions:
1. random.random()         -> Float [0.0, 1.0)
2. random.randint(a, b)    -> Random int in [a, b]
3. random.choice(seq)      -> Random item from list
4. random.shuffle(seq)     -> Shuffle list in place
5. random.sample(pop, k)   -> k unique elements

Use case: Games, testing, AI randomness, simulations
Usage: import random
"""

import random
print("Random float:", random.random())
print("Random int 1–10:", random.randint(1, 10))
print("Random choice:", random.choice(["apple", "banana", "cherry"]))

# Exercises
# 1. Dice roller
def roll_dice(): return random.randint(1, 6)
# 2. Random password
def random_password(): return ''.join(random.sample("abcdef123456", 6))
# 3. Shuffle list
def shuffle_list(lst): random.shuffle(lst); return lst
# 4. Pick random student
def pick_student(students): return random.choice(students)
# 5. Lottery draw
def lottery_draw(): return random.sample(range(1, 50), 6)


## 3️⃣ Module: datetime
"""
✅ Most Used & Essential Functions:
1. datetime.now()              -> Current date & time
2. datetime.strptime()         -> Convert string to datetime
3. datetime.strftime()         -> Format datetime to string
4. timedelta(days=, hours=)    -> Add/subtract time

Use case: Logs, timestamps, age calculator, deadlines
Usage: from datetime import datetime, timedelta
"""

from datetime import datetime, timedelta
print("Now:", datetime.now())
print("Formatted:", datetime.now().strftime("%Y-%m-%d %H:%M"))

# Exercises
# 1. Get current date/time
def current_time(): return datetime.now()
# 2. Format datetime
def format_now(): return datetime.now().strftime("%A, %d %B %Y")
# 3. Days till birthday
def days_until_birthday(birth_date): return (birth_date - datetime.now()).days
# 4. Past date
def one_week_ago(): return datetime.now() - timedelta(days=7)
# 5. Future date
def add_days(n): return datetime.now() + timedelta(days=n)


## 4️⃣ Module: time
"""
✅ Most Used & Essential Functions:
1. time.time()        -> Current time in seconds
2. time.sleep(x)      -> Pause program for x seconds
3. time.ctime()       -> Convert time to readable form

Use case: Delays, performance measurement
Usage: import time
"""

import time
print("Current timestamp:", time.time())
print("Readable:", time.ctime())

# Exercises
# 1. Pause for 2 seconds
def wait_2s(): time.sleep(2)
# 2. Timer
def measure_runtime():
    start = time.time()
    for _ in range(1000000): pass
    end = time.time()
    return end - start
# 3. Print every second for 3 seconds
def print_countdown():
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)


## 5️⃣ Module: os
"""
✅ Most Used & Essential Functions:
1. os.getcwd()               -> Get current working directory
2. os.listdir(path)          -> List files in directory
3. os.mkdir(name)            -> Create new directory
4. os.rename(src, dst)       -> Rename file/folder
5. os.remove(path)           -> Delete file
6. os.path.exists(path)      -> Check if path exists

Use case: File handling, directory automation
Usage: import os
"""

import os
print("Current working dir:", os.getcwd())
print("Files:", os.listdir())

# Exercises
# 1. Create folder
def create_folder(name): os.mkdir(name)
# 2. Rename file/folder
def rename_item(old, new): os.rename(old, new)
# 3. Delete file
def delete_file(name): os.remove(name)
# 4. Check file exists
def file_exists(path): return os.path.exists(path)
# 5. List directory
def list_directory(path): return os.listdir(path)


## 6️⃣ Module: sys
"""
✅ Most Used & Essential Functions:
1. sys.argv             -> List of command-line arguments
2. sys.exit()           -> Exit the program
3. sys.version          -> Python version
4. sys.path             -> List of directories for module search

Use case: Command-line tools, Python info, dynamic imports
Usage: import sys
"""

import sys
print("Python version:", sys.version)
print("Path:", sys.path[:3])  # Limiting output

# Exercises
# 1. Print command-line arguments
def print_args(): return sys.argv
# 2. Exit script (not used in demo)
def exit_script(): sys.exit()
# 3. Show Python version
def show_version(): return sys.version
# 4. Show module search paths
def show_paths(): return sys.path
# 5. Count args
def count_args(): return len(sys.argv)


## 7️⃣ Module: json
"""
✅ Most Used & Essential Functions:
1. json.dumps(obj)          -> Convert dict to JSON string
2. json.loads(json_str)     -> Convert JSON string to dict
3. json.dump(obj, file)     -> Write JSON to file
4. json.load(file)          -> Read JSON from file

Use case: API data, configuration files, web projects
Usage: import json
"""

import json

# Example data
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)
print("JSON String:", json_str)
print("Back to dict:", json.loads(json_str))

# Exercises
# 1. Convert dict to JSON
def dict_to_json(d): return json.dumps(d)
# 2. Convert JSON to dict
def json_to_dict(j): return json.loads(j)
# 3. Save JSON to file
def save_json(filename, d):
    with open(filename, "w") as f:
        json.dump(d, f)
# 4. Load JSON from file
def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)
# 5. Pretty print JSON
def pretty_json(d): return json.dumps(d, indent=4)


## 8️⃣ Module: csv
"""
✅ Most Used & Essential Functions:
1. csv.reader(file)             -> Read rows from CSV file
2. csv.writer(file)             -> Write rows to CSV file
3. csv.DictReader(file)         -> Read CSV into dicts
4. csv.DictWriter(file, fieldnames) -> Write dicts to CSV

Use case: Data files, Excel-like input/output, ML datasets
Usage: import csv
"""

import csv

# Exercises
# 1. Read CSV file
def read_csv(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        return list(reader)

# 2. Write CSV file
def write_csv(filename, data):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

# 3. Read CSV as dicts
def read_csv_dict(filename):
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)

# 4. Write dicts to CSV
def write_csv_dict(filename, data, fieldnames):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# 5. Append row to CSV
def append_csv_row(filename, row):
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)


# TO BE CONTINUED...
# Next modules:
# - re
# - statistics
# - collections
# - itertools
# - functools
# - requests
# - urllib
# - pickle
# - shutil
# - traceback

# Let me know when to continue to next set.
