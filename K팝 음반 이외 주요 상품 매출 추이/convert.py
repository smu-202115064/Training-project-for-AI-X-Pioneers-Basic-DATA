import dataclasses
import pathlib

import pandas as pd  # pip install pandas


DATA_DIR = pathlib.Path(__file__).resolve().parent


@dataclasses.dataclass
class Row:
    판매수량: int
    상품매출액: int
    구분: str
    연도: int


rows = []
rows.append(Row(73135, 2339583996, '응원봉', 2019))
rows.append(Row(7901, 132276660, '응원 액세서리', 2019))
rows.append(Row(1246, 19501647, '슬로건', 2019))
rows.append(Row(88456, 2632070118, '응원봉', 2020))
rows.append(Row(21777, 345265646, '응원 액세서리', 2020))
rows.append(Row(1362, 6606992, '슬로건', 2020))
rows.append(Row(15971, 504216499, '응원봉', 2021))
rows.append(Row(6665, 114680484, '응원 액세서리', 2021))
rows.append(Row(410, 5155300, '슬로건', 2021))


df = pd.DataFrame({
    '판매수량':    [r.판매수량 for r in rows],
    '상품매출액':  [r.상품매출액 for r in rows],
    '구분':        [r.구분 for r in rows],
    '연도':        [r.연도 for r in rows],
})

df.to_csv(str(DATA_DIR / 'data.csv'), index=False, encoding='utf-8')
