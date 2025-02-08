def kecepatan(jarak, waktu):
    """
    Menghitung kecepatan.
    :param jarak: Jarak yang ditempuh (meter)
    :param waktu: Waktu yang diperlukan (detik)
    :return: Kecepatan (meter/detik)
    """
    return jarak / waktu

def percepatan(kecepatan_awal, kecepatan_akhir, waktu):
    """
    Menghitung percepatan.
    :param kecepatan_awal: Kecepatan awal (meter/detik)
    :param kecepatan_akhir: Kecepatan akhir (meter/detik)
    :param waktu: Waktu yang diperlukan (detik)
    :return: Percepatan (meter/detik^2)
    """
    return (kecepatan_akhir - kecepatan_awal) / waktu

def gaya(massa, percepatan):
    """
    Menghitung gaya.
    :param massa: Massa benda (kilogram)
    :param percepatan: Percepatan benda (meter/detik^2)
    :return: Gaya (Newton)
    """
    return massa * percepatan

def energi_kinetik(massa, kecepatan):
    """
    Menghitung energi kinetik.
    :param massa: Massa benda (kilogram)
    :param kecepatan: Kecepatan benda (meter/detik)
    :return: Energi kinetik (Joule)
    """
    return 0.5 * massa * kecepatan ** 2

def energi_potensial(massa, gravitasi, ketinggian):
    """
    Menghitung energi potensial.
    :param massa: Massa benda (kilogram)
    :param gravitasi: Percepatan gravitasi (meter/detik^2)
    :param ketinggian: Ketinggian benda (meter)
    :return: Energi potensial (Joule)
    """
    return massa * gravitasi * ketinggian