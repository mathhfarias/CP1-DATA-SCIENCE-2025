import streamlit as st
import pandas as pd
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
arr = np.zeros(836855861, dtype=np.uint8)  # Uses 1 byte per element instead of 1 byte per bool.
import plotly.figure_factory as ff
from plotnine import *


# Configuração da página
st.set_page_config(page_title="Dashboard de Distribuições Probabilísticas", layout="wide")

# Criando as sub-abas (pages)
pages = st.sidebar.selectbox("Escolha a sua seção:", [
    "Quem sou eu?",
    "Formação e Experiências Profissionais",
    "Skills",
    "Certificados",
    "Análise de Dados"
])

# Melhorando a Sidebar
st.sidebar.markdown("""
    <a href="https://github.com/mathhfarias" target="_blank">
        <button style="
            display: block;
            width: 100%;
            background-color: #24292e;
            color: white;
            padding: 10px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            margin-bottom: 10px;
            cursor: pointer;">
            🔗 GitHub
        </button>
    </a>
    <a href="https://www.linkedin.com/in/matheus-farias-de-lima" target="_blank">
        <button style="
            display: block;
            width: 100%;
            background-color: #0077B5;
            color: white;
            padding: 10px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            margin-bottom: 20px;
            cursor: pointer;">
            💼 LinkedIn
        </button>
    </a>
""", unsafe_allow_html=True)

# Adicionando espaçamento extra antes do "Baixar CV"
st.sidebar.markdown("<br>", unsafe_allow_html=True)

st.sidebar.markdown("### Desenvolvido por Matheus Farias de Lima")

if pages == "Quem sou eu?":
    st.image("IMAGES/MATHEUS.PNG", width=600, use_container_width=True)
    st.write("""
    - 🎓 **Estudante da Faculdade de Informática e Administração Paulista (FIAP)**, atualmente cursando **Engenharia de Software**.
    - 🌍 Apaixonado por **tecnologia e inovação**, com grande interesse em oportunidades internacionais para **expandir experiências profissionais**.
    - 💡 Foco em **desenvolvimento Front-End**, com conhecimento sólido em diversas tecnologias.
    - 🚀 **Experiência prática** com projetos acadêmicos e desenvolvimento de soluções para empresas reais.
    - 🔧 Tecnologias principais: **React, JavaScript, Java, Python, Docker e APIs REST**.
    """)

elif pages == "Formação e Experiências Profissionais":
    st.image("IMAGES/FIAP.png", width=600, use_container_width=True)
    st.header("🎓 Formação e Experiências Profissionais")
    st.write("""
    - **Formação Acadêmica:**
        - Engenharia de Software na **FIAP** (Faculdade de Informática e Administração Paulista).
    - **Experiência Profissional:**
        - Atualmente em busca da primeira oportunidade profissional na área.
    - **Projetos Acadêmicos:**
        - Participação na **Global Solutions da FIAP**, desenvolvendo **websites e aplicativos** para empresas reais.
        - Desenvolvimento de soluções para empresas como **Hospital das Clínicas e Rede Âncora**.
    - **Certificados:**
        - Certificações em **programação** e **soft skills** através de **FIAP Nano-Courses** e **Alura**.
    """)

elif pages == "Skills":
    st.image("IMAGES/SKILLS.png", width=600, use_container_width=True)
    st.header("🚀 Skills")
    st.write("""
    - **Hard Skills:**
        - 🔹 Especialização em **Front-End**
        - 🔹 Linguagens de programação: **React, Python, Java, JavaScript**
        - 🔹 Banco de Dados: **MySQL, PostgreSQL**
        - 🔹 Ferramentas: **Git, Docker, APIs REST**
    - **Soft Skills:**
        - 🗣️ **Habilidade de comunicação:** Clareza ao expressar ideias e facilitar o trabalho em equipe.
        - 🤝 **Trabalho em equipe:** Capacidade de colaboração e escuta ativa para contribuir em projetos.
        - ⏳ **Gestão de tempo e organização:** Priorização de tarefas e eficiência no cumprimento de prazos.
    - **Idiomas:**
        - 🌍 **Fluente em inglês**, certificado pelo **OHLA (Flórida) & TOEFL**.
        - 🌍 **Básico em espanhol**, aulas durante o periodo escolar.   
    """)

