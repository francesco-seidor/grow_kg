---
id: 06-management-accounting/criar-grupo-de-classes-de-custo-mds-bnp-650
title: Criar grupo de classes de custo – MDS (BNP) (BNP_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese master data script BNP: create a cost element group with Administrar grupos de classes de custo (F5373) as Controlador - custos indiretos, S/4HANA Cl"
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-element-groups]
aliases: [BNP_S4CLD2608_Master_Data_PT_XX]
keywords: [Cost Element Groups, cost element group creation, cost accounting master data, business roles, controlling area, chart of accounts, test procedures, BNP]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-650
topic: 06-management-accounting/cost-element-groups
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar grupo de classes de custo – MDS (BNP) (BNP_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Cost Element Groups** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar grupo de classes de custo – MDS (BNP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894036)

[2 Pré-requisitos 3](#_Toc233894037)

[2.1 Acesso ao sistema 3](#_Toc233894038)

[2.2 Funções 3](#_Toc233894039)

[2.3 Unidades organizacionais necessárias 3](#_Toc233894040)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233894041)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233894042)

[3 Tabela de síntese 5](#_Toc233894043)

[4 Procedimentos de teste 6](#_Toc233894044)

[4.1 Criar dados mestre do grupo de classes de custo 6](#_Toc233894045)

## Objetivo

Contexto empresarial

Grupos de classes de custo são normalmente utilizados para agrupar classes de custo com características similares para fins de reporting. Grupos de classes de custo podem ser utilizados no sistema de informação, por exemplo. Você pode utilizar a estrutura do grupo de classes de custo para definir a estrutura das linhas dos seus relatórios. Os totais são calculados no relatório para cada nó.

Você também pode utilizar os grupos de classes de custo sempre que quiser processar várias classes de custo em uma operação. Por exemplo, no planejamento de centros de custo, de distribuição ou avaliação.

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
| Controlador - custos indiretos | SAP_BR_OVERHEAD_ACCOUNTANT | Contabilidade de custos indiretos | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### Unidades organizacionais necessárias

A estrutura organizacional e os dados mestre da sua empresa foram criados no seu sistema ERP durante a implementação. A estrutura organizacional reflete a estrutura da sua empresa. Os dados mestre representam grupos de classes de custo, dependendo do foco operacional da sua empresa.

| Objeto de dados | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Área de contabilidade de custos | Dados gerais | Obrigatório |  |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre do grupo de classes de custo podem fazer referência a outros dados mestre. A tabela seguinte oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados do grupo de classes de custo.

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Plano de contas | Unidades organizacionais | Opcional |  |

### Parâmetros principais para a criação de dados

Este item de escopo não tem condições empresariais.

## Tabela de síntese

Este item de escopo é composto por várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar dados mestre do grupo de classes de custo](#unique_9) [página ] 6 | Controlador - custos indiretos | Administrar grupos de classes de custo(F5373) | Os grupos de classes de custo podem ser criados de acordo com os novos requisitos empresariais. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar dados mestre do grupo de classes de custo

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Pré-requisito

Você inseriu e salvou os dados básicos para o material.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Controlador - custos indiretos. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar grupos de classes de custo(F5373). | O app é aberto. |  |
| 3 | Inserir novo grupo de classes de custo | Na tela Administrar grupos de classes de custo, clique em Criar. Na tela Criar grupo de classes de custo: 1ª tela, efetue as seguinte entrada:Grupo de classes de custo: <Grupo de classes de custo>Pressione Enter.Como alternativa, escolha uma referência dos grupos de centros de custos existentes. | Na tela Criar grupo de classes de custo: estrutura é exibida. |  |
| 4 | Inserir classe de custo e/ou grupo de classes de custo | Os novos dados mestre são exibidos na tela Grupo de classes de custo: Estrutura. Efetue a seguinte entrada:Descrição: <Descrição>Além disso, você pode efetuar as seguintes entradas, posicionando o seu cursor sobre a sua seleção, e utilizar os seguintes botões de navegação:Nível inferior : <insira um grupo de classes de custo no nível inferior>Classe de custo: (Opção Inserir) - Adicionar classes de custo ou intervalos de classesMesmo nível: <insira grupos de classes de custo adicionais no mesmo nível inferior> | Os novos dados mestre são exibidos na tela Grupo de classes de custo: Estrutura. |  |
| 5 | Salvar os dados | Clique em Salvar. | O grupo de classes de custo é criado e salvo. |  |

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
- related-to :: [[06-management-accounting/create-cost-element-group-mds-bnp-647]]
- related-to :: [[06-management-accounting/kostenartengruppe-anlegen-sds-bnp-646]]
- related-to :: [[06-management-accounting/mds-bnp-649]]
- related-to :: [[06-management-accounting/mds-bnp-651]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 9,695 chars in the whole document
