---
id: 02-business-partner-and-product-master-data/criar-mestre-de-produtos-do-tipo-embalagem-mds-3y1-392
title: "Criar mestre de produtos do tipo \"Embalagem\" – MDS (3Y1) (3Y1_S4CLD2608_Master_Data_PT_XX)"
description: "Portuguese SAP S/4HANA Cloud 2608 master data script (3Y1): create packaging-type product master in Basic, SD and WM views via MM01/MM02/F1602."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-packaging]
aliases: [3Y1_S4CLD2608_Master_Data_PT_XX]
keywords: ["Product Master: Packaging and Returnable Packaging", packaging product master, material master data, sales view data, warehouse management data, business roles, material types, number ranges, industry sector, brazil tax fields]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y1_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-392
topic: 02-business-partner-and-product-master-data/product-master-packaging
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar mestre de produtos do tipo "Embalagem" – MDS (3Y1) (3Y1_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y1_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Packaging and Returnable Packaging** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar mestre de produtos do tipo "Embalagem" – MDS (3Y1) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893720)

[2 Pré-requisitos 3](#_Toc233893721)

[2.1 Acesso ao sistema 3](#_Toc233893722)

[2.2 Funções 3](#_Toc233893723)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893724)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893725)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233893726)

[2.5.1 Tipo de material e intervalos de numeração 4](#_Toc233893727)

[2.5.2 Setor industrial 5](#_Toc233893728)

[3 Tabela de síntese 6](#_Toc233893729)

[4 Procedimentos 7](#_Toc233893730)

[4.1 Criar dados mestre de materiais – Visão básica 7](#_Toc233893731)

[4.2 Criar dados mestre de materiais – Visão SD 9](#_Toc233893732)

[4.3 Atualizar dados mestre de material – Visão WM 12](#_Toc233893733)

[5 Anexo 14](#_Toc233893734)

## Objetivo

Este script de dados mestre fornece procedimentos para criar materiais de embalagem/mestre de produtos usados pelos itens de escopo Administração de depósitos.

Este documento fornece um procedimento detalhado para testar o item de escopo após a ativação da solução, refletindo o escopo predefinido da solução. Cada etapa do processo, relatório ou item está coberto em uma seção própria que fornece as interações do sistema (etapas de teste) em uma visão de tabela. As etapas que não estão no escopo do processo, mas que são necessárias para teste, estão marcadas de modo correspondente. É necessário adicionar etapas específicas do projeto.

|  |
| --- |
| Nota Os valores deste script de teste (notação decimal, formatos de data etc.) são apresentados na notação padrão dos EUA. Se o sistema de teste estiver configurado para usar uma notação diferente, insira os valores apropriados. |

## Pré-requisitos

### Acesso ao sistema

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece o URL para acessar os vários apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) |
| --- | --- | --- | --- |
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Dados mestre - produtos / Governança de produto | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre são dependentes das unidades organizacionais da empresa. Os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Dados básicos | Independente de unidades organizacionais | Unidade de medida básicaGrupo de materiais e assim por diante. |  | n/a |
| Dados de vendas | Independente de unidades organizacionais | Grupo de transporte, Tipo de material de embalagemPeso admissível na embalagem,Volume admissível da embalagem, e assim por diante. |  | n/a |
| Dados WM | Independente de unidades organizacionais | Tipo de unidade comercialTipo de UC padrão |  | n/a |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre pode fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre de Empacotamento.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Unidade de medida básica | Dados básicos | Obrigatório |  |

|  |
| --- |
| Nota Os campos específicos do Brasil são necessários para obter um cálculo de imposto adequado. Verifique o capítulo Definir campos específicos do BR para dados mestre para o capítulo Dados mestre de materiais no documento Criar dados mestre para o Brasil (JD0_BR). |

### Parâmetros principais para a criação de dados

Nesta seção, descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para o empacotamento de um registro de dados mestre:

#### Tipo de material e intervalos de numeração

Com a ajuda de tipos de material, o sistema determina que segmentos de dados (visões) podem ser atualizados ou que campos são obrigatórios ou opcionais. Com base em tipos de material, o sistema também determina os intervalos de numeração para materiais. No conteúdo padrão SAP, todos os tipos de material utilizam a mesma definição de intervalo de numeração.

| Intervalo de numeração | Intervalo/ID do parceiro de negócios | Comentários |
| --- | --- | --- |
| Alfanumérico externo | A – ZZZZZZZZ | Este intervalo deve iniciar com um caractere. Em geral, o ID não deve ter mais de 40 caracteres. |
| Numérico interno | 1-99999999 | Este intervalo é utilizado se o sistema tiver que atribuir automaticamente um valor numérico a um material. |

#### Setor industrial

O conteúdo padrão só fornece um setor industrial M.

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| Criar dados mestre de materiais – Visão básica | Especialista em dados mestre - Dados do produto | Criar material(MM01)/ Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados básicos criados. |
| Criar dados mestre de materiais – Visão SD | Especialista em dados mestre - Dados do produto | Criar material(MM01)/ Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados de vendas criados. |
| Atualizar dados mestre de material – Visão WM | Especialista em dados mestre - Dados do produto | Modificar material(MM02)/ Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados WM criados. |

## Procedimentos

Esta seção descreve procedimentos para cada segmento ou etapa do processo que faz parte deste registro mestre.

### Criar dados mestre de materiais – Visão básica

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do material. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Procedimento: Opção 1 – Criar material

Use o seguinte procedimento, se o seu acesso do usuário disponibilizar o app Criar material.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | Exibe-se Criar material (1ª tela). |  |
| 3 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Tipo de material: Embalagem | A tela Seleção de visões é exibida. |  |
| 4 | Clicar em Seleção de visões. | Clique em Seleção de visões. | A caixa de diálogo Seleção de visões é exibida. |  |
| 5 | Clicar em visões | Na caixa de diálogo Seleção de visões , marque o campo de seleção Dados básicos 1 e Dados básicos 2 . Clique em Continuar (Enter). | A tela Criar material <número do seu material> (Embalagem), é exibida |  |
| 6 | Inserir dados básicos | Na tela Criar material > Número do seu material > (Embalagem) , efetue as seguintes entradas:Descr.:<descrição do seu material> |  |  |
| 7 | Inserir dados básicos | Na guia Dados básicos 1, na seção Dados gerais, efetue as seguintes entradas:Unidade de medida básica:<UM>, por exemplo, UNGr.ctg.itm.ger.: VERP |  |  |
| 7 | Inserir dados básicos | Na seção Dimensões/EANs, efetue as seguintes entradas:Peso bruto: por exemplo, 20Unidade de peso: por exemplo, KGPeso líquido: por exemplo, 15Volume: por exemplo, 138Unidade de volume: por exemplo, CD3Pressione Enter. | Depois de concluir a descrição, vá até a próxima guia, Dados básicos 2. |  |
| 8 | Preencher dados básicos | Não são necessárias entradas para a visão Dados básicos 2. |  |  |
| 9 | Salvar os dados | Clique em Salvar. | Os dados básicos são criados e salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | A tela Administrar dados mestre do produto(F1602) é exibida. |  |
| 3 | Selecionar Criar novo mestre de produtos | Na tela Administrar dados mestre do produto(F1602), clique em Criar e depois em Produto. | A tela Criar registro de dados mestre é exibida. |  |
| 4 | Inserir dados para campos obrigatórios | Na tela Criar registro de dados mestre, efetue as seguintes entradas:Número do produto: por exemplo, Z …Você insere qualquer ID alfanumérico externo e esse ID deve começar com um caractere alfanumérico. Se você não fornecer nenhuma entrada, o sistema atribui automaticamente um ID numérico.Para mais informações sobre o número do produto, consulte as seções anteriores Tipo de material e Intervalos de números.Tipo de produto: VERPUnidade básica: por exemplo, UNDescrição: <qualquer descrição>Selecione OK. |  |  |
| 5 | Inserir dados básicos | Na guia Informações gerais, efetue a seguinte entrada:Na seção Dados básicos:Setor de atividade: por exemplo, 00Clique em Ver mais e efetue a seguinte entrada:Grupo de categorias de item geral: VERP |  |  |
| 6 | Inserir dados de descrição | Na seção Descrições, clique em Criar e efetue as seguintes entradas:Idioma: por exemplo, DEDescrição do produto: <sua descrição> |  |  |
| 7 | Selecionar unidade de medida básica | Na seção Unidades de medida básicas, clique em Exibir mais para inserir os dados adicionais. |  |  |
| 8 | Insira outros Dados de medida | Na seção Peso, efetue as seguintes entradas:Peso bruto: por exemplo, 20 KGPeso líquido: por exemplo, 15 KGNa seção Volume, efetue a seguinte entrada:Volume: por exemplo, 138 CD3 |  |  |
| 9 | Salvar os dados | Clique em Criar. | Uma mensagem do sistema indica que o objeto foi salvo. |  |

### Criar dados mestre de materiais – Visão SD

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do material. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você precisa concluir a seção anterior, Criar dados mestre de materiais – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas de dados básicos, como descrito no procedimento anterior.

|  |
| --- |
| Nota Devido à restrição de performance no app Administrar dados mestre do produto, nem todos os campos podem ser visualizados e editados. Se você encontrar algum campo em falta, selecione a opção 1 para criar o material ou adicione esses campos no app Administrar dados mestre do produto por meio da diretriz em Adaptar IUs SAP Fiori no momento da execução - Adaptação de usuário-chave \| SAP Help Portal |

Procedimento: Opção 1 – Criar material

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Clique em Criar material(MM01). | A tela Criar material (Visão inicial) é exibida. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (Visão inicial), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: EmbalagemEscolha Selecionar visões. | Depois de preencher as entradas, é aberta uma nova tela, Seleção de visões. |  |
| 3 | Clicar em visões | Na tela Selecionar visões, clique em Vendas: dados gerais/do centro e selecione Continuar.Nota Só para a Polônia: clique também Comércio exterior – Dados de exportação para inserir o número de classificação PKWiU. | É exibida uma tela com Níveis organizacionais. |  |
| 4 | Clique em Continuar | Na tela Níveis organizacionais, na seção Nível organizacional, não insira dados para Centro, organização de vendas e canal de distribuiçãoClique em Continuar.As seguintes informações são exibidas na parte inferior da visão: O material já existe e será ampliado.pSó para a Polônia: se você selecionou Comércio exterior - dados de exportação, selecione Centro. |  |  |
| 5 | Inserir dados de vendas | Na guia Vendas: Gerais/do Centro, na seção Dados de expedição (tempos em dias), efetue as seguintes entradas:Grupo transp.: 0001 |  |  |
| 6 | Inserir dados de material de embalagem | Na seção Dados de material de embalagem, efetue as entradas a seguir.Tipo de material de embalagemPes.admiss.embalagemToler.excesso-pesoVol.emb.admissívelTol.excesso volumeEncerrado |  |  |
| 7 | Apenas para a Polônia: Inserir dados de vendas | Na seção Comércio internacional: exportação, insira os seguintes dados:• Código de controle: por exemplo, 26.40.20.0 | O código PKWiU é atualizado para a Polônia. |  |
| 8 | Salvar os dados | Clique em Salvar. | Seus dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app Administrar dados mestre do produto(F1602) se abre e vários campos de pesquisa são exibidos. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que guiará você para a visão Produto.Clique em Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecione Vendas | Na tela Produto, clique em Vendas.efetue as seguintes entradas:Grupo de transporte: 0001Peso admissível da embalagem:Volume permitido da embalagem: |  |  |
| 4 | Salvar os dados | Clique em Salvar. | Uma mensagem do sistema indica que o objeto foi salvo. |  |

### Atualizar dados mestre de material – Visão WM

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do material. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você precisa concluir o procedimento anterior, Criar dados mestre de materiais (produto) – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas de dados básicos, como descrito no procedimento anterior.

Procedimento: Opção 1 – Criar material

Utilize o seguinte procedimento, caso seu acesso de usuário ofereça o app Modificar material(MM02).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Modificar material(MM02). | Exibe-se Criar material (primeira tela). |  |
| 2 | Inserir dados básicos de material | Na tela Modificar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Clique em Seleção de visões. | Seleção de visões é aberta. |  |
| 3 | Clicar em visões | Na telaSeleção de visões, selecione as seguintes visões:Execução WMEmbalagem WMClique em Continuar. |  |  |
| 4 | Inserir Dados de execução WM | Na guia Execução WM, efetue as seguintes entradas:Tipo de UC padrão: por exemplo, SP1 |  |  |
| 5 | Inserir dados da embalagem WM | Na guia Embalagem WM, efetue as seguintes entradas:Tipo de Unidade comercial: por exemplo, SP1 |  |  |
| 6 | Salvar os dados | Clique em Salvar. |  |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app Administrar dados mestre do produto(F1602) se abre e vários campos de pesquisa são exibidos. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o Número do produto no campo de pesquisa Produto.Selecione o Produto da lista que guiará você para a visão Produto.Clique em Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Clicar em Execução | Na visão Produto, selecione a guia Administração de depósitos. |  |  |
| 4 | Insira Dados de execução | Na seção Execução, efetue as seguintes entradas:Tipo de unidade comercial padrão: por exemplo, SP1 |  |  |
| 5 | Insira Dados da embalagem | Na seção Embalagem, efetue as seguintes entradas:Tipo de unidade comercial: por exemplo, SP1 |  |  |
| 6 | Salvar os dados | Clique em Salvar. | A mensagem do sistema indica que o objeto foi salvo. |  |

## Anexo

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
- related-to :: [[02-business-partner-and-product-master-data/create-product-master-of-type-packaging-mds-3y1-389]]
- related-to :: [[02-business-partner-and-product-master-data/mds-3y1-391]]
- related-to :: [[02-business-partner-and-product-master-data/mds-3y1-393]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-emba]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y1_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 21,179 chars in the whole document
