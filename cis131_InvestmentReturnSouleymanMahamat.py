'''
Souleyman Mahamat
cis-131
01-21-2025

This script, with an initial deposit of $1000, calculates and displays
how much money would be in a 7% return investment account after 10, 20, and 30
years when untouched.
'''

#Initialize Variables

principal = 1000
term_years = [10,20,30] # Uses list for future expansion.
rate = 0.07 # annual rate
final_amount = [] # Uses list for future expansion.


# loops will expansion future expansion

for n in term_years:
    final_amount.append(principal * (1 + rate)**n) # calculates final amount

print(f'''
    Principal: ${principal}
    Rate: {rate * 100:.2f}%
''')

for i in range(len(term_years)):
    
    print(f'''
        Years: {term_years[i]} 
        Final amount: ${final_amount[i]:.2f}
    ''')