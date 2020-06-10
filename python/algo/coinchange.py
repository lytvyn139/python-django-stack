input = 168
def get_the_change(input):
    quoters = input // 25
    input = input % 25

    dimes = input // 10
    input = input % 10

    nickels = input // 5
    input = input % 5

    pennies = input // 1
    input = input % 1

    report = [
        {'25¢' : quoters},
        {'10¢' : dimes},
        {' 5¢' : nickels},
        {' 1¢' : pennies}
    ]
    for i in range(len(report)):
        print(f"{report[i]}")

print(get_the_change(input))