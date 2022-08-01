def check(num_list):

    return sum(num_list) % 10


numbers = list(map(lambda x: int(x) ** 2, input().split()))

print(check(numbers))
