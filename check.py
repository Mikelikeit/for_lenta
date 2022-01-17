import pandas as pd


def check_domains():
    # функция для проверки доменов
    competition_file = pd.read_excel('competition.xlsx')
    domains_file = pd.read_excel('domains.xlsx')
    list_name_col_domains_file = domains_file.columns.values.tolist()  # список всех названий столбцов из domains.xlsx
    list_name_col_competition_file = competition_file.columns.values.tolist() # список всех названий столбцов из competition.xlsx
    final_list_name = list(set(list_name_col_domains_file).intersection(list_name_col_competition_file))
    final_list_name.sort()
    data_cf = []  # формируем список всех данных из столбцов нужных нам
    try:
        for dom_col in final_list_name:
            data = set(competition_file[dom_col].tolist())
            n_d = []
            for i in data:
                n_d.append(i)
            data_cf.append(n_d)
        n_d1 = []  # список списков data_cf из финальных даных с ошибками или новых
        all_lst_dom = [domains_file[dom_col].tolist() for dom_col in final_list_name]
        for i in range(len(data_cf)):
            n_d1.append([df_value for df_value in data_cf[i] if
                         df_value not in all_lst_dom[i]])  # делаем проверку на совпадение
        final_data_cf = dict(zip(final_list_name, n_d1))  # объединяем 2 списка в словарь
        # формируем эксель с новыми даными или ошибками

        for y in range(len(final_list_name)):
            df = [pd.DataFrame({f'{dom}': final_data_cf[f'{dom}']}) for dom in final_list_name]
            all_df = pd.concat(df, axis=1)
            all_df.to_excel('./new_domains.xlsx')

    except Exception as e:
        print(
            f'Упс, какая-то ощибка {e}. Обратитесь к разработчику ПО')


def main():
    check_domains()


if __name__ == '__main__':
    main()
