import random
import math
import numpy as np


generasi = int(input("Masukan berapa generasi yang ingin anda buat uji coba : "))
metode = int(
    input(
        "\nSilahkan pilih metode untuk menghitung\n1. µ,λ\n2. µ+λ\n3. µ/r,λ\n4. µ/r+λ\nMasukan Input Angka: "
    )
)
jenis = int(
    input(
        "\nSilahkan pilih jenis ayam\n1. Broiler Starter\n2. Broiler Finihser\n3. Petelur Starter\n4. Petelur Layer\n5. Petelur Finisher\nMasukan angka: "
    )
)
# Membuat fungsi untuk menghitung nilai fungsi
loop = False


class BroilerS:
    protein = 19
    lemak = 7.4
    serat = 6
    kalsium1 = 0.90
    kalsium2 = 1.20
    fosfor1 = 0.60
    fosfor2 = 1
    em = 2900


class BroilerF:
    protein = 18
    lemak = 8
    serat = 6
    kalsium1 = 0.90
    kalsium2 = 1.20
    fosfor1 = 0.60
    fosfor2 = 1
    em = 2900


class PetelurS:
    protein = 20
    lemak1 = 2.5
    lemak2 = 7
    serat = 6.5
    kalsium1 = 1.05
    kalsium2 = 1.1
    fosfor = 0.48
    em = 2980



class PetelurL:
    protein = 18
    lemak1 = 3.5
    lemak2 = 3.7
    serat = 7
    kalsium1 = 3.25
    kalsium2 = 4
    fosfor = 0.40
    em = 2750


class PetelurF:
    protein = 17
    lemak1 = 2.5
    lemak2 = 7
    serat = 6.5
    kalsium1 = 3.25
    kalsium2 = 4
    fosfor1 = 0.33
    fosfor2 = 0.37
    em = 2750


class jagung:
    protein = 8.6
    lemak = 3.9
    serat = 2
    kalsium = 0.09
    fosfor = 0.3
    em = 3370


class sorgum:
    protein = 10
    lemak = 2.8
    serat = 2
    kalsium = 0.4
    fosfor = 2.13
    em = 3250


class beras:
    protein = 8
    lemak = 1.7
    serat = 9
    kalsium = 0.09
    fosfor = 0.08
    em = 2660


class mkelapa:
    protein = 14.1
    lemak = 8.12
    serat = 23.32
    kalsium = 0.29
    fosfor = 0.79
    em = 1450
class baru: #AMPAS TAHU
    protein = 18.7
    lemak = 5.32
    serat = 14.53
    kalsium = 0.32
    fosfor = 0.45
    em = 0


# FUNGSI MENGHITUG PENALTI BROILER
child = []


