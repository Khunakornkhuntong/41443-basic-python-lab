bill, tip_percent, people = input().split()
bill = float(bill)
tip_percent = float(tip_percent)
people = int(people)

tip_amount = bill * (tip_percent / 100)

total_bill = bill + tip_amount

each_person_pays = total_bill / people

print(f"Each person pays: {each_person_pays:.2f}")
