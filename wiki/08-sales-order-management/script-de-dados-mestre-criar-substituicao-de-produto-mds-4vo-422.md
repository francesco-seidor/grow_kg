---
id: 08-sales-order-management/script-de-dados-mestre-criar-substituicao-de-produto-mds-4vo-422
title: Script de dados mestre - Criar substituição de produto - MDS (4VO) (4VO_S4CLD2608_Master_Data_PT_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (PT) for creating product substitutions and product exclusions, with optional reason, group and control setup."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/product-and-location-substitution]
aliases: [4VO_S4CLD2608_Master_Data_PT_XX]
keywords: ["Product, Plant and Storage Location Substitution", product substitution, product exclusion, substitution reasons, substitution groups, substitution controls, product master data, master data scripts, fiori launchpad roles, 4VO]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-422
topic: 08-sales-order-management/product-and-location-substitution
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar substituição de produto - MDS (4VO) (4VO_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Product, Plant and Storage Location Substitution** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar substituição de produto - MDS (4VO) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893801)

[2 Pré-requisitos 3](#_Toc233893802)

[2.1 Acesso ao sistema 3](#_Toc233893803)

[2.2 Funções 3](#_Toc233893804)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893805)

[2.4 Dados mestre obrigatórios 4](#_Toc233893806)

[2.5 Etapas preliminares 4](#_Toc233893807)

[2.5.1 Criar motivo para substituição do produto (opcional) 4](#_Toc233893808)

[2.5.2 Criar grupo para substituição (opcional) 5](#_Toc233893809)

[2.5.3 Criar controle para substituição (opcional) 7](#_Toc233893810)

[3 Tabela de síntese 9](#_Toc233893811)

[4 Procedimentos de teste 10](#_Toc233893812)

[4.1 Criar substituição de produto 10](#_Toc233893813)

[4.2 Criar exclusão de produtos 11](#_Toc233893814)

## Objetivo

Neste documento, você encontrará como criar dados mestre de substituição e exclusão de produto no sistema SAP S/4HANA Cloud Public Edition.

Substituição de produto é uma técnica usada para substituir um produto por outro. Uma substituição de produto pode ser criada por vários motivos. Por exemplo:

- O produto não está mais em estoque
- O produto está fora da garantia
- O produto de substituição é abundante no estoque

A exclusão de produto permite que os clientes excluam um produto de ser um substituto. Por exemplo, a exclusão pode ser criada para um produto obsoleto.

## Pré-requisitos

Esta seção resume todos os pré-requisitos necessários para conduzir o teste em termos de sistemas, usuários, dados mestre, dados organizacionais, outros dados de teste e condições empresariais.

### Acesso ao sistema

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece o URL para acessar os diversos apps atribuídos à sua função. |

### Funções

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) | Efetuar login |
| --- | --- | --- | --- | --- |
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Dados mestre - produtos / Governança de produto | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Unidades organizacionais necessárias

A estrutura organizacional reflete a estrutura da sua empresa. Os substitutos de produto podem ser dependentes das unidades organizacionais (centro) da empresa. Também pode ser independente da unidade organizacional. A tabela a seguir fornece uma síntese das unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Substituição de produto e exclusão de produto | Centro |  | O centro não é obrigatório na substituição/exclusão de produto. A substituição/exclusão de produto pode ocorrer sem restrição de centro. | Centro:____________ |

### Dados mestre obrigatórios

Os dados de substituição de produto referem-se aos dados mestre do produto. Os dados mestre obrigatórios para o script de teste representam materiais/produtos. Crie seus próprios dados mestre seguindo os dados mestre de amostra fornecidos abaixo.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Material | Criar substituição de produtoCriar exclusão de produtos | Obrigatório | Para criar uma substituição ou exclusão de produto, devem existir pelo menos 2 dados mestre de materiais/produtos no sistema |

Para mais informações sobre a criação de objetos de dados mestre, consulte [Scripts de dados mestre (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data).

Tabela 1: Referência a script de dados mestre

| MDS | Descrição |
| --- | --- |
| BNF | Criar mestre de produtos do tipo "Produto comercializável" – MDS |

### Etapas preliminares

#### Criar motivo para substituição do produto (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções sobre como criar motivo para substituição/exclusão de produtos. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar motivos da substituição - Produtos(F4789). | A tela Administrar motivos de substituição - Produtos é exibida. |  |
| 3 | Clicar em Criar | Na tela Administrar motivos de substituição - Produtos, clique em Criar. | A tela Motivo é exibida. |  |
| 4 | Inserir um motivo | Na seção Cabeçalho, efetue a seguinte entrada:Motivo: <insira o novo código do motivo para substituição, por exemplo, Upgrade> |  |  |
| 5 | Salvar os dados | Clique em Criar. | A mensagem do sistema Objeto salvo é exibida. |  |
| 6 | Clicar em Criar | Na seção Descrição, clique em Criar. | A tela Descrição do motivo é exibida. |  |
| 7 | Inserir dados de descrição | Na seção Descrição, efetue as seguintes entradas:Código de idioma: <insira o código de idioma aplicável para o Motivo, por exemplo, EN para inglês>Descrição do motivo: <insira texto para descrever o Motivo, por exemplo, Aplicável para produtos que passam por upgrades> |  |  |
| 8 | Salvar os dados | Clique em Criar. | A mensagem do sistema Descrição criada é exibida. |  |

#### Criar grupo para substituição (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de grupos para substituição/exclusão de produtos. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar grupos de substituição - Produtos(F4788). | A tela Administrar grupos de substituição – Produtos é exibida. |  |
| 3 | Selecionar Criar | Na tela Administrar grupos de substituição – Produtos, selecione Criar. | A tela Administrar grupos de substituição – Criar produtos é exibida. |  |
| 4 | Inserir grupo | Efetue as seguintes entradas na seção Cabeçalho:Grupo: <Insira o novo grupo para a substituição, por exemplo, STANDARD_DISPLAY> |  |  |
| 5 | Salvar os dados | Clique em Criar. | É exibida a mensagem do sistema de que o objeto foi salvo. |  |
| 6 | Selecionar Criar | Na seção Descrição, selecione Criar. | A tela Criar descrição do grupo é exibida. |  |
| 7 | Inserir dados de descrição | Na seção Descrição, efetue as seguintes entradas:Código de idioma: <insira o idioma aplicável para o grupo, por exemplo, EN inglês>Descrição do grupo: <Inserir texto para descrever o grupo, por exemplo, Todas as exibições padrão do computador> |  |  |
| 8 | Salvar os dados | Clique em Criar. | É exibida a mensagem do sistema de que o objeto foi salvo. |  |
| 9 | Clicar em Voltar | Na seção Título, clique em < (Voltar). | A tela Administrar grupos de substituição – Produtos é exibida. |  |
| 10 | Ativar dados do grupo | Clique em Definir como ativo. | A mensagem do sistema exibe que o objeto está ativo. |  |

#### Criar controle para substituição (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de controle para grupos de substituição/exclusão de produtos. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar controles de substituição - Produtos(F4787). | A tela Administrar controles de substituição – Produtos é exibida. |  |
| 3 | Selecionar Criar | Na tela Administrar controles de substituição – Produtos, selecione Criar. | A tela Administrar controles de substituição – Criar produtos é exibida. |  |
| 4 | Inserir controle | Efetue a seguinte entrada na seção Cabeçalho:Controle: <insira o novo controle para substituição, por exemplo, SALE> |  |  |
| 5 | Salvar os dados | Clique em Criar. | É exibida a mensagem do sistema de que o objeto foi salvo. |  |
| 6 | Selecionar Criar | Na seção Descrição, clique em Criar. | A tela Criar descrição de controle é exibida. |  |
| 7 | Inserir dados de descrição | Na seção Descrição, efetue as seguintes entradas:Código de idioma: <insira o idioma aplicável para o controle, por exemplo, EN inglês>Descrição do controle: <insira o texto para descrever o controle, por exemplo, Para venda> |  |  |
| 8 | Salvar os dados | Clique em Criar. | É exibida a mensagem do sistema de que o objeto foi salvo. |  |
| 9 | Clicar em Voltar | Na seção Título, selecione < (Voltar). | A tela Administrar controles de substituição – Produtos é exibida. |  |
| 10 | Grupos atribuídos | Na seção grupos atribuídos, clique em Atribuir. | A tela Atribuir grupos ao controle é exibida. |  |
| 11 | Seleciona grupo | Na caixa de diálogo Atribuir grupos ao controle, pesquise e clique em Grupo.Por exemplo, clique em Grupo<STANDARD_DISPLAY>Clique em Atribuir. | É exibida a mensagem do sistema de que o objeto está atribuído. |  |

## Tabela de síntese

Este item de escopo é composto pelo processo de segmentos fornecido na tabela abaixo.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Segmento | Função empresarial | Transação / App | Resultados previstos |
| --- | --- | --- | --- |
| [Criar substituição de produto](#unique_11) [página ] 10 | Especialista em dados mestre - Dados do produto | Administrar substituições - Produtos(F4785) | O registro de substituição do produto é criado. |
| [Criar exclusão de produtos](#unique_12) [página ] 11 | Especialista em dados mestre - Dados do produto | Administrar exclusões - Produtos(F4786) | O registro de exclusão do produto é criado. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar substituição de produto

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação da substituição de produto. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar substituições - Produtos(F4785). | A tela Administrar substituições – Produtos é exibida. |  |
| 3 | Clicar em Criar | Na visão Administrar substituições – Produtos, clique em Criar. | O layout de coluna flexível Administrar substituições – Produtos é exibido com a tela Criar. |  |
| 4 | Inserir dados de cabeçalho | Efetue as seguintes entradas na seção Cabeçalho:Produto: <insira o produto que requer um substituto>Produto substituto: <insira o substituto>Centro: <número do centro>Os dados do produto e do produto substituto são obrigatórios para criar uma substituição. |  |  |
| 5 | Inserir dados de informações gerais | Na seção Informações gerais, efetue as seguintes entradas:Motivo: <insira o motivo para a criação do substituto. por exemplo, Upgrade>Válido desde: <insira a data e hora de início da validade>Válido até: <insira a data e a hora do fim da validade>Fuso horário: <insira o fuso horário aplicável à validade>As entradas acima são opcionais. |  |  |
| 6 | Salvar os dados | Clique em Criar. | É exibida a mensagem do sistema objeto salvo. |  |
| 7 | Ativar dados de substituição do produto | Clique em Definir como ativo. | A mensagem do sistema mostra que o objeto está ativo. |  |

### Criar exclusão de produtos

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de exclusão de produtos. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar exclusões - Produtos(F4786). | A tela Administrar exclusões – Produtos é exibida. |  |
| 3 | Clicar em Criar | Na visão Administrar exclusões – Produtos, clique em Criar. | A tela Administrar exclusões – Criar produtos é exibida. |  |
| 4 | Inserir dados de cabeçalho | Efetue as seguintes entradas na seção Cabeçalho:Produto: <insira o produto que deve ser excluído da substituição>Centro: <número do centro>O produto é obrigatório para criar uma exclusão. |  |  |
| 5 | Inserir dados de informações gerais | Na seção Informações gerais, efetue as seguintes entradas:Motivo: <Insira o motivo para a exclusão do produto>Válido desde: <insira a data e hora de início da validade>Válido até: <insira a data e a hora do fim da validade>Fuso horário: <insira o fuso horário aplicável à validade>As entradas acima são opcionais. |  |  |
| 6 | Salvar os dados | Clique em Criar. | É exibida a mensagem do sistema objeto salvo. |  |
| 7 | Ativar dados de exclusão de produto | Clique em Definir como ativo. | A mensagem do sistema mostra que o objeto está ativo. |  |

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
- related-to :: [[08-sales-order-management/creacion-de-sustitucion-de-producto-mds-4vo-420]]
- related-to :: [[08-sales-order-management/create-product-substitution-mds-4vo-419]]
- related-to :: [[08-sales-order-management/mds-4vo-421]]
- related-to :: [[08-sales-order-management/mds-4vo-423]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 18,654 chars in the whole document
