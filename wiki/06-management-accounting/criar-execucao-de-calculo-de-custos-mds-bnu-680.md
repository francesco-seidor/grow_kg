---
id: 06-management-accounting/criar-execucao-de-calculo-de-custos-mds-bnu-680
title: Criar execução de cálculo de custos – MDS (BNU) (BNU_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese master data script (BNU) for creating and executing a product cost estimate run in SAP S/4HANA Cloud Public Edition 2608, with prerequisites and test steps."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/product-costing-and-standard-cost-updates]
aliases: [BNU_S4CLD2608_Master_Data_PT_XX]
keywords: [Product Costing Runs and Standard Cost Updates, cost estimate run, product costing, costing variant, test procedures, business roles, organizational units, master data prerequisites, price update, BNU]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-680
topic: 06-management-accounting/product-costing-and-standard-cost-updates
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar execução de cálculo de custos – MDS (BNU) (BNU_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Product Costing Runs and Standard Cost Updates** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar execução de cálculo de custos – MDS (BNU) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894105)

[2 Pré-requisitos 3](#_Toc233894106)

[2.1 Acesso ao sistema 3](#_Toc233894107)

[2.2 Funções 3](#_Toc233894108)

[2.3 Unidades organizacionais necessárias 3](#_Toc233894109)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233894110)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233894111)

[2.5.1 Variante de cálculo de custos 5](#_Toc233894112)

[3 Tabela de síntese 6](#_Toc233894113)

[4 Procedimentos de teste 7](#_Toc233894114)

[4.1 Criar execução de cálculo de custos 7](#_Toc233894115)

[4.2 Efetuar execução de cálculo de custos 8](#_Toc233894116)

## Objetivo

Este documento contém etapas de processo que precisam ser efetuadas como pré-requisito antes de você poder iniciar o trabalho nos scripts de teste padrão dos cenários de logística selecionados.

Neste documento, você encontra uma descrição de como criar e efetuar uma execução de cálculo de custos do produto para materiais utilizados em sua empresa/em seu centro. O objetivo é planejar custos para materiais sem referência a ordens e definir preços para materiais e outros objetos de contabilidade de custos.

Você pode utilizar o planejamento de custos do produto para analisar os custos dos produtos da sua empresa, como:

- Produtos semiacabados
- Serviços
- Outros bens intangíveis

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
| Empregado da contabilidade de custos - estoque | SAP_BR_INVENTORY_ACCOUNTANT | Contabilidade de estoques | SAP_BR_INVENTORY_ACCOUNTANT |  |

### Unidades organizacionais necessárias

Para criar uma execução de cálculo de custos, você precisa indicar a Área de contabilidade de custos e a Empresa.

|  |
| --- |
| Nota Na coluna Unidade organizacional a ser utilizada, insira seu valor para o segmento de dados relevante para seu ambiente do sistema. Para a empresa: por exemplo,10 = Alemanha ,17 = EUA |

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser utilizada |
| --- | --- | --- | --- | --- |
| Dados do cálculo de custos | Área de contabilidade de custos |  |  | Área de contabilidade de custos:____________ |
|  | Empresa |  |  | Empresa:__________ |
| Seleção | Centro |  |  | Centro:__________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados da lista técnica podem fazer referência a outros dados mestre. A tabela seguinte oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios que devem ser utilizados em uma lista técnica.

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Materiais | Criar cálculo custos > Etapa do processo > Seleção | Obrigatório | Normalmente, você especifica os tipos de material para indicar para que materiais a execução de cálculo de custos deve criar um cálculo de custos do produto. |
| Dados mestre de produção (LT, roteiro, centro de trabalho, etc.). | Em Criar estimativa de custos--> Etapa de processo --> Explosão da estrutura | Opcional (ou) obrigatório | Caso os produtos semiacabados sejam utilizados na execução de cálculo de custos (por exemplo, produtos do tipo de material "ACAB" (produtos acabados) ou "SEMI" (produtos semiacabados), estes produtos têm uma lista técnica que é "explodida" na execução de cálculo de custos.Ao mesmo tempo, o(s) roteiro(s) é(são) selecionado(s). Dados adicionais dos centros de trabalho, centros de custo atribuídos e tipos de atividades utilizadas, juntamente com taxas de custos, são determinados para calcular os dados do cálculo de custos final. |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar uma lista técnica:

#### Variante de cálculo de custos

A variante de cálculo de custos define um link entre a aplicação e o customizing, uma vez que todos os cálculos de custos são executados e gravados com referência a uma variante de cálculo de custos.

| Variante de cálculo de custos | Descrição | Comentário |
| --- | --- | --- |
| PYC1 | Padrão do cálculo de custos | Esta variante de cálculo de custos é utilizada para criar cálculos de custos do produto padrão para os materiais selecionados. Com base no resultado, os dados da avaliação do material serão atualizados. |

## Tabela de síntese

Este item de escopo é composto por várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar execução de cálculo de custos](#unique_10) [página ] 7 | Empregado da contabilidade de custos - estoque | Administrar execuções de cálculo de custos - Custos estimados(F1865) | A ficha de dados do cabeçalho com dados do cálculo de custos é exibida. |
| [Efetuar execução de cálculo de custos](#unique_11) [página ] 8 | Empregado da contabilidade de custos - estoque | Administrar execuções de cálculo de custos - Custos estimados(F1865) |  |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar execução de cálculo de custos

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta atividade você cria um cálculo de custos

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovado/ Reprovado /Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar logon | Efetue o logon no launchpad do SAP Fiori como Empregado da contabilidade de custos - estoque. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar execuções de cálculo de custos - Custos estimados(F1865). | É exibida a visão Administrar execução de cálculo de custos - custos estimados. |  |
| 3 | Criar execução de cálculo de custos | Selecione Criar. | É exibida a visão Criar nova execução de cálculo de custos. |  |
| 4 | Inserir parâmetros para a execução de cálculo de custos | Efetue as seguintes entradas e pressione ENTER.Execução de cálculo de custos: Test1Data da execução de cálculo de custos: <insira a data atual>Descrição: Execução de cálculo de custos teste 1Variante de cálculo de custos: PYC1Versão do cálculo de custos: 1Área de contabilidade de custos: A000Empresa: 1010Data cálc.custos: de: <data atual>Data cálc.custos até: Aceite o valor propostoData da estrutura quantitativa: <data atual>Data de avaliação: <data atual> |  |  |
| 5 | Gravar a execução de cálculo de custos | Selecione Gravar. |  |  |

### Efetuar execução de cálculo de custos

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta atividade você efetua a execução de cálculo de custos. Os materiais configurados não estão incluídos.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovado/ Reprovado /Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar logon | Efetue o logon no launchpad do SAP Fiori como Empregado da contabilidade de custos - estoque. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar execuções de cálculo de custos - Custos estimados(F1865). | É exibida a visão Administrar execução de cálculo de custos - custos estimados. |  |
| 3 | Selecionar execução de cálculo de custos | Procure a execução de cálculo de custos criada na etapa anterior, clique na entrada e em Processar para acessar os detalhes da execução de cálculo de custos. |  |  |
| 4 | Abrir execução de cálculo de custos | Efetue a entrada seguinte:Execução de cálculo de custos: Insira a execução de cálculo de custos criada na etapa anterior e selecione Enter.Expanda a seção Processamento. |  |  |
| 5 | Criar cálculos de custos | Na tabela Processamento, para cada linha, existe um botão Modificar parâmetro na coluna Parâmetros. Selecione o que está na linha de seleção e efetue as seguintes entradas:Tipo de material: SEMI, MATPR, ACABCentro: 1010Anule a seleção de Processamento em background e selecione a opção EXPLO.Grave as suas entradas e selecione Voltar.Selecione Executar, que é exibido na coluna Executar, e o semáforo de status para a linha Seleção fica verde. | A seleção é executada. |  |
| 6 | Criar cálculos de custos | Para a linha Cálculo de custos, selecione o botão Modificar parâmetro. Na Execução de cálculo de custos: Cálculo de custos – Modificar parâmetros, desmarque o código Processamento em background e, em seguida, selecione Gravar.Selecione VoltarSelecione Executar, que é exibido na coluna Executar, e o semáforo de status para a linha Cálculo de custos fica verde. | A execução de cálculo de custos é efetuada. |  |
| 7 | Criar cálculos de custos | Selecione Processar > Resultados do cálculo de custos no menu.Se o semáforo do status para esta linha for vermelho, revise o relatório de níveis de cálculo de custos. Corrija os erros no relatório. Para executar de novo o cálculo de custos (se necessário), repita as etapas para a explosão da estrutura e as linhas de cálculo de custos. | A execução de cálculo de custos é efetuada. |  |
| 8 | Criar cálculos de custos | Na linha Análise, selecione o botão Modificar parâmetro. Selecione SAP&11 para a configuração de parâmetros. Na Execução de cálculo de custos: Análise – Modificar parâmetros, desmarque o código Processamento em background e, em seguida, selecione Gravar.Selecione Voltar.Selecione Executar, que é exibido na coluna Executar. | A execução de cálculo de custos é efetuada. |  |
| 9 | Criar cálculos de custos | Na linha Marcação, selecione o botão Bloquear.Na tela Atualização de preço: Medida organizacional, selecione a empresa: 1010.Na caixa de diálogo que aparece, insira a variante de cálculo de custos de PYC1 e a versão de cálculo de custos de 1 e, depois, pressione Enter. O semáforo do status da linha fica verde.Selecione Voltar.Selecione Modificar parâmetro e desmarque Processamento em background.Selecione Gravar.Selecione Voltar e Executar. | A execução de cálculo de custos é efetuada. |  |
| 10 | Criar cálculos de custos | Em Liberar linha, selecione Modificar parâmetro e desmarque a Execução de teste e o Processamento em background.Selecione Gravar.Selecione Voltar e Executar. | Os preços atuais serão atualizados nos dados mestre de materiais. |  |

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
- related-to :: [[06-management-accounting/crear-ejecucion-del-calculo-del-coste-mds-bnu-678]]
- related-to :: [[06-management-accounting/kalkulationslauf-anlegen-sds-bnu-676]]
- related-to :: [[06-management-accounting/master-data-script-create-costing-run-mds-bnu-677]]
- related-to :: [[06-management-accounting/mds-bnu-679]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 15,514 chars in the whole document
