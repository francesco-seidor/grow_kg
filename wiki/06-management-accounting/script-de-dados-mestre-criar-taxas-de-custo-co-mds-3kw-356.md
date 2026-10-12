---
id: 06-management-accounting/script-de-dados-mestre-criar-taxas-de-custo-co-mds-3kw-356
title: Script de dados mestre - Criar taxas de custo CO – MDS (3KW) (3KW_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP S/4HANA Cloud Public Edition master data test script (3KW) for creating service, planned and actual cost rates in Controlling, plus the display report."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-rates]
aliases: [3KW_S4CLD2608_Master_Data_PT_XX]
keywords: ["CO Cost Rates (Service, Plan and Actual)", cost rates, service cost rates, planned cost rates, actual cost rates, cost rate display, intercompany offsetting accounts, intercompany margin accounts, business roles, master data scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-356
topic: 06-management-accounting/cost-rates
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar taxas de custo CO – MDS (3KW) (3KW_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **CO Cost Rates (Service, Plan and Actual)** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar taxas de custo CO – MDS (3KW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893682)

[2 Pré-requisitos 3](#_Toc233893683)

[2.1 Acesso ao sistema 3](#_Toc233893684)

[2.2 Funções 3](#_Toc233893685)

[2.3 Etapas preliminares 4](#_Toc233893686)

[2.3.1 Opcional: Atualizar contas de compensação interempresariais (somente para lançamentos interempresariais) 4](#_Toc233893687)

[2.3.2 Opcional: Atualizar contas de margem (somente para lançamentos interempresariais com taxas interempresariais) 5](#_Toc233893688)

[3 Tabela de síntese 7](#_Toc233893689)

[4 Procedimentos de teste 8](#_Toc233893690)

[4.1 Administrar taxas de custo - Serviços 8](#_Toc233893691)

[4.2 Administrar taxas de custo - planejadas 11](#_Toc233893692)

[4.3 Administrar taxas de custo - Reais 12](#_Toc233893693)

[5 Análise 14](#_Toc233893694)

[5.1 Exibir taxas de custos 14](#_Toc233893695)

## Objetivo

Vários apps estão disponíveis para a atualização de taxas de custos (preços de atividade). Cada app tem um objetivo diferente, dependendo de como as taxas podem ser definidas e quais objetos podem receber alocações de atividade.

| App | Itens de escopo afetados | Comentários |
| --- | --- | --- |
| Administrar taxas de custo - Serviços(F3161) | Registro de tempos (1Q4)Contabilidade de custos indiretos (J54)Registro de tempos – Serviços baseados em projetos (J12)Administração e monitorização de ordens de serviço (3D2) | Registro de tempos |
| Administrar taxas de custo - planejadas(F3162) | Cálculo de custos padrão (BEG)Encerramento do período – Centro (BEI)Encerramento do período – Ordens de manutenção (BF7) | Confirmações de produção, planejamento da ordem e confirmações reais |
| Administrar taxas de custo - Real(F3422) | Cálculo de custo real (33Q) | Utilizado para inserir taxas de custos reais para atividades de centros de custo.As taxas de custos reais só são necessárias se um cliente quiser utilizar o cálculo de custos real. |

Este documento fornece um procedimento detalhado para testar o item de escopo após a ativação da solução, refletindo o escopo predefinido da solução. Cada etapa do processo, relatório ou item está coberto em uma seção própria que fornece as interações do sistema (etapas de teste) em uma visão de tabela. As etapas que não estão no escopo do processo, mas que são necessárias para teste, estão marcadas de modo correspondente. É necessário adicionar etapas específicas do projeto.

|  |
| --- |
| Nota Os valores deste script de teste (notação decimal, formatos de data etc.) são apresentados na notação padrão dos EUA. Se o sistema de teste estiver configurado para usar uma notação diferente, insira os valores apropriados. |

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

### Etapas preliminares

#### Opcional: Atualizar contas de compensação interempresariais (somente para lançamentos interempresariais)

Utilização

Esta atividade permite que você crie e atualize contas de compensação para lançamentos interempresariais. As contas de compensação interempresariais são originadas da conta do Razão da atividade.

Procedimento

Dependendo de seu ambiente de configuração para o SAP S/4HANA Cloud Public Edition, escolha uma das seguintes opções:

Configurar sua solução:

1. Efetue login no launchpad do SAP Fiori como Especialista de configuração - configuração de processo empresarial.
2. Abra Administrar sua solução(F1241).
3. Se necessário, selecione Definir versão local para modificar o país.
4. Clique em Configurar sua solução.
5. Na seção Etapas de configuração, coluna Nome, para a linha Determinação automática de contas (100297), selecione Configurar.
6. Continue com o procedimento na tabela a seguir.

SAP Central Business Configuration:

1. Efetue login na experiência em projetos no SAP Central Business Configuration.
2. Vá para o app Business Processes Configuration. Para localizar a atividade na visão de árvore, procure a atividade Automatic Account Determination.
3. Escolha Open Documentation para o item encontrado para ver mais detalhes sobre esta atividade de configuração.
4. Selecione o link para navegar diretamente para o sistema SAP S/4HANA Cloud Public Edition. Efetue login no launchpad do SAP Fiori como Especialista de configuração - configuração de processo empresarial.
5. Continue com o procedimento na tabela a seguir.

| Nº da etapa | Nome da etapa | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Selecionar uma área | Efetue as seguintes entradas para a linha exibida e clique em Etapa 2:Área: ControllingSubárea: Contabilidade do centro de custosProcessar: Atribuir contas de compensação interempresariais para lançamentos reais |  |  |
| 2 | Selecionar parâmetros | Efetue as seguintes entradas e clique em Etapa 3:Plano de contas: YCOA |  |  |
| 3 | Atualizar determinação de contas | Adicione uma conta relevante para a compensação interempresarial.Nota O conteúdo padrão é fornecido com a conta do Razão de compensação 68888800 - conta de compensação interempresarial - viagem e 99999900 - conta de compensação interempresarial - consultoria. Você pode usar esta referência para criar suas próprias contas, se necessário (com o tipo de conta do Razão N- despesa ou rendimento não operacional). |  |  |

#### Opcional: Atualizar contas de margem (somente para lançamentos interempresariais com taxas interempresariais)

Utilização

Esta atividade permite que você crie e atualize contas de margem para lançamentos interempresariais. Esta etapa é necessária se você atualizar e lançar taxas interempresariais. As contas de compensação do Razão de margem são derivadas com base na conta do Razão de alocação de atividade.

Procedimento

Dependendo de seu ambiente de configuração para o SAP S/4HANA Cloud Public Edition, escolha uma das seguintes opções:

Configurar sua solução:

1. Efetue login no launchpad do SAP Fiori como Especialista de configuração - configuração de processo empresarial.
2. Abra Administrar sua solução(F1241).
3. Se necessário, selecione Definir versão local para modificar o país.
4. Selecione Configurar sua solução.
5. Na seção Etapas de configuração, coluna Nome, para a linha Determinação automática de contas (100297), selecione Configurar.
6. Continue com o procedimento na tabela a seguir.

SAP Central Business Configuration:

1. Efetue login na experiência em projetos no SAP Central Business Configuration.
2. Para localizar a atividade na visão de árvore, procure a atividade Automatic Account Determination.
3. Selecione Open Documentation para o item encontrado para ver mais detalhes sobre esta atividade de configuração.
4. Selecione o link para navegar diretamente para o sistema SAP S/4HANA Cloud Public Edition. Efetue login no launchpad do SAP Fiori como Especialista de configuração - configuração de processo empresarial.
5. Continue com o procedimento na tabela a seguir.

| Nº da etapa | Nome da etapa | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Selecionar uma área | Efetue as seguintes entradas para a linha exibida e clique em Etapa 2:Área: ControllingSubárea: Contabilidade do centro de custosProcessar: Atribuir contas de margem interempresariais |  |  |
| 2 | Selecionar parâmetros | Efetue as seguintes entradas e clique em Etapa 3:Plano de contas: YCOA |  |  |
| 3 | Atualizar determinação de contas | Adicione uma conta relevante para a margem interempresarial para alocação de atividade do Razão.Nota O conteúdo padrão é fornecido com a conta de margem 97777700 - margem interempresarial. Se necessário, você pode usar isso como referência para criar sua própria conta de margem (com a conta do Razão P - custo primário e receita). |  |  |

## Tabela de síntese

Este item de escopo é composto por várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Administrar taxas de custo - Serviços](#unique_8) [página ] 8 | Controlador - custos indiretos | Administrar taxas de custo - Serviços(F3161) | As taxas de custos são atualizadas para os serviços. |
| [Administrar taxas de custo - planejadas](#unique_9) [página ] 11 | Controlador - custos indiretos | Administrar taxas de custo - planejadas(F3162) | As taxas de custos são atualizadas para o plano. |
| [Administrar taxas de custo - Reais](#unique_10) [página ] 12 | Controlador - custos indiretos | Administrar taxas de custo - Real(F3422) | As taxas de custos são atualizadas para os dados reais. |

## Procedimentos de teste

### Administrar taxas de custo - Serviços

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Contexto

Utilize este app para inserir taxas de custo de acordo com vários critérios. As taxas de custos são utilizadas em alocações de atividade para os seguintes objetos de receptor via registro de tempos ou alocação direta de atividade:

- Centros de custo
- Elementos PEP de projeto
- Ordens de serviço

Este app permite a você definir as taxas de custo para os níveis de custo de serviços e empregados específicos, por isso é útil para provedores de serviços profissionais. No entanto, este pode também ser utilizado por empresas de produção se houver uma necessidade para taxas de custo para os níveis de custo de serviços e empregados.

Os seguintes campos estão disponíveis para a atualização de preço:

- Empresa (fornecimento) sempre preenchida. Por isso, não é relevante para sequência de acesso
- Empresa a ser faturada (recebimento)
- Preço ICO (código)
- Centro de custo (fornecimento)
- Tipo de atividade (fornecimento)
- Nível de custo de serviço (fornecimento)
- Número pessoal (fornecimento)
- Work item (novo) (recebimento)
- Elemento PEP (recebimento)

A sequência da lista exibe as chaves com a prioridade mais alta no fim da lista (elemento PEP).

As seguintes regras são verificadas na atualização da tabela de preços.

- Empresa emissora é necessária
- Um ou vários dos campos seguintes devem ser preenchidos: Tipo de atividade, Nível de custo de serviço ou Número pessoal (apenas o centro de custo não é suportado)
- Os campos Número pessoal e Centro de custo se excluem reciprocamente como campos-chave para um preço. A pessoa tem uma determinada taxa de custos ou a taxa de câmbio média do centro de custo é válida.
- Os campos Nº pessoal e Nível de custo de serviços se excluem reciprocamente como campos-chave para um preço. A pessoa tem uma determinada taxa de custos ou a taxa de câmbio média do nível de custo de serviço é válida.
- O nível de custo de serviço e centro de custo são uma combinação de chaves permitida
- As categorias de centro de custo, como definidas no tipo de atividade, controlam as combinações permitidas de centro de custo e tipo de atividade.
- Se uma taxa de custo intraempresarial for inserida, a empresa receptora deve ser deixada em branco
- Taxas de custo específicas de PEP podem ser utilizadas para alocações de atividade intraempresariais e interempresariais. Se uma empresa receptora e um elemento PEP tiverem sido inseridos, o sistema verifica se o elemento PEP está atribuído à empresa receptora (o sistema não deriva automaticamente a empresa receptora do elemento PEP, e isso pode levar a problemas com taxas de custo migradas).
- Verifique e defina o código ICO
    - Se a empresa receptora estiver em branco, utilize o código ICO de entrada do usuário
    - Se a empresa receptora não for igual à empresa emissora, defina o código ICO como verdadeiro
    - Caso contrário, defina o código ICO como falso

| Centro de custo | Tipo de atividade | Nível de custo de serviço | Número pessoal (empregado) | Work item (recebimento) | PEP+Elemento (recebimento) | Empresa a ser faturada (recebimento) | Comentário |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Emissor | Destinatário |  |  |  |  |  |  |
|  | X |  |  |  |  |  | Pelo menos um campo (tipo de atividade, nível de custo de serviços, número pessoal) tem de ser preenchido |
|  |  | X |  |  |  |  |  |
| NUNCA |  | NUNCA | X |  |  |  |  |
| NUNCA | X | NUNCA | X |  |  |  | Nº pessoal s/CC, sem nível de custo de serviços |
| X | X |  |  |  |  |  | CC + tipo atividade |
| X |  | X |  |  |  |  | CC + nível de custo de serviço |
| X | X | X |  |  |  |  | CC + tipo atividade + nível de custo de serviço |
|  | X | X |  |  |  |  | tipo atividade + nível de custo de serviço |
|  | X |  |  | (X) | (X) |  | PEP ou work item pode ser preenchido |
|  |  | X |  | (X) | (X) |  |  |
| NUNCA |  | NUNCA | X | (X) | (X) |  |  |
| NUNCA | X | NUNCA | X | (X) | (X) |  |  |
| X | X |  |  | (X) | (X) |  |  |
| X |  | X |  | (X) | (X) |  |  |
| X | X | X |  | (X) | (X) |  |  |
|  | X | X |  | (X) | (X) |  |  |
|  | X |  |  | (X) | (X) | X | Taxas ICO |
|  |  | X |  | (X) | (X) | X |  |
| NUNCA |  | NUNCA | X | (X) | (X) | X |  |
| NUNCA | X | NUNCA | X | (X) | (X) | X |  |
| X | X |  |  | (X) | (X) | X |  |
| X |  | X |  | (X) | (X) | X |  |
| X | X | X |  | (X) | (X) | X |  |
|  | X | X |  | (X) | (X) | X |  |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovado/Reprovado/Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue o logon no launchpad do SAP Fiori como Controlador - custos indiretos. |  |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar taxas de custo - Serviços(F3161). | A tela Administrar taxas de custo - Serviços é exibida. |  |
| 3 | Empresa | Efetue a seguinte entrada e selecione Adicionar:Empresa: <empresa> |  |  |
| 4 | Atualizar taxas de custos de serviços | Efetue as entradas a seguir e selecione Gravar.Empresa receptora: <deixar em branco>Nota Este campo só deve ser usado no caso de taxas de custo interempresariais, caso contrário deixe em branco.Centro de custo: <centro de custo>Tipo de atividade: <tipo de atividade>Elemento PEP: <esse é um campo opcional>Do exercício: <ano corrente>Do período: <período atual>Taxa: 100Nota Esta taxa é utilizada para o lançamento em todos os ledgers.Moeda: <moeda>Por: 1Unidade de atividade: H | Taxas de custos são criadas. |  |

### Administrar taxas de custo - planejadas

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Contexto

Esta atividade é utilizada para planejar as taxas de custo para atividades de centros de custo em um ambiente de produção. As taxas são utilizadas em:

- Alocações de atividade para ordens de produção e ordens de manutenção
- Custos de materiais

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovado/Reprovado/Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar logon | Efetue o logon no launchpad do SAP Fiori como Controlador - custos indiretos. |  |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar taxas de custo - planejadas(F3162). | A tela Administrar taxas de custos – Planejadas é exibida. |  |
| 3 | Adicionar | Selecione Adicionar. |  |  |
| 4 | Atualizar taxas de custos planejadas | Efetue as entradas a seguir e selecione Gravar.Centro de custo: <centro de custo>Tipo de atividade: <tipo de atividade>Do exercício: <ano corrente>Do período: <período atual>Moeda: <moeda>Montante fixo: <montante>:Taxa variável: <montante>:Nota Esta taxa é utilizada para o lançamento em todos os ledgers. | As taxas de custos são atualizadas para o plano. |  |

### Administrar taxas de custo - Reais

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Contexto

Esta atividade é usada para inserir taxas de custos reais para atividades de centros de custo usadas no cálculo de custos reais. As taxas de custos reais podem ser atualizadas por ledger.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovado/Reprovado/Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar logon | Efetue o logon no launchpad do SAP Fiori como Controlador - custos indiretos. |  |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar taxas de custo - Real(F3422). | A tela Administrar taxas de custos - Reais é exibida. |  |
| 3 | Adicionar | Selecione Adicionar. |  |  |
| 4 | Atualizar taxas de custos reais | Efetue as entradas a seguir e selecione Gravar.Centro de custo: <centro de custo>Tipo de atividade: <tipo de atividade>Ledger: <por exemplo, 0L ou seu ledger principal>NotaSe você usar o cálculo da taxa de custos reais, o sistema calcula taxas de custos reais por ledger. Se você quiser ver ou corrigir automaticamente as taxas de custo calculadas, deve inserir um ledger. As taxas de custos reais com campo de ledger em branco são utilizadas para lançamentos em todos os ledgers. Se existirem taxas de custos reais específicas de ledger, o sistema utiliza as taxas específicas de ledger.Para visualizar a coluna do ledger, adapte as configurações na lista de taxas de custo e selecione o ledger.Do exercício: <ano corrente>Do período: <período atual>Moeda: <moeda>Montante fixo: <montante>:Taxa variável: <montante>:Nota Esta taxa é utilizada para o lançamento em todos os ledgers. | As taxas de custos são atualizadas para os dados reais. |  |

## Análise

### Exibir taxas de custos

Objetivo

Este relatório permite que você selecione e visualize os vários tipos de taxa de custo.

Pré-requisito

As taxas de custo já devem existir.

Procedimento

| Número da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Controlador - custos indiretos. |  |  |
| 2 | Acessar o app SAP Fiori | Abra Exibir taxas de custos(F5150). | A tela Exibir taxas de custos é exibida. |  |
| 3 | Inserir critérios de seleção | Efetue as seguintes entradas e clique em Ir:Ledger: <mantenha este campo em branco>Nota Se você deixar o campo de seleção em branco, serão exibidas as taxas iguais e válidas para todos os ledgers (por exemplo, tarifa planejada). A indicação de um ledger na seleção limita a exibição da taxa de custo às taxas atualizadas somente para ledgers específicos selecionados e aplicável somente a taxas reais.Centro de custo: <por exemplo, 10101101>Tipo de atividade: <por exemplo, 11>Período do exercício fiscal desde: <período atual>Período do exercício fiscal até: <período atual> |  |  |

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
- related-to :: [[06-management-accounting/co-mds-3kw-355]]
- related-to :: [[06-management-accounting/co-mds-3kw-357]]
- related-to :: [[06-management-accounting/crear-tasas-de-coste-co-mds-3kw-354]]
- related-to :: [[06-management-accounting/master-data-script-create-co-cost-rates-mds-3kw-353]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 23,845 chars in the whole document
