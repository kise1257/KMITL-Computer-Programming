print(" *** Water Supply Calculator ***")
usage = int(input("Total usage : "))
bill = 0
if usage <= 10:
    bill = usage * 5
elif usage <= 50:
    bill = 10 * 5 + (usage - 10) * 10
elif usage <= 100:
    bill = 10 * 5 + 40 * 10 + (usage - 50) * 12
elif usage <= 500:
    bill = 10 * 5 + 40 * 10 + 50 * 12 + (usage - 100) * 15
elif usage <= 1000:
    bill = 10 * 5 + 40 * 10 + 50 * 12 + 400 * 15 + (usage - 500) * 18
elif usage <= 5000:
    bill = 10 * 5 + 40 * 10 + 50 * 12 + 400 * 15 + 500 * 18 + (usage - 1000) * 20
else:
    bill = 10 * 5 + 40 * 10 + 50 * 12 + 400 * 15 + 500 * 18 + 4000 * 20 + (usage - 5000) * 21

print(f"Total Amount = {bill:,.2f} baht")
print("===== End of program =====")