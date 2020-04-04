

def add_derived_titles(df):
    titles = df.Name.str.extract(' ([A-Za-z]+)\.', expand=False)

    titles = titles.replace(['Lady', 'Countess', 'Capt', 'Col',
                             'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    titles = titles.replace(['Mlle', 'Ms'], 'Miss')
    titles = titles.replace('Mme', 'Mrs')
    df['Title'] = titles
    return df
