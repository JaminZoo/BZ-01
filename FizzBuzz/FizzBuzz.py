# i = 1;
# 
# while (i <= 100):
# 	if(i%3 == 0 and i%5 == 0): 
# 		print "FizzBuzz"
# 	elif(i%3 == 0 and i != 0): 
# 		print "Fizz"
# 	elif(i%5 == 0):
# 			print "Buzz"
# 	elif(i%3 != 0 or i%5 != 0):
# 		print(i)
# 	else:			#continue looping through at increments of 1
# 		i += 1		# same as i = i + 1
# 		continue		
# 	i += 1
	
for i in range(1, 101):
	if i%3 == 0 and i%5 == 0:
		print "FizzBuzz"
	elif i%3 == 0 and not i%5 == 0:
		print "Fizz"
	elif i%5 == 0 and not i%3 == 0:
		print "Buzz"
	else:
		print i 
		
		