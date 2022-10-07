# Taxa Rotatividade Telecom

Desenvolver uma análise e um modelo preditivo para identificar os fatores mais relevantes na decisão dos clientes de cancelar o plano. Sendo assim, sabendo os motivos que levam ao cancelamento, ajudar a empresa a entender melhor as necessidades e prioridades dos clientes, buscando manter um maior número de clientes ativos, ou seja, uma menor taxa de rotatividade.

Levando em consideração os dados de usabilidade dos produtos ofertados ao cliente pela empresa de telecomunicação, acreditasse ponderar os fatores que levam um cliente a desistir do plano com a empresa de telecomunicação e destacar as prioridades que uma empresa deve seguir para manter seus clientes.

## Dados

Estão divididos em dois arquivos:

* Dataset contendo 70 mil linhas e 172 colunas, incluindo a variável target.
* Dicionário de dados com os significados dos acrônimos das variáveis. Para compreensão dos termos da área de telecomunicações.

### Colunas

* CIRCLE_ID: Área a qual o cliente pertence
* LOC: Ligações locais - dentro da mesma área
* STD: chamadas padrão - fora da área
* IC: Chamadas recebidas
* OG: Chamadas realizadas
* T2T: Ligações entre mesma operadora (entre celulares)
* T2M: Ligações entre outra operadora de celular
* T2O: Ligações para outra operadora de linha fixa
* T2F: Ligações para linha fixa da mesma operadora
* T2C: Ligações para o próprio call center
* ARPU: Receita média por cliente
* MOU: Minutos de uso - chamadas de voz
* AON: Tempo na operadora - número de dias que o cliente está usando a operadora
* ONNET: Todos os tipos de chamadas dentro da mesma operadora
* OFFNET: Todos os tipos de chamadas de fora da operadora
* ROAM: Indica que o cliente está na zona de roaming (itinerância) durante a chamada
* SPL: Chamadas especiais
* ISD: Chamadas internacionais
* RECH: Recarga
* NUM: Número
* AMT: Valor em moeda local
* MAX: Máximo
* DATA: Internet móvel
* 3G: Network 3G
* AV: Média
* VOL: Volume de uso da internet móvel (em MB)
* 2G: Network 2G
* PCK: Serviços pré-pagos
* NIGHT: Serviços somente noturnos
* MONTHLY: Serviços com validade equivalente a um mês
* SACHET: Serviços com validade menor que um mês
* *.6: KPI relativo ao mês de junho
* *.7: KPI relativo ao mês de julho
* *.8: KPI relativo ao mês de agosto
* FB_USER: Serviço de benefício ao uso do Facebook e outras redes sociais similares
* VBC: Custo baseado em volume - quando nenhum serviço específico é adquirido e pago por uso

## Requisitos
O python deve ser igual ou maior de 3.10.2
## Como executar o projeto

1. Crie o ambiente com o comando:
**python -m venv NOME_DA_PASTA_DO_AMBIENTE**
2. Ative o ambiente com o comando:
* Windows: **.\NOME_DA_PASTA_DO_AMBIENTE\Scripts\activate.bat**
* Linux: **source <NOME_DA_PASTA_DO_AMBIENTE>/bin/activate**
3. Atualiza o pip: **python -m pip install --upgrade pip**
4. Instale as dependências: **pip install -r requirements.txt**
5. execute o arquivo python api.py: **python src/server/api.py**

## Como executar o projeto localmente
Acessando o link: **http://127.0.0.1:33507** ou **http://localhost:33507**
## Como executar o projeto no heroku
Acessando o link: **https://churn-probability.herokuapp.com/**

## Dados de teste
Estão na pasta data com o nome de teste.csv.