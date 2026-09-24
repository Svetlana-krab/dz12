#Mendel’s First Law
def dominant_probability(k:int,m:int,n:int)->float:
    """
aa*aa                               1
n/all (n-1)/all-1
Aa*aa                  aa*Aa       0.5
(m/all)*(n/(all-1)    (n/all)*(m/(all-1)
Aa*Aa                              0.25
(m/all) * ((m-1)/(all-1))"""

    assert isinstance(k,int) and k>=0, "k не должно быть отрицательным"
    assert isinstance(m,int) and m>=0, "m не должно быть отрицательным"
    assert isinstance(n,int) and n>=0, "n не должно быть отрицательным"

    all=k+m+n
    assert all>=2, "В популяции должно быть хотя бы 2 особи(пол не важен))"

    p_aa_aa=(n/all) *((n-1)/(all-1))*1
    p_Aa_aa=2*(m/all)*(n/(all-1))*0.5
    p_Aa_Aa=(m/all) * ((m-1)/(all-1))*0.25
    p_recessive= p_aa_aa + p_Aa_aa + p_Aa_Aa
    P_dominant= 1-p_recessive
    return P_dominant
print("Введите k,m,n через пробел:")
k,m,n=map(int,input().split())
result= dominant_probability(k,m,n)
print(f"Вероятность доминантного потомства: {result:.5f}")

output_path="Mendel_First_Law.txt"
with open(output_path, "a", encoding="utf-8") as file:
    file.write(f"k={k}, m={m}, n={n}\n")
    file.write(f"Вероятность доминантного потомства: {result:.5f}\n")
    file.write(f"="*40+"\n")
