---
id: 11-inventory-warehouse-and-transportation/script-de-dados-mestre-atualizar-posicoes-no-deposito-e-atribuicoes-de
title: Script de dados mestre - Atualizar posições no depósito e atribuições de posições fixas (3KR) (3KR_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP master data script 3KR: create, change, display, mass-change warehouse storage bins and assign fixed bins in EWM via Fiori, release 2608."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-storage-bins]
aliases: [3KR_S4CLD2608_Master_Data_PT_XX]
keywords: [EWM Storage Bins and Fixed Bin Assignments, storage bins, fixed bin assignment, bin mass change, master data scripts, warehouse management, business roles, business partner, 3KR]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-338
topic: 11-inventory-warehouse-and-transportation/ewm-storage-bins
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Atualizar posições no depósito e atribuições de posições fixas (3KR) (3KR_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **EWM Storage Bins and Fixed Bin Assignments** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Atualizar posições no depósito e as atribuições de posições fixas no depósito – MDS (3KR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893660)

[2 Pré-requisitos 3](#_Toc233893661)

[2.1 Acesso ao sistema 3](#_Toc233893662)

[2.2 Funções 3](#_Toc233893663)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893664)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893665)

[3 Tabela de síntese 5](#_Toc233893666)

[4 Procedimentos de teste 6](#_Toc233893667)

[4.1 Criar posições no depósito 6](#_Toc233893668)

[4.2 Alterar posições no depósito 7](#_Toc233893669)

[4.3 Exibir posições no depósito 8](#_Toc233893670)

[4.4 Executar alteração em massa de posições no depósito 9](#_Toc233893671)

[4.5 Atribuir posições fixas no depósito 10](#_Toc233893672)

## Objetivo

Neste documento, você pode aprender a executar as seguintes atividades para criar posições no depósito e atribuições de posições fixas no depósito:

- [Criar posições no depósito](#unique_2) [página ] 6
- [Alterar posições no depósito](#unique_3) [página ] 7
- [Exibir posições no depósito](#unique_4) [página ] 8
- [Executar alteração em massa de posições no depósito](#unique_5) [página ] 9
- [Atribuir posições fixas no depósito](#unique_6) [página ] 10

A descrição inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema normal. Você aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo do fornecimento de conteúdo do SAP S/4HANA, por SAP Best Practices, não são descritos neste documento, apesar de poderem aparecer na tela.

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

### Unidades organizacionais necessárias

Alguns segmentos de dados mestre são dependentes das unidades organizacionais da empresa. Dados gerais (central) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Tudo | Número do depósito |  |  |  |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre pode fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre <tipo>.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Parceiro de negócios | Atribuir posições fixas no depósito | Obrigatório | Parceiro de negócios como pessoa autorizada a dispor para o depósito |

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Segmento | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar posições no depósito](#unique_2) [página ] 6 | Chefe do depósito (EWM) | Criar posições no depósito(/SCWM/LS01) | As posições no depósito são criadas. |
| [Alterar posições no depósito](#unique_3) [página ] 7 | Chefe do depósito (EWM) | Editar posições no depósito(/SCWM/LS02) | As posições no depósito são modificadas. |
| [Exibir posições no depósito](#unique_4) [página ] 8 | Chefe do depósito (EWM) | Exibir posições no depósito(/SCWM/LS03) | As posições no depósito são exibidas. |
| [Executar alteração em massa de posições no depósito](#unique_5) [página ] 9 | Chefe do depósito (EWM) | Edição em massa de posições no depósito(/SCWM/LS11) | As modificações em massa das posições no depósito são executadas. |
| [Atribuir posições fixas no depósito](#unique_6) [página ] 10 | Chefe do depósito (EWM) | Atribuir posições fixas no depósito(/SCWM/BINMAT) | A atribuição de posição fixa no depósito é criada. |

## Procedimentos de teste

Esta seção descreve procedimentos para cada segmento ou etapa do processo que faz parte deste registro mestre.

### Criar posições no depósito

Objetivo

Nesta sessão, você encontra uma descrição de como criar posições em depósito no SAP S/4HANA, usando o launchpad do SAP Fiori.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Chefe do depósito (EWM). |  |  |
| 2 | Acessar o app | Abra Criar posições no depósito(/SCWM/LS01). |  |  |
| 3 | Inserir ID da posição no depósito | Na tela Criar posições no depósito(/SCWM/LS01), insira os seguintes dados:Número do depósito: <seu nº de depósito>Posição no depósito: <ID da posição no depósito>Pressione Enter. |  |  |
| 4 | Inserir atributos de posição no depósito | Na guia Posição no depósito, insira os seguintes dados:Tipo de depósito: <tipo de depósito>Nota Apenas o campo Tipo de depósito é obrigatório. Todos os outros campos abaixo são opcionais:Peso máximoVolume máximoCorredor da posição no depósitoCoordenada XEmpilhamentoCoordenada YNível da posiçãoCoordenada ZÂngulo da posição |  |  |
| 5 | Salvar os dados | Clique em Salvar. | Uma mensagem de êxito indica que a posição no depósito foi salva. |  |

### Alterar posições no depósito

Objetivo

Nesta seção, você modifica posições no depósito em SAP S/4HANA com o launchpad do SAP Fiori.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Chefe do depósito (EWM). |  |  |
| 2 | Acessar o app | Abra Editar posições no depósito(/SCWM/LS02). |  |  |
| 3 | Inserir ID da posição no depósito | Na tela Editar posições no depósito(/SCWM/LS02), insira os seguintes dados:Número do depósito: <seu nº de depósito>Posição no depósito: <ID da posição no depósito>Pressione Enter. |  |  |
| 4 | Alterar atributos de posição no depósito | Na guia Posição no depósito, altere os valores a seguir se necessário.Nota Apenas os seguintes campos podem ser alterados:Peso máximoVolume máximoCorredor da posição no depósitoCoordenada XEmpilhamentoCoordenada YNível da posiçãoCoordenada ZÂngulo da posição |  |  |
| 5 | Salvar os dados | Clique em Salvar. | Uma mensagem de êxito indica que a posição no depósito foi salva. |  |

### Exibir posições no depósito

Objetivo

Nesta seção, você exibe as posições no depósito no SAP S/4HANA, usando o launchpad do SAP Fiori.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Chefe do depósito (EWM). |  |  |
| 2 | Acessar o app | Abra Exibir posições no depósito(/SCWM/LS03). |  |  |
| 3 | Inserir ID da posição no depósito | Na tela Exibir posições no depósito(/SCWM/LS03), insira os seguintes dados:Número do depósito: <seu nº de depósito>Posição no depósito: <ID da posição no depósito>Pressione Enter. | Os atributos de posição no depósito são exibidos. |  |

### Executar alteração em massa de posições no depósito

Objetivo

Nesta seção, você efetua uma modificação em massa de posições no depósito em SAP S/4HANA, usando o launchpad do SAP Fiori.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Chefe do depósito (EWM). |  |  |
| 2 | Acessar o app | Abra Edição em massa de posições no depósito(/SCWM/LS11). |  |  |
| 3 | Inserir critérios de filtragem | Na tela Alteração em massa de posições no nº de depósito XXXX, insira os seguintes dados:Número do depósito: <seu nº de depósito>Você pode inserir os seguintes valores como critérios de seleção/de filtro:Posição no depósito: <ID da posição no depósito> para <ID da posição no depósito>Tipo de depósito: <ID do tipo de depósito> para <ID do tipo de depósito>Status bloqueadoNota Se você marcar o campo de seleção Seleções dinâmicas, você pode selecionar vários filtros para seleção de posição no depósito.Clique em Executar. | É exibida a lista de posições no depósito que correspondem aos critérios de seleção. |  |
| 4 | Alteração em massa de posições no depósito | Selecione as entradas que desejar marcando os campos de seleção correspondentes.Clique em Excluir para excluir várias posições no depósito de cada vez.ouClique em Editar para alterar várias posições no depósito ao mesmo tempo. Você poderá modificar os seguintes atributos das posições no depósito.Peso máximoVolume máximoCorredor da posição no depósitoEmpilhamentoNível da posiçãoÂngulo da posição |  |  |
| 5 | Salvar os dados | Clique em Salvar. | Uma mensagem do sistema informa que as alterações da posição no depósito foram salvas. |  |

### Atribuir posições fixas no depósito

Objetivo

Nesta seção, você efetua uma atribuição de posição fixa no depósito em SAP S/4HANA, usando o launchpad do SAP Fiori.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Chefe do depósito (EWM). |  |  |
| 2 | Acessar o app | Abra Atribuir posições fixas no depósito(/SCWM/BINMAT). |  |  |
| 3 | Inserir critérios de filtragem | Na tela Atualizar posições fixas no depósito, insira os seguintes dados:Número do depósito: <seu nº de depósito>Produto: <ID do produto> para <ID do produto>Pessoa autorizada a dispor: <ID do parceiro de negócios> para <ID do parceiro de negócios>Nota A pessoa autorizada a dispor é o parceiro de negócios atualizado para o número de depósito.Posição no depósito: <ID da posição no depósito> para <ID da posição no depósito>Tipo de depósito: <ID do tipo de depósito> para <ID do tipo de depósito>Clique em Executar. | É exibida a lista de posições fixas atribuídas que correspondem aos critérios de seleção. |  |
| 4 | Criar atribuição de posição fixa no depósito | Na tela Nº do depósito XXXX: exibir posição fixa no depósito, clique em Editar.Na tela Nº do depósito XXXX: atualizar posição fixa no depósito, clique em Criar.Na nova linha criada, insira os seguintes valores:Autorizado a dispor: <ID do parceiro de negócios para a pessoa autorizada a dispor>Posição no depósito: <ID da posição fixa no depósito>Tipo: <ID do tipo da posição fixa no depósito>Produto: <ID do produto>Qtd.máx.: <quantidade>Exibir UM: <UM para quantidade máxima> por exemplo, PCQtd.mín.: <quantidade>Exibir UM: <UM para quantidade mínima> por exemplo, PCSe você tiver atualizado os dados do mestre de produtos do depósito os valores nos seguintes campos:Nº máx. de posiçõesQuantidade máximaQuantidade mínimaExibir UM para as quantidades máximas/mínimasOs valores dos campos Qtd.máx e Qtd.mín. na posição fixa no depósito serão calculados com base nos valores dos campos Quantidade máxima, Quantidade mínima e Nº máx. de posições nos dados do mestre de produtos no depósito. Exibir UM também será preenchido a partir dos dados do mestre de produtos do depósito. |  |  |
| 5 | Salvar os dados | Clique em Salvar. | Uma mensagem do sistema informa que as posições no depósito foram salvas. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/maintain-storage-bins-and-fixed-bin-assignments-mds-3kr-335]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kr-337]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kr-339]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-actualizar-ubicaciones-y-asignaciones-de-ubic]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 15,807 chars in the whole document