def penalty_broiler(
    x1, x2, x3, x4,x5, protein, lemak, serat, kalsium1, kalsium2, fosfor1, fosfor2, em,
):
    penalty_protein = (
        x1 * sorgum.protein
        + x2 * jagung.protein
        + x3 * mkelapa.protein
        + x4 * baru.protein
        + x5 * beras.protein
    )

    penalty_lemak = (
        x1 * sorgum.lemak
        + x2 * jagung.lemak
        + x3 * mkelapa.lemak
        + x4 * baru.lemak
        + x5 * beras.lemak
    )

    penalty_serat = (
        x1 * sorgum.serat
        + x2 * jagung.serat
        + x3 * mkelapa.serat
        + x4 * baru.serat
        + x5 * beras.serat
    )

    penalty_kalsium = (
        x1 * sorgum.kalsium
        + x2 * jagung.kalsium
        + x3 * mkelapa.kalsium
        + x4 * baru.kalsium
        + x5 * beras.kalsium
    )

    penalty_fosfor = (
        x1 * sorgum.fosfor
        + x2 * jagung.fosfor
        + x3 * mkelapa.fosfor
        + x4 * baru.fosfor
        + x5 * beras.fosfor
    )

    penalty_em = (
        x1 * sorgum.em
        + x2 * jagung.em
        + x3 * mkelapa.em
        + x4 * baru.em
        + x5 * beras.em
    )

    if penalty_protein < protein:
        penalty_protein = abs(protein - penalty_protein)
    else:
        penalty_protein = 0
    if penalty_em < em:
        penalty_em = abs(em - penalty_em)
    else:
        penalty_em = 0
    if penalty_lemak > lemak:
        penalty_lemak = abs(lemak - penalty_lemak)
    else:
        penalty_lemak = 0

    if penalty_serat > serat:
        penalty_serat = abs(serat - penalty_serat)
    else:
        penalty_serat = 0

    if penalty_kalsium < kalsium1:
        penalty_kalsium = abs(kalsium1 - penalty_kalsium)
    elif penalty_kalsium > kalsium2:
        penalty_kalsium = abs(kalsium2 - penalty_kalsium)
    else:
        penalty_kalsium = 0

    if penalty_fosfor < fosfor1:
        penalty_fosfor = abs(kalsium1 - penalty_fosfor)
    elif penalty_fosfor > fosfor2:
        penalty_fosfor = abs(kalsium2 - penalty_fosfor)
    else:
        penalty_fosfor = 0

    total_penalty = (
        penalty_protein
        + penalty_lemak
        + penalty_serat
        + penalty_kalsium
        + penalty_fosfor
        + penalty_em
    )
    satu = float(1.00)
    hasil = np.power(total_penalty, -1)

    return hasil

# MENGHITUNG PENA;TY PETELUR
def penalty_petelur(
    x1, x2, x3, x4, x5, protein, lemak1, lemak2, serat, kalsium1, kalsium2, fosfor1, fosfor2, em
):
    penalty_protein = (
        x1 * sorgum.protein
        + x2 * jagung.protein
        + x3 * mkelapa.protein
        + x4 * baru.protein
        + x5 * beras.protein
    )

    penalty_lemak = (
        x1 * sorgum.lemak
        + x2 * jagung.lemak
        + x3 * mkelapa.lemak
        + x4 * baru.lemak
        + x5 * beras.lemak
    )

    penalty_serat = (
        x1 * sorgum.serat
        + x2 * jagung.serat
        + x3 * mkelapa.serat
        + x4 * baru.serat
        + x5 * beras.serat
    )

    penalty_kalsium = (
        x1 * sorgum.kalsium
        + x2 * jagung.kalsium
        + x3 * mkelapa.kalsium
        + x4 * baru.kalsium
        + x5 * beras.kalsium
    )

    penalty_fosfor = (
        x1 * sorgum.fosfor
        + x2 * jagung.fosfor
        + x3 * mkelapa.fosfor
        + x4 * baru.fosfor
        + x5 * beras.fosfor
    )

    penalty_em = (
        x1 * sorgum.em
        + x2 * jagung.em
        + x3 * mkelapa.em
        + x4 * baru.em
        + x5 * beras.em
    )

    if penalty_protein != protein:
        penalty_protein = abs(protein - penalty_protein)
    else:
        penalty_protein = 0

    if penalty_lemak < lemak1:
        penalty_lemak = abs(lemak1 - penalty_lemak)
    elif penalty_lemak > lemak2:
        penalty_lemak = abs(lemak2 - penalty_lemak)
    else:
        penalty_lemak = 0

    if penalty_serat > serat:
        penalty_serat = abs(serat - penalty_serat)
    else:
        penalty_serat = 0

    if penalty_kalsium < kalsium1:
        penalty_kalsium = abs(kalsium1 - penalty_kalsium)
    elif penalty_kalsium > kalsium2:
        penalty_kalsium = abs(kalsium2 - penalty_kalsium)
    else:
        penalty_kalsium = 0

    if penalty_fosfor != fosfor1:
        penalty_fosfor = abs(fosfor1 - penalty_fosfor)
    else:
        penalty_fosfor = 0

    if jenis == 5:
        if penalty_fosfor < fosfor1:
            penalty_fosfor = abs(fosfor1 - penalty_fosfor)
        elif penalty_fosfor > fosfor2:
            penalty_fosfor = abs(fosfor2 - penalty_fosfor)
        else:
            penalty_kalsium = 0

    if penalty_em < em:
        penalty_em = abs(em - penalty_em)
    elif penalty_em > em:
        penalty_em = abs(em - penalty_em)
    else:
        penalty_em = 0

    total_penalty = (
        penalty_protein
        + penalty_lemak
        + penalty_serat
        + penalty_kalsium
        + penalty_fosfor
        + penalty_em
    )

    satu = float(1.00) # petelur
    hasil = (10 * satu) / (total_penalty * 10)

    return hasil


