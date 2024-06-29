import pandas as pd

def perform_operations(series1, series2):
    addition = series1 + series2
    print("Addition:")
    print(addition)
    
    subtraction = series1 - series2
    print("\nSubtraction:")
    print(subtraction)
    
    multiplication = series1 * series2
    print("\nMultiplication:")
    print(multiplication)
    
    division = series1 / series2
    print("\nDivision:")
    print(division)

def get_series_input():
    series1_input = input("Enter elements for Series 1 (separated by space): ")
    series2_input = input("Enter elements for Series 2 (separated by space): ")
    series1 = pd.Series(map(float, series1_input.split()))
    series2 = pd.Series(map(float, series2_input.split()))
    return series1, series2

def main():
    series1, series2 = get_series_input()
    
    perform_operations(series1, series2)

if __name__ == "__main__":
    main()
