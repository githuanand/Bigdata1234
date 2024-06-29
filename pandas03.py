import pandas as pd

def create_dataframe():
    num_rows = int(input("Enter the number of rows for the DataFrame: "))
    data = []
    for i in range(num_rows):
        row = []
        for j in range(2):
            value = input(f"Enter value for row {i+1}, column {j+1}: ")
            row.append(value)
        data.append(row)
    df = pd.DataFrame(data, columns=['Column1', 'Column2'])
    return df

def main():
    df = create_dataframe()

    last_two_rows = df.tail(2)

    series = last_two_rows.iloc[:, 1]

    print("Series extracted from the second column of the last two rows:")
    print(series)

if __name__ == "__main__":
    main()
