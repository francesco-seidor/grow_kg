---
id: 11-inventory-warehouse-and-transportation/script-de-dados-mestre-atualizar-atributos-de-produtos-de-deposito-mds
title: Script de dados mestre - Atualizar atributos de produtos de depósito - MDS (3KQ) (3KQ_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP S/4HANA Cloud Public Edition 2608 master data script (3KQ): updating warehouse product attributes via the /SCWM/MON monitor or app F1602."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-warehouse-product-attributes]
aliases: [3KQ_S4CLD2608_Master_Data_PT_XX]
keywords: [EWM Warehouse Product Attributes, warehouse product attributes, warehouse management monitor, product master data, master data scripts, mass modification, putaway and stock removal control, replenishment, business roles, 3KQ]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-332
topic: 11-inventory-warehouse-and-transportation/ewm-warehouse-product-attributes
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Atualizar atributos de produtos de depósito - MDS (3KQ) (3KQ_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **EWM Warehouse Product Attributes** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Atualizar atributos de produtos de depósito – MDS (3KQ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893653)

[2 Pré-requisitos 3](#_Toc233893654)

[2.1 Acesso ao sistema 3](#_Toc233893655)

[2.2 Funções 3](#_Toc233893656)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893657)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893658)

[3 Tabela de síntese 5](#_Toc233893659)

[4 Procedimentos de teste 6](#_Toc233893660)

[4.1 Atualizar atributos de produto do depósito – Com Monitor de depósito 6](#_Toc233893661)

[4.2 Atualizar atributos de produtos de depósito 7](#_Toc233893662)

## Objetivo

Neste documento, você pode aprender a como criar atributos relevantes para depósito para o mestre de produtos/material. Existem duas opções para atualizar os atributos de depósito:

- Você pode atualizar atributos de produtos de depósito com o app Monitor de administração de depósitos(/SCWM/MON). Este app pode ser usado para modificações individuais ou em massa.
- Você pode atualizar atributos de produtos de depósito com o app Administrar dados mestre do produto(F1602). Este app pode ser usado para modificações individuais.

Este documento inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema normal. O leitor aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo do fornecimento de conteúdo do SAP S/4HANA, por SAP Best Practices, não são descritos neste documento, apesar de poderem aparecer na IU.

Você usa esses dados mestre para todos os processos empresariais da administração de depósitos.

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
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Dados mestre - produtos / Governança de produto | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |

### Unidades organizacionais necessárias

Alguns segmentos de dados mestre são dependentes das unidades organizacionais da empresa. Dados gerais (central) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Tudo | Número do depósito |  |  |  |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre pode fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre <tipo>.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Parceiro de negócios | Atualizar atributos de produtos de depósito | Obrigatório | Parceiro de negócios como pessoa autorizada a dispor para o depósito |

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Segmento | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Atualizar atributos de produto do depósito – Com Monitor de depósito](#unique_7) [página ] 6 | Chefe do depósito (EWM) | Monitor de administração de depósitos(/SCWM/MON) | Uma modificação em massa de produtos de depósito é executada. |
| [Atualizar atributos de produtos de depósito](#unique_8) [página ] 7 | Especialista em dados mestre - Dados do produto | Administrar dados mestre do produto(F1602) | Atributos de depósito criados para dados mestre de material. |

## Procedimentos de teste

Esta seção descreve procedimentos para cada segmento ou etapa do processo que faz parte deste registro mestre.

### Atualizar atributos de produto do depósito – Com Monitor de depósito

Objetivo

Nesta seção, você atualiza atributos de produtos de depósito usando o app Monitor de administração de depósitos(/SCWM/MON). Este app pode ser usado para modificações individuais ou em massa.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Chefe do depósito (EWM). |  |  |
| 2 | Acessar o app | Abra Monitor de administração de depósitos(/SCWM/MON). | A tela Monitor de administração de depósitos SAP - Número do depósito XX50 é exibida. |  |
| 3 | Selecionar Menu | Na hierarquia do lado esquerdo da tela, clique em Dados mestre do produto > Atributo de depósito. |  |  |
| 4 | Inserir número do produto | Na caixa de diálogo /SCWM/SAPLPROD_OVERVIEW, insira os seguintes dados:Seção Atributos básicos:Número do produto: <nº do produto> para <nº do produto>Seção Opções adicionais:Apenas produtos sem dados de depósito: XClique em Executar. | O sistema exibe os produtos que ainda não foram atualizados com dados do depósito na área direita da tela. |  |
| 5 | Selecionar produtos | Na área Atributos de depósito, selecione os produtos e, em seguida, selecione Mais métodos > Modificação/Criação em massa. |  |  |
| 6 | Selecionar produtos | Na caixa de diálogo /SCWM/SAPLPROD_OVERVIEW, insira os seguintes dados onde aplicável.Na seção Dados de depósito:Cód.controle de entrada em depósitoCód.ctrl saída do depósitoCódigo de depósito em blocoCódigo de inventário rotativoCód.tipo determ. proc.Clique em Executar.Nota No Cloud Warehouse Management, o código de controle de entrada em depósito e o código de controle de saída do depósito são geralmente atualizados com o mesmo valor. No entanto, em um processo de reabastecimento usado no depósito, estes dois campos devem ser atualizados de modo diferente para habilitar o processo. |  |  |
| 7 | Salvar os dados | Confirme as modificações na caixa de diálogo. | Uma mensagem do sistema informa que os produtos foram salvas com êxito. |  |

### Atualizar atributos de produtos de depósito

Objetivo

Nesta seção, você encontra uma descrição de como atualizar atributos de produto do depósito com o app Administrar dados mestre do produto(F1602). Este app pode ser usado para modificações individuais.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. |  |  |
| 2 | Acessar o app | Abra Administrar dados mestre do produto(F1602). |  |  |
| 3 | Inserir número do material | Na tela Administrar dados mestre do produto(F1602), insira os seguintes dados:Produto: <Número do material>Clique em Ir. | Os dados mestre de materiais são exibidos na seção Produto. |  |
| 4 | Selecionar material | Selecione a linha dos dados mestre de material. |  |  |
| 5 | Clique em Administração de depósitos | Na tela do Produto, clique na guia Administração de depósitos e vá para Administração de depósitos > Depósito. |  |  |
| 6 | Editar dados mestre de materiais | Na tela Produto, clique em Editar. |  |  |
| 7 | Adicionar dados de depósito | Na seção Depósito, clique no número do seu depósito.Se não existir um número de depósito, clique em Criar. |  |  |
| 8 | Inserir valores | Na tela Depósito, insira os seguintes dados:Na seção Informações gerais:Depósito: <nº do depósito EWM>Pessoa autorizada a dispor: <ID do parceiro de negócios para a pessoa autorizada a dispor>Código de determinação do tipo de processoCódigo de inventário rotativoNota Somente Depósito e Pessoa autorizada a dispor são campos obrigatórios. Os valores a seguir são opcionais.Na seção Entrada em depósito:Código de controle da entrada em depósitoNa seção Saída do depósito:Código de controle da saída de depósitoNota No Cloud Warehouse Management, o código de controle de entrada em depósito e o código de controle de saída do depósito são atualizados com o mesmo valor. No entanto, em um processo de reabastecimento usado no depósito, estes dois campos devem ser atualizados de modo diferente para habilitar o processo. |  |  |
|  | Criar dados do tipo de depósito para reabastecimento | Na seção Tipos de depósito, clique em Criar.Em Novo registro – tipo de depósito, insira os seguintes dados:Na seção Informações gerais:Tipo de depósito: <tipo de depósito>Número máximo de posições: <Número de posições>Na seção Reabastecimento:Quantidade mínima de reabastecimento / Exibir unidade de medida: <Quantidade> / <unidade de medida>Quantidade mínima / Exibir unidade de medida: <Quantidade> / <unidade de medida>Quantidade máxima / Exibir unidade de medida: <Quantidade> / <unidade de medida> |  |  |
| 9 | Salvar os dados | Clique em Aplicar. | Os dados do depósito são salvos. |  |
| 10 | Volte para a tela Produto | Volte para a tela Produto. |  |  |
| 11 | Clique em Administração de depósitos | Na tela Produto, clique na guia Centros. |  |  |
| 12 | Adicionar dados do centro | Na seção Centros, clique no centro.Se não existir o seu centro, clique em Adicionar. |  |  |
| 13 | Inserir valores | Na tela Centro, insira os seguintes dados na seção Informações gerais:Perfil do número de série <perfil do número de série> |  |  |
| 14 | Salvar os dados | Clique em Aplicar. | Os dados de centro são salvos. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/actualizar-atributos-de-productos-de-almacen-mds-3kq-es-330]]
- related-to :: [[11-inventory-warehouse-and-transportation/attribute-fur-lagerprodukte-pflegen-sds-3kq-328]]
- related-to :: [[11-inventory-warehouse-and-transportation/master-data-script-maintain-warehouse-products-attributes-3kq-329]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kq-331]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 13,700 chars in the whole document
