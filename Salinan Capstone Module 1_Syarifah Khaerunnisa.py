# Dummy Data Vaksin dan Storage
vaccines = [
     {"name": "Bio-TCV", "batch_number": "BTC001", "expiry_date": "2025-05-01", "stock": 100, "required_temp": 2, "type": "virus"},
    {"name": "Bio-TCV", "batch_number": "BTC002", "expiry_date": "2025-06-01", "stock": 80, "required_temp": 2, "type": "virus"},
    {"name": "Vaksin BIO-Td", "batch_number": "BTD001", "expiry_date": "2024-12-15", "stock": 50, "required_temp": 8, "type": "bacteria"},
    {"name": "Vaksin BIO-Td", "batch_number": "BTD002", "expiry_date": "2024-11-10", "stock": 40, "required_temp": 8, "type": "bacteria"},
    {"name": "DTP", "batch_number": "DTP001", "expiry_date": "2026-07-20", "stock": 75, "required_temp": 2, "type": "bacteria"},
    {"name": "DTP", "batch_number": "DTP002", "expiry_date": "2026-08-20", "stock": 60, "required_temp": 2, "type": "bacteria"},
    {"name": "nOPV2", "batch_number": "NOP001", "expiry_date": "2025-01-10", "stock": 120, "required_temp": 4, "type": "virus"},
    {"name": "Influenza", "batch_number": "INF001", "expiry_date": "2024-09-30", "stock": 90, "required_temp": 2, "type": "virus"},
    {"name": "Indovac", "batch_number": "IND001", "expiry_date": "2025-04-25", "stock": 30, "required_temp": 2, "type": "virus"},
]

storage_rooms = [
    {"room_id": 1, "temperature": 2, "capacity": 500, "used_capacity": 150},
    {"room_id": 2, "temperature": 8, "capacity": 100, "used_capacity": 60},
    {"room_id": 3, "temperature": 4, "capacity": 150, "used_capacity": 30},
]

# Perapihan dengan Tabel
def display_table(data):
    # Header tabel
    print("{:<20} {:<12} {:<15} {:<10} {:<15} {:<10}".format("Name", "Batch Num", "Expiry Date", "Stock", "Req Temp (°C)", "Type"))
    print("-" * 85)
    
    # Mencetak setiap baris data
    for item in data:
        print("{:<20} {:<12} {:<15} {:<10} {:<15} {:<10}".format(
            item["name"], item["batch_number"], item["expiry_date"], item["stock"], item["required_temp"], item["type"]
        ))
# Main Menu (Fungsi Utama)
def main():
    while True:
        print("\n--- Main Menu ---")
        print("1. Input Vaksin Baru")
        print("2. Lihat Stok Vaksin")
        print("3. Exit")
        choice = input("Pilih opsi: ")

        if choice == "1":
            create_vaccine()
        elif choice == "2":
            read_vaccines()
        elif choice == "3":
            print("Selesai.")
            break
        else:
            print("Opsi tidak valid, coba lagi.")
# Input Vaksin Baru (Fungsi Create)
def create_vaccine():
    print("\n--- Input Vaksin Baru ---")
    name = input("Nama Vaksin: ")
    batch_number = input("Nomor Batch: ")
    expiry_date = input("Tanggal Kedaluwarsa (YYYY-MM-DD): ")
    stock = int(input("Jumlah Stok: "))
    required_temp = int(input("Suhu Penyimpanan yang Dibutuhkan: "))
    type = input("Jenis Vaksin (bacteria/virus): ")

    # Cek ruangan yang cocok
    suitable_room = None
    for room in storage_rooms:
        if room["temperature"] == required_temp:
            suitable_room = room
            break

    if not suitable_room:
        print("Tidak ada ruangan dengan suhu yang sesuai. Stok baru tidak bisa ditambahkan.")
        return

    # Cek kapasitas ruangan
    available_capacity = suitable_room["capacity"] - suitable_room["used_capacity"]
    if suitable_room["used_capacity"] + stock > suitable_room["capacity"]:
        print(f"Ruangan penyimpanan penuh. Kapasitas hanya tersedia: {available_capacity} unit.")
    else:
        # Tambahkan vaksin ke dalam stok
        vaccines.append({
            "name": name,
            "batch_number": batch_number,
            "expiry_date": expiry_date,
            "stock": stock,
            "required_temp": required_temp,
            "type": type
        })
        suitable_room["used_capacity"] += stock
        print("Vaksin berhasil ditambahkan ke stok.")

# Display Data Vaksin (Fungsi Read)
def read_vaccines():
    print("\n--- Stok Vaksin ---")
    
    display_table(vaccines)
    
    # Pilihan untuk sort, filter, update, remove 
    print("\nPilih opsi:")
    print("1. Urutkan Data")
    print("2. Filter Data")
    print("3. Update Stok")
    print("4. Remove Stok")
    choice = input("Pilih opsi: ")

    if choice == "1":
        sort_stock()
    elif choice == "2":
        filter_stock()
    elif choice == "3":
        update_stock()
    elif choice == "4":
        remove_stock()
    else:
        print("Opsi tidak valid.")
