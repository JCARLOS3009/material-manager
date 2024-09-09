# Sistema de Gestão para Construção de Moradias de Emergência

Este software foi desenvolvido em Python para atender as necessidades de controle de materiais de construção, logística de transporte e gestão de estoque de alimentos em projetos de construção de moradias de emergência para comunidades carentes.

## Funcionalidades

- **Controle de Materiais de Construção**: Monitora a quantidade de materiais disponíveis, seu uso em diferentes projetos e a necessidade de reposição.
- **Logística de Transporte**: Gera rotas otimizadas para a entrega de materiais e alimentos, considerando a urgência e as necessidades das comunidades.
- **Gestão de Estoque de Alimentos**: Mantém o controle do estoque de alimentos, garantindo que os suprimentos necessários estejam disponíveis e sejam distribuídos de forma eficiente.

## Estrutura do Projeto

O software é modular e foi estruturado para ser facilmente escalável. Abaixo está a estrutura básica dos diretórios:

/gestao_moradias_emergencia
│
├── app.py # Código principal do software
├── controllers # Módulos de controle (materiais, transporte, estoque)
│ ├── controle_materiais.py
│ ├── logistica_transporte.py
│ └── gestao_estoque.py
├── models # Definição dos modelos de dados
│ ├── materiais.py
│ ├── transporte.py
│ └── alimentos.py
├── views # Interfaces e templates (se aplicável)
│ └── templates # Arquivos HTML e interfaces de usuário
├── utils # Funções utilitárias e auxiliares
│ └── calculos.py
└── requirements.txt # Dependências do projeto
## Requisitos

Antes de executar o software, certifique-se de que o Python 3.6 ou superior esteja instalado no seu sistema. Além disso, todas as dependências necessárias estão listadas no arquivo `requirements.txt`.

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/gestao-moradias-emergencia.git
   cd gestao-moradias-emergencia
   ```
##Execução do Software
Para iniciar o software, execute o seguinte comando:
  ```bash
    python app.py
  ```
O software fornecerá uma interface para gerenciar materiais, transporte e estoque de alimentos de forma integrada. A interface pode ser acessada via um navegador da web (se uma interface gráfica foi implementada) ou por meio de uma linha de comando.

##Personalização
Controle de Materiais: As regras de uso e reposição de materiais podem ser ajustadas no módulo controle_materiais.py.
Logística de Transporte: Parâmetros de rotas e urgências podem ser configurados no módulo logistica_transporte.py.
Gestão de Estoque: As funcionalidades de gestão de alimentos estão no módulo gestao_estoque.py.

Amostra de Deploy do Software em:
https://replit.com/@JosCarlosCarl39/Flask-Python-CRUD-SQLite?v=1
