# PIPA — Public Indicators Platform for Angola

PIPA é uma plataforma de conhecimento dedicada à exploração, análise e
divulgação de indicadores públicos oficiais de Angola. Inspirada na
filosofia de storytelling de dados do [Our World in Data](https://ourworldindata.org/),
o objetivo do PIPA é transformar informação estatística complexa em
conhecimento acessível para cidadãos, investigadores, jornalistas,
decisores políticos e instituições públicas.

PIPA não é apenas um dashboard. É uma plataforma de conhecimento.

## Visão Geral da Arquitetura

O PIPA segue uma arquitetura em camadas estrita, onde cada camada
comunica apenas com a camada imediatamente adjacente:

```
Streamlit UI (app/)
        │
        ▼
Components (components/)      ← apenas apresentação, sem lógica de negócio
        │
        ▼
Services (services/)          ← lógica de negócio
        │
        ▼
Repositories (repositories/)  ← acesso a dados
        │
        ▼
Supabase (database/)          ← fonte única da verdade
```

### Regras arquiteturais obrigatórias

1. Lógica de negócio NUNCA existe dentro das páginas Streamlit.
2. Toda consulta à base de dados passa pela camada de Services.
3. Componentes de visualização nunca conhecem detalhes da base de dados.
4. Páginas comunicam apenas com Services.
5. Services comunicam apenas com Repositories.
6. Repositories comunicam apenas com o Supabase.
7. Nenhum módulo acede à implementação interna de outro módulo.

### Estrutura de diretórios

```
PIPA/
├── app/                # Interface Streamlit (páginas e entrypoint)
│   └── pages/
├── components/          # Componentes visuais reutilizáveis
├── services/             # Lógica de negócio
├── repositories/         # Acesso a dados (Supabase)
├── database/             # Cliente Supabase (singleton)
├── models/               # Entidades de domínio (Province, Indicator, Observation)
├── utils/                # Configuração e utilitários
├── .streamlit/           # Configuração e segredos do Streamlit
├── requirements.txt
├── .env.example
└── .gitignore
```

## Base de Dados

O PIPA utiliza um modelo dimensional (Star Schema) no Supabase
(PostgreSQL), com as seguintes tabelas principais:

| Tabela | Descrição |
|---|---|
| `dim_provincia` | Províncias de Angola |
| `dim_setor` | Setores estatísticos |
| `dim_indicador` | Indicadores estatísticos |
| `fonte_dados` | Fontes oficiais de dados |
| `fato_indicador` | Observações numéricas |

Todos os valores numéricos apresentados pela plataforma têm origem
exclusivamente na base de dados. A Inteligência Artificial nunca gera
valores estatísticos — apenas interpreta e explica informação já
existente.

## Instalação

### Pré-requisitos

- Python 3.10 ou superior
- Uma conta e projeto no [Supabase](https://supabase.com/)

### Passos

1. Clone o repositório:

   ```bash
   git clone https://github.com/<sua-organizacao>/PIPA.git
   cd PIPA
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Configuração das Variáveis de Ambiente

O PIPA lê as credenciais do Supabase tanto de variáveis de ambiente
(`.env`) como dos segredos do Streamlit (`.streamlit/secrets.toml`),
consoante o ambiente de execução.

### Desenvolvimento local (.env)

Copie o ficheiro de exemplo e preencha com as suas credenciais:

```bash
cp .env.example .env
```

```
SUPABASE_URL=https://<seu-projeto>.supabase.co
SUPABASE_KEY=<sua-chave-anon-ou-service>
```

### Streamlit Cloud (secrets.toml)

Copie o ficheiro de exemplo:

```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

```toml
SUPABASE_URL = "https://<seu-projeto>.supabase.co"
SUPABASE_KEY = "<sua-chave-anon-ou-service>"
```

> **Importante:** nem `.env` nem `.streamlit/secrets.toml` devem ser
> submetidos ao repositório Git — ambos já estão incluídos no
> `.gitignore`.

## Como Executar a Aplicação

```bash
streamlit run app/main.py
```

A aplicação ficará disponível em `http://localhost:8501`.

## Deployment

O deployment de produção é feito através do **Streamlit Cloud**,
ligado diretamente ao repositório oficial no GitHub. Cada atualização
enviada para a branch de produção despoleta automaticamente um novo
deployment. As credenciais do Supabase devem ser configuradas nos
segredos da aplicação, diretamente no painel do Streamlit Cloud.

## Estado do Projeto

Este repositório encontra-se em fase de desenvolvimento ativo do MVP.
Consulte a especificação técnica oficial do projeto para mais detalhes
sobre a arquitetura, o modelo de dados e a estratégia de deployment.