# Mengurutkan data (Fungsi Sort)
def sort_stock():
    print("\nPilih opsi sorting:")
    print("1. Berdasarkan Tanggal Kedaluwarsa")
    print("2. Berdasarkan Stok")
    sort_choice = input("Pilih opsi: ")

    if sort_choice == "1":
        print("\n--- Mengurutkan berdasarkan Tanggal Kedaluwarsa ---")
        sorted_vaccines = sorted(vaccines, key=lambda v: v["expiry_date"])
        display_table(sorted_vaccines)
    elif sort_choice == "2":
        print("\n--- Mengurutkan berdasarkan Jumlah Stock ---")
        sorted_vaccines = sorted(vaccines, key=lambda v: v["stock"])
        display_table(sorted_vaccines)
    else:
        print("Opsi tidak valid.")
        return
# Filter data
def filter_stock():
    print("\nPilih opsi filter:")
    print("1. Berdasarkan Jenis Vaksin")
    print("2. Berdasarkan Suhu Penyimpanan")
    filter_choice = input("Pilih opsi: ")

    if filter_choice == "1":
        filter_vaccine_type()
    elif filter_choice == "2":
        filter_room_temperature()
    else:
        print("Opsi tidak valid.")

# Filter berdasarkan Jenis Vaksin
def filter_vaccine_type():
    print("\n--- Filter berdasarkan Jenis Vaksin ---")
    vaccine_type = input("Masukkan jenis vaksin (bacteria/virus): ")
    
    filtered_vaccines = [v for v in vaccines if v['type'].lower() == vaccine_type.lower()]
    
    if not filtered_vaccines:
        print("Tidak ada vaksin yang ditemukan dengan jenis tersebut.")
        return
    
    display_table(filtered_vaccines)


# Filter berdasarkan Suhu Penyimpanan
def filter_room_temperature():
    print("\n--- Filter berdasarkan Suhu Penyimpanan ---")
    required_temp = int(input("Masukkan suhu penyimpanan (2/4/8): "))
    
    filtered_vaccines = [v for v in vaccines if v['required_temp'] == required_temp]
    display_table(filtered_vaccines)
    
    if not filtered_vaccines:
        print("Tidak ada vaksin yang ditemukan dengan suhu penyimpanan tersebut.")
        return
    
    display_table(filtered_vaccines)

# Update Stok (Fungsi Update)
def update_stock():
    batch_number = input("\nMasukkan nomor batch vaksin yang ingin di-update: ")
    for vaccine in vaccines:
        if vaccine["batch_number"] == batch_number:
            # Cari ruangan yang sesuai
            for room in storage_rooms:
                if room["temperature"] == vaccine["required_temp"]:
                    available_capacity = room["capacity"] - room["used_capacity"]
                    print(f"Stok saat ini: {vaccine['stock']}")
                    print(f"Kapasitas ruangan tersisa: {available_capacity} unit")

                    update_choice = input("Apakah ingin menambah atau mengurangi stok? (tambah/kurang): ").lower()
                    if update_choice not in ["tambah", "kurang"]:
                        print("Opsi tidak valid.")
                        return

                    update_amount = int(input("Jumlah stok yang ingin di-update: "))
                    
                    if update_choice == "tambah":
                        if room["used_capacity"] + update_amount > room["capacity"]:
                            print(f"Ruangan penuh! Kapasitas hanya tersedia: {available_capacity} unit. Stok tidak bisa di-update.")
                            return
                        else:
                            vaccine["stock"] += update_amount
                            room["used_capacity"] += update_amount
                            print("Stok berhasil ditambahkan.")
                            return
                    
                    elif update_choice == "kurang":
                        if update_amount > vaccine["stock"]:
                            print("Jumlah pengurangan lebih besar dari stok yang ada. Stok tidak bisa di-update.")
                            return
                        else:
                            vaccine["stock"] -= update_amount
                            room["used_capacity"] -= update_amount
                            print("Stok berhasil dikurangi.")
                            return

    print("Batch number tidak ditemukan.")

# Menghapus stok (Fungsi Remove)
def remove_stock():
    batch_number = input("\nMasukkan nomor batch vaksin yang ingin dihapus: ")
    for vaccine in vaccines:
        if vaccine["batch_number"] == batch_number:
            # Kembalikan kapasitas ruangan
            for room in storage_rooms:
                if room["temperature"] == vaccine["required_temp"]:
                    room["used_capacity"] -= vaccine["stock"]
            vaccines.remove(vaccine)
            print("Vaksin berhasil dihapus.")
            return
    print("Batch number tidak ditemukan.")

# Mulai aplikasi
main()