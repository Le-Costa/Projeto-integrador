# ================================================================
# 2. CONEXÃO COM O LAKEHOUSE
# ================================================================
import os
spark.conf.set("spark.sql.session.timeZone", "UTC")

conectado = None
for alvo in (LAKEHOUSE, f"{LAKEHOUSE}.dbo"):      # sem schema / com schema
    try:
        spark.sql(f"USE {alvo}")
        conectado = alvo
        break
    except Exception:
        pass

if conectado:
    print(f"✔ Conectado ao Lakehouse: {conectado}")
else:
    print(f"✘ Não consegui usar o Lakehouse '{LAKEHOUSE}'. Diagnóstico:")
    print("  Lakehouse padrão adicionado ao notebook?", os.path.exists("/lakehouse/default"))
    try:
        nomes = [db.name for db in spark.catalog.listDatabases()]
        print("  Bancos que o notebook enxerga:", nomes)
    except Exception as erro:
        print("  Não foi possível listar os bancos:", erro)
    raise RuntimeError(
        "Adicione o Lakehouse no painel Explorer, marque como padrão e confira o nome em LAKEHOUSE.")
