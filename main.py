from src.calculator import add, subtract, multiply, divide


def main():
    print("=== Simple Calculator ===")
    print(f"10 + 3  = {add(10, 3)}")
    print(f"10 - 3  = {subtract(10, 3)}")
    print(f"10 * 3  = {multiply(10, 3)}")
    print(f"10 / 3  = {divide(10, 3):.4f}")


if __name__ == "__main__":
    main()
