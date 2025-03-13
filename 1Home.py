import streamlit as st
import pandas as pd
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
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

# Adicionando espaçamento extra
st.sidebar.markdown("<br>", unsafe_allow_html=True)

st.sidebar.markdown("### Desenvolvido por Matheus Farias de Lima")

if pages == "Quem sou eu?":
    st.image("IMAGES/MATHEUS.PNG", width=600, use_container_width=True)
    st.write("""
    -  **Estudante da Faculdade de Informática e Administração Paulista (FIAP)**, atualmente cursando **Engenharia de Software**.
    -  Apaixonado por **tecnologia e inovação**, com grande interesse em oportunidades internacionais para **expandir experiências profissionais**.
    -  Foco em **desenvolvimento Front-End**, com conhecimento sólido em diversas tecnologias.
    -  **Experiência prática** com projetos acadêmicos e desenvolvimento de soluções para empresas reais.
    -  Tecnologias principais: **React, JavaScript, Java, Python, Docker e APIs REST**.
    """)

elif pages == "Formação e Experiências Profissionais":
    st.image("IMAGES/FIAP.png", width=600, use_container_width=True)
    st.header(" Formação e Experiências Profissionais")
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
    st.header(" Skills")
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
    st.image("IMAGES/CERTIFICADO FORMAÇÃO SOCIAL E SUSTENTABILIDADE.jpeg", width=600, use_container_width=True)
    st.image("IMAGES/CERTIFICADO HTML E CSS.JPG", width=600, use_container_width=True)

