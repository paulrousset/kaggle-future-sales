import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from googletrans import Translator


def plot_quantiles(df: pd.DataFrame, var: float, title: str, width: int = 12, height: int = 4,
                   label_size: float = 8.5) -> None:
    """Plotting quantiles for a given variable."""
    quantiles = df[var].quantile([0.01, 0.05, 0.1, 0.25, 0.5, .75, .9, .95, 0.99])

    sns.set_context('paper')
    sns.set_color_codes('muted')
    f, ax = plt.subplots(figsize=(width, height))
    sns.barplot(x=quantiles.values, y=quantiles.index.astype(str),  color='b', edgecolor='w')
    sns.despine(bottom=True)
    ax.bar_label(ax.containers[0], size=label_size, fmt='%1.0f')
    if title:
        plt.title(title)
    plt.show()


def plot_histograms(volume: pd.DataFrame, sales: pd.DataFrame, title1: str, title2: str, share_axis: bool = True,
                    width: int = 15, height: int = 6) -> None:
    """Plotting two histograms (volumes & sales)."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(width, height))
    if not share_axis:
        fig.subplots_adjust(hspace=.6)
    # Volume Dimension
    volume.plot.bar(ax=ax1)
    ax1.set_title(title1)
    ax1.legend().set_visible(False)
    ax1.set(xlabel=None)
    # Sales Dimension
    if share_axis:
        sales.plot.bar(ax=ax2, sharex=ax1)
    else:
        sales.plot.bar(ax=ax2)
    ax2.set_title(title2)
    ax2.legend().set_visible(False)
    ax2.set(xlabel=None)


def get_quantiles_from_values(df: pd.DataFrame, variable: float, values: [], unit: str) -> None:
    """Print quantiles corresponding to given values."""
    for value in values:
        quantile = stats.percentileofscore(df[variable], value).round(1)
        print("{}% of cases have {} under {}".format(quantile, unit, value))


categories_english = {
    'Аксессуары' : 'Accessories',
    'Гарнитуры/Наушники':'Headsets/Headphones',
    'Билеты (Цифра)':'Tickets (Digital)',
    'Доставка товара':'Delivery of Goods',
    'Игровые консоли':'Game consoles',
    'Кино, Музыка, Игры':'Movie, Music, Games',
    'Игры ':'Games',
    'Цифра':'Number',
    'Карты оплаты':'Payment Cards',
    'Кино':'Movie',
    'Книги':'Books',
    'Артбуки':'Artbooks',
    'энциклопедии':'Encyclopedia', 
    'Аудиокниги':'Audiobooks',
    'Бизнес':'Business',
    'литература':'litterature',
    'Комиксы':'Comics', 
    'манга':'Manga',
    'Компьютерная':'Computer',
    'Методические':'Methodical',
    'материалы':'Materials',
    'Открытки':'Postcards',
    'наклейки':'stickers',
    'Познавательная':'Cognitive',
    'Путеводители':'Guides',
    'Художественная':'Artistic',
    'Музыкальное видео':'Music Video',
    'Музыка':'Music',
    'Подарки':'Gifts',
    'Программы':'Programs',
    'Служебные':'Service',
    'Билеты':'Tickets',
    'Чистые носители':'Pure media',
    'шпиль' : 'Spire',
    'штучные':'Piece',
    'Элементы питания':'Batteries',
    'Прочие':'Other',
    'Обучающие':'Educational',
    'Для дома и офиса':'For Home and Office',
    'Предприятие':'Company',
    'Фигурки':'Figurines',
    'в навеску':'in bulk',
    'Сувениры':'Souvenirs',
    'Настольные игры':'Board Games',
    'Сумки, Альбомы, Коврики д/мыши':'Bags, Albums, Mouse pads',
    'Сертификаты, услуги':'Certificates, services',
    'Мягкие игрушки':'Stuffed toys',
    'Гаджеты, роботы, спорт':'Gadgets, robots, sports',
    'Атрибутика':'paraphernalia',
    'Подарочные':'Gift',
    'Винил':'Vinyl',
    'производства': 'Production',
    'фирменного':'Branded',
    'локального':'Local',
    'Коллекционные издания':'Collectors Editions',
    'Коллекционное':'Collectible',
    'издания':'Editions',
    'Стандартные':'Standard',
    'Дополнительные':'Additional',
    'для игр':'for games',   
    'компактные':'Compact',
    'Развитие':'Development',
}


shops_english = {
    '!Якутск Орджоникидзе, 56 фран': 'Iakoutsk -',
    '!Якутск ТЦ "Центральный" фран': 'Iakoutsk -',
    'Адыгея ТЦ "Мега"':'Adygea - Mega Mall',
    'Балашиха ТРК "Октябрь-Киномир"':'',
    'Волжский ТЦ "Волга Молл"':'Volgograd - Volga Mall',
    'Вологда ТРЦ "Мармелад"':'Vologda - Marmelad',
    'Воронеж (Плехановская, 13)':'Voronezh - Plekhanovskaya',
    'Воронеж ТРЦ "Максимир"': 'Voronezh - Maksimir',
    'Воронеж ТРЦ Сити-Парк "Град"': 'Voronezh - City Park Grad',
    'Выездная Торговля':'Outbound Trade',
    'Жуковский ул. Чкалова 39м?':'Zhukovsky st. Chkalova 39m²',
    'Жуковский ул. Чкалова 39м²':'Zhukovsky st. Chkalova 39m²',
    'Интернет-магазин ЧС':'Internet - EShop',
    'Казань ТЦ "Бехетле"':'Kazan - Bekhetle Mall',
    'Казань ТЦ "ПаркХаус" II':'Kazan - Parkhouse II Mall',
    'Калуга ТРЦ "XXI век"':'Kalouga - 21st Century',
    'Коломна ТЦ "Рио"':'Kolomna (Moscow) - Rio',
    'Красноярск ТЦ "Взлетка Плаза"':'Krasnoiark - Vzletka Plaza Mall',
    'Красноярск ТЦ "Июнь"':'Krasnoiark - June Mall',
    'Курск ТЦ "Пушкинский"':'Kursk - Pushkinsky Mall',
    'Москва "Распродажа"':'Moscow - Sale',
    'Москва МТРЦ "Афи Молл"':'Moscow - Afi Mall',
    'Москва Магазин С21':'Moscow - Store C21',
    'Москва ТК "Буденовский" (пав.А2)':'Moscow - Budenovskiy - A2)',
    'Москва ТК "Буденовский" (пав.К7)':'Moscow - Budenovskiy - K7)',
    'Москва ТРК "Атриум"':'Moscow - Atrium',
    'Москва ТЦ "Ареал" (Беляево)':'Moscow - Areal (Belyaevo)',
    'Москва ТЦ "МЕГА Белая Дача II"':'Moscow - Mega Belaya Dacha II',
    'Москва ТЦ "МЕГА Теплый Стан" II':'Moscow - Mega Teply Stan II',
    'Москва ТЦ "Новый век" (Новокосино)':'Moscow - New Age (Novokosino)',
    'Москва ТЦ "Перловский"':'Moscow - Perlovskiy',
    'Москва ТЦ "Семеновский"':'Moscow - Semenovsky',
    'Москва ТЦ "Серебряный Дом"':'Moscow - Silver House',
    'Мытищи ТРК "XL-3"':'Mytishchi - XL-3',
    'Н.Новгород ТРЦ "РИО"':'Nijni Novgorod - Rio',
    'Н.Новгород ТРЦ "Фантастика"':'Nijni Novgorod - Fantastica',
    'Новосибирск ТРЦ "Галерея Новосибирск"':'Novosibirsk - Gallery Novosibirsk',
    'Новосибирск ТЦ "Мега"':'Novosibirsk - Mega',
    'Омск ТЦ "Мега"':'Omsk - Mega',
    'РостовНаДону ТРК "Мегацентр Горизонт"':'Rostov - Mega Center Horizon',
    'РостовНаДону ТРК "Мегацентр Горизонт" Островной':'Rostov - Mega Center Horizon - Ostrovnoy',
    'РостовНаДону ТЦ "Мега"':'Rostov - Mega',
    'СПб ТК "Невский Центр"': 'Saint-Petersburg : Nevskiy Center',
    'СПб ТК "Сенная"': 'Saint-Petersburg : Sennaya',
    'Самара ТЦ "Мелодия"': 'Samara - Melody',
    'Самара ТЦ "ПаркХаус"': 'Samara - Parkhouse',
    'Сергиев Посад ТЦ "7Я"': 'Sergiev Posad - 7Ya',
    'Сургут ТРЦ "Сити Молл"':'Sourgout - City Mall',
    'Томск ТРЦ "Изумрудный Город"':'Tomsk - Emerald City',
    'Тюмень ТРЦ "Кристалл"':'Tyumen - Crystal',
    'Тюмень ТЦ "Гудвин"':'Tyumen - Goodwin',
    'Тюмень ТЦ "Зеленый Берег"':'Tyumen - Green Coast',
    'Уфа ТК "Центральный"':'Ufa - Central',
    'Уфа ТЦ "Семья" 2':'Ufa - Semya 2',
    'Цифровой склад 1С-Онлайн':'Internet - Digital Warehouse 1C Online',
    'Чехов ТРЦ "Карнавал"':'Chekhov - Carnival',
    'Якутск Орджоникидзе, 56':'Yakutsk - Ordzhonikidze',
    'Якутск ТЦ "Центральный"':'Yakutsk - Central',
    'Ярославль ТЦ "Альтаир"':'Yaroslavl - Altair',
}