elif pages == "Certificados":
    st.image("IMAGES/CERTIFICADO DESIGN THINKING.png", width=600, use_container_width=True) 
    st.image("IMAGES/CERTIFICADO GESTÃO DE INFRAESTRUTURA DE TI.png", width=600, use_container_width=True)
    st.image("IMAGES/CERTIFICADO FORMAÇÃO SOCIAL E SUSTENTABILIDADE.JPEG", width=600, use_container_width=True)
    st.image("IMAGES/CERTIFICADO HTML E CSS.JPG", width=600, use_container_width=True)

                
elif pages == "Análise de Dados":
    st.header("📊 Análise de Dados")

    st.write("Carregue um arquivo Excel para visualizar a distribuição de uma variável numérica.")
    uploaded_file = st.file_uploader("Carregue seu arquivo Excel", type=["xlsx", "xls"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("📌 **Amostra dos dados:**")
        st.write("""

    **Problema:**

    Analisar o comportamento dos views da Stream para entender quais fatores influenciam a satisfação e o tempo de visualização, visando melhorar a retenção de clientes e a recomendação de conteúdo.

---

### 📝 Dados e Tipos:

#### Estrutura dos Dados:
O dataset contém 1000 registros e 11 colunas. Aqui está um resumo das colunas e seus tipos:

    - Channel (string): Nome do canal.
    - Watch time (Minutes) (int64): Tempo total assistido em minutos.
    - Stream time (Minutes) (int64): Tempo total de transmissão em minutos.
    - Peak viewers (int64): Máximo de espectadores simultâneos.
    - Average viewers (int64): Média de espectadores por transmissão.
    - Followers (int64): Total de seguidores do canal.
    - Followers gained (int64): Número de seguidores ganhos.
    - Views gained (int64): Número de visualizações ganhas.
    - Partnered (bool): Indica se o canal é parceiro do Twitch.
    - Mature (bool): Indica se o canal possui conteúdo adulto.
    - Language (string): Idioma principal do canal.

### Estatísticas Descritivas:
    - Média de Watch Time: 418 milhões de minutos
    - Máximo de Watch Time: 6.2 bilhões de minutos
    - Média de Peak Viewers: 37 mil espectadores
    - Máximo de Peak Viewers: 639 mil espectadores
    - Média de seguidores ganhos: 205 mil
    - Distribuição de idiomas: O inglês domina, com 343 canais parceiros transmitindo nesse idioma.

---

## ❓ Principais Perguntas

### 📌 Quais são os 10 principais canais por pico de espectadores?
| #  | Canal           | Pico de Espectadores |
|----|---------------|--------------------|
| 1  | Summit1g      | 310.998           |
| 6  | NICKMERCS     | 407.428           |
| 15 | MontanaBlack88| 110.109           |
| 16 | Sodapoppin    | 393.348           |
| 28 | Pestily       | 616.168           |

### 📌 Quais são os 10 principais canais por seguidores ganhos?
| #  | Canal           | Seguidores Ganhos |
|----|---------------|-------------------|
| 1  | Summit1g      | 25.610            |
| 6  | NICKMERCS     | 46.084.211        |
| 15 | MontanaBlack88| 67.740            |
| 16 | Sodapoppin    | 2.786.162         |
| 28 | Pestily       | 24.029.726        |

### 📌 Quais são os 10 principais canais por visualizações ganhas?
| #  | Canal           | Visualizações Obtidas |
|----|---------------|----------------------|
| 1  | Summit1g      | 5.310.163            |
| 6  | NICKMERCS     | 1.089.824            |
| 15 | MontanaBlack88| 181.600              |
| 16 | Sodapoppin    | 19.659               |
| 28 | Pestily       | 168.112              |

### 📌 Existe uma correlação entre o tempo de transmissão e o pico de espectadores?
    - A correlação entre o tempo de transmissão e o pico de espectadores é de aproximadamente ###-0.02###   .
    - Isso indica uma correlação negativa muito fraca, praticamente inexistente.
    - Em outras palavras, **não há uma relação linear significativa** entre o tempo de transmissão e o número de espectadores simultâneos.

### 📌 Qual é a distribuição de canais por idioma?
| Idioma      | Quantidade de Canais |
|------------|--------------------|
| 🇬🇧 English    | 20                 |
| 🇰🇷 Korean     | 2                  |
| 🇪🇸 Spanish    | 3                  |
| 🇵🇹 Portuguese | 3                  |
| 🇩🇪 German     | 2                  |
| 🇫🇷 French     | 3                  |
| 🇷🇺 Russian    | 1                  |

---

### 📊 Distribuições:

    #### - **Distribuição Normal:**
    A idade dos assinantes pode seguir uma distribuição normal, permitindo analisar a probabilidade de encontrar assinantes em determinadas faixas etárias.  
    O tempo de visualização também pode seguir uma distribuição normal, permitindo analisar a probabilidade de tempo de visualização em um determinado intervalo.

    #### - **Distribuição Binomial:**
    A probabilidade de um assinante assistir a um filme completo pode ser modelada por uma distribuição binomial, onde cada visualização é um evento independente com probabilidade de sucesso (assistir completo) ou fracasso (não assistir completo).  
    A probabilidade de um usuário dar uma avaliação positiva para um conteúdo pode ser modelada por uma distribuição binomial.

    #### - **Distribuição de Poisson:**
    O número de visualizações de um determinado conteúdo em um período de tempo pode ser modelado por uma distribuição de Poisson.  
    O número de avaliações recebidas por um determinado conteúdo em um período de tempo também pode ser modelado por uma distribuição de Poisson.
    """)
        st.write(df.head())
        
        colunas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
        if colunas_numericas:
            coluna_escolhida = st.selectbox("🔎 Escolha uma coluna numérica:", colunas_numericas)
            
            if coluna_escolhida:
                st.write("📊 **Distribuição dos dados:**")
                st.write(df[coluna_escolhida].describe())
                
                dist = st.selectbox("📈 Escolha a distribuição para análise:", ["Poisson", "Normal", "Binomial"])
                
                if dist == "Poisson":
                    lambda_est = df[coluna_escolhida].mean()
                    x = np.arange(0, 2 * lambda_est)
                    y = stats.poisson.pmf(x, lambda_est)
                    st.write("📌 **Distribuição de Poisson**")
                    fig = go.Figure(data=[go.Bar(x=x, y=y)])
                    st.plotly_chart(fig)
                
                elif dist == "Normal":
                    mu_est = df[coluna_escolhida].mean()
                    sigma_est = df[coluna_escolhida].std()
                    x = np.linspace(mu_est - 4*sigma_est, mu_est + 4*sigma_est, 100)
                    y = stats.norm.pdf(x, mu_est, sigma_est)
                    st.write("📌 **Distribuição Normal**")
                    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines')])
                    st.plotly_chart(fig)
                
                elif dist == "Binomial":
                    n = 10  # número de tentativas fixo
                    p = df[coluna_escolhida].mean() / max(df[coluna_escolhida])
                    x = np.arange(0, n + 1)
                    y = stats.binom.pmf(x, n, p)
                    st.write("📌 **Distribuição Binomial**")
                    fig = go.Figure(data=[go.Bar(x=x, y=y)])
                    st.plotly_chart(fig)