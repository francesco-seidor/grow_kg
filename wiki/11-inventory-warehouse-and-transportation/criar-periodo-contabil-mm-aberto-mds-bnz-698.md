---
id: 11-inventory-warehouse-and-transportation/criar-periodo-contabil-mm-aberto-mds-bnz-698
title: Criar período contábil MM aberto – MDS (BNZ) (BNZ_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP master data script (BNZ, 2608): close the MM period and open a new posting period with Encerrar períodos (MMPV) as Especialista em dados mestre - Dados do produto."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/mm-posting-periods]
aliases: [BNZ_S4CLD2608_Master_Data_PT_XX]
keywords: [MM Posting Periods, mm posting period, period closing, material valuation, business roles, fiori launchpad access, master data scripts, test procedures, BNZ]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-698
topic: 11-inventory-warehouse-and-transportation/mm-posting-periods
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar período contábil MM aberto – MDS (BNZ) (BNZ_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **MM Posting Periods** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar período contábil MM aberto – MDS (BNZ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894122)

[2 Pré-requisitos 3](#_Toc233894123)

[2.1 Acesso ao sistema 3](#_Toc233894124)

[2.2 Funções 3](#_Toc233894125)

[3 Tabela de síntese 4](#_Toc233894126)

[4 Procedimentos de teste 5](#_Toc233894127)

[4.1 Fechar período MM e abrir novo período contábil 5](#_Toc233894128)

## Objetivo

A informação do estoque de material e alguns dados de avaliação como o valor do estoque total, o estoque total, a classe de elementos de avaliação, o código de controle de preço e a unidade de preço são mantidos por período contábil financeiro. O período deve ser definido pelo início de cada novo período contábil para assegurar que os valores e o movimento de mercadorias sejam lançados no período correto. Normalmente, apenas o período contábil atual está aberto para lançamento. Todos os outros períodos contábeis estão fechados.

Um lançamento de retorno a um período anterior é somente possível se o código correspondente for definido no registro de controle. O código é definido automaticamente na inicialização e após cada mudança de período. Em alguns casos, porém, poderá ser necessário definir o código manualmente.

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
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Dados mestre - produtos / Governança de produto | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

## Tabela de síntese

Este item de escopo consiste de várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Fechar período MM e abrir novo período contábil](#unique_6) [página ] 5 | Especialista em dados mestre - Dados do produto | Encerrar períodos(MMPV) | O período contábil está atualizado. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Fechar período MM e abrir novo período contábil

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Encerrar períodos(MMPV).Nota Se não conseguir encontrar o bloco Encerrar períodos,na lista de opções no canto superior direito do launchpad do Fiori, selecione Catálogo de blocos. No grupo Dados mestre – Administração, navegue até o bloco Encerrar períodos e adicione-os ao grupo Minha página inicial. | O app é aberto. |  |
| 3 | Inserir dados de seleção | Na tela Diferimento de períodos mestre de material, efetue as seguintes entradas:Da empresa: <sua empresa>Para a empresa: <sua empresa>Período: <período a ser aberto>Exercício fiscal: <exercício corrente>:Verificar e fechar período: selecionadoNota No campo Período, insira dois dígitos para o mês. Por exemplo, janeiro igual a 01, outubro igual a 10, etc.Se você quiser abrir o período atual, insira o mês atual nos períodos seguintes. |  |  |
| 4 | Clicar em Executar | Na tela Diferimento de períodos mestre de material, clique em Executar. |  |  |
| 5 | Verificar resultado | Se um log exibir O período atual (mês/ano) do registro de controle é <período/ano que você inseriu>", você pode parar aqui.Nota Se o período contábil ainda estiver no passado, repita as etapas acima, período a período, até alcançar o período (atual) correto. Por exemplo, se o período atual exibido for 04 2014 e você quiser abrir o período 12 2015, não poderá fazer isso diretamente. Em vez disso, você precisa abrir o período seguinte 05 2014 e depois 06 2014, etc. até alcançar o período atual. Se você quiser fechar períodos de inventário do ano passado, pode haver uma mensagem do sistema exibida na Etapa 3 indicando que você está abrindo/fechando um período do ano passado. Você deve confirmar essa mensagem do sistema. | O período contábil está atualizado. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/crear-nuevo-periodo-contable-mm-abierto-mds-bnz-696]]
- related-to :: [[11-inventory-warehouse-and-transportation/create-new-open-mm-posting-period-mds-bnz-695]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-bnz-699]]
- related-to :: [[11-inventory-warehouse-and-transportation/mm-mds-bnz-697]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 9,017 chars in the whole document