## fungsi memasukan ke tabel child broiler
def generate_child(
    parent_utama,
    jumlah_child_per_parent,
    jumlah_parent,
    protein,
    lemak,
    serat,
    kalsium1,
    kalsium2,
    fosfor1,
    fosfor2,
    em,
):

    for i in range(jumlah_parent):
        parent = parent_utama[i]
        for j in range(jumlah_child_per_parent):
            # Hitung x dan sigma untuk child
            sigma = parent[5:10]  # nilai sigma dari parent
            child_x = hitung_x(parent[:5], sigma)
            child_fitness = penalty_broiler(
                child_x[0],
                child_x[1],
                child_x[2],
                child_x[3],
                child_x[4],
                protein,
                lemak,
                serat,
                kalsium1,
                kalsium2,
                fosfor1,
                fosfor2,
                em,
            )

            if child_fitness < float(parent[10]):
                new_sigma = [s * 0.9 for s in sigma]
            else:
                new_sigma = [s * 1.1 for s in sigma]

            child.append(
                [
                    "C{}".format(len(child) + 1),
                    "P{}".format(i + 1),
                    "{:.4f}".format(float(child_x[0])),
                    "{:.4f}".format(float(child_x[1])),
                    "{:.4f}".format(float(child_x[2])),
                    "{:.4f}".format(float(child_x[3])),
                    "{:.4f}".format(float(child_x[4])),
                    "{:.4f}".format(float(new_sigma[0])),
                    "{:.4f}".format(float(new_sigma[1])),
                    "{:.4f}".format(float(new_sigma[2])),
                    "{:.4f}".format(float(new_sigma[3])),
                    "{:.4f}".format(float(new_sigma[4])),
                    (child_fitness),
                ]
            )

    return child


## memasukan ke tabel child untuk petelur
def generate_child_petelur(
    parent_utama,
    jumlah_child_per_parent,
    protein,
    lemak1,
    lemak2,
    serat,
    kalsium1,
    kalsium2,
    fosfor1,
    fosfor2,
    em,
):

    for i in range(jumlah_parent):
        parent = parent_utama[i]
        for j in range(jumlah_child_per_parent):
            # Hitung x dan sigma untuk child
            sigma = parent[5:10]  # nilai sigma dari parent
            child_x = hitung_x(parent[:5], sigma)
            child_fitness = penalty_petelur(
                child_x[0],
                child_x[1],
                child_x[2],
                child_x[3],
                child_x[4],
                protein,
                lemak1,
                lemak2,
                serat,
                kalsium1,
                kalsium2,
                fosfor1,
                fosfor2,
                em,
            )

            if child_fitness < float(parent[10]):
                new_sigma = [s * 0.9 for s in sigma]
            else:
                new_sigma = [s * 1.1 for s in sigma]

            child.append(
                [
                    "C{}".format(len(child) + 1),
                    "P{}".format(i + 1),
                    "{:.4f}".format(float(child_x[0])),
                    "{:.4f}".format(float(child_x[1])),
                    "{:.4f}".format(float(child_x[2])),
                    "{:.4f}".format(float(child_x[3])),
                    "{:.4f}".format(float(child_x[4])),
                    "{:.4f}".format(float(new_sigma[0])),
                    "{:.4f}".format(float(new_sigma[1])),
                    "{:.4f}".format(float(new_sigma[2])),
                    "{:.4f}".format(float(new_sigma[3])),
                    "{:.4f}".format(float(new_sigma[4])),
                    (child_fitness),
                ]
            )

    return child


