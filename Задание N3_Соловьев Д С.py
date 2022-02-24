def nfib(n):
    fib = [1, 1]
    for i in range(n-2):
        fib.append(fib[i] + fib[i + 1])    
    return fib

print(f'Спиок через list(): {list(i for i in nfib(20))}')
print(f'Генератор списка: {[i for i in nfib(20)]}')
a = []
for i in nfib(20):
    a.append(i)
print(f'Спомощью цикла for: {a}')
print(f'Генератор множества: { {i for i in nfib(20)} }')