elif pages == "Análise de Dados":
    st.header(" Análise de Dados")

    st.write("Carregue um arquivo Excel para visualizar a distribuição de uma variável numérica.")
    uploaded_file = st.file_uploader("Carregue seu arquivo Excel", type=["xlsx", "xls"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write(" ## Amostra dos dados: Twitch Streaming")
        st.write("""
    ## Problema:

    Analisar o comportamento dos views da Stream para entender quais fatores influenciam a satisfação e o tempo de visualização, visando melhorar a retenção de clientes e a recomendação de conteúdo.

  
---

    
### 📝 Dados e Tipos:

#### Estrutura dos Dados:
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
### 1. Medidas Centrais:
### Média:

- Tempo assistido: ~418 milhões de minutos
- Tempo de transmissão: ~120 mil minutos
- Pico de espectadores: ~37 mil
- Média de espectadores: ~4,7 mil
- Seguidores: ~570 mil
- Seguidores ganhos: ~205 mil
- Visualizações ganhas: ~11,6 milhões

### Mediana (valor central dos dados, menos sensível a outliers):

- Tempo assistido: ~235 milhões de minutos
- Tempo de transmissão: ~108 mil minutos
- Pico de espectadores: ~16,6 mil
- Média de espectadores: ~2,4 mil
- Moda (valor mais frequente nos dados):

Por exemplo, o tempo assistido mais frequente é de ~122 milhões de minutos.

### 2. Análise de Dispersão:
### Desvio padrão (média de quanto os valores se afastam da média):

- Tempo assistido: ~549 milhões de minutos
- Pico de espectadores: ~60 mil
- Média de espectadores: ~8,4 mil
- Variância (outra forma de medir dispersão):Altíssima para tempo assistido e pico de espectadores, o que indica grande variação nos dados.

### 3. Correlação entre Variáveis:
Correlação forte (próximo de 1 ou -1):

- Tempo assistido x Pico de espectadores (0.58) → canais mais assistidos tendem a ter picos maiores.
- Seguidores ganhos x Seguidores (0.71) → canais maiores ganham mais seguidores.
- Média de espectadores x Pico de espectadores (0.68) → canais que atraem grandes públicos momentâneos também mantêm boa audiência média.
- Correlação negativa: Tempo de transmissão x Média de espectadores (-0.25) → canais que transmitem muito podem ter menos espectadores médios, sugerindo que qualidade pode ser mais importante que quantidade.
                 
                 """)

        st.write("""      
##  **Perguntas e Respostas - Análise de Dados do Twitch**

    Nesta seção, analisamos os dados do Twitch e respondemos a algumas perguntas-chave sobre audiência, engajamento e crescimento dos canais.

    *** 1. O crescimento de seguidores está mais correlacionado com o tempo de transmissão ou com o pico de espectadores?**
    A análise mostra que a quantidade de seguidores ganhos está mais relacionada com a capacidade do canal de atrair grandes audiências momentâneas do que com a quantidade de tempo que ele fica no ar. A correlação entre tempo de transmissão e seguidores ganhos é praticamente nula.

    ### 2. Os canais que não transmitem em inglês têm crescimento proporcionalmente menor?**
    Como o inglês domina em número de canais e seguidores, os canais em outros idiomas têm, proporcionalmente, um crescimento menor. No entanto, isso pode ser mais uma questão de volume do que de potencial, pois esses canais atendem nichos específicos.

    ### 3. Existe uma relação entre o conteúdo adulto Mature e o número médio de espectadores?**
    O Twitch tende a favorecer conteúdos não adultos em recomendações e destaques, o que pode impactar a popularidade geral. Para responder com precisão, seria necessário cruzar essa informação com os números médios de espectadores.

    ### 4. Há canais com poucos seguidores, mas que conseguem altos picos de espectadores? O que isso pode indicar?**
    Sim! Um exemplo é o canal Pestily, que teve um pico de 616.168 espectadores, mas não está entre os que mais ganharam seguidores. Isso pode indicar eventos pontuais, colaborações ou torneios que atraem público temporário, sem conversão em seguidores.

    ### 5. Existe um idioma que apresenta maior fidelização dos espectadores em termos de média de visualizações ganhas?**
    Canais em idiomas menos comuns podem ter públicos mais fiéis, pois atendem comunidades específicas com menos alternativas. Porém, o inglês lidera em número absoluto de visualizações.

    ###  Quais são os 10 principais canais por pico de espectadores?
    | #  | Canal         | Pico de Espectadores |
    |----|---------------|--------------------|
    | 1  | Summit1g      | 310.998            |
    | 6  | NICKMERCS     | 407.428            |
    | 15 | MontanaBlack88| 110.109            |
    | 16 | Sodapoppin    | 393.348            |
    | 28 | Pestily       | 616.168            |

    ###  Quais são os 10 principais canais por seguidores ganhos?
    | #  | Canal         | Seguidores Ganhos |
    |----|---------------|-------------------|
    | 1  | Summit1g      | 25.610            |
    | 6  | NICKMERCS     | 46.084.211        |
    | 15 | MontanaBlack88| 67.740            |
    | 16 | Sodapoppin    | 2.786.162         |
    | 28 | Pestily       | 24.029.726        |

    ###  Quais são os 10 principais canais por visualizações ganhas?
    | #  | Canal         | Visualizações Obtidas |
    |----|---------------|----------------------|
    | 1  | Summit1g      | 5.310.163            |
    | 6  | NICKMERCS     | 1.089.824            |
    | 15 | MontanaBlack88| 181.600              |
    | 16 | Sodapoppin    | 19.659              |
    | 28 | Pestily       | 168.112              |

    ### 📌 Existe uma correlação entre o tempo de transmissão e o pico de espectadores?
    - A correlação entre o tempo de transmissão e o pico de espectadores é de aproximadamente ###-0.02###.
    - Isso indica uma correlação negativa muito fraca, praticamente inexistente.
    - Em outras palavras, **não há uma relação linear significativa** entre o tempo de transmissão e o número de espectadores simultâneos.

    ###  Qual é a distribuição de canais por idioma?
    | Idioma     | Quantidade de Canais |
    |------------|--------------------|
    | English    | 20                 |
    | Korean     | 2                  |
    | Spanish    | 3                  |
    | Portuguese | 3                  |
    | German     | 2                  |
    | French     | 3                  |
    | Russian    | 1                  |
    
        """)
                            
        st.write(r"""
### 📊 Distribuições:

#### - **Distribuição Normal:**
   A distribuição normal é usada para modelar variáveis contínuas que seguem uma distribuição simétrica em torno de uma média.  
   Por exemplo, o tempo de exibição dos streamers pode seguir uma distribuição normal, permitindo analisar a probabilidade de um streamer ter um tempo de exibição em um determinado intervalo.  
   A fórmula da distribuição normal para calcular a probabilidade de uma variável \( X \) estar entre dois valores \( a \) e \( b \) é:
   \[
   P(a < X < b) = \Phi\left(\frac{b - \mu}{\sigma}\right) - \Phi\left(\frac{a - \mu}{\sigma}\right)
   \]
   Onde:
   - \( \mu \): Média da distribuição.
   - \( \sigma \): Desvio padrão da distribuição.
   - \( \Phi \): Função de distribuição acumulada da normal padrão.

#### - **Distribuição Binomial:**
   A distribuição binomial é usada para calcular a probabilidade de um número específico de sucessos em um número fixo de tentativas independentes, onde cada tentativa tem apenas dois resultados possíveis (sucesso ou fracasso).  
   Por exemplo, a probabilidade de um streamer ser parceiro da Twitch pode ser modelada por uma distribuição binomial, onde cada streamer é uma tentativa com probabilidade de sucesso (ser parceiro) ou fracasso (não ser parceiro).  
   A fórmula da distribuição binomial para calcular a probabilidade de exatamente \( k \) sucessos em \( n \) tentativas é:
   \[
   P(X = k) = C(n, k) \cdot p^k \cdot (1-p)^{n-k}
   \]
   Onde:
   - \( n \): Número total de tentativas.
   - \( k \): Número de sucessos desejados.
   - \( p \): Probabilidade de sucesso em uma única tentativa.
   - \( C(n, k) \): Coeficiente binomial, que representa o número de combinações de \( n \) elementos tomados \( k \) a \( k \).

#### - **Distribuição de Poisson:**
   A distribuição de Poisson é usada para modelar o número de eventos que ocorrem em um intervalo de tempo ou espaço, quando esses eventos acontecem com uma taxa média conhecida e são independentes do tempo desde o último evento.  
   Por exemplo, o número de visualizações de um determinado conteúdo em um período de tempo pode ser modelado por uma distribuição de Poisson.  
   A fórmula da distribuição de Poisson para calcular a probabilidade de \( k \) eventos ocorrerem em um intervalo é:
   \[
   P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}
   \]
   Onde:
   - \( \lambda \): Taxa média de ocorrência dos eventos.
   - \( k \): Número de eventos desejados.
   - \( e \): Constante de Euler (aproximadamente 2.71828).
""")
        
        # Move the code that uses `df` inside the `if uploaded_file is not None:` block
        st.write(df.head())
        colunas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
        if colunas_numericas:
            coluna_escolhida = st.selectbox(" Escolha uma coluna numérica:", colunas_numericas)

            if coluna_escolhida:
                st.write(" **Distribuição dos dados:**")
                st.write(df[coluna_escolhida].describe())

                dist = st.selectbox(" Escolha a distribuição para análise:", ["Poisson", "Normal", "Binomial"])

                if dist == "Poisson":
                    lambda_est = df[coluna_escolhida].mean()
                    x = np.arange(0, 2 * lambda_est)
                    y = stats.poisson.pmf(x, lambda_est)
                    st.write(" **Distribuição de Poisson**")
                    fig = go.Figure(data=[go.Bar(x=x, y=y)])
                    st.plotly_chart(fig)

                elif dist == "Normal":
                    mu_est = df[coluna_escolhida].mean()
                    sigma_est = df[coluna_escolhida].std()
                    x = np.linspace(mu_est - 4*sigma_est, mu_est + 4*sigma_est, 100)
                    y = stats.norm.pdf(x, mu_est, sigma_est)
                    st.write(" **Distribuição Normal**")
                    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines')])
                    st.plotly_chart(fig)

                elif dist == "Binomial":
                    n = 10  # número de tentativas fixo
                    p = df[coluna_escolhida].mean() / max(df[coluna_escolhida])
                    x = np.arange(0, n + 1)
                    y = stats.binom.pmf(x, n, p)
                    st.write(" **Distribuição Binomial**")
                    fig = go.Figure(data=[go.Bar(x=x, y=y)])
                    st.plotly_chart(fig)