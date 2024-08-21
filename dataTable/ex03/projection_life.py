from load_csv import load
import matplotlib.pyplot as plt


def projection_life(data_income, data_life):
    data_income = data_income.dropna(subset=["1900"])
    data_life = data_life.dropna(subset=["1900"])
    common_countries = set(data_income["country"]).intersection(
        set(data_life["country"])
    )
    data_income = data_income[data_income["country"].isin(common_countries)]
    data_life = data_life[data_life["country"].isin(common_countries)]

    # parse data_income 1900
    data_income_1900 = data_income.loc[:, "1900"].to_list()
    # parse data_life 1900
    data_life_1900 = data_life.loc[:, "1900"].to_list()

    tick_positions = [300, 1000, 10000]
    # plot

    plt.figure(figsize=(12, 6))
    plt.scatter(data_income_1900, data_life_1900)
    plt.xticks(ticks=tick_positions, rotation=45)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")
    plt.grid(True)
    plt.show()

    print(data_income_1900)
    print(data_life_1900)
    return


def main():
    data_income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if data_income is None:
        return
    data_life = load("life_expectancy_years.csv")
    if data_life is None:
        return

    try:
        projection_life(data_income, data_life)
        return
    except Exception as error:
        print(f"error happend {error}")
        return
    except KeyboardInterrupt:
        print("Process interupted by user.")
        plt.close("all")
    return


if __name__ == "__main__":
    main()
