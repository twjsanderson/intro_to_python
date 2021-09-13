# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is ordered* and changeable. No duplicate members.

first_list = [2, 3, 4, 5, 6, 7, 8, 9]

# Conditional loop
# Return new list > base
def conditional_loop(list, base):
    res = []
    for x in list:
        if x > base:
            res.append(x)
    return res

# Linear search
def linear_search(list, el):
    for x in list:
        if x == el:
            return str(el) + " is present at index " + str(list.index(el))
    return str(el) + " is not present in list"

# Is an entire string included in another string
def is_str_included(str1, str2):
    if (len(str1) < 1 or len(str2) < 1):
        return False

    if str1 in str2:
        return True

    return False

print('conditional_loop: ', conditional_loop(first_list, 5))
print('linear_search: ', linear_search(first_list, 211))
print('is_included: ', is_str_included('th', 'thssii'))

print('====================================================')

sec_list = [23, 53, 635, 6, 323, 432, 53453, 31]
third_list = [23, 23, 62, 53, 312, 635, 62, 3232, 4322, 534532, 312]

# Does list include duplicate v1
def has_duplicate1(list):
    first_el = list[0]
    length = len(list)
    i = 1

    if length == 1: return False

    while i < length:
        if first_el == list[i]: return True
        i += 1
    
    list.pop(0)
    return has_duplicate1(list)

# Does list include duplicates v2
# sets cannot have duplicates, you can use the .add() method on a set
def has_duplicate2(list):
    numbersChecked = set()
    for x in list:
        if x in numbersChecked: return True
        numbersChecked.add(x)
    return False

# Does list include duplicates v3
# sets cannot have duplicates, just compare lengths to confirm equality
def has_duplicate3(list):
    return len(list) != len(set(list))

# Show list of all duplicate elements
def show_duplicates(list):
    dups = []
    numbersChecked = set()
    for x in list:
        if x in numbersChecked: dups.append(x)
        numbersChecked.add(x)
    return dups

# Return list without duplicates
def remove_duplicates(list):
    no_dups = []
    numbersChecked = set()
    for x in list:
        if x not in numbersChecked: no_dups.append(x)
        numbersChecked.add(x)
    return no_dups

print('has_duplicate1: ', has_duplicate1(sec_list))
print('has_duplicate2: ', has_duplicate2(sec_list))
print('has_duplicate3: ', has_duplicate3(sec_list))
print('show_duplicates: ', show_duplicates(sec_list))
print('remove_duplicates: ', remove_duplicates(third_list))

print('====================================================')

first_dict = {
    "name": "tom",
    "job": "Dev",
    "years exp": 3,
    "languages": ["python", "JavaScript", "Go"]
}

def get_value_from_key(dict, key):
    return dict[key]

def show_all_keys(dict):
    return dict.keys()

def show_all_values(dict):
    return dict.values()

def update_dict_entry(dict, entry):
    if type(entry) is not type(dict): return 'entry arg must be a dictionary'
    dict.update(entry)
    return dict


print('get_value_from_dic: ', get_value_from_key(first_dict, 'job'))
print('show_all_keys: ', show_all_keys(first_dict))
print('show_all_values: ', show_all_values(first_dict))
print('update_dict_entry: ', update_dict_entry(first_dict, {"favourite food": "pizza"} ))

print('====================================================')

# User class
# self variable is like 'this', represents the instance of the object (ie. class) itself
# self can be called anything, but convention is to name it 'self'
# __init__ is like a constructor function in JavaScript
class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # must pass self into the function to use properties inside __init__ 
    def show_email_password(self):
        return (f'{self.email} {self.password}')

    # shows all attributes set to this instance
    def show_instance_attributes(self):
        return self.__dict__
    
    # update a specific instance attribute with a new value
    def update_attribute(self, attribute, new_value):
        for attr in self.__dict__:
            if attribute == attr:
                self.__dict__[attr] = new_value
        return self.__dict__

user1 = User('tom', 'tom@example.com', '123456')

print(user1.show_email_password())
print(user1.show_instance_attributes())
print(user1.update_attribute('name', 'joe'))

class SportClimber:
    climber_type = 'sport'                              # class attributes

    def __init__(self, name, highest_grade, shoes): 
        self.name = name                                # instance attributes, passed in when creating new instance
        self.highest_grade = highest_grade
        self.shoes = shoes
    
    @staticmethod
    def show_climber_type():                            # static method, dont need self passed in, can access class attr.
        return SportClimber.climber_type + ' climber'   # cannot access instance attr. or anything on the self variable

    @classmethod
    def show_climber_type_from_class(cls):              # class method, takes class instance as first arg 'cls', can be called in or on the class
        return cls.climber_type + ' climber'            # ie. SportClimber.show_climber_type_from_class() == SportClimber().show_climber_type_from_class
                                                        # can access class attr., cannot access instance attr.
                                                        # can have logic that requires specific info from the class instance data

    def show_favourite_shoes(self):                     # non-static method/instance method, need self passed in to access instance attr.
        return self.shoes
    
sportClimber1 = SportClimber('Tom', '5.11d', 'Skwamas')

print(sportClimber1.show_climber_type())
print(sportClimber1.show_climber_type_from_class())
print(sportClimber1.show_favourite_shoes())

print('====================================================')

# Inheritance
# todo list

