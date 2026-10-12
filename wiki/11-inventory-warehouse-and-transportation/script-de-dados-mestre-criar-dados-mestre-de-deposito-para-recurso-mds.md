---
id: 11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-dados-mestre-de-deposito-para-recurso-mds
title: "Script de dados mestre: Criar dados mestre de depósito para recurso – MDS (3Y2) (3Y2_S4CLD2608_Master_Data_PT_XX)"
description: "Portuguese master data test script (3Y2): create and delete warehouse resources in the EWM warehouse monitor (/SCWM/MON) as warehouse clerk."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-warehouse-resources]
aliases: [3Y2_S4CLD2608_Master_Data_PT_XX]
keywords: [EWM Warehouse Resources, warehouse resource, warehouse monitor, master data scripts, resource deletion, extended warehouse management, business roles, warehouse number, sap fiori launchpad, 3Y2]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y2_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-398
topic: 11-inventory-warehouse-and-transportation/ewm-warehouse-resources
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre: Criar dados mestre de depósito para recurso – MDS (3Y2) (3Y2_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y2_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **EWM Warehouse Resources** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar dados mestre de depósito para recurso – MDS (3Y2) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893711)

[2 Pré-requisitos 3](#_Toc233893712)

[2.1 Acesso ao sistema 3](#_Toc233893713)

[2.2 Funções 3](#_Toc233893714)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893715)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893716)

[3 Tabela de síntese 5](#_Toc233893717)

[4 Procedimentos de teste 6](#_Toc233893718)

[4.1 Criar recurso de depósito 6](#_Toc233893719)

[4.2 Excluir recurso de depósito 7](#_Toc233893720)

## Objetivo

Neste documento, você pode criar dados mestre para recursos de depósito. Você pode atualizar os recursos de depósito com o app de controle de depósito (/SCWM/MON). Este documento inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema normal. Você aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo do fornecimento de conteúdo do SAP S/4HANA, por SAP Best Practices, não são descritos neste documento, apesar de poderem aparecer na tela. Você usa esses dados mestre para todos os processos empresariais da administração de depósitos.

Este documento fornece um procedimento detalhado para testar o item de escopo após a ativação da solução, refletindo o escopo predefinido da solução. Cada etapa do processo, relatório ou item está coberto em uma seção própria que fornece as interações do sistema (etapas de teste) em uma visão de tabela. As etapas que não estão no escopo do processo, mas que são necessárias para teste, estão marcadas de modo correspondente. É necessário adicionar etapas específicas do projeto.

|  |
| --- |
| Nota Os valores deste script de teste (notação decimal, formatos de data etc.) são apresentados na notação padrão dos EUA. Se o sistema de teste estiver configurado para usar uma notação diferente, insira os valores apropriados. |

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

Os registros de dados mestre pode fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre <tipo>.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
|  |  |  |  |

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Segmento | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| Criar recurso de depósito | Chefe do depósito (EWM) | Monitor de administração de depósitos(/SCWM/MON) | A criação do recurso no depósito é executada. |
| Excluir recurso de depósito | Chefe do depósito (EWM) | Monitor de administração de depósitos(/SCWM/MON) | A exclusão do recurso no depósito é executada. |

## Procedimentos de teste

Esta seção descreve procedimentos para cada segmento ou etapa do processo que faz parte deste registro mestre.

### Criar recurso de depósito

Objetivo

Nesta seção, você cria recursos de depósito usando o app Monitor de administração de depósitos(/SCWM/MON).

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Chefe do depósito (EWM). |  |  |
| 2 | Acessar o app | Abra Monitor de administração de depósitos(/SCWM/MON). | A caixa de diálogo Monitor de administração de depósitos é exibida. |  |
| 3 | Inserir número de depósito | Na caixa de diálogo Monitor de administração de depósitos, efetue as seguintes entradas:Número do depósito: <seu nº de depósito>Clique em Executar. |  |  |
| 4 | Selecionar Menu | Na hierarquia do lado esquerdo da tela, clique em Administração de recursos > Recurso. |  |  |
| 5 | Exibir recurso | Na caixa de diálogo aberta, clique em Executar. | O sistema exibe todos os recursos que foram criados para o depósito. |  |
| 6 | Criar recurso | Clique em Mais métodos > Criar recurso. |  |  |
| 7 | Inserir valores | Na caixa de diálogo aberta, insira os seguintes dados:Recurso: <ID do recurso>Nota O ID do recurso é limitado a 18 caracteres.Clique em Executar. | Um recurso foi criado corretamente. |  |

### Excluir recurso de depósito

Objetivo

Nesta seção, você exclui atributos de produtos de depósito usando o app Monitor de administração de depósitos(/SCWM/MON).

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Chefe do depósito (EWM). |  |  |
| 2 | Acessar o app | Abra Monitor de administração de depósitos(/SCWM/MON). | A caixa de diálogo Monitor de administração de depósitos é exibida. |  |
| 3 | Inserir número de depósito | Na caixa de diálogo Monitor de administração de depósitos aberta, efetue as seguintes entradas:Número do depósito: <seu nº de depósito>Clique em Executar. |  |  |
| 4 | Selecionar Menu | Na hierarquia do lado esquerdo da tela, clique em Administração de recursos > Recurso. |  |  |
| 5 | Exibir recurso | Na caixa de diálogo, clique em Executar. | O sistema exibe todos os recursos que foram criados para o depósito. |  |
| 6 | Excluir recurso | Clique no recurso que deve ser excluído e, em seguida, em Mais métodos > Excluir recurso. |  |  |
| 7 | Confirmar exclusão | Na caixa de diálogo Excluir recurso, clique em Sim.Nota Você não pode excluir um recurso específico que ainda esteja sendo usado no depósito. Isso é, a exclusão não pode ser feita quando um usuário estiver conectado no recurso ou se um usuário tiver definido o recurso como recurso padrão. | Um recurso foi excluído com êxito. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/crear-datos-maestros-de-almacen-para-recurso-mds-3y2-396]]
- related-to :: [[11-inventory-warehouse-and-transportation/master-data-script-create-warehouse-master-data-for-resource-mds-3y2-3]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3y2-397]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3y2-399]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y2_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 10,811 chars in the whole document