def generate_child_petelur_v2(
    parent_utama,
    jumlah_child_per_parent,
    protein,
    lemak1,
    lemak2,
    serat,
    kalsium1,
    kalsium2,
    fosfor1,
    fosfor2,
    em,
):

    child = []
    jumlah_parent = len(parent_utama)

    # Generate child dari setiap kombinasi parent
    for i in range(len(parent_utama)):
        for j in range(len(parent_utama)):
            if i != j:
                parent1 = parent_utama[i]
                parent2 = parent_utama[j]

                # Menghitung sigma dan x untuk child
                child_sigma = []
                child_x = []
                for k in range(5):
                    sigma_k = (
                        np.random.uniform(low=0, high=1) * parent1[5 + k]
                        + np.random.uniform(low=0, high=1) * parent2[5 + k]
                    )
                    x_k = (
                        np.random.uniform(low=0, high=1) * parent1[k]
                        + np.random.uniform(low=0, high=1) * parent2[k]
                    )
                    child_sigma.append(sigma_k)
                    child_x.append(x_k)

                # Hitung mutasi pada x menggunakan fungsi hitung_x
                child_x = hitung_x(child_x, child_sigma)

                # Hitung fitness child
                child_fitness = penalty_petelur(
                    child_x[0],
                    child_x[1],
                    child_x[2],
                    child_x[3],
                    child_x[4],
                    protein,
                    lemak1,
                    lemak2,
                    serat,
                    kalsium1,
                    kalsium2,
                    fosfor1,
                    fosfor2,
                    em,
                )

                # Hitung sigma untuk child berdasarkan fitness
                if child_fitness < float(max(parent1[10], parent2[10])):
                    new_sigma = [s * 0.9 for s in child_sigma]
                else:
                    new_sigma = [s * 1.1 for s in child_sigma]

                child.append(
                    [
                        "C{}".format(len(child) + 1),
                        "P{}".format(i + 1),
                        "{:.4f}".format(float(child_x[0])),
                        "{:.4f}".format(float(child_x[1])),
                        "{:.4f}".format(float(child_x[2])),
                        "{:.4f}".format(float(child_x[3])),
                        "{:.4f}".format(float(child_x[4])),
                        "{:.4f}".format(float(new_sigma[0])),
                        "{:.4f}".format(float(new_sigma[1])),
                        "{:.4f}".format(float(new_sigma[2])),
                        "{:.4f}".format(float(new_sigma[3])),
                        "{:.4f}".format(float(new_sigma[4])),
                        (child_fitness),

                    ]
                )

        return child


