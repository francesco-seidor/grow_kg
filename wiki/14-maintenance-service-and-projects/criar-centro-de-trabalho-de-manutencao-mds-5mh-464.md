---
id: 14-maintenance-service-and-projects/criar-centro-de-trabalho-de-manutencao-mds-5mh-464
title: Criar centro de trabalho de manutenção – MDS (5MH) (5MH_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese master data script (5MH) for creating a maintenance work center (CR01) in SAP S/4HANA Cloud Public Edition 2608, with test steps."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/maintenance-work-centers]
aliases: [5MH_S4CLD2608_Master_Data_PT_XX]
keywords: [Maintenance Work Centers, maintenance work center, work center master data, work center category, standard value key, capacity planning, cost center, business roles, master data scripts, 5MH]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-464
topic: 14-maintenance-service-and-projects/maintenance-work-centers
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar centro de trabalho de manutenção – MDS (5MH) (5MH_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Maintenance Work Centers** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar centro de trabalho de manutenção – MDS (5MH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893823)

[2 Pré-requisitos 3](#_Toc233893824)

[2.1 Acesso ao sistema 3](#_Toc233893825)

[2.2 Funções 3](#_Toc233893826)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893827)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893828)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233893829)

[2.5.1 Categoria do centro de trabalho 4](#_Toc233893830)

[3 Tabela de síntese 5](#_Toc233893831)

[4 Procedimento 6](#_Toc233893832)

[4.1 Criar centro de trabalho de manutenção 6](#_Toc233893833)

## Objetivo

Neste documento você encontra uma descrição sobre como criar um registro de dados mestre do grupo de centro de trabalho de manutenção para o seu sistema S/4HANA. A descrição inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema "normal". O leitor aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo de conteúdo do S/4HANA, fornecido pelo SAP Best Practices, não estão descritos neste documento, embora possam aparecer na interface de usuário (IU).

Um registro mestre de centro de trabalho de manutenção criada como descrito aqui, pode ser usada para processos de manutenção.

## Pré-requisitos

Esta seção resume todos os pré-requisitos para a criação de um centro de trabalho.

### Acesso ao sistema

O teste deve ser conduzido com o seguinte sistema:

Tabela 1:

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece o URL para acessar os vários apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (espaço) | ID (espaço) |
| --- | --- | --- | --- |
| Engenheiro de produção - produção discreta | SAP_BR_PRODN_ENG_DISC | Engenharia de produção - produção discreta | SAP_BR_PRODN_ENG_DISC |

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre são dependentes das unidades organizacionais da empresa. Os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Todos os dados | Centro |  | Todos os dados para um centro de trabalho dependem do centro. | Centro: –––––-- |

### Dados mestre obrigatórios e opcionais

Os registros de dados do centro de trabalho podem fazer referência a outros dados mestre. A tabela seguinte oferece uma síntese dos objetos de dados mestre, opcionais e obrigatórios, a serem usados em um centro de trabalho.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Chave de valor padrão | Na guia Dados básicos da tela do centro de trabalho, você encontra a entrada da chave de valor padrão na seção de atualização de valores padrão. | Obrigatório | O sistema utiliza valores padrão como parâmetros com o valor padrão de origem em fórmulas para calcular o tempo de execução, as necessidades de capacidade e os custos. Você utiliza a chave de valor padrão para atribuiir um ID de parâmetro a valores padrão. Este ID de parâmetro identifica o valor padrão em uma fórmula. Você pode utilizar o ID de parâmetro para determinar a palavra-chave para um valor padrão, como a preparação, a máquina ou a mão-de-obra. |

### Parâmetros principais para a criação de dados

Nesta seção, descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um centro de trabalho de manutenção:

#### Categoria do centro de trabalho

A categoria do centro de trabalho determina que dados podem ser atualizados no registro mestre para o centro de trabalho. A distinção dos centros de trabalho pode ser feita pela categoria (por exemplo, centro de trabalho de produção, centro de trabalho de manutenção, centro de trabalho de serviço etc.)

Tabela 2:

| Categoria do centro de trabalho | Descrição |
| --- | --- |
| 0005 | Manutenção |

## Tabela de síntese

Este item de escopo é composto por várias etapas de processo listadas na tabela.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar centro de trabalho de manutenção](#unique_10) [página ] 6 | SAP_BR_PRODN_ENG_DISC | Criar centro de trabalho(CR01) | O centro de trabalho é criado. |

## Procedimento

Esta seção descreve os procedimentos para cada etapa do processo que pertence a este item de escopo. Você pode também pode utilizar estes procedimentos para testar a criação de dados mestre.

### Criar centro de trabalho de manutenção

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como SAP_BR_PRODN_ENG_DISC. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar centro de trabalho(CR01). | É aberta uma nova janela exibindo Criar centro de trabalho: 1ª tela. |  |
| 3 | Inserir código do centro | Insira o código do centro: <1010> | A tela Criar organização é exibida. |  |
| 4 | Inserir ID do centro de trabalho | Insira o ID do centro de trabalho: </RES-0100>Nota O comprimento do campo do ID do centro de trabalho é inferior a 8. |  |  |
| 5 | Categoria do centro de trabalho | Selecione a categoria do centro de trabalho: <0005 > Manutenção do centro |  |  |
| 6 | Selecionar dados básicos | Clique no botão Dados básicos, no canto superior esquerdo da tela. | A tela Criar centro de trabalho: dados básicos é exibida. |  |
| 7 | Inserir a descrição do centro de trabalho, selecionar a pessoa responsável, a utilização e a chave de valor padrão | Na guia Dados básicos, insira os seguintes dados:Descrição: por exemplo, RES-0100Pessoa responsável: por exemplo, <YMM> Supervisor de mecânico de manutençãoUso: por exemplo, <004> Somente listas de tarefas de manutençãoChave de valor padrão: por exemplo, <SAP0> Nenhum valor padrão |  |  |
| 8 | Inserir chave de controle | Na guia Valores padrão, insira os seguintes dados:Chave de controle: por exemplo, <YBM1> Manutenção - Interno. |  |  |
| 9 | Definir fórmulas de capacidade e outras | Na guia Capacidades, insira os seguintes dados:Categoria de capacidade: por exemplo, <002> PessoaOutra fórmula: por exemplo, <YBPM01> Proj:RqmtsNetwkMai | Pressione Enter. A tela Criar capacidade do centro de trabalho: cabeçalho, é exibida. |  |
| 10 | Definir capacidade do centro de trabalho | Na seção Capacidade do centro de trabalho: cabeçalho, insira os dados seguintes:Descrição da categoria da capacidade: por exemplo, Capacidade mecânicaResponsável pela capacidade: por exemplo, <A> Grupo de planejamento ACalendário de fábrica: ID do calendário para seu país, por exemplo, <01> Alemanha (padrão)Unidade básica de recurso: Por exemplo, <H> HoraHora de início: por exemplo, 06:00:00Hora final: por exemplo, <14:30:00>Duração de intervalos: por exemplo, <00:30:00>Ocupação da capacidade: por exemplo, <100>Nº capacidades indivs.: por exemplo, <10>Planejamento a longo prazo: <X> | Pressione Enter. A tela volta para a síntese de capacidades. |  |
| 11 | Inserir dados de programação | Na guia Programação, insira os seguintes dados:Categoria de capacidade: por exemplo, <002> Pessoa |  |  |
| 12 | Inserir dados do cálculo de custos | Na guia Cálculo de custos, insira os seguintes dados:Data de início: por exemplo, <01/01/2015>Centro de custos: por exemplo, < 10101701> Centro e Manutenção (DE)Tipo de atividade processamento interno: por exemplo, 11 Horas de pessoalChave de fórmula para o cálculo de custos: por exemplo, <YBPM01> Proj:RqmtsNetwkMaint |  |  |
| 13 | Salvar os dados | Salve as entradas | As entradas são salvas. |  |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example | Words or characters quoted from the screen. These include field names, screen titles, pushbuttons labels, menu names, menu paths, and menu options.Textual cross-references to other documents. |
| Example | Emphasized words or expressions. |
| EXAMPLE | Technical names of system objects. These include report names, program names, transaction codes, table names, and key concepts of a programming language when they are surrounded by body text, for example, SELECT and INCLUDE. |
| Example | Output on the screen. This includes file and directory names and their paths, messages, names of variables and parameters, source text, and names of installation, upgrade and database tools. |
| Example | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example> | Variable user entry. Angle brackets indicate that you replace these words and characters with appropriate entries to make entries in the system. |
| EXAMPLE | Keys on the keyboard, for example, F2 or ENTER. |

|  |
| --- |
|  |
| www.sap.com/contactsap |
| © 2026 SAP SE or an SAP affiliate company. All rights reserved.No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE or an SAP affiliate company. The information contained herein may be changed without prior notice. Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors. National product specifications may vary.These materials are provided by SAP SE or an SAP affiliate company for informational purposes only, without representation or warranty of any kind, and SAP or its affiliated companies shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP or SAP affiliate company products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty. SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE (or an SAP affiliate company) in Germany and other countries. All other product and service names mentioned are the trademarks of their respective companies. See [www.sap.com/copyright](http://www.sap.com/copyright) for additional trademark information and notices. |

<!-- image omitted: SAP Logo -->

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/create-maintenance-work-center-mds-5mh-461]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mh-463]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mh-465]]
- related-to :: [[14-maintenance-service-and-projects/script-de-datos-maestros-crear-puesto-de-trabajo-de-mantenimiento-mds]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 12,455 chars in the whole document
