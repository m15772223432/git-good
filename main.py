from src.calculator import add, subtract, multiply, divide,power


def main():
    print("=== Simple Calculator ===")
    print(f"10 + 3  = {add(10, 3)}")
    print(f"10 - 3  = {subtract(10, 3)}")
    print(f"10 * 3  = {multiply(10, 3)}")
    print(f"10 / 3  = {divide(10, 3):.4f}")
    print(f"10 ** 3 = {power(10, 3)}")

if __name__ == "__main__":
    main()
