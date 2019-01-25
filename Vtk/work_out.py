# Exam

## 1
def prime(to):
    for itr in range(1, to + 1):
        for jtr in range(2, to + 1):
            if (itr % jtr) == 0 and itr != jtr and itr != 1:
                break
        else:
            yield itr

print(list(prime(20)))

## 2
# zip() takes any number of iterables and returns a zip object that is an iterator of tuples - it combines
# lists with each other
# eg.

t1 = ['a', 'b', 'c']
t2 = [1, 2, 3]

z1 = list(zip(t1, t2))
print(z1)

print(*z1)
print(list(zip(*z1)))

# Lambda expressions are one-liner simplier functions that are used especially inside functions which

