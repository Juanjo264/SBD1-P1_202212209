import oracledb

try:
    conn = oracledb.connect(user="SYSTEM", password="99437", dsn="localhost:1521/XEPDB1")
    print("✅ Conexión exitosa a Oracle XE en Docker")
    conn.close()
except Exception as e:
    print("❌ Error de conexión:", e)
