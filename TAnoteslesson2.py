#a list is a container for your infomation
#names of thing, text 
#each is a variable 

attendees = ['Shannon', 'Jenn', 'Grace']

#empty list
coolpeople = []

print attendees[0] # Shannon
print attendees[1] # Jenn
print attendees[2] # Grace
print attendees[0:2] # Shannon, Jenn

#why does it tells it's a list for [0:2], mulitple items return back in a list 
#print attendees[3] yeilds an error since there is no 3 in the list

#lot of ways to find the length our list
#first way
print len(attendees)

#second way 
number_of_attendees = len(attendees)
print number_of_attendees 

#append adds an item to the end 
#this is the code for it list.append() 

#start with an empty list
attendees_ages = []

attendees_ages.append(28)
print attendees_ages 

attendees_ages.append(27)
print attendees_ages

#before we used sclining with print to say show me item with slice numbers, now we can change the list using slice number

days_of_week = ['Monday', 'Tuesday']
days_of_week.append('Wednesday')
days_of_week.append('Thursday')
days_of_week.append('Friday')
days_of_week.append('Saturday')
days_of_week.append('Sunday')

print days_of_week
print len(days_of_week)

#removing items from the list 
#pop takes it out

day = days_of_week.pop()
print day

#you get sunday 
#always starts from the top just like plates
#by default it pops of the top 

print days_of_week
#we popped it off and saved it to a variable 

days = days_of_week.pop(3)
print days

#we can remove from wherever we want so the above takes off Thursday
#can you pop off into a list? 
daysq = ['M', 'T', 'W', 'R', 'F', 'S', 'N']
dayq = daysq.pop()
print dayq

months = ['January', 'February']

months.extend(['March', 'April'])

print months
#list.append() adds one to the end
#list.extend() adds many

#Remove the first month
months.pop(0)

# Insert 'January' before index 0
months.insert(0, 'January')

print months 

#address example
address = "1133 19th St NW Washington, DC 20036"
print address
#now let's split on the spaces 
address_as_list = address.split(" ")
print address_as_list

#membership
#The in keyword allows you to check whether a value exists in the list

python_class = ["Jess", "Joy", "Ashley"]
'ann' in 'Shannon'
'Frankenstein' in python_class

#range 0 to 5
print range(5)

#range (start, stop) from start to stop
range(5, 10)

#now lets loopl through this
for number in range(10):
	print number
#so instead of the repeating code from earlier we can use loops

days_of_week = ['Monday','Tuesday',…]

for day in days_of_week:
	print day

#we can also this for numbers and use our formatting form before
for week in range(1, 5):
		print "Week {0}".format(week)

#we can nest loops so the we can do both
for week in range(1, 5):
		print "Week {0}".format(week)

		for day in days_of_week:
				print day

#or even nest this deeper
for month in months_in_year:
		print month

		for week in range(1, 5):
				print "Week {0}".format(week)

				for day in days_of_week:
						print day

#enumerate() is a function that you use with a for loop to get the index (position) of that list item, too.
#remember the class excerise where we all stoop up and told our positions 

#zip() is a function that you use with a for loop to use each item in multiple lists all at once 
#you can bring them together

#while loops as long as the answer to the question is yes
#we provide a way for the while loop to end 
#conditionals are key to the while loop
#while loops you need a yes or no question

if bread >= 2:
	print "I'm making a sandwich"


while bread >= 2:
	print "I'm making a sandwich"
