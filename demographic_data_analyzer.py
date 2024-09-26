import pandas as pd

def calculate_demographic_data(print_data=True):
    # Ler dados do arquivo
    df = pd.read_csv('adult.data.csv')  # Certifique-se de que o caminho do arquivo está correto

    # Contar quantas pessoas de cada raça estão representadas neste conjunto de dados
    race_count = df['race'].value_counts()

    # Calcular a idade média dos homens
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Calcular a porcentagem de pessoas que possuem diploma de bacharel
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Cálculos para educação superior e salário
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)
    
    lower_education = ~higher_education
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # Calcular o número mínimo de horas que uma pessoa trabalha por semana
    min_work_hours = df['hours-per-week'].min()

    # Calcular a porcentagem de pessoas que trabalham o número mínimo de horas e têm um salário >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # Cálculos para o país com a maior porcentagem de pessoas que ganham >50K
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack().fillna(0)
    
    # Calcular porcentagens e arredondá-las para uma casa decimal
    highest_earning_country_percentage = (country_salary['>50K'] * 100).round(1).max()
    
    # Obter o nome do país com a maior porcentagem
    highest_earning_country = country_salary['>50K'].idxmax()

    # Identificar a ocupação mais popular na Índia para aqueles que ganham >50K
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    if print_data:
        print("Número de cada raça:\n", race_count) 
        print("Idade média dos homens:", average_age_men)
        print(f"Porcentagem com diplomas de Bacharel: {percentage_bachelors}%")
        print(f"Porcentagem com educação superior que ganham >50K: {higher_education_rich}%")
        print(f"Porcentagem sem educação superior que ganham >50K: {lower_education_rich}%")
        print(f"Tempo mínimo de trabalho: {min_work_hours} horas/semana")
        print(f"Porcentagem de ricos entre aqueles que trabalham menos horas: {rich_percentage}%")
        print("País com a maior porcentagem de ricos:", highest_earning_country)
        print(f"Maior porcentagem de ricos em um país: {highest_earning_country_percentage}%")
        print("Principais ocupações na Índia:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }