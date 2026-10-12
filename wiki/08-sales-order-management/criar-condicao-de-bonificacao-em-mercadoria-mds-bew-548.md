---
id: 08-sales-order-management/criar-condicao-de-bonificacao-em-mercadoria-mds-bew-548
title: Criar condição de bonificação em mercadoria – MDS (BEW) (BEW_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP S/4HANA Cloud master data script (BEW) for creating free-goods (bonificação em mercadoria) conditions via app VBN2, for the Pricing Specialist."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/free-goods]
aliases: [BEW_S4CLD2608_Master_Data_PT_XX]
keywords: [Free Goods and Free-of-Charge Delivery, free goods condition, master data scripts, pricing conditions, condition records, pricing specialist role, sales order, key combinations, master data requirements, BEW]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BEW_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-548
topic: 08-sales-order-management/free-goods
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar condição de bonificação em mercadoria – MDS (BEW) (BEW_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BEW_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Free Goods and Free-of-Charge Delivery** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar condição de bonificação em mercadoria – MDS (BEW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893964)

[2 Pré-requisitos 3](#_Toc233893965)

[2.1 Acesso ao sistema 3](#_Toc233893966)

[2.2 Funções 3](#_Toc233893967)

[2.3 Dados mestre obrigatórios e opcionais 3](#_Toc233893968)

[3 Tabela de síntese 5](#_Toc233893969)

[4 Procedimentos de teste 6](#_Toc233893970)

[4.1 Criar condição de bonificação em mercadoria 6](#_Toc233893971)

## Objetivo

Contexto empresarial

Alguns clientes podem receber mercadorias gratuitas ao investirem um determinado montante. Uma condição de bonificação em mercadoria permite que este contrato seja atualizado para um determinado cliente e material. É utilizada na transação da ordem do cliente.

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
| Especialista em preços | SAP_BR_PRICING_SPECIALIST | Gestão de preços | SAP_BR_PRICING_SPECIALIST |  |

### Dados mestre obrigatórios e opcionais

A tabela seguinte oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados ao criar condições de preço.

Se você tiver instalado um pacote básico SAP Best Practices, você pode utilizar os dados de amostra do pacote básico ou adicionar os seus próprios dados mestre, como obrigatório:

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Valores de amostra | Comentários |
| --- | --- | --- | --- | --- |
| Organização de vendas | Primeira tela | Obrigatório | <Número de organização de vendas> |  |
| Canal de distribuição | Primeira tela | Obrigatório | <Número de canal de distribuiçãor> |  |
| Cliente | Primeira tela | Obrigatório | <Número do cliente> |  |
| Material | Primeira tela | Opcional | Por exemplo, TG11 |  |

|  |
| --- |
| Lembrete Valores de amostra dos valores de dados mestre são específicos de países/regiões; os dados de amostra do pacote básico fornecem valores localizados para os países/regiões suportados. |

## Tabela de síntese

Criar condição de bonificação em mercadoria – MDS consiste das etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App SAP Fiori | Resultados esperados |
| --- | --- | --- | --- |
| [Criar condição de bonificação em mercadoria](#unique_7) [página ] 6 | Especialista em preços | Administrar bonificação em mercadoria - Vendas(VBN2) | É criado o registro de condição de mercadorias gratuitas. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar condição de bonificação em mercadoria

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir descreve a criação das condições de preço.

|  |
| --- |
| Lembrete Os valores de amostra para valores de dados mestre são específicos de país/região. Substitua os valores específicos de país/região fornecidos pelo sistema SAP S/4HANA Cloud Public Edition ou use os valores de dados mestre criados para esse fim. |

Procedimento

| Etapa do teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | O launchpad do SAP Fiori é exibido. | O launchpad do SAP Fiori é exibido. |
| 2 | Acessar o app SAP Fiori | Abra Administrar bonificação em mercadoria - Vendas(VBN2). | A nova visão que se abre exibe Modificar determinação de bonificação em mercadoria. |  |
| 3 | Tipo de condição para a determinação de preços | Na visão Modificar determinação de bonificação em mercadoria, insira as seguintes informações:Tipo de desconto: Por exemplo, YA00Pressione Enter. | A visão Modificar bonificação em mercadoria SD (YA00): seleção é aberta. |  |
| 4 | Combinação de chaves | Material / clientee selecione Selecionar. |  |  |
| 5 | Seleção | Na visão Modificar bonificação em mercadoria SD (YA00): seleção, insira as informações a seguir:Organização de vendas: <empresa>Canal de distribuição: por exemplo, 10Cliente: <número do cliente>Válido em: <Data>Clique em Executar. | A visão Modificar bonificação em mercadoria SD (YA00) é exibida. |  |
| 6 | Modificar condição de preço | Na tela Modificar bonificação em mercadoria SD (YA00), insira os dados abaixo:Material: Por exemplo, TG11Qtd.mín.: por exemplo, 1.000Para: por exemplo, 500Unidade: por exemplo, UNQtd. adic.: por exemplo, 10Adicionar unidade qtd.: por exemplo, Unid.Tipo cálc.: por exemplo, 1Bonif.mercadoria: por exemplo, 1 | A condição da bonificação em mercadoria é atualizada. |  |
| 7 | Salvar | Clique em Salvar. | A condição da bonificação em mercadoria é salva. |  |

Combinação de chaves: Organização de vendas/Canal de distribuição/Grupo de preços/Material

| Etapa do teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | O launchpad do SAP Fiori é exibido. | O launchpad do SAP Fiori é exibido. |
| 2 | Acessar o app SAP Fiori | Abra Administrar bonificação em mercadoria - Vendas(VBN2). | A nova visão que se abre exibe Modificar determinação de bonificação em mercadoria. |  |
| 3 | Tipo de condição para a determinação de preços | Na visão Modificar determinação de bonificação em mercadoria, insira as seguintes informações:Tipo de desconto: Por exemplo, YA00Pressione Enter. | A visão Modificar bonificação em mercadoria SD (YA00): seleção é aberta. |  |
| 4 | Combinação de chaves | Organização de vendas / Canal de distribuição / Grupo de preços / Materiale selecione Selecionar. |  |  |
| 5 | Seleção | Na visão Modificar bonificação em mercadoria SD (YA00): seleção, insira as informações a seguir:Organização de vendas: <empresa>Canal de distribuição: por exemplo, 10Grupo de preços: <grupo de preços>Válido em: <Data>Clique em Executar. | A visão Modificar bonificação em mercadoria SD (YA00) é exibida. |  |
| 6 | Modificar condição de preço | Na tela Modificar bonificação em mercadoria SD (YA00), insira os dados abaixo:Material: Por exemplo, TG11Qtd.mín.: por exemplo, 1.000Para: por exemplo, 500Unidade: por exemplo, UNQtd. adic.: por exemplo, 10Adicionar unidade qtd.: por exemplo, Unid.Tipo cálc.: por exemplo, 1Bonif.mercadoria: por exemplo, 1 | A condição da bonificação em mercadoria é atualizada. |  |
| 7 | Salvar | Clique em Salvar. | A condição da bonificação em mercadoria é salva. |  |

Combinação de chaves: Organização de vendas/Canal de distribuição/Material

| Etapa do teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | O launchpad do SAP Fiori é exibido. | O launchpad do SAP Fiori é exibido. |
| 2 | Acessar o app SAP Fiori | Abra Administrar bonificação em mercadoria - Vendas(VBN2). | A nova visão que se abre exibe Modificar determinação de bonificação em mercadoria. |  |
| 3 | Tipo de condição para a determinação de preços | Na visão Modificar determinação de bonificação em mercadoria, insira as seguintes informações:Tipo de desconto: Por exemplo, YA00Pressione Enter. | A visão Modificar bonificação em mercadoria SD (YA00): seleção é aberta. |  |
| 4 | Combinação de chaves | Organização de vendas/Canal de distribuição/Materiale selecione Selecionar. |  |  |
| 5 | Seleção | Na visão Modificar bonificação em mercadoria SD (YA00): seleção, insira as informações a seguir:Organização de vendas: <empresa>Canal de distribuição: por exemplo, 10Válido em: <Data>Clique em Executar. | A visão Modificar bonificação em mercadoria SD (YA00) é exibida. |  |
| 6 | Modificar condição de preço | Na tela Modificar bonificação em mercadoria SD (YA00), insira os dados abaixo:Material: Por exemplo, TG11Qtd.mín.: por exemplo, 1.000Para: por exemplo, 500Unidade: por exemplo, UNQtd. adic.: por exemplo, 10Adicionar unidade qtd.: por exemplo, Unid.Tipo cálc.: por exemplo, 1Bonif.mercadoria: por exemplo, 1 | A condição da bonificação em mercadoria é atualizada. |  |
| 7 | Salvar | Clique em Salvar. | A condição da bonificação em mercadoria é salva. |  |

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
- related-to :: [[08-sales-order-management/master-data-script-create-free-goods-condition-mds-bew-545]]
- related-to :: [[08-sales-order-management/mds-bew-547]]
- related-to :: [[08-sales-order-management/mds-bew-549]]
- related-to :: [[08-sales-order-management/naturalrabattkondition-anlegen-sds-bew-544]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BEW_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 13,022 chars in the whole document
