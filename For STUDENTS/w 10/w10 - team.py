# https://byui-cse.github.io/cse110-course/lesson10/teach.html
# 10 Teach: Team Activity

#LISTS
names = []
balances = []

name = ""

#CONDITIONAL
while name != "quit":

    name = input("\nWhat's the name of the account?: ")

    if name != "quit":
        balance = float(input("What's the balance?: "))
        names.append(name)
        balances.append(balance)
    else:
        break

#FOR LOOP AND OUTPUT
print("Account information:")
for i in range(len(names)) and range(len(balances)):

    name = names[i]
    balance = balances[i]

    print(f"{name} - ${balance}")

total = sum(balances)

print(f"\nTotal: ${total:.2f}")
print(f"Avarage: ${total / len(names):.2f}")