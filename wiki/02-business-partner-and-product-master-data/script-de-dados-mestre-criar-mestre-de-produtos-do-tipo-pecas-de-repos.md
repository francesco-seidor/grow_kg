---
id: 02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-pecas-de-repos
title: "Script de dados mestre - Criar mestre de produtos do tipo \"Peças de reposição\" – MDS (2J7) (2J7_S4CLD2608_Master_Data_PT_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (PT): create spare-parts (ERSA) material master via MM01, with optional document link via F2733/MM02."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-spare-parts]
aliases: [2J7_S4CLD2608_Master_Data_PT_XX]
keywords: ["Product Master: Spare Parts", spare parts material master, material master creation, purchasing data, mrp planning data, warehouse data, accounting valuation data, document info records, linking documents to materials, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2J7_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-266
topic: 02-business-partner-and-product-master-data/product-master-spare-parts
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar mestre de produtos do tipo "Peças de reposição" – MDS (2J7) (2J7_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2J7_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Spare Parts** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar mestre de produtos do tipo "Peças de reposição" – MDS (2J7) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893567)

[2 Pré-requisitos 3](#_Toc233893568)

[2.1 Funções 3](#_Toc233893569)

[2.2 Unidades organizacionais necessárias 3](#_Toc233893570)

[2.3 Dados mestre obrigatórios e opcionais 4](#_Toc233893571)

[2.4 Parâmetros principais para a criação de dados 5](#_Toc233893572)

[2.4.1 Tipo de material e intervalos de numeração 5](#_Toc233893573)

[2.4.2 Setor industrial 5](#_Toc233893574)

[3 Tabela de síntese 6](#_Toc233893575)

[4 Procedimentos de teste 7](#_Toc233893576)

[4.1 Criar dados mestre de materiais - Dados básicos 7](#_Toc233893577)

[4.2 Criar dados mestre de materiais - Dados de compra 8](#_Toc233893578)

[4.3 Criar dados mestre de materiais - Dados MRP/de planejamento (dados do centro) 10](#_Toc233893579)

[4.4 Criar dados mestre de materiais - Dados do depósito 12](#_Toc233893580)

[4.5 Criar dados mestre de materiais - Dados contábeis (dados da área de avaliação) 14](#_Toc233893581)

[4.6 Criar documento (opcional) 15](#_Toc233893582)

[4.7 Modificar dados mestre de materiais - Ligar o documento aos dados mestre de materiais (opcional) 16](#_Toc233893583)

## Objetivo

Este módulo cria um registro de dados mestre do produto para peças de reposição.

## Pré-requisitos

Esta seção resume todos os pré-requisitos necessários para conduzir o teste em termos de sistemas, usuários, dados mestre, dados organizacionais, outros dados de teste e condições empresariais.

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) | Efetuar login |
| --- | --- | --- | --- | --- |
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Dados mestre - produtos / Governança de produto | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Designer | SAP_BR_DESIGN_ENGINEER | Administração de documentos | SAP_BR_DESIGN_ENGINEER |  |

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre do material são dependentes das unidades organizacionais da empresa, os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Dados básicos | Independente de unidades organizacionais | Descrição do material (texto breve), número do material, grupo de materiais, unidade de medida básica, etc. | Os dados básicos só existem uma vez para um registro de dados mestre de materiais. | não aplicável |
| Dados de compras | Centro | Grupo de compradores, grupo de materiais, tempo de processamento da EM, etc. | Os dados de compras podem existir para cada organização de compras, para a qual o material deve ser utilizado em processos de compras. | Centro:__________ |
| Dados MRP/de planejamento | Centro, depósito | Tipo de MRP, planejador MRP, tamanho do lote, prazo de entrega planejado, etc. | Podem existir dados do centro para cada ID do centro da sua estrutura da empresa no qual o registro mestre de materiais é usado.Os dados do depósito (contexto de planejamento) são opcionais com base na necessidade de efetuar o planejamento específico do depósito | Centro:____________Depósito:__________ |
| Dados do depósito | Centro, depósito | Número de notas de EM, período máximo de armazenamento, tempo mínimo restante prateleira, etc. |  | Centro:____________Depósito:__________ |
| Dados contábeis | Área de avaliação (=centro), tipo de avaliação | Classe de avaliação, por preço unitário, controle do preço, etc. | Podem existir dados da área de avaliação para cada ID do centro da sua estrutura empresarial para o qual o registro mestre de materiais é utilizado. Cada centro representa uma área de avaliação (por exemplo, preço de avaliação diferente de um material em centros diferentes) | Centro:____________Tipo de avaliação:__________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre de materiais podem fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre de materiais.

|  |
| --- |
| Nota Os campos específicos do Brasil são necessários para obter um cálculo de imposto adequado.Verifique Nota Fiscal Brasil - JD0 no capítulo Definir campos específicos do BR para dados mestre para dados mestre de materiais. |

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
|  |  | Opcional |  |
|  |  | Obrigatório |  |

### Parâmetros principais para a criação de dados

Nos seguintes tópicos desta seção, são descritos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um registro de dados mestre de materiais.

#### Tipo de material e intervalos de numeração

Com a ajuda de tipos de material, o sistema determina que segmentos de dados (visões) podem ser atualizados ou que campos são obrigatórios ou opcionais. Com base em tipos de material, o sistema também determina os intervalos de numeração para materiais. No conteúdo padrão SAP, todos os tipos de material utilizam a mesma definição de intervalo de numeração

| Intervalo de numeração | Intervalo/ID do parceiro de negócios | Comentários |
| --- | --- | --- |
| Alfanumérico externo | A – ZZZZZZZZ | Este intervalo deve iniciar com um caractere. Em geral, o ID não deve ter mais que 8 dígitos. |
| Numérico interno | 1 – 99999999 | Este intervalo é utilizado se o sistema tiver que atribuir automaticamente um valor numérico a um material. |

#### Setor industrial

O conteúdo padrão só fornece um setor industrial M.

|  |
| --- |
| Nota Atualmente, isto só é visível no SAP GUI. |

## Tabela de síntese

Este item de escopo consiste de várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar dados mestre de materiais - Dados básicos](#unique_10) [página ] 7 | Especialista em dados mestre - Dados do produto | Criar material(MM01) | Os dados mestre de material básico são criados. |
| [Criar dados mestre de materiais - Dados de compra](#unique_11) [página ] 8 | Especialista em dados mestre - Dados do produto | Criar material(MM01) | Os dados mestre de compras são criados. |
| [Criar dados mestre de materiais - Dados MRP/de planejamento (dados do centro)](#unique_12) [página ] 10 | Especialista em dados mestre - Dados do produto | Criar material(MM01) | Os dados mestre do planejamento MRP são criados. |
| [Criar dados mestre de materiais - Dados do depósito](#unique_13) [página ] 12 | Especialista em dados mestre - Dados do produto | Criar material(MM01) | Os dados mestre do depósito são criados |
| [Criar dados mestre de materiais - Dados contábeis (dados da área de avaliação)](#unique_14) [página ] 14 | Especialista em dados mestre - Dados do produto | Criar material(MM01) | Os dados mestre contábeis são criados. |
| [Criar documento (opcional)](#unique_15) [página ] 15 | Designer | Administrar documentos(F2733) | Um novo registro info de documento é criado e os metadados são adicionados. Os anexos são adicionados ao documento. |
| [Modificar dados mestre de materiais - Ligar o documento aos dados mestre de materiais (opcional)](#unique_16) [página ] 16 | Especialista em dados mestre - Dados do produto | Modificar material(MM02) | O documento criado na etapa anterior está ligado aos dados mestre de materiais. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar dados mestre de materiais - Dados básicos

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do material.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | É exibida a página Início.Nota O login no launchpad do SAP Fiori só é relevante para utilização de Web GUI. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | Uma nova tela, Criar material (1ª tela), será aberta. |  |
| 3 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: por exemplo, ERSA Peças de reposição | Uma nova tela será aberta exibindo Selecionar visões. |  |
| 4 | Selecionar Visões | Na tela Seleção de visões, clique em Dados básicos 1 e Dados básicos 2. Em seguida, clique em Continuar. | Uma nova tela é aberta exibindo a visão Criar material (peças de reposição). |  |
| 5 | Inserir dados básicos | Na visão Criar material ... (peças de reposição), na guia Dados básicos 1, insira a descrição (texto breve). |  |  |
| 6 | Inserir dados básicos | Na guia Dados básicos 1, na seção Dados gerais, efetue as seguintes entradas:Unidade de medida básica: por exemplo, UnidadeGrupo de materiais: por exemplo, YBPM01 |  |  |
| 7 | Salvar os dados | Selecione Salvar | O número do material é criado. |  |

### Criar dados mestre de materiais - Dados de compra

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do material.

Pré-requisito

Você completou e salvou os dados básicos para o material, como descrito na seção anterior Criar dados mestre de materiais – Dados básicos.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | É exibida a página Início.Nota O login no launchpad do SAP Fiori só é relevante para utilização de Web GUI. |  |
| 2 | Abrir bloco Criar material | Na seção Mestre de produtos, clique em Criar material(MM01). | Uma nova tela exibindo Criar material (1ª tela) será aberta. |  |
| 3 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: número do material criado na etapa anterior.Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: por exemplo, ERSA Peças de reposição | Uma nova tela exibindo Selecionar visões será aberta. |  |
| 4 | Selecionar Visões | Na tela Selecionar visões, selecione Compras e, em seguida, Continuar.Nota Só para a Polônia: Para inserir o código PKWiU, selecione também Comércio Internacional: importação. | Uma nova tela exibindo os níveis organizacionais será aberta. |  |
| 5 | Inserir dados dos níveis organizacionais | Efetue as seguintes entradas na tela Unidades organizacionais, na seção Níveis organizacionais:Centro: <código do centro>Selecione Continuar. | Uma nova tela é aberta exibindo Criar material (peças de reposição).Nota Na parte inferior da tela é exibida a seguinte mensagem do sistema: O material já existe e será ampliado. |  |
| 6 | Inserir dados de compras | Efetue as seguintes entradas na tela Criar material (peças de reposição), na guia Compras, seção Dados gerais:Grupo de compradores: nº do grupo de compradores |  |  |
| 7 | Inserir dados de compras | Na seçãoOutros dados/dados de fabricante, efetue a seguinte entrada:Tempo de processamento da entrada de mercadorias: por exemplo, 1 |  |  |
| Só para a Polônia | Inserir dados de vendas | Na seção Comércio internacional: importação, insira os seguintes dados:Código de controle: por exemplo, 41.00.30.0Em seguida, clique em Salvar. | O código PKWiU é atualizado para a Polônia. |  |
| 8 | Salvar os dados | Clique em Salvar. | O número do material é criado. |  |

### Criar dados mestre de materiais - Dados MRP/de planejamento (dados do centro)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do material.

Pré-requisito

Você concluiu as seção anterior, Criar dados mestre de materiais – Dados básicos e salvou os dados mestre de compras.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | É exibida a página Início.Nota O login no launchpad do SAP Fiori só é relevante para utilização de Web GUI. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | Uma nova visão exibindo Criar material (1ª tela) será aberta. |  |
| 3 | Inserir dados básicos de material | Em Criar material (visão inicial), efetue as seguintes entradas:Material: número do material criado na etapa anteriorSetor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: por exemplo, ERSA Peças de reposição | Uma nova visão exibindo Selecionar visões será aberta. |  |
| 4 | Selecionar Visões | Na visão Selecionar visões, selecione MRP1, MRP2, MRP3 e MRP4. depois clique em Continuar. | Uma nova visão exibindo os níveis organizacionais será aberta. |  |
| 5 | Inserir dados dos níveis organizacionais | Na visão Níveis organizacionais, na seção Níveis organizacionais, efetue as seguintes entradas:Centro: <número do centro>Depósito: <depósito> | Uma nova visão é aberta exibindo Criar material (peças de reposição). |  |
| 6 | Inserir dados MRP/de planejamento | Efetue as seguintes entradas na visão Criar material (peças de reposição), na guia MRP 1, seção Procedimento MRP:Tipo de MRP: por exemplo, PDPlanejador MRP: por exemplo, 001 | Você chama a seguinte mensagem de sistema na parte inferior da visão: o material já existe e será ampliado. |  |
| 7 | Inserir dados MRP/de planejamento | Na seçãoDados do tamanho do lote, efetue a seguinte entrada:Procedimento de dimensionamento de lotes: por exemplo, EX | Você navegou para a guia seguinte, MRP 2 |  |
| 8 | Inserir dados MRP/de planejamento | Efetue as seguintes entradas na visão Criar material (peças de reposição), na guia MRP 2, seção Suprimento:Tipo de suprimento: por exemplo, F Dep. Local no depósito: <localização>Depósito para EP <Localização> |  |  |
| 9 | Inserir dados MRP/de planejamento | Na seção Programação, efetue as seguintes entradas:Prazo de entrega planejado: Por exemplo, 3Tempo de processamento da entrada de mercadorias: por exemplo, 1Chave de prazos: por exemplo, 000 | Você navegou para a guia seguinte, MRP 3. |  |
| 10 | Inserir dados MRP/de planejamento | Efetue as seguintes entradas na visão Criar material (peças de reposição), na guia MRP 3, seção Verificação de disponibilidade:Verificação de disponibilidade: por exemplo, EOTempo total reposição por exemplo, 3 | Você navegou para a guia seguinte, MRP 4. |  |
| 11 | Inserir dados MRP/de planejamento | Efetue as seguintes entradas na visão Criar material (peças de reposição), na guia MRP 4, seção Explosão da lista técnica/necessidades dependentes:Indiv./colet.: 2 |  |  |
| 12 | Salvar os dados | Selecione Salvar | O número do material é criado. |  |

### Criar dados mestre de materiais - Dados do depósito

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do material.

Pré-requisito

Você preencheu os dados para o material, tal como descrito no procedimento anterior, Criar dados mestre de materiais – Dados básicos, e salvou os dados MRP/de planejamento.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | É exibida a página Início.Nota O login no launchpad do SAP Fiori só é relevante para utilização de Web GUI. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | Uma nova visão exibindo Criar material (visão inicial) será aberta. |  |
| 3 | Inserir dados básicos de material | Em Criar material (visão inicial), efetue as seguintes entradas:Material: número do material criado na etapa anterior.Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: por exemplo, ERSA Peças de reposição | Uma nova visão exibindo Selecionar visões será aberta. |  |
| 4 | Selecionar Visões | Na visão Selecionar visões, selecione as seguintes visões e clique em Continuar:Dados gerais do centro/armazenamento 1Dados gerais do centro/armazenamento 2 | Uma nova visão exibindo os níveis organizacionais será aberta. |  |
| 5 | Inserir dados dos níveis organizacionais | Na visão Níveis organizacionais, na seção Níveis organizacionais, efetue as seguintes entradas:Centro: <código do centro>Depósito: <número do depósito> | Uma nova visão é aberta exibindo Criar material (peças de reposição).Nota Uma mensagem do sistema será exibida na parte inferior da visão: O material já existe e será ampliado. |  |
| 6 | Inserir dados do depósito | Na visão Criar material (peças de reposição), na guia Dds.cen./armazmto. 1, na seção Dados gerais, efetue as seguintes entradas:Número de notas de EM: por exemplo, 1 | Você navegou para a guia seguinte, Dds.centro/armazmto.2. |  |
| 7 | Confirmar entradas | Na guia Dds.cen./armazmto 2, na seção Parâmetros gerais de centro, efetue a seguinte entrada:Centro de lucro. |  |  |
| 8 | Salvar os dados | Clique em Salvar. | O número do material é criado. |  |

### Criar dados mestre de materiais - Dados contábeis (dados da área de avaliação)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do material.

Pré-requisito

Você criou os dados para o material descrito no procedimento anterior, Criar dados mestre de materiais – Dados básicos, concluiu e salvou os dados do depósito.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | É exibida a página Início.Nota O login no launchpad do SAP Fiori só é relevante para utilização de Web GUI. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | Criar material (primeira tela) é exibida. |  |
| 3 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: <o número do material que você criou na etapa anterior>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: por exemplo, ERSA Peças de reposição | A visão Seleção de visões é exibida. |  |
| 4 | Selecionar Visões | Em Selecionar visões, selecione o seguinte e clique em Continuar:Contabilidade 1Contabilidade 2 | A visão Níveis organizacionais é exibida. |  |
| 5 | Inserir dados dos níveis organizacionais | Na visão Níveis organizacionais, na seção Níveis organizacionais, efetue as seguintes entradas:Centro | A visão Criar material (peças de reposição) será exibida.Esta mensagem do sistema será exibida: O material já existe e será ampliado. |  |
| 6 | Inserir dados contábeis | Na visão Criar material (peças de reposição), na guia Contabilidade 1, seção Dados de avaliação gerais, efetue a seguinte entrada:Classe de avaliação: 3040 |  |  |
| 7 | Inserir dados contábeis | Na seçãoPreços e valores, efetue as seguintes entradas:Preço padrão por exemplo, 100Unidade de preço: 1Ctrl. prç.: manter como padrão | A guia seguinte, Contabilidade 2, é aberta. |  |
| 8 | Confirmar entradas | Você não efetuou entradas na guia Contabilidade 2. |  |  |
| 9 | Salvar os dados | Clique em Salvar. | O número do material é criado. |  |

### Criar documento (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de documentos.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori usando suas credenciais de usuário Designer. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar documentos(F2733). | A tela Administrar documentos(F2733) é exibida. |  |
| 3 | Criar novo documento | Na visão Administrar documento, selecione Criar para criar um novo documento. | A visão Documento é exibida. |  |
| 4 | Inserir metadados | Na guia Informações gerais da visão Documento, efetue as seguintes entradas:Tipo de documento: por exemplo, YBODocumento parcial: por exemplo, 000Na guia Dados do documento da visão Documento, efetue as seguintes entradas:Descrição: por exemplo, <SparePartsDoc001> | Os metadados são atualizados na visão Documento com valores padrão. |  |
| 5 | Carregar anexos no documento | Na visão Documento , vá para a guia Originais e clique em Upload para navegar e carregar os documentos apropriados:Nome do arquivo: por exemplo, <test001.jpg> | Os documentos aparecerão como anexados. |  |
| 6 | Salvar o documento | Clique em Criar para salvar o documento. | Um novo documento do tipo YBO é criado e salvo.Anote o número do documento. |  |
| 7 | Modificar status | Na visão Documento, clique em Editar e, na seção Dados do documento, defina o Status do documento como Re (Liberado) |  |  |
| 8 | Salvar o documento | Clique em Salvar para salvar o documento. |  |  |

### Modificar dados mestre de materiais - Ligar o documento aos dados mestre de materiais (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para ligar um documento aos dados mestre do material.

Pré-requisito

Você criou os dados para o material descrito no procedimento anterior, Criar dados mestre de materiais - Dados básicos, e concluiu o procedimento opcional Criar documento.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Modificar material(MM02). | Uma nova janela mostrando Criar material (1ª tela) será exibida. |  |
| 3 | Inserir dados básicos de material | Em Modificar material (1ª tela), efetue as seguintes entradas:Material: <número do material criado na etapa anterior>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro. |  |  |
| 4 | Selecionar Visões | Em Modificar material (1ª tela), clique em Selecionar visões na barra superior. | Uma nova visão exibindo Selecionar visões será aberta. |  |
| 5 | Selecionar Visões | Na janela Marcar visão(ões), selecione as visões seguintes e escolha Continuar:Dados básicos 1 | Uma nova janela será aberta exibindo a tela Modificar material … (peças de reposição) |  |
| 6 | Abrir dados adicionais | Na tela Modificar material … (peças de reposição), selecione Dados adicionais na barra superior. |  |  |
| 7 | Inserir dados do documento | Selecione a guia Dados do documento e, em Documentos ligados, clique em Todas as versões. Selecione o sinal positivo (+) para inserir uma nova linha. Procure o documento criado no procedimento anterior. |  |  |
| 8 | Copiar dados do documento | Selecione o documento criado na etapa anterior e clique em Copiar para inserir o documento na linha. |  |  |
| 9 | Salvar os dados | Clique em Salvar. | O número do material será modificado. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-spare-parts-mds-2j7-2]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2j7-265]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2j7-267]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-piez]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2J7_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 31,054 chars in the whole document