def generate_child_v2(
    parent_utama,
    jumlah_child_per_parent,
    jumlah_parent,
    protein,
    lemak,
    serat,
    kalsium1,
    kalsium2,
    fosfor1,
    fosfor2,
    em,
):

    for i in range(len(parent_utama)):
        for j in range(len(parent_utama)):
            if i != j:
                parent1 = parent_utama[i]
                parent2 = parent_utama[j]

                # Menghitung sigma dan x untuk child
                child_sigma = []
                child_x = []
                for k in range(5):
                    sigma_k = (
                        np.random.uniform(low=0, high=1) * parent1[5 + k]
                        + np.random.uniform(low=0, high=1) * parent2[5 + k]
                    )
                    x_k = (
                        np.random.uniform(low=0, high=1) * parent1[k]
                        + np.random.uniform(low=0, high=1) * parent2[k]
                    )
                    child_sigma.append(sigma_k)
                    child_x.append(x_k)

                # Hitung mutasi pada x menggunakan fungsi hitung_x
                child_x = hitung_x(child_x, child_sigma)
                child_fitness = penalty_broiler(
                    child_x[0],
                    child_x[1],
                    child_x[2],
                    child_x[3],
                    child_x[4],
                    protein,
                    lemak,
                    serat,
                    kalsium1,
                    kalsium2,
                    fosfor1,
                    fosfor2,
                    em,
                )

                # Hitung sigma untuk child berdasarkan fitness

                if child_fitness < float(max(parent1[10], parent2[10])):
                    new_sigma = [s * 0.9 for s in child_sigma]
                else:
                    new_sigma = [s * 1.1 for s in child_sigma]

                child.append(
                    [
                        "C{}".format(len(child) + 1),
                        "P{}".format(i + 1),
                        "{:.4f}".format(float(child_x[0])),
                        "{:.4f}".format(float(child_x[1])),
                        "{:.4f}".format(float(child_x[2])),
                        "{:.4f}".format(float(child_x[3])),
                        "{:.4f}".format(float(child_x[4])),
                        "{:.4f}".format(float(new_sigma[0])),
                        "{:.4f}".format(float(new_sigma[1])),
                        "{:.4f}".format(float(new_sigma[2])),
                        "{:.4f}".format(float(new_sigma[3])),
                        "{:.4f}".format(float(new_sigma[4])),
                        (child_fitness),

                    ]
                )

        return child


def hitung_x(parent, sigma):
    child_x = []
    for i in range(5):
        r1 = np.random.uniform(0, 1)
        r2 = np.random.uniform(0, 1)
        N = math.sqrt(-2 * math.log(r1)) * math.sin(2 * math.pi * r2)
        x = parent[i] + sigma[i] * N
        if x < 0 :
          x = abs(x)
        x = max(min(x, 1), 0.0)
        child_x.append(x)
    return child_x



if loop == False:  # INPUT JUMLAH PARRENT DAN CHILD
    jumlah_parent = int(input("\nMasukkan jumlah parent: "))
    jumlah_child_per_parent = int(input("\nMasukkan jumlah child per parent: "))
    jumlah_child = jumlah_parent * jumlah_child_per_parent
while jumlah_parent <= 0 or jumlah_child_per_parent <= 0:
    print("harap masukan angka yang valid")
    jumlah_parent = int(input("Masukkan jumlah parent: "))
    jumlah_child_per_parent = int(input("Masukkan jumlah child per parent: "))
    jumlah_child = jumlah_parent * jumlah_child_per_parent
