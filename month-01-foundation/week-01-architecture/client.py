from pymodbus.client import ModbusTcpClient

# Inisialisasi client
client = ModbusTcpClient('127.0.0.1', port=5020)

if client.connect():
    print("[+] Terhubung ke Inverter. Membaca data...")
    
    # PERHATIAN: Di pymodbus 3.x, parameter 'slave' diganti menjadi 'device_id'
    result = client.read_holding_registers(address=1, count=3, device_id=1)
    
    if not result.isError():
        suhu = result.registers[0]
        daya_kw = result.registers[1] / 1000  # Konversi Watt ke kW
        status = "ON" if result.registers[2] == 1 else "OFF"
        
        print(f"Output: Waktu: 08:00 | Suhu: {suhu}°C | Daya: {daya_kw}kW | Status: {status}")
    else:
        print("[-] Gagal membaca data:", result)
        
    client.close()
else:
    print("[-] Gagal terhubung ke server.")