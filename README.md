
# Iris Classification API

## 1. Sobre o projeto

Este projeto desenvolve uma API REST para classificação de espécies de flores
utilizando Machine Learning.

A aplicação utiliza o conjunto de dados Iris e um modelo de Regressão
Logística treinado com a biblioteca Scikit-learn.

A API recebe as medidas de uma flor e retorna a classe prevista e o nome
da espécie correspondente.

O projeto foi desenvolvido como parte de um trabalho acadêmico sobre
Machine Learning, desenvolvimento de APIs e implantação de modelos
preditivos.

## 2. Objetivos

- Treinar e avaliar um modelo de Machine Learning.
- Disponibilizar o modelo por meio de uma API REST.
- Validar os dados recebidos pela aplicação.
- Implementar testes automatizados.
- Organizar o projeto em módulos para facilitar sua manutenção.

## 3. Tecnologias utilizadas

- Python
- Pandas
- Scikit-learn
- Joblib
- FastAPI
- Uvicorn
- Pytest
- HTTPX

## 4. Conjunto de dados

Foi utilizado o conjunto de dados Iris, composto por 150 amostras de flores,
com quatro características de entrada:

- Comprimento da sépala (sepal length).
- Largura da sépala (sepal width).
- Comprimento da pétala (petal length).
- Largura da pétala (petal width).

O modelo classifica as amostras em três espécies:

- Setosa
- Versicolor
- Virginica

## 5. Modelo de Machine Learning

O modelo utiliza um pipeline composto por:

1. Imputação de valores ausentes pela mediana.
2. Padronização das características com StandardScaler.
3. Classificação por Regressão Logística.

O modelo foi treinado com os dados de treinamento e avaliado separadamente
nos conjuntos de validação e teste.

## 6. Resultados

### Métricas de validação

- Acurácia: 0.8636
- Precisão macro: 0.8611
- Revocação macro: 0.8571
- F1-score macro: 0.8564

### Métricas de teste

- Acurácia: 0.9565
- Precisão macro: 0.9630
- Revocação macro: 0.9583
- F1-score macro: 0.9582

As métricas representam os resultados obtidos durante a avaliação do modelo
neste experimento. O desempenho pode variar conforme a divisão dos dados,
as configurações e o ambiente de execução.

## 7. Estrutura do projeto

```text
projeto-ml-api/
├── models/
│   └── model.joblib
├── reports/
│   └── metrics.json
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   ├── services.py
│   └── routers/
│       ├── __init__.py
│       ├── health.py
│       └── predict.py
├── tests/
│   └── test_api.py
├── requirements.txt
└── README.md
