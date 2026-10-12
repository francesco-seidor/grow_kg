---
id: 08-sales-order-management/criar-registro-info-de-material-do-cliente-mds-2yx-296
title: Criar registro info de material do cliente – MDS (2YX) (2YX_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP master data script (2YX, 2608): create a customer-material info record in app F2499 as internal sales representative, incl. sales unit conversion."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-material-info-records]
aliases: [2YX_S4CLD2608_Master_Data_PT_XX]
keywords: [Customer-Material Info Records, customer material info, sales unit conversion, business roles, sales organization, distribution channel, master data scripts, fiori launchpad access, test procedures, 2YX]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-296
topic: 08-sales-order-management/customer-material-info-records
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar registro info de material do cliente – MDS (2YX) (2YX_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Customer-Material Info Records** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar registro info de material do cliente – MDS (2YX) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893611)

[2 Pré-requisitos 3](#_Toc233893612)

[2.1 Acesso ao sistema 3](#_Toc233893613)

[2.2 Funções 3](#_Toc233893614)

[2.3 Dados mestre obrigatórios e opcionais 3](#_Toc233893615)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893616)

[3 Tabela de síntese 5](#_Toc233893617)

[4 Procedimentos de teste 6](#_Toc233893618)

[4.1 Criar informações de material do cliente 6](#_Toc233893619)

## Objetivo

Neste documento, você encontra uma descrição sobre como criar informações de cliente/material para seu sistema SAP S/4HANA Cloud Public Edition. A descrição inclui os segmentos de dados relevantes para o appliance SAP S/4HANA Cloud Public Edition. Os campos que não são relevantes para o escopo do conteúdo do SAP S/4HANA Cloud Public Edition não estão descritos neste documento.

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
| Representante de vendas interno | SAP_BR_INTERNAL_SALES_REP | Venda interna / Devoluções dos clientes / Faturamento | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |

### Dados mestre obrigatórios e opcionais

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Cliente | Primeira tela | Obrigatório |  |
| Organização de vendas | Primeira tela | Obrigatório |  |
| Canal de distribuição | Primeira tela | Obrigatório |  |
| Material | Primeira tela | opcional |  |

### Dados mestre obrigatórios e opcionais

Nesta seção, você encontra alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar uma condição de determinação de preços:

Organização de vendas: <Organização de vendas>

Canal de distribuição: <canal de distribuição>

Cliente: <Cliente>

Material: <número do material>

## Tabela de síntese

Este item de escopo é composto por várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App SAP Fiori | Resultados esperados |
| --- | --- | --- | --- |
| [Criar informações de material do cliente](#unique_8) [página ] 6 | Representante de vendas interno | Administrar materiais de cliente(F2499) | O registro info de cliente-material é criado. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar informações de material do cliente

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Representante de vendas interno. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar materiais de cliente(F2499). | O app é aberto. |  |
| 3 | Acessar a criação de materiais do cliente | Clique em Criar. | É exibida a tela Material do cliente. |  |
| 4 | Inserir especificações básicas sobre o material do cliente | Efetue as seguintes entradas:Cliente: <Cliente>Produto: <Número do material>Organização de vendas: <organização de vendas>Canal de distribuição: <canal de distribuição>Descrição do material do cliente: forneça uma descrição para este cliente e material. | As informações básicas de material do cliente são atualizadas. |  |
| 5 | Inserir unidade de vendas | Na seção Conversão de unidades, efetue a seguinte entrada:1 PAL (unidade do cliente): 2 unidades (unidade básica) | A unidade de venda para a combinação de material do cliente é atualizada.NotaPara atualizar a unidade de venda e a conversão nesta tela, os dados mestre de materiais da unidade de medida e conversão devem ser atualizados. Você pode consultar outros scripts de dados mestre, por exemplo, Criar mestre de produtos do tipo "Produto comercializável" – MDS - BNF para produtos comercializáveis.Assim que a unidade de vendas for atualizada nesta tela, ela será exibida no documento de vendas. |  |
| 6 | Clicar em Criar | Clique em Criar. | O material do cliente é criado com sucesso. |  |

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
- related-to :: [[08-sales-order-management/crear-registro-info-para-cliente-y-material-mds-2yx-294]]
- related-to :: [[08-sales-order-management/create-customer-material-info-record-mds-2yx-293]]
- related-to :: [[08-sales-order-management/kundenmaterial-infosatz-anlegen-sds-2yx-292]]
- related-to :: [[08-sales-order-management/mds-2yx-295]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 9,035 chars in the whole document
