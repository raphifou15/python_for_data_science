from load_csv import load
import matplotlib.pyplot as plt


def extract_years_values(data):
    """
    Extract the years and values from the DataFrame
    :param data: pd.DataFrame
    :return: tuple
    """
    data_x = data.columns.tolist()
    data_x = [int(num) for num in data_x]
    data_y = data.values[0].tolist()
    data_y = [float(num[:-1]) for num in data_y]
    return data_x, data_y


def filter_country_data(data, country):
    """
    Filter the data for a specific country and drop the 'country' column.
    :param data: pd.DataFrame
    :param country: str
    :return: pd.DataFrame
    """
    country_data = data[data["country"] == country]
    return country_data.drop(columns=["country"])


def filter_years(data, start_year=1800, end_year=2050):
    """
    Filter the columns of the DataFrame to include only the specified range
    of years.
    :param data: pd.DataFrame
    :param start_year: int
    :param end_year: int
    :return: pd.DataFrame
    """
    return data.loc[
        :, [col for col in data.columns if start_year <= int(col) <= end_year]
    ]


def aff_pop(data):
    """
    Plot the population of France and Belgium over the years
    :param data: pd.DataFrame
    :return None
    """
    try:
        france_data = filter_country_data(data, "France")
        belgium_data = filter_country_data(data, "Belgium")

        france_data = filter_years(france_data)
        belgium_data = filter_years(belgium_data)

        fr_x, fr_y = extract_years_values(france_data)
        be_x, be_y = extract_years_values(belgium_data)

        plt.figure(figsize=(12, 6))
        plt.plot(fr_x, fr_y, label="France", color="green")
        plt.plot(be_x, be_y, label="Belgium", color="blue")
        tick_positions = list(range(1800, 2050, 40))
        tick_positions2 = [i for i in range(20, 61, 20)]
        plt.xlabel("Years")
        plt.ylabel("Population")
        plt.xticks(ticks=tick_positions, rotation=45)
        plt.yticks(
            ticks=tick_positions2,
            labels=[f"{i}M" for i in tick_positions2],
            rotation=45,
        )
        plt.title("Population Projections")
        plt.legend(loc="lower right")
        plt.show()

    except Exception as error:
        raise error


def main():
    """
    Main function
    load the data and plot the population of France and Belgium over the years
    :return None
    """
    data = load("population_total.csv")
    if data is None:
        return
    try:
        aff_pop(data)
    except Exception as error:
        print(f"error happend {error}")
        return
    except KeyboardInterrupt:
        print("Process interupted by user.")
        plt.close("all")
    return


if __name__ == "__main__":
    main()
