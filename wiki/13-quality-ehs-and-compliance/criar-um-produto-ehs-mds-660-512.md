---
id: 13-quality-ehs-and-compliance/criar-um-produto-ehs-mds-660-512
title: Criar um produto EHS – MDS (660) (660_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese master data script 660: create an EHS product master record via Administrar dados mestre do produto (F1602) in SAP S/4HANA Cloud Public Edition 2608."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-waste-management-products]
aliases: [660_S4CLD2608_Master_Data_PT_XX]
keywords: [EHS Products and Chemical Compliance Materials for Waste, ehs product, product master data, waste management, business roles, test scripts, 660]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/660_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-512
topic: 13-quality-ehs-and-compliance/ehs-waste-management-products
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar um produto EHS – MDS (660) (660_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/660_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **EHS Products and Chemical Compliance Materials for Waste** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar um produto EHS – MDS (660) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893923)

[2 Pré-requisitos 3](#_Toc233893924)

[2.1 Acesso ao sistema 3](#_Toc233893925)

[2.2 Funções 3](#_Toc233893926)

[3 Tabela de síntese 4](#_Toc233893927)

[4 Procedimentos 5](#_Toc233893928)

[4.1 Criar dados mestre do produto EHS – Dados gerais 5](#_Toc233893929)

## Objetivo

Neste documento, você encontra uma descrição sobre como criar um registro de dados mestre de produto EHS para o seu sistema SAP S/4HANA. A descrição inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema "normal". O leitor aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo do fornecimento de conteúdo do S/4HANA, por SAP Best Practices, não são descritos neste documento, apesar de eles poderem aparecer na IU.

Um registro mestre de produto EHS criado da forma aqui descrita pode ser usado mais tarde em processos de gerenciamento de resíduos.

Este documento fornece um procedimento detalhado para testar o item de escopo após a ativação da solução, refletindo o escopo predefinido da solução. Cada etapa do processo, relatório ou item está coberto em uma seção própria que fornece as interações do sistema (etapas de teste) em uma visão de tabela. As etapas que não estão no escopo do processo, mas que são necessárias para teste, estão marcadas de modo correspondente. É necessário adicionar etapas específicas do projeto.

|  |
| --- |
| Nota Os valores deste script de teste (notação decimal, formatos de data etc.) são apresentados na notação padrão dos EUA. Se o sistema de teste estiver configurado para usar uma notação diferente, insira os valores apropriados. |

## Pré-requisitos

Esta seção resume todos os pré-requisitos necessários para conduzir o teste em termos de sistemas, usuários, dados mestre, dados organizacionais, outros dados de teste e condições empresariais.

### Acesso ao sistema

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece a você o URL para acessar os diversos apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome | ID |
| --- | --- |
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST |

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

| Segmento | Função empresarial | App/transação | Resultados esperados |
| --- | --- | --- | --- |
| [Criar dados mestre do produto EHS – Dados gerais](#unique_6) [página ] 5 | Especialista em dados mestre – Dados do produto | Administrar dados mestre do produto (F1602) | Um produto EHS é criado. |

## Procedimentos

Esta seção descreve procedimentos para cada segmento ou etapa de processo que faz parte deste registro mestre.

### Criar dados mestre do produto EHS – Dados gerais

Objetivo

O seguinte procedimento fornece instruções para a criação de um produto EHS que pode ser usado mais tarde para processos de gerenciamento de resíduos EHS.

Procedimento (usando launchpad do SAP Fiori)

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori usando suas credenciais de usuário. | É exibida a página Início. |  |
| 2 | Navegar para os dados mestre do produto | Abra o app Administrar dados mestre do produto (F1602) | O app Administrar dados mestre do produto é aberto e um relatório de lista é exibido. |  |
| 3 | Criar um produto | Na caixa de diálogo Criar, selecione Produto. | A tela Criar registro de dados mestre de um produto é exibida. |  |
| 4 | Selecionar registros de dados mestre de um produto | Na mesma tela:Insira um <Número do produto> no campo Número do produto.Selecione um <Tipo de produto> no campo Tipo de produto.Selecione um <Grupo de produtos> no campo Grupo de produtos.Insira uma <Descrição> no campo Descrição.Selecione uma <Unidade básica> por meio das entradas possíveis para o campo Unidade básica.Clique em OK. | O produto contém informações do registro de dados mestre. |  |
| 5 | Salvar as informações | Clique em Salvar. | O Produto é criado. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/crear-un-producto-ehs-mds-660-510]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-660-511]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-660-chinese-513]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-produkt-anlegen-sds-660-508]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/660_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 7,762 chars in the whole document
