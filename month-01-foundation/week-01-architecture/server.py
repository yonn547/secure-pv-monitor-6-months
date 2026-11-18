import asyncio
from pymodbus.server import StartAsyncTcpServer
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusDeviceContext,
    ModbusServerContext
)

async def run_server():
    # 1. Buat Data Blocks (MULAI DARI ADDRESS 1)
    di_block = ModbusSequentialDataBlock(1, [0] * 100)
    co_block = ModbusSequentialDataBlock(1, [0] * 100)
    # Alamat 1: Suhu (75), Alamat 2: Daya (5200), Alamat 3: Status (1)
    hr_block = ModbusSequentialDataBlock(1, [75, 5200, 1] + [0] * 97)
    ir_block = ModbusSequentialDataBlock(1, [0] * 100)

    # 2. Bungkus ke dalam Device Context (Ini yang hilang sebelumnya)
    device = ModbusDeviceContext(di=di_block, co=co_block, hr=hr_block, ir=ir_block)

    # 3. Bungkus ke dalam Server Context
    context = ModbusServerContext(devices=device, single=True)

    print("[+] Simulator Inverter PLTS berjalan di localhost port 5020...")
    print("[+] Tekan Ctrl+C untuk menghentikan.")

    # 4. Jalankan Server
    await StartAsyncTcpServer(
        context=context,
        address=("127.0.0.1", 5020)
    )

if __name__ == "__main__":
    try:
        asyncio.run(run_server())
    except KeyboardInterrupt:
        print("\n[+] Server dihentikan.")