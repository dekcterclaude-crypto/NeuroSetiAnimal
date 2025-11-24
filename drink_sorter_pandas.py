import pandas as pd

data = {
    "Напиток": ['Пепси', 'Кока-Кола', 'пепси от Ивана' 'Фанта', 'Пепси лайт', 'Кола чери', 'Фанта клубника'
                , 'Спрайт'],
    "Холодильник": [""] * 7
}

df = pd.DataFrame(data)

#фция сортировки
def assign_fridge(drink_name):
    name = drink_name.lower()
    if 'пепси' in name:  # Исправлено на нижний регистр
        return 'пепси'
    elif 'кола' in name:  # Исправлено на нижний регистр
        return 'кола'
    elif 'фанта' in name:  # Исправлено на нижний регистр
        return 'фанта'
    else:
        return 'неизвестно'  # Исправлена опечатка

df['Холодильник'] = df['Напиток'].apply(assign_fridge)

print(df)