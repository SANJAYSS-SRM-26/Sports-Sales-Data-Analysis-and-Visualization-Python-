import pandas as pd
import matplotlib.pyplot as plt


def main():
    print("\nMAIN MENU")
    print("1. Display DataFrame")
    print("2. Data Analysis")
    print("3. Visualizing the Data")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    while ch != 4:
        if ch == 1:
            DisplayDataFrame()
        elif ch == 2:
            DataAnalysis()
        elif ch == 3:
            VisualizeData()
        else:
            print("Invalid choice")

        ch = int(input("\nEnter your choice: "))

    print("Exiting...")

def DisplayDataFrame():
    print(df)

def DataAnalysis():
    print("\nDATA ANALYSIS MENU")
    print("1. Minimum Quantity")
    print("2. Maximum Quantity")
    print("3. Sum of Total")

    ch = int(input("Enter your choice: "))

    while ch != 4:
        if ch == 1:
            MinQuantity()
        elif ch == 2:
            MaxQuantity()
        elif ch == 3:
            SumTotal()
        else:
            print("Invalid choice")

        ch = int(input("\nEnter your choice: "))

def MinQuantity():
    print("Minimum Units Sold:", df['Quantity'].min())

def MaxQuantity():
    print("Maximum Units Sold:", df['Quantity'].max())

def SumTotal():
    print("Sum of Total:", df['Total'].sum())

def VisualizeData():
    print("\nGRAPHS")
    print("1. Line Graph")
    print("2. Vertical Bar Graph")
    print("3. Exit")

    ch = int(input("Enter your choice: "))

    while ch != 3:
        if ch == 1:
            LineGraph()
        elif ch == 2:
            VerticalBarGraph()
        else:
            print("Invalid choice")

        ch = int(input("\nEnter your choice: "))

def LineGraph():
    plt.plot(df['Customer Name'], df['Total'], color='blue', linewidth=2)
    plt.xlabel('Customer Name')
    plt.ylabel('Total')
    plt.title('Sports Sales Report - Line Graph')
    plt.show()

def VerticalBarGraph():
    plt.bar(df['Customer Name'], df['Total'], color='green')
    plt.xlabel('Customer Name')
    plt.ylabel('Total')
    plt.title('Sports Sales Report - Vertical Bar Graph')
    plt.xticks(rotation=90)
    plt.show()

if __name__ == "__main__":
    main()
