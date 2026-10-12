---
id: 12-production-and-manufacturing/script-de-dados-mestre-criar-centro-de-trabalho-da-producao-mds-bnj-62
title: Script de dados mestre - Criar centro de trabalho da produção – MDS (BNJ) (BNJ_S4CLD2608_Master_Data_PT_XX)
description: SAP S/4HANA Cloud Public Edition 2608 master data script (Portuguese) for creating production work centers and optional work center groups via Fiori apps.
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-work-centers]
aliases: [BNJ_S4CLD2608_Master_Data_PT_XX]
keywords: [Production Work Centers and Work Center Groups, work centers, work center groups, work center category, master data scripts, business roles, standard value keys, capacity planning, routings, production costing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-620
topic: 12-production-and-manufacturing/production-work-centers
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar centro de trabalho da produção – MDS (BNJ) (BNJ_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Production Work Centers and Work Center Groups** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar centro de trabalho da produção – MDS (BNJ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894056)

[2 Pré-requisitos 3](#_Toc233894057)

[2.1 Acesso ao sistema 3](#_Toc233894058)

[2.2 Funções 3](#_Toc233894059)

[2.3 Unidades organizacionais necessárias 3](#_Toc233894060)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233894061)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233894062)

[2.5.1 Categoria do centro de trabalho 4](#_Toc233894063)

[3 Tabela de síntese 5](#_Toc233894064)

[4 Procedimentos de teste 6](#_Toc233894065)

[4.1 Criar centro de trabalho 6](#_Toc233894066)

[4.2 (Opcional) Administrar grupos de centros de trabalho 8](#_Toc233894067)

[4.2.1 Criar grupo de centros de trabalho (opcional) 8](#_Toc233894068)

[4.2.2 Atribuir centro de trabalho (opcional) 9](#_Toc233894069)

[5 Anexo 11](#_Toc233894070)

[5.1 Criar roteiro 11](#_Toc233894071)

## Objetivo

Um centro de trabalho é o local onde são executadas as operações de produção. Por exemplo, um centro de trabalho pode representar uma linha de produção, máquina, grupo de máquinas, empregado ou grupo de empregados.

Um centro de trabalho possui informações utilizadas para planejamento de capacidades (por exemplo, capacidade disponível), programação (por exemplo, fórmula do tempo de processamento) e cálculo de custos (por exemplo, centro de custos). Essa informação é utilizada em listas de tarefas e transações como as ordens de trabalho de produção. As informações são específicas de um centro de produção (conhecido como centro).

## Pré-requisitos

Esta seção resume todos os pré-requisitos necessários para conduzir o teste em termos de sistemas, usuários, dados mestre, dados organizacionais, outros dados de teste e condições empresariais.

### Acesso ao sistema

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece o URL para acessar os diversos apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) | Efetuar login |
| --- | --- | --- | --- | --- |
| Engenheiro de produção - produção discreta | SAP_BR_PRODN_ENG_DISC | Engenharia de produção - produção discreta | SAP_BR_PRODN_ENG_DISC |  |

### Unidades organizacionais necessárias

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser utilizada |
| --- | --- | --- | --- | --- |
| Todos os dados | Centro |  | Todos os dados para um centro de trabalho dependem do centro. | Centro:__________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados do centro de trabalho podem fazer referência a outros dados mestre. A tabela seguinte oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um centro de trabalho.

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Chave de valor padrão | Na IU do centro de trabalho, guia de dados básicos, você encontra a entrada da chave de valor padrão na seção atualização de valores padrão. | Obrigatório | O sistema utiliza valores padrão como parâmetros com o valor padrão de origem em fórmulas para calcular o tempo de execução, as necessidades de capacidade e os custos.Você utiliza a chave de valor padrão para atribuiir um ID de parâmetro a valores padrão. Este ID de parâmetro identifica o valor padrão em uma fórmula. Você pode utilizar o ID de parâmetro para determinar a palavra-chave para um valor padrão, como a preparação, a máquina ou a mão-de-obra. |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um centro de trabalho:

#### Categoria do centro de trabalho

A categoria do centro de trabalho determina que dados podem ser atualizados no registro mestre para o centro de trabalho. Os centros de trabalho podem ser distinguidos pela sua categoria (por exemplo, centro de trabalho de produção, centro de trabalho de manutenção e centro de trabalho de serviço, etc.)

| Categoria do centro de trabalho | Descrição |
| --- | --- |
| 0001 | Máquina |
| 0007 | Linha de produção |

## Tabela de síntese

Este item de escopo é composto por várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação | Resultados esperados |
| --- | --- | --- | --- |
| [Criar centro de trabalho](#unique_10) [página ] 6 | Engenheiro de produção - produção discreta | Administrar centros de trabalho(F6175) |  |
| [Criar grupo de centros de trabalho (opcional)](#unique_11) [página ] 8 | Engenheiro de produção - produção discreta | Administrar grupos de centros de trabalho(F4044) |  |
| [Atribuir centro de trabalho (opcional)](#unique_12) [página ] 9 | Engenheiro de produção - produção discreta | Administrar grupos de centros de trabalho(F4044) |  |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar centro de trabalho

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Engenheiro de produção - produção discreta. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Abrir o app SAP Fiori | Clique em Administrar centros de trabalho(F6175). |  |  |
| 3 | Selecionar Criar | Selecione Criar. | É exibida uma nova tela Criar centro de trabalho: 1ª tela. |  |
| 4 | Inserir código do centro | Insira Código do centro. | A tela Criar organização é exibida. |  |
| 5 | Inserir ID do centro de trabalho | Insira ID do centro de trabalho.Nota O comprimento do campo do ID do centro de trabalho é inferior a 8. |  |  |
| 6 | Categoria do centro de trabalho | Selecione a categoria do centro de trabalho:<0001> Máquina<0007> Linha de produção |  |  |
| 7 | Selecionar dados básicos | Selecione o botão Dados básicos na parte superior esquerda da tela. | A tela Criar centro de trabalho: dados básicos é exibida. |  |
| 8 | Inserir dados | Na guia Dados básicos, insira os seguintes dados:Descrição: <insira a descrição>Pessoa responsável: <pessoa responsável ou pessoa responsável pelo centro>Utilização: <009>Chave de valor padrão: <SAP1> |  |  |
| 9 | Definir as fórmulas de capacidade e processamento | Na guia capacidades, insira os seguintes dados:Categoria de capacidade: <001(máquina/002(pessoa)>Configurar fórmula: <SAP005>Fórmula de processamento: <SAP006>Pressione Enter. | A tela Criar capacidade do centro de trabalho: cabeçalho é exibida. |  |
| 10 | Definir capacidade do centro de trabalho | Na seção Capacidade do centro de trabalho: cabeçalho, insira os seguintes dadosDescrição da categoria da capacidade: <adicionar uma descrição>Responsável pela capacidade: Pressione F4 para procurar pela pessoa responsável pelo centro.ID do calendário de fábrica: <calendário para seu país>Versão ativa: <1>Unidade básica de capacidade: por exemplo, DHora de início: <hora de início>Hora final: <hora final>Duração de intervalos: <duração de intervalos>Tempo da operação: <tempo da operação>Utilização de capacidades: <100>Nº capacids. indiv.: <10>Relevante para programação finita: <X>Planejamento a longo prazo: <X>Pode ser utilizado por várias operações: <X>Pressione Enter. | A tela volta para a síntese de capacidades. |  |
| 11 | Inserir dados de programação | Na guia Programação, insira os seguintes dados:Categoria de capacidade: <001(máquina/002(pessoa)>Tempo de setup: <SAP001>Duração de processamento: <SAP002> |  |  |
| 12 | Inserir dados do cálculo de custos | Na guia Cálculo de custos, insira os seguintes dados:Centro de custo: <centro de custo para sua empresa>Tipo de atividade (para configurar): <3>Fórmula (para configurar): <SAP005>Tipo de atividade (máquina): <1>Fórmula (máquina): <SAP006>Tipo de atividade （trabalho）: <11>Fórmula （trabalho）: <SAP007>Unidade de atividade: selecione a UM necessária, por exemplo, min. |  |  |
| 13 | Salvar os dados | Salve as entradas. |  |  |

### (Opcional) Administrar grupos de centros de trabalho

Objetivo

Este capítulo mostra como agrupar os centros de trabalho, se necessário.

#### Criar grupo de centros de trabalho (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Esta etapa do processo mostra como criar grupo de centros de trabalho.

É possível verificar os grupos de centros de trabalho de amostra criados por meio da etapa de processo Criar e atribuir grupo de centros de trabalho no item de escopo 31L.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Engenheiro de produção - produção discreta. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app | Abra Administrar grupos de centros de trabalho(F4044). | O app é aberto. |  |
| 3 | Criar grupo | Clique em Criar acima da tabela.Na tela Criar grupo, efetue as seguintes entradas:Grupo: <inserir o nome do grupo>Centro: 1010Tipo de grupo: <ALTERNATIVO> ou <MESMA LINHA> ou <RESPONSABILIDADE>Descrição: <Inserir a descrição>Clique em Criar. | O grupo de centros de trabalho foi criado. |  |

#### Atribuir centro de trabalho (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Esta etapa do processo mostra como atribuir centros de trabalho a grupos de centros de trabalho.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Engenheiro de produção - produção discreta. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app | Abra Administrar grupos de centros de trabalho(F4044). | O app é aberto. |  |
| 3 | Selecionar o grupo | Procure o grupo criado na etapa anterior e escolha o ícone ">" no fim da linha. | A lista de informações detalhadas é exibida no painel direito. |  |
| 4 | Atribuir centro de trabalho | Na seção Componentes do grupo, clique em Atribuir centro de trabalho.Selecione um ou mais centros de trabalho na caixa de diálogo e clique em OK.Nota Caso um centro de trabalho já tenha sido atribuído a outro grupo, será exibida uma mensagem de erro: Centro de trabalho 'XXX' já atribuído a esse tipo de grupo. | Os centros de trabalho atribuídos ao grupo são exibidos.Os centros de trabalho foram atribuídos com êxito. |  |

## Anexo

### Criar roteiro

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Roteiro |  |  | Para executar esta atividade, execute o script de teste Criar roteiro – MDS (BNL). |

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
- related-to :: [[12-production-and-manufacturing/create-production-work-center-mds-bnj-617]]
- related-to :: [[12-production-and-manufacturing/mds-bnj-619]]
- related-to :: [[12-production-and-manufacturing/mds-bnj-621]]
- related-to :: [[12-production-and-manufacturing/script-de-datos-maestros-crear-puesto-de-trabajo-de-produccion-mds-bnj]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 15,920 chars in the whole document
