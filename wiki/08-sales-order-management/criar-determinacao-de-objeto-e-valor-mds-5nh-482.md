---
id: 08-sales-order-management/criar-determinacao-de-objeto-e-valor-mds-5nh-482
title: Criar determinação de objeto e valor - MDS (5NH) (5NH_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese master data script (5NH) for SAP S/4HANA Cloud Public Edition: create characteristic combinations, accesses and substitution controls for product/plant/warehouse substitution in AATP."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/product-and-location-substitution]
aliases: [5NH_S4CLD2608_Master_Data_PT_XX]
keywords: ["Product, Plant and Storage Location Substitution", object and value determination, substitution controls, characteristic combinations, access sequences, product substitution, plant substitution, warehouse substitution, availability check, master data scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NH_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-482
topic: 08-sales-order-management/product-and-location-substitution
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar determinação de objeto e valor - MDS (5NH) (5NH_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NH_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Product, Plant and Storage Location Substitution** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar determinação de objeto e valor - MDS (5NH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893845)

[2 Pré-requisitos 3](#_Toc233893846)

[2.1 Acesso ao sistema 3](#_Toc233893847)

[2.2 Funções 3](#_Toc233893848)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893849)

[2.4 Dados mestre obrigatórios 4](#_Toc233893850)

[2.5 Etapas preliminares 4](#_Toc233893851)

[2.5.1 Criar controle para substituição do produto (opcional) 4](#_Toc233893852)

[2.5.2 Criar controle para substituição de centro (opcional) 6](#_Toc233893853)

[2.5.3 Criar controle para substituição de depósito (opcional) 7](#_Toc233893854)

[3 Tabela de síntese 10](#_Toc233893855)

[4 Procedimentos de teste 11](#_Toc233893856)

[4.1 Criar combinação de características 11](#_Toc233893857)

[4.2 Criar acesso 12](#_Toc233893858)

## Objetivo

Neste documento, você aprenderá a criar uma combinação e o acesso com valores de característica para os dados mestre da combinação do seu sistema SAP S/4HANA Cloud Public Edition.

A determinação de objeto e valor permite que um usuário configure as características para determinar um controle que seria utilizado para substituir um produto/centro/depósito na ordem do cliente durante a verificação de disponibilidade.

Isso permite a integração da substituição de dados mestre com a confirmação baseada em alternativa (ABC) da funcionalidade AATP.

## Pré-requisitos

Esta seção resume todos os pré-requisitos necessários para conduzir o teste em termos de sistemas, usuários, dados mestre, dados organizacionais, outros dados de teste e condições empresariais.

### Acesso ao sistema

| sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece a você o URL para acessar os vários apps atribuídos a sua função. |

### Funções

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) | Efetuar login |
| --- | --- | --- | --- | --- |
| Administrador de cumprimento de ordens | SAP_BR_ORDER_FULFILLMNT_MNGR | Administração de cumprimento da ordem | SAP_BR_ORDER_FULFILLMNT_MNGR |  |
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Dados mestre - produtos / Governança de produto | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Unidades organizacionais necessárias

Não são necessários dados organizacionais específicos.

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

### Dados mestre obrigatórios

Não são necessários dados mestre específicos.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
|  |  |  |  |

Para mais informações sobre criação de objetos de dados mestre, consulte Tabela 1: Referência a script de dados mestre:

| MDS | Descrição |
| --- | --- |
|  |  |

### Etapas preliminares

#### Criar controle para substituição do produto (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções sobre a criação de controle para grupos de substituição/exclusão de produtos. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar controles de substituição - Produtos(F4787). | O app é aberto. |  |
| 3 | Selecione Create | Na tela Administrar controles de substituição – Produtos, clique em Criar. | A tela Administrar controles de substituição - Criar produtos é exibida. |  |
| 4 | Inserir controle | Na seção Cabeçalho, efetue a seguinte entrada:Controle: <insira o novo controle para substituição, por exemplo, VENDA> |  |  |
| 5 | Selecione Create | Clique em Criar. | A mensagem do sistema Acesso criado é exibida. |  |
| 6 | Criar descrição | Na seção Descrição, clique em Criar. | A tela Criar descrição de controle é exibida. |  |
| 7 | Inserir dados de descrição | Na seção Descrição, efetue as seguintes entradas:Código de idioma: <insira o idioma aplicável ao controle, por exemplo, IN para inglês>Descrição do controle: <insira o texto para descrever o controle, por exemplo, Para venda> |  |  |
| 8 | Selecione Create | Clique em Criar. | A mensagem do sistema Descrição de controle criada é exibida. |  |
| 9 | Clicar em Voltar | Na seção Título, clique em < (Voltar). | A tela Administrar controles de substituição - Produtos é exibida. |  |
| 10 | Grupos atribuídos | Na seção grupos atribuídos, clique em Atribuir. | A caixa de diálogo Atribuir grupos ao controle é exibida. |  |
| 11 | Seleciona grupo | Na caixa de diálogo Atribuir grupos ao controle, pesquise e clique em Grupo.Por exemplo, escolha o grupo STANDARD_DISPLAY.Nota Se nenhum grupo disponível for exibido, você pode primeiro passar pela etapa do processo Criar grupo para substituição (opcional) no script de dados mestre Criar substituição de produto - MDS - 4VO.Clique em Atribuir. | A mensagem do sistema Objeto foi atribuído é exibida. |  |

#### Criar controle para substituição de centro (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de controle para controles de substituição/exclusão de centro. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Administrador de cumprimento de ordens. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar controles de substituição - Unidades gerenciais(F5312). | O app é aberto. |  |
| 3 | Selecione Create | Na tela Administrar controles de substituição – Unidades gerenciais, clique em Criar. | A tela Administrar controles de substituição - Criar localizações é exibida. |  |
| 4 | Inserir controle | Na seção Cabeçalho, efetue as seguintes entradas:Categoria da unidade gerencial: <centro>Controle: <insira o novo controle para substituição, por exemplo, REGION> |  |  |
| 5 | Salvar os dados | Clique em Salvar. | A mensagem do sistema Controle criado é exibida. |  |
| 6 | Selecione Create | Na seção Descrição, clique em Criar. | A tela Criar descrição de controle é exibida. |  |
| 7 | Inserir dados de descrição | Na seção Descrição, efetue as seguintes entradas:Código de idioma: <insira o código de idioma aplicável para o controle, por exemplo, IN para inglês>Descrição do controle: <insira o texto para descrever o controle, por exemplo, para uma região> |  |  |
| 8 | Salvar os dados | Clique em Criar. | A mensagem do sistema Descrição de controle criada é exibida. |  |
| 9 | Clicar em Voltar | Na seção Título, clique em < (Voltar). | A tela Administrar controles de substituição - Localizações é exibida. |  |
| 10 | Grupos atribuídos | Na seção Grupos atribuídos, clique em Atribuir. | A caixa de diálogo Atribuir grupos ao controle é exibida. |  |
| 11 | Seleciona grupo | Na caixa de diálogo Atribuir grupos ao controle, pesquise e clique em Grupo.Por exemplo, escolha o grupo <SOUTH_REGION> .Nota Se nenhum grupo disponível for exibido, você pode primeiro passar pela etapa do processo Criar grupo para substituição de centro (opcional) no script de dados mestre Criar substituição e exclusão de local – MDS - 5NG.Clique em Atribuir. | A mensagem do sistema Os grupos foram atribuídos é exibida. |  |

#### Criar controle para substituição de depósito (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de controle para controles de substituição/exclusão de Depósito. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Administrador de cumprimento de ordens. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar controles de substituição - Unidades gerenciais(F5312). | O app é aberto. |  |
| 3 | Clicar em Criar | Na tela Administrar controles de substituição – Unidades gerenciais, clique em Criar. | A tela Administrar controles de substituição - Criar localizações é exibida. |  |
| 4 | Inserir controle | Na seção Cabeçalho, efetue as seguintes entradas:Categoria da unidade gerencial: <Depósito>Controle: <insira o novo controle para substituição, por exemplo, STORAGE_TYPE> |  |  |
| 5 | Clicar em Criar | Clique em Criar. | A mensagem do sistema Controle criado é exibida. |  |
| 6 | Clicar em Criar | Na seção Descrição, clique em Criar. | A tela Criar descrição de controle é exibida. |  |
| 7 | Inserir dados de descrição | Na seção Descrição, efetue as seguintes entradas:Código de idioma: <insira o código de idioma aplicável para o controle, por exemplo, IN para inglês>Descrição do controle: <insira o texto para descrever o controle, por exemplo, para categoria da unidade gerencial> |  |  |
| 8 | Salvar os dados | Clique em Criar. | A mensagem do sistema Descrição de controle criada é exibida. |  |
| 9 | Clicar em Voltar | Na seção Título, clique em < (Voltar). | A tela Administrar controles de substituição - Localizações é exibida. |  |
| 10 | Grupos atribuídos | Na seção Grupos atribuídos, clique em Atribuir. | A caixa de diálogo Atribuir grupos ao controle é exibida. |  |
| 11 | Seleciona grupo | Na caixa de diálogo Atribuir grupos ao controle, pesquise e clique em Grupo.Por exemplo, escolha o Grupo <COLD_STORAGE>.Nota Se nenhum Grupo disponível for exibido, você pode primeiro passar pela etapa do processo Criar grupo para substituição de depósito (opcional) no script de dados mestre Criar substituição e exclusão de local – MDS - 5NG.Clique em Atribuir. | A mensagem do sistema Os grupos foram atribuídos é exibida. |  |

## Tabela de síntese

Este item de escopo é composto pelo processo de segmentos fornecido na tabela abaixo.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Segmento | Função empresarial | Transação / App | Resultados previstos |
| --- | --- | --- | --- |
| [Criar combinação de características](#unique_11) [página ] 11 | Administrador de cumprimento de ordens | Administrar combinações de características(F5303). | A combinação de características é criada. |
| [Criar acesso](#unique_12) [página ] 12 | Administrador de cumprimento de ordens | Administrar sequências de acesso - Substituições(F5302) | O acesso é criado para a combinação criada nos segmentos acima e os valores da característica são definidos para os acessos. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar combinação de características

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções sobre criação da Combinação de características. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Administrador de cumprimento de ordens. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar combinações de características(F5303). | O app é aberto. |  |
| 3 | Selecione Create | Na tela Administrar combinação de características, clique em Criar. | A tela Administrar combinação de características é exibida. |  |
| 4 | Inserir dados de cabeçalho | Na seção Cabeçalho, efetue as seguintes entradas:Combinação: <insira o nome da combinação>Descrição da combinação : <insira a descrição da combinação>Utilização: substituiçãoTipo de catálogo: <Base (documento de vendas) com utilização SUBSTN>Combinação, Utilização e Tipo de catálogo são obrigatórios para criar uma Substituição. |  |  |
| 5 | Atribuir características | Na seção Características, efetue as seguintes entradas para atribuir as Características:Clique em AtribuirEscolher as Características na telaClique em Atribuir.Defina a ordem das Características usando a seta para cima ou para baixo |  |  |
| 6 | Selecione Create | Clique em Criar. | A mensagem do sistema A combinação foi criada é exibida. |  |

### Criar acesso

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento fornece instruções para criar o acesso para a combinação e definição de valores CVC para o acesso. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Administrador de cumprimento de ordens. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar sequências de acesso - Substituições(F5302) | A tela Administrar combinações de valores de característica – Substituição é exibida. |  |
| 3 | Selecionar Criar | Na visão Administrar combinações de valores de característica – Substituição, na guia Produtos, clique em Criar (3 guias Produtos, Centro e Depósito estão disponíveis). | A tela Administrar combinações de valores de característica – Substituição é exibida. |  |
| 4 | Inserir detalhes | Na janela Pop up, efetue as seguintes entradas:Combinação: <selecione a combinação nas entradas possíveis>Status: <selecione o status necessário na lista de opções> O campo Status é predefinido com o status Ativo.Clique em CriarA combinação é obrigatória para criar um acesso. | A mensagem do sistema mostra que o acesso foi criado. |  |
| 5 | Inserir detalhes de controles atribuídos | Na seção Controles atribuídos , adicione as características e os detalhes de controle:Clique em AdicionarCaracterísticas: <insira os valores de características ou escolha nas entradas possíveis>Status: <O status está ativo por padrão>Executar substituição: <Ativado por padrão>Controle: <Opcional - insira o controle de substituição do produto>Adicione múltiplos valores, conforme necessário. | As características Colunas mostradas na seção Controles atribuídos são as atribuídas à Combinação escolhida ao criar o acesso. |  |
| 6 | Criar acesso | Clique em Criar. | A mensagem do sistema mostra que o Acesso foi criado. |  |

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
- related-to :: [[08-sales-order-management/5nh-483]]
- related-to :: [[08-sales-order-management/crear-determinacion-de-objeto-y-valor-mds-5nh-480]]
- related-to :: [[08-sales-order-management/create-object-and-value-determination-mds-5nh-479]]
- related-to :: [[08-sales-order-management/mds-5nh-481]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NH_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 19,569 chars in the whole document
