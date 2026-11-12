# Make a GWA Calculator and compute its average 

num_subj = int(input("Enter subjects taken: "))

total_GxU = 0
total_units = 0
ineligible = False
print()

for i in range (1, num_subj + 1):

    # Get user input and calculate grade x units

    subj_grade = float(input(f"Enter subject {i} grade: "))
    subj_units = int(input("Enter units taken: "))
    subjGxU = subj_grade * subj_units

    total_GxU += subjGxU
    total_units += subj_units
    
    if subj_grade > 2.00:
    	ineligible = True

    print()

gwa = total_GxU / total_units

print(f"GWA: {gwa}")

if gwa <= 1.75 and gwa >= 1.26:
    if ineligible:
        print("Ineligible for honors (Reason: Grade below 2.00)")
    else:
        print("Dean's Lister")
elif gwa <= 1.25 and gwa >= 1.00:
    if ineligible:
        print("Ineligible for honors (Reason: Grade below 2.00)")
    else:
        print("President's Lister")
else:
    print("Ineligible for honors (Reason: Did not meet GWA Requirement)")