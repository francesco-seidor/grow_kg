---
id: 13-quality-ehs-and-compliance/criar-um-material-de-informacoes-de-conformidade-quimica-ehs-mds-65z-5
title: Criar um material de informações de conformidade química EHS – MDS (65Z) (65Z_S4CLD2608_Master_Data_PT_XX)
description: Portuguese master data script (65Z) for creating an EHS chemical compliance information material via Manage Material Data (F4864) in SAP S/4HANA Cloud Public Ed
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-waste-management-products]
aliases: [65Z_S4CLD2608_Master_Data_PT_XX]
keywords: [EHS Products and Chemical Compliance Materials for Waste, chemical compliance material, master data script, waste management, business roles, environmental manager, 65Z]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-506
topic: 13-quality-ehs-and-compliance/ehs-waste-management-products
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar um material de informações de conformidade química EHS – MDS (65Z) (65Z_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **EHS Products and Chemical Compliance Materials for Waste** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar um material de informações de conformidade química EHS – MDS (65Z) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893849)

[2 Pré-requisitos 3](#_Toc233893850)

[2.1 Acesso ao sistema 3](#_Toc233893851)

[2.2 Funções 3](#_Toc233893852)

[3 Tabela de síntese 4](#_Toc233893853)

[4 Procedimentos 5](#_Toc233893854)

[4.1 Criar dados mestre de materiais de informação de conformidade química EHS – Dados gerais 5](#_Toc233893855)

## Objetivo

Neste documento, você encontra uma descrição sobre como criar um registro de dados mestre de materiais de informação de conformidade química EHS para o seu sistema SAP S/4HANA. A descrição inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema "normal". O leitor aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo do fornecimento de conteúdo do S/4HANA, por SAP Best Practices, não são descritos neste documento, apesar de eles poderem aparecer na IU.

Um registro mestre de materiais de informações de conformidade química EHS que é criado como descrito aqui pode ser usado mais tarde em processos de gerenciamento de resíduos.

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

| Nome (modelo de função) | ID (modelo de função) |
| --- | --- |
| Responsável ambiental | SAP_BR_EHS_ENV_MGMT |

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

| Segmento | Função empresarial | App/transação | Resultados esperados |
| --- | --- | --- | --- |
| [Criar dados mestre de materiais de informação de conformidade química EHS – Dados gerais](#unique_6) [página ] 5 | Responsável ambiental | Administrar dados de material (F4864) | É criado um material de informação de conformidade química EHS (CCI). |

## Procedimentos

Esta seção descreve procedimentos para cada segmento ou etapa de processo que faz parte deste registro mestre.

### Criar dados mestre de materiais de informação de conformidade química EHS – Dados gerais

Objetivo

O procedimento a seguir fornece instruções para a criação de um material de informação de conformidade química EHS que pode ser empregado mais tarde para processos de gerenciamento de resíduos EHS.

Procedimento (usando launchpad do SAP Fiori)

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori usando suas credenciais de usuário. | É exibida a página Início. |  |
| 2 | Abrir Administrar dados mestre de cliente | Abra o app Administrar dados do material (F4864). | O app Administrar dados do material é aberto e é exibido um relatório de lista. |  |
| 3 | Criar material novo | Clique em Criar.Na tela:Insira um <Nome> no campo Nome interno.Selecione uma <função de logística> na lista de opções Função de logística.Clique em Salvar. | A guia Material novo é exibida e um novo material é criado. |  |
| 4 | Adicionar um produto | Clique em Editar.Na seção Produto , clique em Adicionar e selecione um produto.Clique em Salvar.Nota: Apenas um produto deve ser atribuído a um material. | Um produto é adicionado ao material e as informações são salvas. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/crear-un-material-de-informacion-de-conformidad-de-producto-quimico-eh]]
- related-to :: [[13-quality-ehs-and-compliance/create-an-ehs-chemical-compliance-information-material-mds-65z-503]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-65z-chinese-507]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-65z-japanese-505]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 7,158 chars in the whole document
