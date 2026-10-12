---
id: 11-inventory-warehouse-and-transportation/atualizar-area-de-abastecimento-da-producao-mds-3ks-344
title: Atualizar área de abastecimento da produção – MDS (3KS) (3KS_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese master data script (3KS) for optionally assigning warehouse storage bins to a production supply area (AAP) in SAP S/4HANA Cloud Public Edition, with prerequisites and test steps."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-production-integration]
aliases: [3KS_S4CLD2608_Master_Data_PT_XX]
keywords: [EWM Production Supply and Receipt, production supply area, storage bin assignment, warehouse master data, master data script, business roles, business conditions, warehouse production integration, kanban warehouse supply, 3KS]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-344
topic: 11-inventory-warehouse-and-transportation/ewm-production-integration
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Atualizar área de abastecimento da produção – MDS (3KS) (3KS_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **EWM Production Supply and Receipt** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Atualizar área de abastecimento da produção – MDS (3KS) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893656)

[2 Pré-requisitos 3](#_Toc233893657)

[2.1 Acesso ao sistema 3](#_Toc233893658)

[2.2 Funções 3](#_Toc233893659)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893660)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893661)

[2.5 Condições empresariais 4](#_Toc233893662)

[3 Tabela de síntese 5](#_Toc233893663)

[4 Procedimentos de teste 6](#_Toc233893664)

[4.1 (OPCIONAL) Atribuir posição à AAP – Depósito 6](#_Toc233893665)

[4.2 (OPCIONAL) Atribuir posição no depósito à AAP 7](#_Toc233893666)

## Objetivo

Neste documento, você pode aprender a executar as seguintes atividades para criar dados mestre do depósito para o abastecimento da produção:

- [(OPCIONAL) Atribuir posição à AAP – Depósito](#unique_2) [página ] 6
- [(OPCIONAL) Atribuir posição no depósito à AAP](#unique_3) [página ] 7

A criação e a replicação da área de abastecimento da produção, bem como a atribuição da posição no depósito à AAP devem ser efetuadas por meio da execução das etapas relevantes no script de dados mestre ou documentos de script de teste mencionados no capítulo Condição empresarial. Este script de dados mestre é apenas para os clientes verificarem as configurações relevantes e criarem manualmente as configurações caso as condições empresariais não tenham sido atendidas.

A descrição inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema normal. Você aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo do fornecimento de conteúdo do SAP S/4HANA, por SAP Best Practices, não são descritos neste documento, apesar de poderem aparecer na IU.

Você usa esses dados mestre para processos empresariais de integração da produção na Administração de depósitos.

## Pré-requisitos

### Acesso ao sistema

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece o URL para acessar os vários apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) |
| --- | --- | --- | --- |
| Chefe do depósito (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Escritório de depósito | SAP_BR_WAREHOUSE_CLERK_EWM |

### Unidades organizacionais necessárias

Alguns segmentos de dados mestre são dependentes das unidades organizacionais da empresa. Dados gerais (central) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Tudo | Número do depósito |  |  |  |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre pode fazer referência a outros dados mestre. A tabela a seguir fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem usados ao criar uma atribuição de posição no depósito para o registro de dados mestre AAP.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Parceiro de negócios | Atribuir posição à AAP - Depósito | Obrigatório | Parceiro de negócios como pessoa autorizada a dispor para o depósito |
| Área de abastecimento da produção | Atribuir posição à AAP - Depósito | Obrigatório | A área de abastecimento da produção que é criada no SAP S/4HANA. Consulte o capítulo de condições empresariais. |
| Produto | Atribuir posição à AAP - Depósito | Obrigatório |  |
| Posição no depósito | Atribuir posição à AAP - Depósito | Obrigatório |  |

### Condições empresariais

Antes de testar este item de escopo, é necessário cumprir as condições empresariais a seguir.

| ID do item de escopo | Condição empresarial |
| --- | --- |
| 40D – Criar área de abastecimento da produção – MDS | Este script de dados mestre é o pré-requisito para este documento.Ao criar a Área de Abastecimento da Produção (AAP), use o depósito Cloud WM, por exemplo, 105W.Após ter executado este script de dados mestre, você criou as seguintes configurações:A área de abastecimento da produção é criada no SAP S/4HANAA área de abastecimento da produção relevante é replicada automaticamente do SAP S/4HANA no Cloud Warehouse. |
| 3DV – Integração de produção do depósito | O pré-requisito para esse documento é a etapa Criar circuito regulador no capítulo Etapas preliminares do script de teste 3DV.Após executar a etapa de trabalho Criar circuito regulador, você criou as seguintes configurações:A área de abastecimento da produção relevante é replicada automaticamente do SAP S/4HANA no Cloud Warehouse.A posição no depósito é atribuída à AAP. |
| 3VT – Kanban em depósito para suprimento de produção | O pré-requisito para este documento é o circuito regulador para Kanban: Etapa de transferência de estoque no capítulo de etapas preliminares do script de teste 3VT.Após executar o circuito regulador para Kanban: etapa de transferência de estoque, você criou as seguintes configurações:A área de abastecimento da produção relevante é replicada automaticamente do SAP S/4HANA no Cloud Warehouse.A posição no depósito é atribuída à AAP. |

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Segmento | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [(OPCIONAL) Atribuir posição à AAP – Depósito](#unique_2) [página ] 6 | Chefe do depósito (EWM) | Atribuir posição no depósito a área de abastecimento da produção - Depósito(/SCWM/PSASTAGE) | A atribuição da posição no depósito à AAP é criada. |
| [(OPCIONAL) Atribuir posição no depósito à AAP](#unique_3) [página ] 7 | Chefe do depósito (EWM) | Atribuir posição no depósito a área de abastecimento da produção(/SCWM/PSASTAGE2) | A atribuição da posição no depósito à AAP é criada. |

## Procedimentos de teste

Esta seção descreve procedimentos para cada segmento ou etapa do processo que faz parte deste registro mestre.

### (OPCIONAL) Atribuir posição à AAP – Depósito

Objetivo

Nesta seção, você administra as atribuições de posição de depósito de todas as áreas de abastecimento da produção do número do depósito em SAP S/4HANA, utilizando o launchpad do SAP Fiori.

Esta etapa é opcional e você pode ignorá-la se a posição no depósito tiver sido atribuída à AAP como esperado. É necessária apenas quando nenhuma atribuição de posição no depósito tiver sido efetuada ainda para a AAP durante a etapa de criação de circuito regulador. Consulte a etapa Criar circuito regulador no capítulo Condição empresarial.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Chefe do depósito (EWM). |  |  |
| 2 | Acessar o app | Abra Atribuir posição no depósito a área de abastecimento da produção - Depósito(/SCWM/PSASTAGE). |  |  |
| 3 | Criar nova entrada | Na tela Modificar visão "Atribuir posição no depósito à AAP": síntese, clique em Novas entradas. |  |  |
| 4 | Inserir valores de atribuição | Na tela Entradas novas: detalhes de entrada adicionadas, insira os seguintes dados:Autorizado a dispor: <ID do parceiro de negócios para a pessoa autorizada a dispor>Área de abastecimento da produção: <área de abastecimento da produção>Produto: <ID do produto>Posição no depósito: <ID da posição no depósito> |  |  |
| 5 | Salvar os dados | Clique em Salvar. | Uma mensagem do sistema informa que a atribuição da posição no depósito para a AAP foi salva. |  |

### (OPCIONAL) Atribuir posição no depósito à AAP

Objetivo

Nesta seção, você administra todas as atribuições de posição no depósito dentro de uma determinada área de abastecimento da produção no SAP S/4HANA, utilizando o launchpad do SAP Fiori.

Esta etapa é opcional e você pode ignorá-la se a posição no depósito tiver sido atribuída à AAP como esperado. É necessária apenas quando nenhuma atribuição de posição no depósito tiver sido efetuada ainda para a AAP durante a etapa de criação de circuito regulador. Consulte a etapa Criar circuito regulador no capítulo Condição empresarial.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Chefe do depósito (EWM). |  |  |
| 2 | Acessar o app | Abra Atribuir posição no depósito a área de abastecimento da produção(/SCWM/PSASTAGE2). |  |  |
| 3 | Determinar área de trabalho | Na tela Determinar entrada da área de trabalho, insira os dados a seguirPessoa autorizada a dispor: <ID do parceiro de negócios para a pessoa autorizada a dispor>Área de abastecimento da produção: <área de abastecimento da produção>Clique em Continuar. |  |  |
| 4 | Criar nova entrada | Na tela Modificar visão "Atribuir posição no depósito à AAP": síntese, clique em Novas entradas. |  |  |
| 5 | Inserir valores de atribuição | Na tela Entradas novas: detalhes de entrada adicionadas, insira os seguintes dados:Produto: <ID do produto>Posição no depósito: <ID da posição no depósito> |  |  |
| 6 | Salvar os dados | Clique em Salvar. | Uma mensagem do sistema informa que a atribuição da posição no depósito para a AAP foi salva. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/maintain-production-supply-area-mds-3ks-341]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-343]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-345]]
- related-to :: [[11-inventory-warehouse-and-transportation/produktionsversorgungsbereich-pflegen-sds-3ks-340]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 13,579 chars in the whole document
