#To get consistent hash codes, set the PYTHONHASHSEED environment variable to 0 to disable hash randomization.
from hashtable import HashTable
from unittest.mock import patch

#1
source = {"hola": "hello", 98.6: 37, False: True}
hash_table = HashTable.from_dict(source, capacity=len(source))
print(str(hash_table))
print('\n')

#2
hash_table2 = HashTable(capacity=100)
hash_table2["easy"] = "Requires Little Effort"
hash_table2["difficult"] = "Needs much skill"

print(hash_table2)
print(hash_table2["easy"])
print('\n')

#3
def test_should_detect_hash_collision():
    assert hash("foobar") not in [1,2,3]
    with patch("builtins.hash", side_effect=[1, 2, 3]):
        assert hash("foobar") == 1
        assert hash("foobar") == 2
        assert hash("foobar") == 3

#4
print(hash("MRO"))

print(hash("MRO") % 10)

print(hash("EAFP"))

print(hash("BFDL"))

print(hash("EAFP") % 10)

print(hash("BFDL") % 10)

print(hash("ABC"))

print(hash("ABC") % 10)
print('\n')

#5
with patch("builtins.hash", return_value=24):
    hash_table3 = HashTable(capacity=100)
    hash_table3["easy"] = "Requires little effort"
    hash_table3["difficult"] = "Needs much skill"

print(hash_table3._slots[24])

print(hash_table3._slots[25])

#6
hash_table4 = HashTable(capacity=1)
for i in range(100):
    num_pairs = len(hash_table4)
    num_empty = hash_table4.capacity - num_pairs
    print(
        f"{num_pairs:> 2}/{hash_table4.capacity:>2}",
        ("X" * num_pairs) + ("." * num_empty)
    )
    hash_table4[i] = i
    
#7 
hash_table5 = HashTable.from_dict({
    "hola":"hello",
    98.6: 37,
    False: True
})

print(hash_table5.keys)
print(hash_table5.values)
print(hash_table5.pairs)

print(hash_table5.pairs == list(zip(hash_table5.keys,hash_table5.values)))