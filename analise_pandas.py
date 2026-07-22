
import pandas as pd

ARQUIVO_ENTRADA = "transacoes.csv"


def analisar_com_pandas(nome_arquivo):
    """Lê, valida e agrupa as transações usando pandas."""

    dados = pd.read_csv(nome_arquivo)

    dados["id"] = pd.to_numeric(dados["id"], errors="coerce")
    dados["valor"] = pd.to_numeric(dados["valor"], errors="coerce")
    dados["data"] = pd.to_datetime(
        dados["data"],
        format="%Y-%m-%d",
        errors="coerce"
    )

    dados_validos = dados[
        dados["id"].notna()
        & dados["cliente_id"].notna()
        & dados["data"].notna()
        & dados["tipo"].isin(["credito", "debito"])
        & dados["valor"].notna()
        & (dados["valor"] > 0)
    ].copy()

    dados_validos["mes"] = dados_validos["data"].dt.strftime("%Y-%m")

    resumo = dados_validos.groupby("mes").agg(
        quantidade=("id", "count"),
        total_credito=(
            "valor",
            lambda valores: valores[
                dados_validos.loc[valores.index, "tipo"] == "credito"
            ].sum()
        ),
        total_debito=(
            "valor",
            lambda valores: valores[
                dados_validos.loc[valores.index, "tipo"] == "debito"
            ].sum()
        ),
        media=("valor", "mean"),
        maior_valor=("valor", "max"),
        menor_valor=("valor", "min")
    )

    resumo["saldo"] = (
        resumo["total_credito"] - resumo["total_debito"]
    )

    resumo = resumo.round(2)

    return dados_validos, resumo


if __name__ == "__main__":
    transacoes_validas, resumo_mensal = analisar_com_pandas(
        ARQUIVO_ENTRADA
    )

    print("===== ANÁLISE COM PANDAS =====")
    print(f"Transações válidas: {len(transacoes_validas)}")
    print()
    print(resumo_mensal)
