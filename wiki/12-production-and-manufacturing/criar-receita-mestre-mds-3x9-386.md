---
id: 12-production-and-manufacturing/criar-receita-mestre-mds-3x9-386
title: Criar receita mestre - MDS (3X9) (3X9_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP S/4HANA Cloud 2608 master data script (3X9) for creating a master recipe for process manufacturing, with phases, production version and component assignment."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/process-resources-and-master-recipes]
aliases: [3X9_S4CLD2608_Master_Data_PT_XX]
keywords: [Process Manufacturing Resources and Master Recipes, master recipe, process manufacturing, production operations, production version, component assignment, change management, task list usage, business roles, master data scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X9_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-386
topic: 12-production-and-manufacturing/process-resources-and-master-recipes
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar receita mestre - MDS (3X9) (3X9_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X9_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Process Manufacturing Resources and Master Recipes** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar receita mestre – MDS (3X9) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893750)

[2 Pré-requisitos 3](#_Toc233893751)

[2.1 Acesso ao sistema 3](#_Toc233893752)

[2.2 Funções 3](#_Toc233893753)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893754)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893755)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233893756)

[2.5.1 Utilização 4](#_Toc233893757)

[3 Tabela de síntese 6](#_Toc233893758)

[4 Procedimentos de teste 7](#_Toc233893759)

[4.1 Criar receita mestre 7](#_Toc233893760)

[5 Anexo 10](#_Toc233893761)

[5.1 Modificação da receita mestre com procedimento de administração de alterações 10](#_Toc233893762)

## Objetivo

Você pode usar a receita mestre para descrever um processo específico da empresa em setores do processo sem relação a uma ordem específica.

Receitas mestre são utilizadas principalmente para o planejamento da produção de produtos. No entanto, você também pode utilizá-las para descrever a limpeza ou a conversão de uma linha de produção.

Receitas mestre são utilizadas como referência para ordens do processo e como a base para o cálculo de custos do produto.

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
| Engenharia de produção - produção por processos | SAP_BR_PRODN_ENG_PROC | Engenharia de produção - produção por processos | SAP_BR_PRODN_ENG_PROC |  |

### Unidades organizacionais necessárias

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser utilizada |
| --- | --- | --- | --- | --- |
| Todos os dados | Centro |  | Todos os dados de uma receita mestre dependem do centro. | Centro:__________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestrede receita podem fazer referência a outros dados mestre. A tabela a seguir oferece uma síntese de objetos de dados mestre opcionais e obrigatórios a serem utilizados em uma receita mestre.

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Material |  | Obrigatório | Conclua o seguinte script de teste como pré-requisito antes de executar as etapas do processo:Criar mestre de produtos do tipo "Matéria-prima" – MDSCriar mestre de produtos do tipo "Produto semiacabado" – MDSCriar mestre de produtos do tipo "Produto acabado" – MDS |
| Recurso | Na tela Criar receita mestre: Síntese de operações, selecione um centro de trabalho para uma operação interna | Obrigatório, (opcional) | O centro de trabalho não é um campo de entrada obrigatório para uma operação externa.Se for necessário, execute o script de teste Criar recurso – MDS. |
| Lista técnica |  | Opcional | Execute o script de teste Criar lista técnica de materiais para produção e vendas – MDS. |
| Registro info para compras |  | (Obrigatório) | Para uma operação externa, você pode utilizar um registro info de compras para capturar todos os dados relevantes de fornecimento |
| Grupo de materiais |  |  |  |
| Classe de custo |  |  |  |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar uma receita mestre.

#### Utilização

| Chave de utilização da lista de tarefas | Descrição |
| --- | --- |
| 1 | Produção |
| 2 | Engenharia/design |
| 3 | Universal |

## Tabela de síntese

Este item de escopo consiste da etapa de processo listada na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação | Resultados previstos |
| --- | --- | --- | --- |
| [Criar receita mestre](#unique_10) [página ] 7 | Engenharia de produção - produção por processos | Gerenciar receitas mestre(F5426) |  |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar receita mestre

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Engenharia de produção - produção por processos. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Gerenciar receitas mestre(F5426). |  |  |
| 3 | Selecione Criar | Selecione Criar. | Criar receita mestre: 1ª tela é exibida. |  |
| 4 | Configurar 1ª tela em Criar receita mestre | Em Criar receita mestre: 1ª tela, insira os seguintes dados.Material: <Número do material acabado/semiacabado>Centro: <Nº de seu centro>Perfil: <YPI1>Pressione Enter. | A tela Criar receita mestre: detalhes do cabeçalho é exibida. |  |
| 5 | Configurar subguia de cabeçalho em Criar receita mestre | Na tela Criar receita mestre: Receita, insira os seguintes dados na subguia Cabeçalho da receita:Utilização: <1 para produção>Status: <4 liberado geral>Grupo de planejamento: <1>Pressione Enter. |  |  |
| 6 | Adicionar uma operação | Insira os seguintes dados na subguia Operações:Recurso: <Recurso>Chave de controle: <YBP4>Descrição: <insira uma descrição para a operação>Pressione Enter. |  |  |
| 7 | Adicionar uma fase | Comece em uma nova linha.Insira os seguintes dados na subguia Operações:Indicador da fase: <X>Operação superior: <ID da operação, por exemplo:0010>Recurso: <Recurso>Chave de controle: <YBP4>Descrição: <insira uma descrição para a operação>Clique duas vezes na fase que você criou. | A tela Criar receita mestre: Operação é exibida. |  |
| 8 | Configurar a seção de valor padrão da fase | Insira os seguintes dados na subguia Valores padrão e retorne.Máquina: <tempo da operação da máquina>Trabalho: <tempo de trabalho> |  |  |
| 9 | Adicionar mais operações ou fase | Repita as etapas anteriores para cada operação ou fase.Se o usuário pretende atribuir componentes neste momento, você deve executar as seguintes etapas, caso contrário você pode salvar as suas entradas e finalizar. |  |  |
| 10 | Selecionar Material | Na visão Criar receita mestre: Receita, selecione a subguia Materiais. | A caixa de diálogo Inserir versão de produção é exibida. |  |
| 11 | Inserir versão de produção | Na caixa de diálogo Inserir versão de produção, faça as seguintes entradas:Versão de produção: <nova versão de produção>Dados da lista técnica – lista técnica alternativa: <sua LisTecAlt>Dados da lista técnica – Uso da lista técnica: <uso>Selecione Verificar. Verifique as informações relevantes, certifique-se de que não haja erros e, em seguida, escolha Fechar. | O indicador de verificação exibe em verde a seção Dados da lista técnica. |  |
| 12 | Fechar tela e adotar modificações | Na caixa de diálogo Inserir versão de produção, selecione Fechar tela e adotar as modificações. | A lista de materiais é exibida em Atribuições componentes mat. na subguia Materiais. |  |
| 13 | Criar uma nova atribuição | Selecione Nova atribuição. | É exibida a caixa de diálogo Nova atribuição. |  |
| 14 | Atribuir à lista de operação | Selecione a lista de oper. |  |  |
| 15 | Selecionar operação | Selecione uma operação e pressione Enter. |  |  |
| 16 | Atribuir outros componentes | Repita as etapas anteriores para outros componentes. |  |  |
| 17 | Salvar os dados | Salve suas entradas. | A receita mestre é criada. |  |
| 18 | Imprimir (opcional) | No app Gerenciar receitas mestre(F5426), procure e escolha a receita mestre criada.Na tela Exibir receita mestre: receita, escolha Menu > Extras > Imprimir receita mestre. | Um arquivo PDF contendo detalhes da receita mestre é baixado. |  |

## Anexo

### Modificação da receita mestre com procedimento de administração de alterações

Se você usar uma receita mestre que necessite de aprovação, consulte o script de teste do item de escopo 5QC – Controle modifs.produto c/registros modificações – Indústrias processo, e siga o capítulo Modificar receita mestre para qualquer alteração.

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
- related-to :: [[12-production-and-manufacturing/create-master-recipe-mds-3x9-383]]
- related-to :: [[12-production-and-manufacturing/mds-3x9-385]]
- related-to :: [[12-production-and-manufacturing/mds-3x9-387]]
- related-to :: [[12-production-and-manufacturing/script-de-datos-maestros-creacion-de-receta-de-planificacion-mds-3x9-3]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X9_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 12,781 chars in the whole document
