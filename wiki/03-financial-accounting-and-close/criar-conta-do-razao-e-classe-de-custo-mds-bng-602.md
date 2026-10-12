---
id: 03-financial-accounting-and-close/criar-conta-do-razao-e-classe-de-custo-mds-bng-602
title: Criar conta do Razão e classe de custo - MDS (BNG) (BNG_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese master data script (BNG) for SAP S/4HANA Cloud Public Edition: creating G/L accounts by copying, via Manage Your Solution (F1241) or SAP Central Business Configuration."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/chart-of-accounts-and-gl-accounts]
aliases: [BNG_S4CLD2608_Master_Data_PT_XX]
keywords: [Chart of Accounts YCOA and G/L Account Creation, gl account master data, chart of accounts, cost element, account types, account groups, business process configuration, sap central business configuration, master data scripts, BNG]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-602
topic: 03-financial-accounting-and-close/chart-of-accounts-and-gl-accounts
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar conta do Razão e classe de custo - MDS (BNG) (BNG_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Chart of Accounts YCOA and G/L Account Creation** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar conta do Razão e classe de custo – MDS (BNG) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894036)

[2 Pré-requisitos 3](#_Toc233894037)

[2.1 Acesso ao sistema 3](#_Toc233894038)

[2.2 Funções 3](#_Toc233894039)

[2.3 Unidades organizacionais necessárias 4](#_Toc233894040)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233894041)

[2.5 Parâmetros principais para a criação de dados 6](#_Toc233894042)

[3 Tabela de síntese 7](#_Toc233894043)

[4 Procedimentos de teste 8](#_Toc233894044)

[4.1 Criar conta do Razão 8](#_Toc233894045)

## Objetivo

Um registro mestre de conta do Razão contém informações sobre a conta que determina como as transações comerciais são lançadas nela e como serão administradas.

O Razão na SAP fornece uma visão abrangente e totalmente atualizada de todos os imobilizados, contas a pagar e contas a receber, e está totalmente integrado com os outros módulos da SAP.

Uma vez que todos os módulos da SAP estão integrados, alguns lançamentos no Razão são gerados automaticamente pelo sistema em background, por exemplo, o lançamento na conta de EM/EF (entrada de mercadorias/entrada de faturas) e os lançamentos no Razão para movimento de estoque.

Algumas contas são "administradas por partidas em aberto”. Elas são usadas como uma conta de compensação para que as partidas individuais possam ser compensadas quando, por exemplo, a entrada e a saída de pagamentos e os materiais são processados.

Outras contas, por exemplo, as contas de reconciliação de cliente e fornecedor, não podem receber lançamentos diretamente, pois são apenas um reflexo dos parceiros de negócios nos livros auxiliares.

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
| Especialista de configuração - configuração de processo empresarial | SAP_BR_BPC_EXPERT | Configuração de processo empresarial / Configuração de processo empresarial - Finanças / Configuração de processo empresarial - Suprimento / Administrar sua solução / Configuração de processo empresarial - Workflow / Configuração empresarial - Administração de funcionalidades / Configuração de processo empresarial - Extensibility Explorer / Configuração de gestão empresarial - Transporte | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre de cliente são dependentes das unidades organizacionais da empresa. Os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser utilizada |
| --- | --- | --- | --- | --- |
| Conta do Razão | EmpresaPlano de contasÁrea de contabilidade de custos | Consulte [Dados mestre obrigatórios e opcionais](#unique_6) [página ] 4 | Os dados da empresa podem existir para cada ID da empresa da sua estrutura empresarial para o qual é utilizado o registro mestre da conta do Razão e da classe de custo. | Empresa:____________Plano de contas____________Área de contabilidade de custos____________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre de cliente podem fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre de cliente.

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Plano de contas | Na IU da conta do Razão, você encontra a entrada na ficha Geral, na seção Controle. | Obrigatório |  |
| Conta do Razão | Na IU da conta do razão, você encontra a entrada na tela Copiar conta. | Obrigatório |  |
| Descrição | Na IU da conta do razão, você encontra a entrada na tela Copiar conta. | Obrigatório |  |
| Tipo de conta | Na IU da conta do Razão, você encontra a entrada na ficha Geral, na seção Controle. | Obrigatório |  |
| Grupo de contas | Na IU da conta do Razão, você encontra a entrada na ficha Geral, na seção Controle. | Obrigatório |  |
| Área funcional | Na IU da conta do Razão, você encontra a entrada na ficha Geral, na seção Controle. | Opcional | Utilizar para contas de resultados. |
| Texto descritivo da conta do Razão | Na IU da conta do Razão, você encontra a entrada na ficha Geral, na seção Descrição. | Opcional |  |
| Campo de seleção da empresa | Na IU da conta do Razão, você encontra a entrada na ficha Geral, na seção Definição em empresa. | Obrigatório | Atribuir a uma ou várias empresas. |
| Bloqueado para criação | Na IU da conta do Razão, você encontra a entrada na ficha Geral, na seção Administração. | Opcional |  |
| Bloqueado para lançamento | Na IU da conta do Razão, você encontra a entrada na ficha Geral, na seção Administração. | Opcional |  |
| Bloqueado para planejamento | Na IU da conta do Razão, você encontra a entrada na ficha Geral, na seção Administração. | Opcional |  |
| Marcado para eliminação | Na IU da conta do Razão, você encontra a entrada na ficha Geral, na seção Administração. | Opcional |  |
| Moeda da conta | Depois de criar uma nova conta do Razão, você encontra os detalhes da empresa na seção Dados de controle > Controle de contas. |  |  |
| Somente saldo em moeda interna | Depois de criar uma nova conta do Razão, você encontra os detalhes da empresa na seção Dados de controle > Controle de contas. | Opcional |  |
| Categoria de imposto | Depois de criar uma nova conta do Razão, você encontra os detalhes da empresa na seção Dados de controle > Controle de contas. | Opcional |  |
| Permitido lançamento sem imposto | Depois de criar uma nova conta do Razão, você encontra os detalhes da empresa na seção Dados de controle > Controle de contas. | Opcional |  |
| Número da conta alternativa | Depois de criar uma nova conta do Razão, você encontra os detalhes da empresa na seção Dados de controle > Controle de contas. | Opcional |  |
| Chave de ordenação | Depois de criar uma nova conta do Razão, você encontra os detalhes da empresa na seção Dados de controle > Gerenciamento de contas. | Opcional |  |
| Área de contabilidade de custos | Depois de criar uma nova conta do Razão, você encontra os detalhes da empresa na seção Dados de controle > Configurações de contabilidade na ACC. | Obrigatório | Opcional para o tipo de conta Conta do balanço |
| Categoria de classe de custo | Depois de criar uma nova conta do Razão, você encontra os detalhes da empresa na seção Dados de controle > Configurações de contabilidade na ACC. | Obrigatório | Opcional para o tipo de conta Conta do balanço |
| Registrar quantidade | Depois de criar uma nova conta do Razão, você encontra os detalhes da empresa na seção Dados de controle > Configurações de contabilidade na ACC. | Opcional |  |
| Grupo de status de campo | Depois de criar uma nova conta do Razão, você encontra os detalhes da empresa na seção Criar/banco/juros > Controle da criação do documento. | Opcional |  |
| Só lançar automaticamente | Depois de criar uma nova conta do Razão, você encontra os detalhes da empresa na seção Criar/banco/juros > Controle da criação do documento. | Opcional |  |
| Suplemento automático Lançamentos | Depois de criar uma nova conta do Razão, você encontra os detalhes da empresa na seção Criar/banco/juros > Controle da criação do documento. | Opcional |  |
| Nível de planejamento | Depois de criar uma nova conta do Razão, você encontra os detalhes da empresa na seção Criar/banco/juros > Dados bancários/financeiros. | Opcional |  |
| Relevante para fluxo de caixa | Depois de criar uma nova conta do Razão, você encontra os detalhes da empresa na seção Criar/banco/juros > Dados bancários/financeiros. | Opcional |  |
| Bloqueado para lançamento | Depois de criar uma nova conta do Razão, você encontra os detalhes da empresa na Administração. | Opcional |  |
| Marcado para eliminação | Depois de criar uma nova conta do Razão, você encontra os detalhes da empresa na Administração. | Opcional |  |
| Texto de tradução | Na IU da conta do Razão, você encontra a entrada na ficha Tradução, na seção Código de idioma. | Opcional | Traduzir descrições para os idiomas necessários. |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um registro de dados mestre de cliente:

Tipo de conta

- Contas do balanço
- Despesa ou rendimento não-operacional
- Custos primários ou receitas
- Custos secundários

Grupos de contas

- Conta de reconciliação pronta para entrada
- Contas do imobilizado
- Contas de demonstração de resultados
- Contas de recursos líquidos
- Contas de administração de materiais
- Contas do Razão (gerais)

## Tabela de síntese

Este item de escopo consiste em várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar conta do Razão](#unique_9) [página ] 8 | Especialista de configuração - configuração de processo empresarial | Administrar sua solução(F1241) |  |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar conta do Razão

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Quando se cria novas contas do Razão, é aconselhável usar um intervalo de números existente como uma referência para elas.

Procedimento

Dependendo de seu ambiente de configuração para o SAP S/4HANA Cloud Public Edition, escolha uma das seguintes opções:

Configurar sua solução:

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista de configuração - configuração de processo empresarial. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar sua solução(F1241). |  |  |
| 3 | Configuração de acesso | Abra Configurar sua solução. | A tela Configurar sua solução: Fase de realização é exibida. |  |
| 4 | Configuração de acesso | Efetue as seguintes entradas:Área de aplicação: finançasÁrea de subaplicação: Razão |  |  |
| 5 | Abrir | Selecione a seta à direita da coluna com o item Plano de contas. |  |  |
| 6 | Selecionar etapa de configuração | Para a etapa Administrar dados mestre de contas do Razão, selecione Configurar. |  |  |
| 7 | Procurar sua conta | Efetue as seguintes entradas e clique em Ir:Visão: Visão do plano de contasPlano de contas: YCOA | O sistema exibe uma lista de contas do Razão correspondentes. |  |
| 8 | Selecionar conta do Razão | Selecione a conta do Razão a partir dos resultados da pesquisa.Nota Clique no link de número da conta azul. | A tela Dados mestre da conta do Razão é exibida. |  |
| 9 | Copiar conta | Selecione Copiar. | A tela Cópia de <número da conta do Razão> é exibida. |  |
| 10 | Criar conta | Efetue as seguintes entradas e clique em OK:Número da conta: <número da conta>Descrição no idioma de atualização (EN): <descrição>Nº conta do grupo: <número da conta>Nota Este campo só estará visível se Consolidação estiver dentro do escopo. | Os dados inseridos na tela Dados mestre da conta do Razão são exibidos. |  |
| 11 | Adicionar descrição | Na seção Informações básicas, efetue as seguintes entradas:Plano de contas: YCOATexto descritivo conta do Razão:<descrição> |  |  |
| 12 | Atribuir empresa | Na seção Atribuição de empresa, selecione uma Empresa a ser atribuída à conta. |  |  |
| 13 | Adicionar traduções | Na seção Tradução, insira os textos breve e descritivo para todos os idiomas necessários. |  |  |
| 14 | Salvar os dados | Clique em Salvar. | O sistema confirma que a conta foi salva com êxito. |  |

SAP Central Business Configuration:

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login na experiência em projetos no SAP Central Business Configuration. | Abrir Workflow flexível ativo |  |
| 2 | Acessar o app SAP Fiori | Vá para o app Business Processes Configuration e procure a seguinte atividade: Manage G/L Account Master Data.Escolha a partida individual no resultado da pesquisa para ver mais detalhes sobre essa atividade de configuração.Clique no botão Go to Activity para navegar diretamente para o sistema SAP S/4HANA Cloud Public Edition. Efetue login no launchpad do SAP Fiori como Especialista de configuração - configuração de processo empresarial. |  |  |
| 3 | Procurar sua conta | Efetue as seguintes entradas e clique em Ir:Visão: Visão do plano de contasPlano de contas: YCOA | O sistema exibe uma lista de contas do Razão correspondentes. |  |
| 4 | Selecionar conta do Razão | Selecione a conta do Razão a partir dos resultados da pesquisa.Nota Clique no link de número da conta azul. | A tela Dados mestre da conta do Razão é exibida. |  |
| 5 | Copiar conta | Selecione Copiar. | A tela Cópia de <número da conta do Razão> é exibida. |  |
| 6 | Criar conta | Efetue as seguintes entradas e clique em OK:Número da conta: <número da conta>Descrição no idioma de atualização (EN): <descrição>Nº conta do grupo: <número da conta>Nota Este campo só estará visível se Consolidação estiver dentro do escopo. | Os dados inseridos na tela Dados mestre da conta do Razão são exibidos. |  |
| 7 | Adicionar descrição | Na seção Informações básicas, efetue as seguintes entradas:Plano de contas: YCOATexto descritivo conta do Razão:<descrição> |  |  |
| 8 | Atribuir empresa | Na seção Atribuição de empresa, selecione uma Empresa a ser atribuída à conta. |  |  |
| 9 | Adicionar traduções | Na seção Tradução, insira os textos breve e descritivo para todos os idiomas necessários. |  |  |
| 10 | Salvar os dados | Clique em Salvar. | O sistema confirma que a conta foi salva com êxito. |  |

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
- related-to :: [[03-financial-accounting-and-close/g-l-mds-bng-601]]
- related-to :: [[03-financial-accounting-and-close/master-data-script-create-g-l-account-and-cost-element-mds-bng-599]]
- related-to :: [[03-financial-accounting-and-close/mds-bng-603]]
- related-to :: [[03-financial-accounting-and-close/sachkonto-und-kostenart-anlegen-sds-bng-598]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 19,016 chars in the whole document
