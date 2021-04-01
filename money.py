
profile = {
  'name': 'bektur',
  'age': 27,
  'balance': 1000
}

journal = {
  'profile1': profile
}


def calculate_spending(*args):
	 return sum(args)

def calculate_regular_spending(gas, water, electricity=1000):
	a = gas + water + electricity
	return a

def calculate_income(job, job2):
	return job + job2

def show_balance(profile):
	return profile['balance']

def add_profile(name, age, balance, jourmal):
	new_profile = {}
	new_profile['name'] = name
	new_profile['age'] = age
	new_profile['balance'] = balance
	length = len(journal)
	journal['profile{}'.format(length+1)] = new_profile
	return journal

def add_keys(job1, job2, *args):
	lst = []
	for i in args:
		lst.append(i)
	return [job1, job2], lst
a, b = add_keys(10, 20, 30, 40, 50, 60)
profile['spending'] = b
profile['income'] = a


show_balance(profile)


