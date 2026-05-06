import pandas as pd

# 1. EXTRAÇÃO: Criando os dados direto no código
dados = {'Nome': ['Felipe', 'Alice', 'Bruno'], 'Saldo': [1000, 500, 2500]}
df = pd.DataFrame(dados)

# 2. TRANSFORMAÇÃO: Criando a mensagem de marketing
df['Mensagem'] = df['Saldo'].apply(lambda s: "Invista já!" if s > 1000 else "Poupe mais!")

# 3. CARREGAMENTO: Salvando o resultado
df.to_csv('resultado_final.csv', index=False)
print("Pipeline ETL finalizado! Veja o arquivo 'resultado_final.csv'")
