# Week 1: Arsitektur OT Dasar & Komunikasi Modbus TCP

## 🎯 Tujuan
Memahami arsitektur dasar sistem kontrol industri (OT) dan membangun komunikasi Modbus TCP antara simulator inverter (server) dan SCADA reader (client).

## 📚 Konsep yang Dipelajari

### Arsitektur OT (Operational Technology)
Sistem kontrol industri terdiri dari 4 lapisan utama:
1. **Field Layer**: Sensor dan aktuator di lapangan (pengukur suhu, penggerak katup)
2. **PLC/Inverter**: Otak lokal yang mengontrol perangkat field secara real-time
3. **SCADA**: Sistem supervisory yang memantau dan mengontrol PLC dari jarak jauh
4. **IT Layer**: Sistem enterprise untuk analisis data historis dan pelaporan

### Protokol Modbus TCP
Modbus adalah protokol komunikasi "bahasa radio" antara SCADA (Master/Client) dan PLC/Inverter (Slave/Server).
- **Coil**: Saklar digital 1-bit (ON/OFF) untuk kontrol biner
- **Holding Register**: Wadah data numerik 16-bit untuk nilai seperti suhu, daya, atau status
- **Master/Slave**: Client meminta data, Server menyediakan data

**Catatan Kritis**: Modbus TCP dirancang tahun 1979 untuk jaringan tertutup. Protokol ini **tidak memiliki enkripsi atau autentikasi bawaan**, menjadikannya sangat rentan jika diekspos ke jaringan publik.

## 🛠️ Implementasi

### File yang Dibuat
- `server.py`: Simulator inverter PLTS menggunakan `pymodbus` 3.16.2
- `client.py`: SCADA reader yang mengambil data dari simulator

### Cara Menjalankan

**Terminal 1 - Jalankan Simulator:**
```bash
python3 server.py