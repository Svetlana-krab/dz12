#Counting Point Mutations
def hamming_distance(f: str, s:str) -> int:
    assert len(f)==len(s), f"Строки разной длины: Первая: {len(f)}; Вторая: {len(s)}"
    for nucleotide in f:
        assert nucleotide in "ACGT", f"Символ '{nucleotide}' в первой стороке не является нуклеотидом"
    for nucleotide in s:
        assert nucleotide in "ACGT", f"Символ '{nucleotide}' во второй стороке не является нуклеотидом"

    distance = 0
    for i in range(len(f)):
        if f[i] != s[i]:
            distance += 1
    return distance

print("Введите 2 строки ДНК(сначала одну -> Enter -> затем вторую)")
f=input().upper()
s=input().upper()

result=hamming_distance(f,s)
print(f"Расстояние Хэмминга: {result}")

with open("Counting_Point_Mutations.txt","w", encoding="utf-8") as file:
    file.write(f"Первая строка: {f}\n")
    file.write(f"Вторая строка: {s}\n")
    file.write(f"Расстояние Хэмминга: {result}\n")
