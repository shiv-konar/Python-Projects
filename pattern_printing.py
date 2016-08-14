'''
Pattern 1
num_lines = 5
*****
*****
*****
*****
*****
'''

num_lines = input('Number of lines:')
print 'Pattern 1'
for i in range(num_lines):
    for j in range(num_lines):
        print '*',
    print ''

'''
Pattern 2
num_lines = 5
*
**
***
****
*****
'''
print '\nPattern 2'
for i in range(1, num_lines + 1):
    print i * '*'


'''
Pattern 3
num_lines = 5
    *
   **
  ***
 ****
*****
'''
print '\nPattern 3'
for i in range(1, num_lines + 1):
    for j in range(1, num_lines - i + 1):
        print ' ',
    for k in range(1, i+1):
        print '*',
    print ''

print '\nPattern 4'
for i in range(1, num_lines + 1):
    for j in range():
        pass