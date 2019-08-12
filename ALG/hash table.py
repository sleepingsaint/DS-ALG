# creating a custom hash table
# use the Python function ord() to get the ASCII value of a letter
# use the python function char() to get letter corresponding to the ASCII value
# Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter
class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def cal_hash(self, st):
        hash_value = (ord(st[0]) * 100) + ord(st[1])
        return hash_value

    def store(self, st):
        hash_value = self.cal_hash(st)
        if self.table[hash_value] is not None:
            if hash_value in self.table:
                self.table[hash_value].append(st)
        else:
            self.table[hash_value] = st

    def lookup(self, st):
        hash_value = self.cal_hash(st)
        if self.table[hash_value] is not None:
            if st in self.table[hash_value]:
                return hash_value
        return -1

# initializing the hash table
hash_table = HashTable()

# test cases
hash_table.store('Udacity')
print(str(hash_table.lookup('Udacity'))+" - Udacity")

