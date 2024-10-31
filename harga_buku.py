def harga_bayaran(jenisbuku, kuantiti): 
    harga_seunit = {1: 6.00, 2: 7.50, 3: 8.90}
    harga_unit = harga_seunit.get(jenisbuku, 0)
    harga_total = harga_unit * kuantiti
    
    kadar_diskaun = {1: 10.00, 2: 8.00, 3: 5.00}
    diskaun_kadar = kadar_diskaun.get(jenisbuku, 0)
    potongan_harga = kira_diskaun(harga_total, diskaun_kadar)
    
    return potongan_harga, harga_total - potongan_harga

def kira_diskaun(harga, kadar_diskaun):
    diskaun = harga * kadar_diskaun / 100
    return diskaun

def main():
    print("Senarai belian buku:")
    print("1.Latihan Pasti A,Bahasa Melayu,Tingkatan 1")
    print("2.Latihan Pasti A,Bahasa Melayu,Tingkatan 2")
    print("3.Latihan Pasti A,Bahasa Melayu,Tingkatan 3")
    while True:
        jenisbuku = int(input("Masukkan jenis buku yang dibeli (1-3): "))
        if jenisbuku > 3 or jenisbuku < 1:
            print("Sila masukkan nombor 1 hingga 3 sahaja.")
        else:
            break # exit when no error 
    kuantiti=int(input("Masukkan kuantiti buku yang dibeli:"))
    potongan_harga,harga_total = harga_bayaran(jenisbuku,kuantiti)
    print("Potongan harga yang diperoleh ialah RM", round(potongan_harga,2))
    print("Jumlah harga yang perlu dibayar ialah RM", round(harga_total,2))
    
if __name__ == "__main__":
    main()
