---
id: 04-tax-and-statutory-reporting/objetivo-script-de-dados-mestre-criar-condicao-de-imposto-mds-2sw-port
title: "Objetivo (Script de dados mestre: Criar condição de imposto - MDS 2SW, Portuguese) (2SW_S4CLD2608_Master_Data_PT_XX)"
description: "Portuguese master data script (2SW) for SAP S/4HANA Cloud 2608: creating tax condition records and creating/modifying purchasing price conditions (MEK1/MEK2)."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/purchasing-tax-condition-records]
aliases: [2SW_S4CLD2608_Master_Data_PT_XX]
keywords: [Tax Condition Records and Purchasing Price Conditions, tax condition records, purchasing price conditions, price condition changes, tax codes, business roles, master data scripts, condition types, 2SW]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-278
topic: 04-tax-and-statutory-reporting/purchasing-tax-condition-records
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Objetivo (Script de dados mestre: Criar condição de imposto - MDS 2SW, Portuguese) (2SW_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Tax Condition Records and Purchasing Price Conditions** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar condição de imposto - MDS (2SW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893593)

[2 Pré-requisitos 3](#_Toc233893594)

[2.1 Acesso ao sistema 3](#_Toc233893595)

[2.2 Funções 3](#_Toc233893596)

[2.3 Dados mestre obrigatórios e opcionais 3](#_Toc233893597)

[3 Tabela de síntese 5](#_Toc233893598)

[4 Procedimentos de teste 6](#_Toc233893599)

[4.1 Criar registros de condições de imposto 6](#_Toc233893600)

[4.2 Criar condições de preço 7](#_Toc233893601)

[4.3 Modificar condições de preço 9](#_Toc233893602)

## Objetivo

Um registro de condição de imposto contém informações específicas de um país ou uma região e um código de imposto cada para combinação de indicador de imposto para material/centro/importação.

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
| Especialista em impostos | SAP_BR_TAX_SPECIALIST | Taxas de imposto | SAP_BR_TAX_SPECIALIST |  |
| Comprador | SAP_BR_PURCHASER | Compras / Determinação da fonte de suprimento e contratação | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre de materiais podem fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre de materiais.

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar uma condição para determinação de preços:

País de destino: por exemplo, DE

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| País de destino | 1ª tela | Obrigatório |  |

## Tabela de síntese

Este item de escopo consiste em várias etapas de processo, indicadas na tabela a seguir.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App SAP Fiori | Resultados esperados |
| --- | --- | --- | --- |
| [Criar registros de condições de imposto](#unique_7) [página ] 6 | Especialista em impostos | Determinar taxas de imposto - Compras(MEK2) | A condição de imposto está definida. |
| [Criar condições de preço](#unique_8) [página ] 7 | Comprador | Criar condições de preço - Compras(MEK1) | As condições de preço são criadas. |
| [Modificar condições de preço](#unique_9) [página ] 9 | Comprador | Modificar condições de preço - Compras(MEK2) | As condições de preço são alteradas. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar registros de condições de imposto

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em impostos. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Determinar taxas de imposto - Compras(MEK2). | O app é aberto. |  |
| 3 | Tipo de condição para a determinação de preços | Na tela Modificar registros de condição, efetue a seguinte entrada e pressione Enter:Tipo de condição: por exemplo, TTX1 | A tela Combinação de chaves é exibida. |  |
| 4 | Combinação de chaves | Na tela Combinação de chaves, marque o campo de seleção Impostos: Material, centro e origem e clique em Selecionar. | A tela Modificar T(TTX1) não dedutível: seleção é exibida. |  |
| 5 | País de destino | Na tela Modificar T(TTX1) não dedutível: Seleção, efetue as seguintes entradas e clique em Executar:País de destino: <Código do país/região> | A tela Modificar condição de imposto não dedutível (TTX1): Síntese é exibida. |  |
| 6 | Modificar a condição de imposto | Na tela Modificar condição de imposto não dedutível (TTX1): Síntese, efetue as seguintes entradas:Ind.imposto material: <Indicador de imposto para material>IndImpCent: <indicador de imposto> <centro>Importação: <Importação>Válido desde: <válido desde>Válido até: <válido até>Código de imposto: <código de imposto> | O registro de condições de imposto é atualizado. |  |
| 7 | Salvar | Clique em Salvar. | O registro de condições de imposto é salvo. |  |
| 8 | Clicar em Voltar | Clique em Voltar duas vezes. |  |  |
| 9 | Tipo de condição para a determinação de preços | Na tela Modificar registros de condição, efetue a seguinte entrada e pressione Enter:Tipo de condição: por exemplo, TTX1 | A caixa de diálogo Combinação de chaves é exibida. |  |
| 10 | Combinação de chaves | Na caixa de diálogo Combinação de chaves, selecione a marcação Imposto: Origem e região do centro e da classificação contábil e clique em Selecionar. | A tela Modificar T(TTX1) não dedutível: seleção é exibida. |  |
| 11 | País de destino | Na tela Modificar T(TTX1) não dedutível: Seleção, efetue as seguintes entradas e clique em Executar:País de destino: <Código do país/região> | A tela Modificar condição de imposto não dedutível (TTX1): Síntese é exibida. |  |
| 12 | Modificar a condição de imposto | Na tela Modificar condição de imposto não dedutível (TTX1): Síntese, efetue as seguintes entradas:IndImpCent: <indicador de imposto> <centro>Ind.imp.class.cont.: <Indicador de imposto de classificação contábil>Importação: <Importação>Região do indicador do imposto: <Região>Válido desde: <válido desde>Válido até: <válido até>Código de imposto: <código de imposto> | O registro de condições de imposto é atualizado. |  |
| 13 | Salvar | Clique em Salvar. | O registro de condições de imposto é salvo. |  |

### Criar condições de preço

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Comprador. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar condições de preço - Compras(MEK1). | O app é aberto. |  |
| 3 | Tipo de condição para a determinação de preços | Efetue as entradas a seguir e pressione Enter:Tipo de condição: por exemplo, PPR0 | A caixa de diálogo Combinação de chaves é exibida. |  |
| 4 | Combinação de chaves | Na tela Combinação de chaves, marque o campo de seleção Registro info de material (específico do centro) e clique em Selecionar. | A tela Criar condição de preço bruto padrão (PPR0): Entrada rápida é exibida. |  |
| 5 | Criar condição de bruto padrão | Na tela Criar condição de preço bruto padrão (PPR0): Entrada rápida, efetue as seguintes entradas:Fornecedor: <fornecedor>Material: <material>Organização de compras: <organização de compras>Centro: <Centro>Infotipo: por exemplo, 0 PadrãoMontante: <Montante>Unidade: <unidade de determinação do preço>Por: <por quantidade>UM: <unidade>Válido desde: <válido desde>Válido até: <válido até> | O registro de condição de bruto padrão é atualizado. |  |
| 6 | Salvar | Clique em Salvar. | O registro de condição é salvo. |  |

### Modificar condições de preço

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Comprador. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Modificar condições de preço - Compras(MEK2). | O app é aberto. |  |
| 3 | Tipo de condição para a determinação de preços | Efetue a seguinte entrada e pressione Enter:Tipo de condição: Por exemplo, PPR0. | A tela Combinação de chaves é exibida. |  |
| 4 | Combinação de chaves | Na tela Combinação de chaves, marque o campo de seleção Registro info de material (específico do centro) e clique em Selecionar. | A tela Criar condição de preço bruto padrão (PPR0): Entrada rápida é exibida. |  |
| 5 | Modificar condição de bruto padrão | Na tela Modificar condição de preço bruto padrão (PPR0): entrada rápida, efetue as seguintes entradas:Fornecedor: <fornecedor>embalagem: <Material>Organização de compras: <organização de compras>Centro: <centro>Infotipo: por exemplo, 0 PadrãoClique em Executar.Efetue a seguinte entrada:Montante: <Montante> | O registro de condição de bruto padrão é modificado. |  |
| 6 | Salvar | Clique em Salvar. | O registro de condição é salvo. |  |

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
- related-to :: [[04-tax-and-statutory-reporting/crear-condicion-para-determinacion-de-impuestos-mds-2sw-276]]
- related-to :: [[04-tax-and-statutory-reporting/master-data-script-create-tax-condition-2sw-275]]
- related-to :: [[04-tax-and-statutory-reporting/mds-2sw-277]]
- related-to :: [[04-tax-and-statutory-reporting/mds-2sw-279]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 13,818 chars in the whole document
