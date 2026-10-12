---
id: 09-subscription-billing-and-contract-accounting/criar-condicao-de-determinacao-de-precos-baseada-em-tipo-de-servico-md
title: Criar condição de determinação de preços baseada em tipo de serviço – MDS (3GD) (3GD_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP master data script 3GD: creating service-type-based pricing conditions PST0, PST1, PST2 in VK12 as Pricing Specialist (convergent billing)."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/consumption-items-and-rating]
aliases: [3GD_S4CLD2608_Master_Data_PT_XX]
keywords: [Consumption Items and Service-Type-Based Rating, service-based pricing conditions, master data scripts, pricing condition types, condition records, convergent billing, pricing specialist role, sales organization, 3GD]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-320
topic: 09-subscription-billing-and-contract-accounting/consumption-items-and-rating
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar condição de determinação de preços baseada em tipo de serviço – MDS (3GD) (3GD_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Consumption Items and Service-Type-Based Rating** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar condição de determinação de preços baseada em tipo de serviço – MDS (3GD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893641)

[2 Pré-requisitos 3](#_Toc233893642)

[2.1 Acesso ao sistema 3](#_Toc233893643)

[2.2 Funções 3](#_Toc233893644)

[2.3 Dados mestre obrigatórios e opcionais 3](#_Toc233893645)

[3 Tabela de síntese 5](#_Toc233893646)

[4 Procedimentos de teste 6](#_Toc233893647)

[4.1 Criar condição para determinação de preços de PST0 6](#_Toc233893648)

[4.2 Criar condição para determinação de preços de PST1 7](#_Toc233893649)

[4.3 Criar condição para determinação de preços de PST2 8](#_Toc233893650)

## Objetivo

Condições para a determinação de preços baseadas em serviços são utilizadas para armazenar a informação necessária à realização da determinação automática de preços na classificação de um faturamento convergente. Elas incluem preços e sobretaxas com base em diferentes variantes. Elas podem ser específicas para um determinado cliente ou material, ou para uma combinação de parâmetros. Uma condição de determinação de preços baseada em serviços contém informações como, por exemplo, um preço em uma moeda específica para um material. Esta informação é utilizada e armazenada nos itens com fatura calculável, itens do plano de cáculo da fatura, documentos de cálculo da fatura e documentos de faturamento.

A informação é geralmente específica para uma determinada unidade de vendas em sua organização.

## Pré-requisitos

Esta seção resume todos os pré-requisitos necessários para conduzir o teste em termos de sistemas, usuários, dados mestre, dados organizacionais, outros dados de teste e condições empresariais.

### Acesso ao sistema

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via SAP Fiori Launchpad. Seu administrador do sistema fornece a você o URL para acessar os vários apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) |
| --- | --- | --- | --- |
| Especialista em preços | SAP_BR_PRICING_SPECIALIST | Gestão de preços | SAP_BR_PRICING_SPECIALIST |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre pode fazer referência a outros dados mestre. A tabela a seguir fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem usados em um registro de dados mestre.

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Organização de vendas | 1ª tela | Obrigatório | <Número de organização de vendas> |
| Canal de distribuição | 1ª tela | Obrigatório | <Número de canal de distribuiçãor> |

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Segmento | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar condição para determinação de preços de PST0](#unique_7) [página ] 6 | Especialista em preços | Definir preços de material - Vendas(VK12) | A condição para determinação de preços é atualizada. |
| [Criar condição para determinação de preços de PST1](#unique_8) [página ] 7 | Especialista em preços | Definir preços de material - Vendas(VK12) | A condição para determinação de preços é atualizada. |
| [Criar condição para determinação de preços de PST2](#unique_9) [página ] 8 | Especialista em preços | Definir preços de material - Vendas(VK12) | A condição para determinação de preços é atualizada. |

## Procedimentos de teste

Esta seção descreve procedimentos para cada segmento ou etapa do processo que faz parte deste registro mestre.

### Criar condição para determinação de preços de PST0

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Este procedimento descreve a criação de condições para determinação de preços de venda: PST0

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | A página Início é exibida. |  |
| 2 | Acessar o app SAP Fiori | Abra Definir preços de material - Vendas(VK12). | É exibida a tela Modificar registros de condição. |  |
| 3 | Tipo de condição para a determinação de preços | Na visão Modificar registros de condição, efetue as seguintes entradas e pressione EnterTipo de condição: PST0 |  |  |
| 4 | Seleção | Na visão Modificar condição prç.bas.tp.serv. (PST0): Seleção, efetue as entradas a seguir e clique em ExecutarOrganização de vendas: <organização de vendas>Canal de distribuição: <canal de distribuição> |  |  |
| 5 | Modificar condição de preço | Na visão Modificar condição prç.bas.tp.serv. (PST0): síntese, efetue as seguintes entradas como abaixo e clique em Gravar.embalagem: CBPTS002Montante: <montante>UM: <UN>Válido desde: <a data atual>Válido até: por exemplo, <data atual + um ano> | A condição para determinação de preços é atualizada. |  |

### Criar condição para determinação de preços de PST1

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Este procedimento descreve a criação de condições para determinação de preços de venda: PST1

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | A página Início é exibida. |  |
| 2 | Acessar o app SAP Fiori | Abra Definir preços de material - Vendas(VK12). | É exibida a tela Modificar registros de condição. |  |
| 3 | Tipo de condição para a determinação de preços | Na visão Modificar registros de condição, efetue as seguintes entradas e pressione Enter:Tipo de condição: PST1 |  |  |
| 4 | Seleção | Na visão Modificar % var.bas.tp.serviço (PST1): Seleção, efetue as entradas a seguir e clique em ExecutarOrganização de vendas: Organização de vendasCanal de distribuição: Canal de distribuição |  |  |
| 5 | Modificar condição de preço | Na visão Modificar % var.bas.tp.serviço (PST1): síntese, efetue as seguintes entradas como abaixo e clique em Gravar.embalagem: CBPTS001Variante: HIGH_ENDMontante: <montante>UM: UNVálido desde: <a data atual>Válido até: por exemplo, <a data atual + um ano> | A condição para determinação de preços é atualizada. |  |

### Criar condição para determinação de preços de PST2

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Este procedimento descreve a criação de condições para determinação de preços de venda: PST2

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | A página Início é exibida. |  |
| 2 | Acessar o app SAP Fiori | Abra Definir preços de material - Vendas(VK12). | É exibida a tela Modificar registros de condição. |  |
| 3 | Tipo de condição para a determinação de preços | Na visão Modificar registros de condição, efetue as seguintes entradas e pressione Enter:Tipo de condição: PST2 |  |  |
| 4 | Seleção | Na visão % var.bas.tp.serviço (PST2): Seleção, efetue as entradas a seguir e clique em ExecutarOrganização de vendas: Organização de vendasCanal de distribuição: Canal de distribuição |  |  |
| 5 | Modificar condição de preço | Na visão Modificar % var.bas.tp.serviço (PST2): síntese, efetue as seguintes entradas como abaixo e clique em Gravar.embalagem: CBPTS001Variante: HIGH_ENDMontante: <montante>Válido desde: <a data atual>Válido até: por exemplo, <a data atual + um ano> | A condição para determinação de preços é atualizada. |  |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-service-type-based-pricing-condition-mds-3gd]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3gd-319]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3gd-321]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-crear-condicion-de-determinacion-de-precios-b]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 12,624 chars in the whole document
