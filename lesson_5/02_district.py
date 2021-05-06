# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()



from district.central_street.house1 import room1 as dc_h1_r1
from district.central_street.house1 import room2 as dc_h1_r2
from district.central_street.house2 import room1 as dc_h2_r1
from district.central_street.house2 import room2 as dc_h2_r2
from district.soviet_street.house1 import room1 as ss_h1_r1
from district.soviet_street.house1 import room2 as ss_h1_r2
from district.soviet_street.house2 import room1 as ss_h2_r1
from district.soviet_street.house2 import room2 as ss_h2_r2

m_s = []
m_s += dc_h1_r1.folks
m_s += dc_h1_r2.folks
m_s += dc_h2_r1.folks
m_s += dc_h2_r2.folks
m_s += ss_h1_r1.folks
m_s += ss_h1_r2.folks
m_s += ss_h2_r1.folks
m_s += ss_h2_r2.folks

print("На районе живут", ", ".join(m_s))

