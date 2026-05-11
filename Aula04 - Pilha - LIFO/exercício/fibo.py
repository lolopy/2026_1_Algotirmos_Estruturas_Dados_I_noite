def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_less_than(n):
    def helper(a, b):
        if a >= n:
            return
        print(a, end=' ')
        helper(b, a + b)
    helper(0, 1)

# Solicitar o valor do usuário
n = int(input("Informe um valor: "))
print("Termos da sequência de Fibonacci menores que", n, ":")
print_fibonacci_less_than(n)