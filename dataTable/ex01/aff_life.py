from load_csv import load
import matplotlib.pyplot as plt


def aff_life(data):
    """
    Plot the life expectancy of France over the years
    :param data: pd.DataFrame
    :return None
    """
    try:
        france_data = data[data["country"] == "France"]
        all_data_execpt_country = france_data.drop(columns=["country"])
        print(all_data_execpt_country)
        x = all_data_execpt_country.columns.tolist()
        y = all_data_execpt_country.values[0].tolist()

        x = [int(num) for num in x]

        max_year = max(x)
        min_year = min(x)
        print(f"max year: {max_year}")
        intval = 40
        tick_positions = list(
            range(min_year - (min_year % intval) + 0, max_year, intval)
        )

        plt.figure(figsize=(12, 6))
        plt.plot(x, y)
        plt.xlabel("Years")
        plt.ylabel("Life expectancy")
        plt.title("France life expectancy Projections")
        plt.xticks(ticks=tick_positions, rotation=45)
        plt.show()

    except Exception as error:
        raise error


def main():
    """
    Main function
    load the data and plot the life expectancy of France over the years
    :return None
    """
    data = load("life_expectancy_years.csv")
    if data is None:
        return
    try:
        aff_life(data)
    except Exception as error:
        print(f"error happend {error}")
        return
    except KeyboardInterrupt:
        print("Process interupted by user.")
        plt.close("all")
    return


if __name__ == "__main__":
    main()
