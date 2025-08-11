# Análise de um banco de dados
# Projeto 2° período

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Carregar a planilha CSV 
df = pd.read_excel("Brasileiro_2019.xlsx", engine='openpyxl')

# Salva os dados em um arquivo CSV para verificação
df.to_csv('brasileirao_completo.csv', index=False)

# Limpeza de dados 
df['Valor mercado'] = df['Valor mercado'].replace({',': ''}, regex=True).astype(float)
df['Pontos'] = df['Pontos'].astype(int)
df['Gols pro'] = df['Gols pro'].astype(int)
df['Reforços 18/19'] = df['Reforços 18/19'].astype(int)
df['Estrangeiros'] = df['Estrangeiros'].astype(int)
df['Saldo de gol'] = df['Saldo de gol'].astype(int)

# Tratar valores não numéricos ou datas na coluna "Média de Idade"
# Verifica se há valores não numéricos
df['Média de Idade'] = pd.to_numeric(df['Média de Idade'], errors='coerce')

# Agora converte para float após a correção
df['Média de Idade'] = df['Média de Idade'].astype(float)

# 1. **Análise de correlação entre o valor de mercado e os pontos**
corr_valor_pontos = df[['Valor mercado', 'Pontos']].corr()
print(f"Correlação entre valor de mercado e pontos:\n{corr_valor_pontos}")

# Gráfico da correlação
plt.figure(figsize=(10, 6))
sns.regplot(x='Valor mercado', y='Pontos', data=df, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
plt.title('Correlação entre Valor de Mercado e Pontos')
plt.xlabel('Valor de Mercado (R$)')
plt.ylabel('Pontos')
plt.show()

# 2. **Times com maior valor de mercado se saíram melhor?**
top_valor_mercado = df[['Times', 'Valor mercado', 'Pontos']].sort_values(by='Valor mercado', ascending=False).head(5)
print(f"Times com maior valor de mercado:\n{top_valor_mercado}")

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(x='Times', y='Pontos', data=top_valor_mercado, palette='viridis')
plt.title('Times com Maior Valor de Mercado e seus Pontos')
plt.xlabel('Times')
plt.ylabel('Pontos')
plt.xticks(rotation=45)
plt.show()

# 3. **Times com mais reforços tiveram melhor desempenho?**
correlacao_reforcos_pontos = df[['Reforços 18/19', 'Pontos']].corr()
print(f"Correlação entre Reforços e Pontos:\n{correlacao_reforcos_pontos}")

# Gráfico de dispersão
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Reforços 18/19', y='Pontos', data=df, color='green')
plt.title('Relação entre Reforços e Pontos')
plt.xlabel('Número de Reforços')
plt.ylabel('Pontos')
plt.show()

# 4. **Estrangeiros influenciam no desempenho?**
correlacao_estrangeiros_pontos = df[['Estrangeiros', 'Pontos']].corr()
print(f"Correlação entre Estrangeiros e Pontos:\n{correlacao_estrangeiros_pontos}")

# Gráfico de dispersão
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Estrangeiros', y='Pontos', data=df, color='purple')
plt.title('Relação entre Estrangeiros e Pontos')
plt.xlabel('Número de Estrangeiros')
plt.ylabel('Pontos')
plt.show()

# 5. **Análise dos times com mais gols marcados**
corr_gols_pontos = df[['Gols pro', 'Pontos']].corr()
print(f"Correlação entre Gols e Pontos:\n{corr_gols_pontos}")

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(x='Times', y='Gols pro', data=df.sort_values(by='Gols pro', ascending=False).head(10), palette='coolwarm')
plt.title('Top 10 Times com Maior Número de Gols Marcados')
plt.xlabel('Times')
plt.ylabel('Gols Marcados')
plt.xticks(rotation=45)
plt.show()

# 6. **Quem tem o jogador com maior número de gols teve maior impacto na tabela?**
artilheiros = df[['Times', 'Jogador', 'Gols']].sort_values(by='Gols', ascending=False).head(10)
print(f"Top 10 Artilheiros:\n{artilheiros}")

# Gráfico de barras para os 10 artilheiros
plt.figure(figsize=(10, 6))
sns.barplot(x='Jogador', y='Gols', data=artilheiros, palette='magma')
plt.title('Top 10 Artilheiros do Campeonato')
plt.xlabel('Jogadores')
plt.ylabel('Gols')
plt.xticks(rotation=45)
plt.show()

# 7. **Média de idade influencia no desempenho?**
correlacao_idade_pontos = df[['Média de Idade', 'Pontos']].corr()
print(f"Correlação entre Média de Idade e Pontos:\n{correlacao_idade_pontos}")

# Gráfico de dispersão
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Média de Idade', y='Pontos', data=df, color='orange')
plt.title('Relação entre Média de Idade e Pontos')
plt.xlabel('Média de Idade')
plt.ylabel('Pontos')
plt.show()

# 8. **Desempenho dos times com menor saldo de gols**
saldo_negativo = df[df['Saldo de gol'] < 0]
print(f"Times com Saldo de Gols Negativo:\n{saldo_negativo[['Times', 'Saldo de gol', 'Pontos']]}")

# Gráfico de barras para saldo de gols negativo
plt.figure(figsize=(10, 6))
sns.barplot(x='Times', y='Saldo de gol', data=saldo_negativo, palette='cool')
plt.title('Times com Saldo de Gols Negativo')
plt.xlabel('Times')
plt.ylabel('Saldo de Gol')
plt.xticks(rotation=45)
plt.show()

# 9. **Média, Mediana e Desvio Padrão**
print("\nMédia, Mediana e Desvio Padrão de pontos, gols e idade:")
print(f"Média de Pontos: {df['Pontos'].mean()}")
print(f"Mediana de Pontos: {df['Pontos'].median()}")
print(f"Desvio Padrão de Pontos: {df['Pontos'].std()}")

# Gráfico de distribuição dos pontos
plt.figure(figsize=(10, 6))
sns.histplot(df['Pontos'], kde=True, color='blue')
plt.title('Distribuição dos Pontos no Campeonato')
plt.xlabel('Pontos')
plt.ylabel('Frequência')
plt.show()

# Gráfico de distribuição de gols
plt.figure(figsize=(10, 6))
sns.histplot(df['Gols pro'], kde=True, color='red')
plt.title('Distribuição dos Gols Marcados')
plt.xlabel('Gols Marcados')
plt.ylabel('Frequência')
plt.show()

# 10. **Moda**
moda_gols = df['Gols pro'].mode()[0]
print(f"Moda dos Gols Marcados: {moda_gols}")
