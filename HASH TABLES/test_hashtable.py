from hashtable import HashTable 

def test_should_create_hashtable():
    assert HashTable(size=100) is not None
    
def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100

def test_sould_create_empty_value_slots():
    #Given
    expected_values = [None, None, None]
    hash_table = HashTable(capacity=3)
    
    #When
    actual_values = hash_table.values
    
    #Then
    assert actual_values == expected_values