for p in range(generasi):

    ############## PROGRAM DIMULAIIIIIIIII #####################


    if loop == False:
        parent_utama = []
        # MENGHITUNG DAN MENINPUTKAN DATA KE TABEL PARENT
        for i in range(jumlah_parent):
            parent = [random.uniform(0, 1) for i in range(11)]

            if jenis == 1:
                parent[10] = penalty_broiler(
                    parent[0],
                    parent[1],
                    parent[2],
                    parent[3],
                    parent[4],
                    BroilerS.protein,
                    BroilerS.lemak,
                    BroilerS.serat,
                    BroilerS.kalsium1,
                    BroilerS.kalsium1,
                    BroilerS.fosfor1,
                    BroilerS.fosfor2,
                    BroilerS.em,
                )
            elif jenis == 2:
                parent[10] = penalty_broiler(
                    parent[0],
                    parent[1],
                    parent[2],
                    parent[3],
                    parent[4],
                    BroilerF.protein,
                    BroilerF.lemak,
                    BroilerF.serat,
                    BroilerF.kalsium1,
                    BroilerF.kalsium1,
                    BroilerF.fosfor1,
                    BroilerF.fosfor2,
                    BroilerF.em,
                )
            elif jenis == 3:
                parent[10] = penalty_petelur(
                    parent[0],
                    parent[1],
                    parent[2],
                    parent[3],
                    parent[4],
                    PetelurS.protein,
                    PetelurS.lemak1,
                    PetelurS.lemak2,
                    PetelurS.serat,
                    PetelurS.kalsium1,
                    PetelurS.kalsium1,
                    PetelurS.fosfor,
                    0,
                    PetelurS.em,
                )
            elif jenis == 4:
                parent[10] = penalty_petelur(
                    parent[0],
                    parent[1],
                    parent[2],
                    parent[3],
                    parent[4],
                    PetelurL.protein,
                    PetelurL.lemak1,
                    PetelurL.lemak2,
                    PetelurL.serat,
                    PetelurL.kalsium1,
                    PetelurL.kalsium1,
                    PetelurL.fosfor,
                    0,
                    PetelurL.em,
                )
            elif jenis == 5:
                parent[10] = penalty_petelur(
                    parent[0],
                    parent[1],
                    parent[2],
                    parent[3],
                    parent[4],
                    PetelurF.protein,
                    PetelurF.lemak1,
                    PetelurF.lemak2,
                    PetelurF.serat,
                    PetelurF.kalsium1,
                    PetelurF.kalsium1,
                    PetelurF.fosfor1,
                    PetelurF.fosfor2,
                    PetelurF.em,
                )

            parent_utama.append(parent)

    else:
        for i in range(jumlah_parent):
            parent = parent_utama[i]
            best_child = best_child_per_parent[i]
            parent[0] = float(best_child[2]) # ubah nilai x1
            parent[1] = float(best_child[3]) # ubah nilai x2
            parent[2] = float(best_child[4]) # ubah nilai x3
            parent[3] = float(best_child[5]) # ubah nilai x4
            parent[4] = float(best_child[6]) # ubah nilai sigma1
            parent[5] = float(best_child[7]) # ubah nilai sigma2
            parent[6] = float(best_child[8]) # ubah nilai sigma3
            parent[7] = float(best_child[9]) # ubah nilai sigma4
            parent[8] = float(best_child[10]) # ubah nilai fintness
            parent[9] = float(best_child[11]) # ubah nilai fintness
            parent[10] = float(best_child[12]) # ubah nilai fintness
            # #debug
            # print ("Child Fitness : \n")
            # print (parent[10])
        ###### IF UNTUK JENIS ########

    if metode != 3 and metode != 4:
        if jenis == 1:
            generate_child(
                    parent_utama,
                    jumlah_child_per_parent,
                    jumlah_parent,
                    BroilerS.protein,
                    BroilerS.lemak,
                    BroilerS.serat,
                    BroilerS.kalsium1,
                    BroilerS.kalsium1,
                    BroilerS.fosfor1,
                    BroilerS.fosfor2,
                    BroilerS.em,

            )
        elif jenis == 2:
            generate_child(
                parent_utama,
                jumlah_child_per_parent,
                jumlah_parent,
                BroilerF.protein,
                BroilerF.lemak,
                BroilerF.serat,
                BroilerF.kalsium1,
                BroilerF.kalsium2,
                BroilerF.fosfor1,
                BroilerF.fosfor2,
                BroilerF.em,
            )
        elif jenis == 3:
            generate_child_petelur(
                parent_utama,
                jumlah_child_per_parent,
                PetelurS.protein,
                PetelurS.lemak1,
                PetelurS.lemak2,
                PetelurS.serat,
                PetelurS.kalsium1,
                PetelurS.kalsium2,
                PetelurS.fosfor,
                0,
                PetelurS.em,
            )
        elif jenis == 4:
            generate_child_petelur(
                parent_utama,
                jumlah_child_per_parent,
                PetelurL.protein,
                PetelurL.lemak1,
                PetelurL.lemak2,
                PetelurL.serat,
                PetelurL.kalsium1,
                PetelurL.kalsium2,
                PetelurL.fosfor,
                0,
                PetelurL.em
            )
        elif jenis == 5:
            generate_child_petelur(
                parent_utama,
                jumlah_child_per_parent,
                PetelurF.protein,
                PetelurF.lemak1,
                PetelurF.lemak2,
                PetelurF.serat,
                PetelurF.kalsium1,
                PetelurF.kalsium2,
                PetelurF.fosfor1,
                PetelurF.fosfor2,
                PetelurF.em
            )
        #### untuk metode 3  dan 4
    if jenis == 1:
        generate_child_v2(
            parent_utama,
            jumlah_child_per_parent,
            jumlah_parent,
            BroilerS.protein,
            BroilerS.lemak,
            BroilerS.serat,
            BroilerS.kalsium1,
            BroilerS.kalsium2,
            BroilerS.fosfor1,
            BroilerS.fosfor2,
            BroilerS.em,
        )
    elif jenis == 2:
        generate_child_v2(
            parent_utama,
            jumlah_child_per_parent,
            jumlah_parent,
            BroilerF.protein,
            BroilerF.lemak,
            BroilerF.serat,
            BroilerF.kalsium1,
            BroilerF.kalsium2,
            BroilerF.fosfor1,
            BroilerF.fosfor2,
            BroilerF.em,
        )
    elif jenis == 3:
        generate_child_petelur_v2(
            parent_utama,
            jumlah_child_per_parent,
            PetelurS.protein,
            PetelurS.lemak1,
            PetelurS.lemak2,
            PetelurS.serat,
            PetelurS.kalsium1,
            PetelurS.kalsium2,
            PetelurS.fosfor,
            0,
            PetelurS.em
        )
    elif jenis == 4:
        generate_child_petelur_v2(
            parent_utama,
            jumlah_child_per_parent,
            PetelurL.protein,
            PetelurL.lemak1,
            PetelurL.lemak2,
            PetelurL.serat,
            PetelurL.kalsium1,
            PetelurL.kalsium2,
            PetelurL.fosfor,
            0,
            PetelurL.em,
        )
    elif jenis == 5:
        generate_child_petelur_v2(
            parent_utama,
            jumlah_child_per_parent,
            PetelurF.protein,
            PetelurF.lemak1,
            PetelurF.lemak2,
            PetelurF.serat,
            PetelurF.kalsium1,
            PetelurF.kalsium2,
            PetelurF.fosfor1,
            PetelurF.fosfor2,
            PetelurF.em
        )

    # Menampilkan tabel child

    if metode == 1 or metode == 3:
     best_child_per_parent = [[] for i in range(jumlah_parent)]
     for i in range(jumlah_parent):
         parent_child = [c for c in child if c[1] == "P{}".format(i+1)] # ambil child dari parent i
         #sorted_child = sorted(parent_child, key=lambda x: float(x[10]), reverse=True) # urutkan child berdasarkan fitness
         sorted_child = sorted(parent_child, key=lambda x: x[12]) # urutkan child berdasarkan fitness
         #best_child_per_parent[i] = sorted_child[0]
         best_child_per_parent[i] = sorted_child[0] #debug

    elif metode == 2 or metode == 4:
      combined_pop = parent + child  # gabungkan array parent dan child
      #sorted_pop = sorted(combined_pop, key=lambda x: float(x[10]) if (isinstance(x, list) and len(x) >= 11) else float('-inf'), reverse=True)
      sorted_pop = sorted(combined_pop, key=lambda x: x[12] if (isinstance(x, list) and len(x) >= 11) else float('-inf'), reverse=True)
      best_child_per_parent = [sorted_pop[i] for i in range(jumlah_parent)]


# loop through each child and print its information
print("\n\nHasil Dari Uji coba setelah", generasi, "generasi adalah\n")
print("Child\tParent\tx1\tx2\tx3\tx4\tx5\tsigma1\tsigma2\tsigma3\tsigma4\tsigm`a5\tfitness")
#best_child_per_parent = sorted(best_child_per_parent, key=lambda x: float(x[10]), reverse=True)
best_child_per_parent = sorted(best_child_per_parent, key=lambda x:x[12], reverse=True)
for c in best_child_per_parent:
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8], c[9], c[10],c[11],c[12]))