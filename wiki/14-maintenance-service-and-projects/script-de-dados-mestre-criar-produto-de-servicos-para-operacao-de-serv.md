---
id: 14-maintenance-service-and-projects/script-de-dados-mestre-criar-produto-de-servicos-para-operacao-de-serv
title: Script de dados mestre - Criar produto de serviços para operação de serviço (MDS 3KV) (3KV_S4CLD2608_Master_Data_PT_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (PT): create service products (SRV_*, FSM expenses), their prices and overtime/calculation-criteria conditions."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-products-for-service-processes]
aliases: [3KV_S4CLD2608_Master_Data_PT_XX]
keywords: [Service Products and Service Prices, service products, product master data, service pricing, overtime pricing, calculation criteria condition, service bundles, service contracts, contract auto-renewal, service expenses]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KV_S4CLD2608_Master_Data_PT_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-350
topic: 14-maintenance-service-and-projects/service-products-for-service-processes
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar produto de serviços para operação de serviço (MDS 3KV) (3KV_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KV_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Service Products and Service Prices** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar produto de serviços para operação de serviço – MDS (3KV) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 3](#_Toc233893685)

[2 Pré-requisitos 4](#_Toc233893686)

[2.1 Acesso ao sistema 4](#_Toc233893687)

[2.2 Funções 4](#_Toc233893688)

[2.3 Unidades organizacionais necessárias 4](#_Toc233893689)

[3 Tabela de síntese 6](#_Toc233893690)

[4 Procedimentos 7](#_Toc233893691)

[4.1 Criar produtos dos serviços 7](#_Toc233893692)

[4.1.1 SRV_01 7](#_Toc233893693)

[4.1.2 SRV_CONTRACT 9](#_Toc233893694)

[4.1.3 SRV_CTR_RENEWAL 11](#_Toc233893695)

[4.1.4 SRV_02 13](#_Toc233893696)

[4.1.5 FSM – Item de despesa 14](#_Toc233893697)

[4.1.6 SRV_03 16](#_Toc233893698)

[4.1.7 SRV_04 18](#_Toc233893699)

[4.1.8 SRV_BUNDLE_01 20](#_Toc233893700)

[4.1.9 SRV_BUNDLE_02 22](#_Toc233893701)

[4.1.10 SRV_05 24](#_Toc233893702)

[4.1.10.1 Criar dados básicos 24](#_Toc233893703)

[4.1.10.2 Criar dados de venda 25](#_Toc233893704)

[4.1.10.3 Criar dados de compras 27](#_Toc233893705)

[4.1.10.4 Criar dados MRP/planejamento 28](#_Toc233893706)

[4.1.10.5 Criar dados do depósito 30](#_Toc233893707)

[4.1.10.6 Criar dados contábeis 31](#_Toc233893708)

[4.2 Definir preços para materiais 33](#_Toc233893709)

[4.2.1 Preço para SRV_01 33](#_Toc233893710)

[4.2.2 Preço para SRV_CONTRACT 34](#_Toc233893711)

[4.2.3 Preço para SRV_CTR_RENEWAL 35](#_Toc233893712)

[4.2.4 Preço para SRV_02 36](#_Toc233893713)

[4.2.5 Preço para SRV_04 37](#_Toc233893714)

[4.2.6 Preço para SRV_BUNDLE_01 38](#_Toc233893715)

[4.2.7 Preço para SRV_05 39](#_Toc233893716)

[4.2.8 Preço para FSM - Despesa EXP_FSM_MILEAGE 41](#_Toc233893717)

[4.3 Definir preços para horas extras 42](#_Toc233893718)

[4.4 Criar registro de condição para critério para cálculo 43](#_Toc233893719)

## Objetivo

Neste documento, você pode encontrar uma descrição sobre como criar registros de dados mestre de produto dos serviços, incluindo preços. A descrição inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema "normal". O leitor aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo não são descritos neste documento, embora eles possam aparecer na interface do usuário.

Um registro mestre de produtos dos serviços que é criado como descrito aqui pode ser utilizado para o processamento de ordem de serviço e de confirmação de serviço.

| ID do produto de serviços | Descrição | Utilização |
| --- | --- | --- |
| SRV_01 | Serviço | representa o próprio serviço, por exemplo, uma instalação, um reparo, uma manutenção |
| SRV_CONTRACT | Produto de contrato | representa o próprio serviço no contrato |
| SRV_CTR_RENEWAL | Produto de prorrogação do contrato de serviços | representa o produto do contrato de prestação de serviços no contrato com valores predefinidos para prorrogação automática |
| SRV_02 | Despesas de serviço | reflete a despesa que poderia ocorrer devido ao serviço, por exemplo, custos de viagem, combustível |
| SRV_03 | Peça de reposição (indefinida) | reflete um material necessário para o serviço e permite a descrição de texto livreeste material não estocável só pode ser suprido |
| SRV_04 | Peça de reposição (definida) | reflete o material como não estocável com integração logística mínima/nenhuma integração logísticaeste material não estocável só pode ser suprido |
| SRV_05 | Peça de reposição de estoque | reflete um material que será retirado do estoque (cenário retirada do estoque) |
| SRV_06 | Peça de reposição de estoque com perfil do número de série | reflete um material com um perfil de números de série atribuído que será retirado do estoque (cenário de retirada do estoque) |
| SRV_BUNDLE_01 | Pacote de serviços 01 | representa um serviço complexo como um pacote com subitens |
| SRV_BUNDLE_02 | Pacote de serviços 02 | representa um serviço complexo como um pacote com subitens (item de serviço e itens de preço fixo) |
| EXP_FSM_TRAVELEXP_FSM_MEALSEXP_FSM_OTHEREXP_FSM_MILEAGE | Despesas de serviço | reflete a despesa, por exemplo, custos de viagem ou refeições, em caso de integração com o SAP Field Service Management. |

## Pré-requisitos

### Acesso ao sistema

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via SAP Fiori Launchpad. Seu administrador do sistema fornece a você o URL para acessar os vários apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) |
| --- | --- | --- | --- |
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Dados mestre - produtos / Governança de produto | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |
| Especialista em preços | SAP_BR_PRICING_SPECIALIST | Gestão de preços | SAP_BR_PRICING_SPECIALIST |

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre são dependentes das unidades organizacionais da empresa. Os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Unidade organizacional a ser utilizada para os EUA | Unidade organizacional a ser utilizada para DE |
| --- | --- | --- | --- |
| Criar material | Centro | 1710 (centro 1 EUA) | 1010 (centro 1 DE) |
| Criar material | Organização de vendas | 1710 (Org.vendas nacional EUA) | 1010 (Org.vendas nacional DE) |
| Criar material | Canal de distribuição | 10 (vendas diretas) | 10 (vendas diretas) |

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Segmento | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| Criar produtos dos serviços | SAP_BR_PRODMASTER_SPECIALIST | Criar material(MM01) | Os produtos dos serviços são criados. |
| Definir preços para materiais (Criar registros de condições) | SAP_BR_PRICING_SPECIALIST | Definir preços de material - Vendas(VK12) | Os preços para produtos dos serviços estão definidos. |
| Definir preços para horas extras (Criar registros de condições) | SAP_BR_PRICING_SPECIALIST | Definir preços de material - Vendas(VK12) | O preço para horas extras foi definido. |

## Procedimentos

Esta seção descreve procedimentos para cada segmento ou etapa do processo que faz parte deste registro mestre.

### Criar produtos dos serviços

#### SRV_01

Objetivo

Este material só é relevante para edição na nuvem.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados de produto (MDG). | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Escolha no app Criar material. | A tela Criar material é exibida. |  |
| 3 | Atualizar dados básicos de material (para serviço de produto dos serviços) | Em Criar material (primeira tela), efetue as seguintes entradas: caixa de diálogo, selecione oMaterial:SRV_01Setor industrialMSe o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido no escuro. Atualmente, só existe uma entrada para o setor industrial (M = engenharia mecânica).Tipo de material:produto dos serviçosEm seguida, clique em Continuar (Enter). | Você atualizou as informações básicas para o novo produto dos serviços.É exibida a caixa de diálogo Selecionar visão(ões). |  |
| 4 | Clicar em visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Dados básicos 1Vendas: Dados da organização de vendas 1Vendas: Dados da organização de vendas 2Vendas: Dados gerais/dados do centroComprasContabilidade1Em seguida, clique em Continuar (Enter). | A tela Nível organizacional é exibida. |  |
| 5 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:Centro:1710 (centro 1 EUA)Org.vendas:1710 ( Org.vendas nac.EUA)Canal de distribuição:10 (vendas diretas)Em seguida, clique em Continuar (Enter). | Os dados organizacionais foram selecionados.A visão Criar material SRV_01 (serviços) é exibida. |  |
| 6 | Atualizar dados básicos | Na visão Dados básicos 1, atualize os seguintes valores:Descr.:serviçoUnidade de medida básica:HR (horas)Grupo de materiais:P001 (serviços)GrpItensGer.:SRVP (produto dos serviços)Em seguida, clique em Continuar (Enter). | Os dados básicos são atualizados e a guia Vendas: organização de vendas 1 é exibida.Nota Para cada idioma diferente utilizado na sua empresa, a descrição correspondente para o produto deve ser atualizada por código de idioma. |  |
| 7 | Atualizar dados da organização de vendas (1) | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados geraisDesconto:X <selecionado>Dados do impostoClassificação fiscal:1 (imposto total)Em seguida, pressione Enter. | Os dados organizacionais de vendas são atualizados. A guia Vendas: organização de vendas 2 é exibida. |  |
| 8 | Atualizar dados da organização de vendas (2) | Na guia Vendas: organização de vendas 2, atualize a seguinte entrada:Grupo de categorias de item:SRVP (produto dos serviços)Em seguida, pressione Enter. | Os dados organizacionais de vendas são atualizados. A guia Vendas: Geral/centro é exibida. |  |
| 9 | Atualizar dados gerais de venda | Na visão Vendas: Geral/centro, atualize os seguintes valores:Unidade de medida básica:HR (horas)Duração do trabalho:1 HRPerfil do serviço:5x10 (Seg-Sex: 7-17h)Perf.resposta:PRIMEIRO (tempo de resposta de primeiro nível)Em seguida, pressione Enter. | Os dados gerais de venda são atualizados. |  |
| 10 | Atualizar dados de compras | Na visão Compras, na seção Dados gerais, efetue as seguintes entradas:Unidade de medida básica: por exemplo, HRGrupo de materiais: por exemplo, P001Grupo de compradores: por exemplo, 001Cód.imp.p/material: por exemplo, 1Em seguida, clique em Continuar (Enter). | Os dados de compras são atualizados. |  |
| 11 | Atualizar dados contábeis | Na visão Contabilidade 1, na seção Dados da avaliação atuais, efetue as seguintes entradas:Unidade de medida básica: por exemplo, HRClasse de avaliação: por exemplo, 3200Em seguida, clique em Salvar. | Os dados contábeis são atualizados.O produto dos serviços é salvo. O sistema exibe a visão Criar material (primeira tela). |  |

#### SRV_CONTRACT

Objetivo

Este material é relevante para edição na nuvem e edição local.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados de produto (MDG). | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Escolha no app Criar material. | É exibido Criar material (1ª tela). |  |
| 3 | Atualizar dados básicos de material (para serviço de produto dos serviços) | Em Criar material (1ª tela), efetue as seguintes entradas:● Material: SRV_CONTRACT● Setor industrialMSe o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido no escuro. Atualmente, só existe uma entrada para o setor industrial (M = engenharia mecânica).● Tipo de material: Produto dos serviçosEm seguida, clique em Continuar (Enter). | Você atualizou as informações básicas para o novo produto dos serviços.É exibida a caixa de diálogo Selecionar visão(ões). |  |
| 4 | Clicar em visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Dados básicos 1Guia Vendas: Dados da organização de vendas 1Guia Vendas: Dados da organização de vendas 2Guia Vendas: Dados gerais/dados do centroEm seguida, clique em Continuar (Enter). | A tela Níveis organizacionais é exibida. |  |
| 5 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:• Centro: 1710 (Centro 1 EUA)• Org.vendas: 1710 ( Org.vendas nac.EUA)• Canal de Distribuição:: 10 (vendas diretas)Em seguida, clique em Continuar (Enter). | Os dados organizacionais foram selecionados.A visão Criar material SRV_CONTRACT (Produto dos serviços) é exibida. |  |
| 6 | Atualizar dados básicos | Na visão Dados básicos 1, atualize os seguintes valores:• Descr..: Produto do contrato de serviços• Unidade de medida básica: US (unidade de serviço)• Grupo de mercadorias: P001 (Serviços)• GenItemGroup: Prod.contrato serviços SCNPEm seguida, clique em Continuar (Enter). | Os dados básicos são atualizados e a guia Vendas: organização de vendas 1 é exibida. |  |
| 7 | Atualizar dados da organização de vendas (1) | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados gerais• Desconto: X <selecionado>Dados do imposto• Classificação fiscal: 1 (imposto total)Em seguida, clique em Continuar (Enter). | Os dados organizacionais de vendas são atualizados. A guia Vendas: organização de vendas 2 é exibida. |  |
| 8 | Atualizar dados da organização de vendas (2) | Na guia Vendas: organização de vendas 2, atualize a seguinte entrada:Grupo de categorias de item: SNCP - Prod. contrato serviçosEm seguida, clique em Continuar (Enter). | Os dados organizacionais de vendas são atualizados. A guia Vendas: Geral/centro é exibida. |  |
| 9 | Atualizar dados gerais de venda | Na visão Vendas: Geral/centro, atualize os seguintes valores:• Unidade de medida básica: US (unidade de serviço)• Duração de trabalho: 1 dia (dias)• Perfil do serviço: 5x10 (Seg-Sex: 7-17h)• Perfil de resposta: PRIMEIRO (tempo de resposta do primeiro nível)Em seguida, clique em Salvar. | Os dados gerais de venda são atualizados. |  |

#### SRV_CTR_RENEWAL

Objetivo

Este material é relevante para edição na nuvem e edição local.

Este material tem valores de renovação automática predefinidos.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados de produto (MDG). | A página Inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Escolha no app Criar material. | É exibido Criar material (1ª tela). |  |
| 3 | Atualizar dados básicos de material (para serviço de produto dos serviços) | Em Criar material (1ª tela), efetue as seguintes entradas:● Material: SRV_CTR_RENEWAL● Setor industrialMSe o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido no escuro. Atualmente, só existe uma entrada para o setor industrial (M = engenharia mecânica).● Tipo de material: Produto dos serviçosEm seguida, clique em Continuar (Enter). | Você atualizou as informações básicas para o novo produto dos serviços.Você atualizou as informações básicas para o novo produto dos serviços. |  |
| 4 | Clicar em visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Dados básicos 1Guia Vendas: Dados da organização de vendas 1Guia Vendas: Dados da organização de vendas 2Guia Vendas: Dados gerais/dados do centroEm seguida, clique em Continuar (Enter). | A tela Níveis organizacionais é exibida. |  |
| 5 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:• Centro: 1710 (Centro 1 EUA)• Org.vendas: 1710 ( Org.vendas nac.EUA)• Canal de Distribuição:: 10 (vendas diretas)Em seguida, clique em Continuar (Enter). | Os dados organizacionais foram selecionados.A visão Criar material SRV_CTR_RENEWAL (Produto dos serviços) é exibida. |  |
| 6 | Atualizar dados básicos | Na visão Dados básicos 1, atualize os seguintes valores:• Descr..: Produto de prorrogação do contrato de serviços• Unidade de medida básica: US (unidade de serviço)• Grupo de mercadorias: P001 (Serviços)• GenItemGroup: Prod.contrato serviços SCNP• Código de prorrogação automática do contrato: 1Em seguida, clique em Continuar (Enter). | Os dados básicos são atualizados e a guia Vendas: organização de vendas 1 é exibida. |  |
| 7 | Atualizar dados da organização de vendas (1) | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados gerais• Desconto: X <selecionado>Dados do imposto• Classificação fiscal: 1 (imposto total)Em seguida, clique em Continuar (Enter). | Os dados organizacionais de vendas são atualizados. A guia Vendas: organização de vendas 2 é exibida. |  |
| 8 | Atualizar dados da organização de vendas (2) | Na guia Vendas: organização de vendas 2, atualize a seguinte entrada:Critérios de agrupamento• Grupo de categorias do item: SRVP (Produto dos serviços)Período de prorrogação da renovação automática• Período de prorrogação padrão: 1• Unidade para prorrogação: Ano e clique em Continuar (Enter). | Os dados organizacionais de vendas são atualizados. A guia Vendas: Geral/centro é exibida. |  |
| 9 | Atualizar dados gerais de venda | Na visão Vendas: Geral/centro, atualize os seguintes valores:• Unidade de medida básica: US (unidade de serviço)• Duração de trabalho: 1 dia (dias)• Perfil do serviço: 5x10 (Seg-Sex: 7-17h)• Perfil de resposta: PRIMEIRO (tempo de resposta do primeiro nível)Em seguida, clique em Salvar. | Os dados gerais de venda são atualizados.O produto dos serviços é salvo. O sistema exibe a visão Criar material (primeira tela). |  |

#### SRV_02

Objetivo

Este material só é relevante para edição na nuvem.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados de produto (MDG). | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Escolha no app Criar material. | É exibido Criar material (1ª tela). |  |
| 3 | Atualizar dados básicos de material (para despesas de serviço de produto dos serviços) | Em Criar material (primeira tela), efetue as seguintes entradas:Material:SRV_02Setor industrialMSe o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido no escuro. Atualmente, só existe uma entrada para o setor industrial (M = engenharia mecânica).Tipo de material:produto dos serviçosEm seguida, clique em Continuar (Enter). | Você atualizou as informações básicas para o novo produto dos serviços.É exibida a caixa de diálogo Selecionar visão(ões). |  |
| 4 | Clicar em visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Dados básicos 1Guia Vendas: Dados da organização de vendas 1Guia Vendas: Dados da organização de vendas 2Guia Vendas: Dados gerais/dados do centroComércio internacional ExportaçãoEm seguida, clique em Continuar (Enter). | A tela Níveis organizacionais é exibida. |  |
| 5 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:Centro:1710 (centro 1 EUA)Org.vendas:1710 ( Org.vendas nac.EUA)Canal de distribuição:10 (vendas diretas)Em seguida, clique em Continuar (Enter). | Os dados organizacionais foram selecionados.A visão Criar material SRV_02 (despesas de serviço) é exibida. |  |
| 6 | Atualizar dados básicos | Na visão Dados básicos 1, atualize os seguintes valores:Descr.:despesas do serviçoUnidade de medida básica:Unid. (unidade)Grupo de materiais:P002 (despesas)GrpItensGer.:SRVE (item de despesas)Em seguida, clique em Continuar (Enter). | Os dados básicos foram atualizados e a guia Vendas: organização de vendas 1 é exibida.Nota Para cada idioma diferente utilizado na sua empresa, a descrição correspondente para o produto deve ser atualizada por código de idioma. |  |
| 7 | Atualizar dados da organização de vendas (1) | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados geraisDesconto: <selecionado>Dados do impostoClassificação fiscal:1 (imposto total)Em seguida, clique em Continuar (Enter). | Os dados organizacionais de vendas são atualizados. A guia Vendas: organização de vendas 2 é exibida. |  |
| 8 | Atualizar dados da organização de vendas (2) | Na guia Vendas: organização de vendas 2, atualize a seguinte entrada:Grupo de categorias de item:SRVE (item de despesas)Em seguida, clique em Continuar (Enter). | Os dados organizacionais de vendas são atualizados. O produto dos serviços é salvo. |  |

#### FSM – Item de despesa

Objetivo

Este material só é relevante para edição na nuvem.

Aplicar itens de serviço para FSM (processamento de ordens de serviço com SAP Field Service Management) como SRV_02, por exemplo, “item de despesa para alojamento”.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | É exibida a Página inicial. |  |
| 2 | Acessar o app SAP Fiori | Escolha no app Criar material. | É exibido Criar material (1ª tela). |  |
| 3 | Atualizar dados básicos de material (para despesas de serviço de produto dos serviços) | Em Criar material (primeira tela), efetue as seguintes entradas:Material:EXP_FSM_ACCOMSetor industrialMSe o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido no escuro. Atualmente, só existe uma entrada para o setor industrial (M = engenharia mecânica).Tipo de material:produto dos serviçosEm seguida, clique em Continuar (Enter). | Você atualizou as informações básicas para o novo produto dos serviços.Você também pode criar como material de despesa, por exemplo:EXP_FSM_MEALSEXP_FSM_OTHEREXP_FSM_TRAVELEXP_FSM_MILEAGEÉ exibida a caixa de diálogo Selecionar visões. |  |
| 4 | Clicar em visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Dados básicos 1Guia Vendas: Dados da organização de vendas 1Guia Vendas: Dados da organização de vendas 2Guia Vendas: Dados gerais/dados do centroContabilidade 1 (só para EXP_FSM_MILEAGE)Em seguida, clique em Continuar (Enter). | A tela Níveis organizacionais é exibida. |  |
| 5 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:Centro:1710 (centro 1 EUA)Org.vendas:1710 ( Org.vendas nac.EUA)Canal de distribuição:10 (vendas diretas)Em seguida, clique em Continuar (Enter). | Os dados organizacionais foram selecionados.A visão Criar material SRV_02 (despesas de serviço) é exibida. |  |
| 6 | Atualizar dados básicos | Na visão Dados básicos 1, atualize os seguintes valores:Descrição:despesas de serviçoPara todas as despesas, exceto EXP_FSM_MILEAGEUnidade de medida básica:Unid. (unidade)Para a despesa EXP_FSM_MILEAGEUnidade de medida básica:KM (quilômetro)Grupo de materiais:P002 (despesas)GrpItensGer.:SRVE (item de despesas)Em seguida, clique em Salvar. | Os dados básicos foram atualizados e a guia Vendas: organização de vendas 1 é exibida. |  |
| 7 | Atualizar dados da organização de vendas (1) | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados geraisDesconto: <selecionado>Dados do impostoClassificação fiscal:1 (imposto total)Em seguida, clique em Salvar. | Os dados organizacionais de vendas são atualizados. A guia Vendas: organização de vendas 2 é exibida. |  |
| 8 | Atualizar dados da organização de vendas (2) | Na guia Vendas: organização de vendas 2, atualize a seguinte entrada:Grupo de categorias de item:SRVE (item de despesas)Em seguida, clique em Salvar.Para a Polônia ou EXP_FSM_MILEAGE: pressione Enter em vez de Salvar. | Os dados organizacionais de vendas são atualizados. O produto de despesas é salvo. |  |
| 9 | Atualizar contabilidade 1(só para EXP_FSM_MILEAGE) | Na visão Contabilidade 1, atualize os seguintes valores:Avaliação atual- Classe de valor: por exemplo, 3300- Preço padrão: por exemplo, 1,50Em seguida, clique em Salvar. | Os dados de Contabilidade 1 são atualizados. O produto de despesas é salvo. |  |

#### SRV_03

Objetivo

Este material só é relevante para edição na nuvem.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados de produto (MDG). | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Escolha no app Criar material. | É exibido Criar material (1ª tela). |  |
| 3 | Atualizar dados básicos de material (para peça de reposição de produto dos serviços) | Em Criar material (primeira tela), efetue as seguintes entradas:Material:SRV_03Setor industrialMSe o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido no escuro. Atualmente, só existe uma entrada para o setor industrial (M = engenharia mecânica).Tipo de material:material não estocávelEm seguida, clique em Continuar (Enter). | Você atualizou as informações básicas para o novo produto dos serviços.É exibida a caixa de diálogo Selecionar visão(ões). |  |
| 4 | Clicar em visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Dados básicos 1Guia Vendas: Dados da organização de vendas 1Guia Vendas: Dados da organização de vendas 2Guia Vendas: Dados gerais/dados do centroComprasContabilidade 1Em seguida, clique em Continuar (Enter). | A tela Níveis organizacionais é exibida. |  |
| 5 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:Centro:1710 (centro 1 EUA)Org.vendas:1710 ( Org.vendas nac.EUA)Canal de distribuição:10 (vendas diretas)Em seguida, clique em Continuar (Enter). | Os dados organizacionais foram selecionados.É exibida a visão Criar material SRV_03 (Peça de reposição). |  |
| 6 | Atualizar dados básicos | Na visão Dados básicos 1, atualize os seguintes valores:Descr.:peça de reposiçãoUnidade de medida básica:Unid. (unidade)Grupo de materiais:YBMM00 (material não estocável sem ID)GrpItensGer.:SRVM (material de serviço)Em seguida, clique em Continuar (Enter). | Os dados básicos são atualizados e a guia Vendas: organização de vendas 1 é exibida.Nota Para cada idioma diferente utilizado na sua empresa, a descrição correspondente para o produto deve ser atualizada por código de idioma. |  |
| 7 | Atualizar dados da organização de vendas (1) | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados geraisDesconto: <selecionado>Dados do impostoClassificação fiscal:1 (imposto total)Em seguida, pressione Enter. | Os dados organizacionais de vendas são atualizados. A guia Vendas: organização de vendas 2 é exibida. |  |
| 8 | Atualizar dados da organização de vendas (2) | Na guia Vendas: organização de vendas 2, atualize a seguinte entrada:Grupo de categorias de item:SRVM (material de serviço) | Os dados organizacionais de vendas são atualizados. |  |
| 9 | Atualizar dados de compras | Na visão Compras, na seção Dados gerais, efetue as seguintes entradas:Unidade de medida básica: por exemplo, EAGrupo de materiais: por exemplo, YBM00Grupo de compradores: por exemplo, 001Cód.imp.p/material: por exemplo, 1Em seguida, clique em Continuar (Enter). | Os dados de compras são atualizados. |  |
| 10 | Atualizar dados contábeis | Na visão Contabilidade 1, na seção Dados da avaliação atuais, efetue as seguintes entradas:Classe de avaliação: por exemplo, YB01Controle de preço: por exemplo, SPreço padrão: por exemplo, 1Unidade de preço: por exemplo, 1Em seguida, clique em Salvar. | Os dados contábeis são atualizados.O produto dos serviços é salvo. O sistema exibe a visão Criar material (primeira tela). |  |

#### SRV_04

Objetivo

Este material só é relevante para edição na nuvem.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados de produto (MDG). | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Escolha no app Criar material. | É exibido Criar material (1ª tela). |  |
| 3 | Atualizar dados básicos de material (para peça de reposição administrada por produto dos serviços) | Em Criar material (primeira tela), efetue as seguintes entradas:● Material: SRV_04● Setor industrialMSe o campo de entrada Setor industrial estiver oculto, nenhuma entrada será necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido no escuro. Atualmente, só existe uma entrada para o setor industrial (M = engenharia mecânica).● Tipo de material: material não estocávelEm seguida, clique em Continuar (Enter). | Você atualizou as informações básicas para o novo produto dos serviços.É exibida a caixa de diálogo Selecionar visões. |  |
| 4 | Clicar em visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Dados básicos 1Guia Vendas: Dados da organização de vendas 1Guia Vendas: Dados da organização de vendas 2Guia Vendas: Dados gerais/dados do centroComércio internacional ExportaçãoComprasContabilidade 1Em seguida, clique em Continuar (Enter). | A tela Níveis organizacionais é exibida. |  |
| 5 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:● Centro: 1710 (Centro 1 EUA)● Org.vendas: 1710 ( Org.vendas nac.EUA)● Canal distrib.: 10 (vendas diretas)Em seguida, clique em Continuar (Enter). | Os dados organizacionais são selecionados.É exibida a visão Criar material SRV_04 (peça de reposição administrada (não estocável)). |  |
| 6 | Atualizar dados básicos | Na visão Dados básicos 1, atualize os seguintes valores:● Descr.: Peça de reposição administrada (não estocável)● Unidade de medida básica: Unid. (unidade)● Grupo de mercadorias: YBMM01 (material não estocável com ID)●GenItemGroup: SRVM (material de serviço)Em seguida, clique em Continuar (Enter). | Os dados básicos são atualizados e a guia Vendas: organização de vendas 1 é exibida.Nota Para cada idioma diferente utilizado na sua empresa, a descrição correspondente para o produto deve ser atualizada por código de idioma. |  |
| 7 | Atualizar dados da organização de vendas (1) | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados gerais• Desconto: <Selecionado>Dados do imposto• Classificação fiscal: 1 (imposto total)Em seguida, pressione Enter. | Os dados organizacionais de vendas são atualizados. A guia Vendas: organização de vendas 2 é exibida. |  |
| 8 | Atualizar dados da organização de vendas (2) | Na visão Vendas: organização de vendas 2, atualize a seguinte entrada:Grupo de categorias de item: SRVM (material de serviço)Em seguida, clique em Continuar (Enter). | Os dados organizacionais de vendas são atualizados. |  |
| 9 | Peça de reposição: atualizar dados de compras | Na visão Compras, na seção Dados gerais, efetue as seguintes entradas:• Unidade de medida básica: por exemplo, EA• Grupo de mercadorias: por exemplo, YBMM01• Grupo de compradores: por exemplo, 001Cód.imp.p/material: por exemplo, 1Em seguida, clique em Continuar (Enter). | Os dados de compras são atualizados. |  |
| 10 | Atualizar dados contábeis | Na visão Contabilidade 1, na seção Dados da avaliação atuais, efetue as seguintes entradas:• Classe de avaliação: por exemplo, YB01• Controle de preço: por exemplo, S• Preço padrão: por exemplo, 1• Unidade de determinação do preço: por exemplo, 1Em seguida, clique em Salvar. | Os dados contábeis são atualizados.O produto dos serviços é salvo.O sistema exibe a visão Criar material (primeira tela). |  |

#### SRV_BUNDLE_01

Objetivo

Este material só é relevante para edição na nuvem.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados de produto (MDG). | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Escolha no app Criar material. | É exibido Criar material (1ª tela). |  |
| 3 | Atualizar dados básicos de material (para serviço de produto dos serviços) | Em Criar material (primeira tela), efetue as seguintes entradas:● Material: SRV_BUNDLE_01● Setor industrialMSe o campo de entrada Setor industrial estiver oculto, nenhuma entrada será necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido no escuro. Atualmente, só existe uma entrada para o setor industrial (M = engenharia mecânica).● Tipo de material: Produto dos serviçosEm seguida, clique em Continuar (Enter). | Você atualizou as informações básicas para o novo produto dos serviços.É exibida a caixa de diálogo Selecionar visões. |  |
| 4 | Clicar em visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Dados básicos 1Guia Vendas: Dados da organização de vendas 1Guia Vendas: Dados da organização de vendas 2Guia Vendas: Dados gerais/dados do centroComércio internacional ExportaçãoEm seguida, clique em Continuar (Enter). | A tela Níveis organizacionais é exibida. |  |
| 5 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:● Centro: 1710 (Centro 1 EUA)● Org.vendas: 1710 ( Org.vendas nac.EUA)● Canal distrib.: 10 (vendas diretas)Em seguida, clique em Continuar (Enter). | Os dados organizacionais são selecionados.A visão Criar material SRV_BUNDLE_01 (serviços) é exibida. |  |
| 6 | Atualizar dados básicos | Na visão Dados básicos 1, atualize os seguintes valores:● Descr.: Preço fixo de pacote de serviços● Unidade de medida básica: Unid. (unidade)● Grupo de mercadorias: p001 (serviços)●GenItemGroup: SVBL (PF pacote de serviços)Em seguida, clique em Continuar (Enter). | Os dados básicos são atualizados e a guia Vendas: organização de vendas 1 é exibida.Nota Para cada idioma diferente utilizado na sua empresa, a descrição correspondente para o produto deve ser atualizada por código de idioma. |  |
| 7 | Atualizar dados da organização de vendas (1) | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados gerais• Desconto:X <selecionado>Dados do imposto• Classificação fiscal: 1 (imposto total)Em seguida, pressione Enter. | Os dados organizacionais de vendas são atualizados. A guia Vendas: organização de vendas 2 é exibida. |  |
| 8 | Atualizar dados da organização de vendas (2) | Na visão Vendas: organização de vendas 2, atualize a seguinte entrada:Grupo de categorias de item: SVBL (PF pacote de serviços)Em seguida, clique em Continuar (Enter). | Os dados organizacionais de vendas são atualizados. A guia Vendas: Geral/centro é exibida. |  |
| 9 | Atualizar dados gerais de venda | Na visão Vendas: Geral/centro, atualize os seguintes valores:• Unidade de medida básica: Unid. (unidade)• Duração de trabalho: por exemplo, 2 HR (horas)Em seguida, clique em Continuar (Enter). | Os dados gerais de venda são atualizados. |  |

#### SRV_BUNDLE_02

Objetivo

Este material só é relevante para edição na nuvem.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Escolha no app Criar material. | É exibido Criar material (1ª tela). |  |
| 3 | Atualizar dados básicos de material (para serviço de produto dos serviços) | Em Criar material (1ª tela), efetue as seguintes entradas:Material: SRV_BUNDLE_02Setor industrialMSe o campo de entrada Setor industrial estiver oculto, nenhuma entrada será necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido no escuro. Atualmente, só existe uma entrada para o setor industrial (M = engenharia mecânica).Tipo de material: Produto de serviçosEm seguida, clique em Continuar (Enter). | Você atualizou as informações básicas para o novo produto dos serviços.É exibida a caixa de diálogo Selecionar visões. |  |
| 4 | Clicar em visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Dados básicos 1Guia Vendas: Dados da organização de vendas 1Guia Vendas: Dados da organização de vendas 2Guia Vendas: Dados gerais/dados do centroEm seguida, clique em Continuar (Enter). | A tela Níveis organizacionais é exibida. |  |
| 5 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:Centro: 1710 (Centro 1 EUA)Org. vendas: 1710 ( Org.vendas nac.EUA)Canal de Distribuição:: 10 (vendas diretas)Em seguida, clique em Continuar (Enter). | Os dados organizacionais são selecionados.A visão Criar material SRV_BUNDLE_01 (serviços) é exibida. |  |
| 6 | Atualizar dados básicos | Na visão Dados básicos 1, atualize os seguintes valores:Descr.: Pacote de serviçosUnidade de medida básica: Unid. (unidade)Grupo de materiais: p001 (serviços)GenItemGroup: SVBV (pacote de serviços T&M)Em seguida, clique em Continuar (Enter). | Os dados básicos são atualizados e a guia Vendas: organização de vendas 1 é exibida.Nota Para cada idioma diferente utilizado na sua empresa, a descrição correspondente para o produto deve ser atualizada por código de idioma. |  |
| 7 | Atualizar dados da organização de vendas (1) | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados geraisDesconto: X <selecionado>Dados do impostoClassificação fiscal: 1 (imposto total)Em seguida, pressione Enter. | Os dados organizacionais de vendas são atualizados. A guia Vendas: organização de vendas 2 é exibida. |  |
| 8 | Atualizar dados da organização de vendas (2) | Na visão Vendas: organização de vendas 2, atualize a seguinte entrada:Grupo de categorias de item: SVBV (pacote de serviços)Em seguida, clique em Continuar (Enter). | Os dados organizacionais de vendas são atualizados. A guia Vendas: Geral/centro é exibida. |  |
| 9 | Atualizar dados gerais de venda | Na visão Vendas: Geral/centro, atualize os seguintes valores:Unidade de medida básica: Unid. (unidade)Duração de trabalho: por exemplo, 2 HR (horas)Em seguida, clique em Salvar. | Os dados gerais de venda são atualizados. |  |

#### SRV_05

##### Criar dados básicos

Objetivo

Este material só é relevante para edição na nuvem.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados de produto (MDG). | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Escolha no app Criar material. | A tela Criar material (1ª tela) é exibida. |  |
| 3 | Inserir dados básicos de material | Na tela Criar material (1ª tela)Material: SRV_05Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: Produtos comercializáveisClique em Selecionar visões. | Uma nova janela é aberta, Selecionar visões. |  |
| 4 | Clicar em Visões | Em Selecionar visões, selecione Dados básicos 1 e efetue as seguintes entradas: | É aberto Criar material SRV_05 (Produtos comercializáveis). |  |
| 5 | Inserir dados básicos | Insira:Descrição: Peça de reposição de estoqueNa seção Dados gerais, insira o seguinte:Unidade básica: UNGrupo de produtos: L001Setor de atividade: 00GrpCtgsItemGer.: SVST ou NORMNa seção Dimensões/EANs insira o seguinte:Peso bruto: 2Unidade de peso: KGPeso líquido: 1 | Nota Para cada idioma diferente utilizado na sua empresa, a descrição correspondente para o produto deve ser atualizada por código de idioma. |  |
| 6 | Preencher dados básicos | Não são necessárias entradas para Dados básicos 2; você não precisa efetuar entradas. |  |  |
| 7 | Salvar os dados | Na parte inferior direita do display, clique em Salvar para salvar os dados. | Exibe-se Criar material (1ª tela).Os dados básicos são criados e salvos. |  |

##### Criar dados de venda

Objetivo

Este material só é relevante para edição na nuvem.

Pré-requisito

Você deve completar a seção anterior, Criar dados básicos, antes de continuar com esta seção.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Escolha no app Criar material. | É exibido Criar material (visão inicial). |  |
| 2 | Inserir dados básicos de material | Na tela Criar material, efetue as seguintes entradas:Material: SRV_05Tipo de material: Produtos comercializáveisClique em Selecionar visões. | Depois de preencher as entradas, é aberta uma nova janela Marcar visão(ões). |  |
| 3 | Clicar em Visões | Na janela Marcar visões, selecione Vendas: Dados organizacionais de vendas 1, Vendas: dados organizacionais de vendas 2 e Vendas: dados gerais/do centro e clique em Continuar. | É exibida uma janela com Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Em Níveis organizacionais, na seção Nível organizacional, insira as descrições para o seguinte:Centro: 1710Org. vendas: 1710Canal de Distribuição:: 10Clique em Continuar.Nota As informações são exibidas na parte inferior da visão: O material já existe e será ampliado. | A visão Criar material SRV_05 (Produtos comercializáveis). |  |
| 5 | Inserir dados de vendas | Em Material SRV_05 (Produtos comercializáveis), a partir da guia Vendas: organização de vendas 1, na seção Dados gerais, efetue a seguinte entrada:Centro fornecedor: 1710 |  |  |
| 6 | Inserir dados de vendas | Em Material SRV_05 (Produtos comercializáveis), a partir da guia Vendas: organização de vendas 1, na seção Dados de imposto, efetue as seguintes entradasClassificação fiscal: 1Escolha a guia Vendas: Organização de vendas 2. | A seguinte guia Vendas: organização de vendas 2 é exibida. |  |
| 7 | Inserir dados de vendas | Na guia Vendas: organização de vendas 2, na seção Critérios de agrupamento efetue as seguintes entradas:Mat.grp.class.cont.: 01Grupo de categorias de item: SVST ou NORMEscolha a guia Vendas: geral/centro. | A seguinte guia Vendas: geral/centro é exibida. |  |
| 8 | Inserir dados de vendas | Na guia Vendas: geral/centro, na seção Dados gerais, insira os seguintes dados:Verificação de disponibilidade: SP |  |  |
| 9 | Inserir dados de vendas | Na guia Vendas: geral/centro, na seção Dados de expedição (tempos em dias), insira os seguintes dados:Grupo transp.: 0001Grp.carregamento: 0001 |  |  |
| 10 | Inserir dados de vendas | Na seção Parâmetros gerais de centro, insira os seguintes dados:Centro de lucro: <YB700> |  |  |
| Só para a Polônia | Inserir dados de vendas | Na seção Comércio internacional: exportação, insira os seguintes dados:Código de controle: por exemplo, 41.00,30,0 | O código PKWiU é atualizado para a Polônia. |  |
| 11 | Salvar os dados | Na parte inferior da tela, clique em Salvar. | Os dados estão salvos. |  |

##### Criar dados de compras

Objetivo

Este material só é relevante para edição na nuvem.

Pré-requisito

Você deve completar os procedimentos anteriores, antes de continuar com esta seção.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Clique no bloco do app Criar material. | Criar material (1ª tela) é exibido. |  |
| 2 | Inserir dados básicos de material | Na tela Criar material, efetue as seguintes entradas:Material: SRV_05Tipo de material:produtos comercializáveis (HAWA)Clique em Selecionar visões. | A tela Seleção de visões é aberta. |  |
| 3 | Clicar em Visões | Na janela Selecionar visões, selecione Compras e, em seguida, Continuar. | São exibidos Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais, na seção Nível organizacional, efetue a entrada seguinte:Centro: 1710Clique em Continuar.Nota É exibida uma mensagem na parte inferior da tela: O material já existe e será ampliado. | É aberto Criar material SRV_05 (Produtos comercializáveis). |  |
| 5 | Inserir dados de compras | Na tela Material SRV_05 (produtos comercializáveis), na guia Compras, na seção Dados gerais, efetue as seguintes entradas:Grupo de compradores: 001Grupo de mercadorias: L001 |  |  |
| 6 | Inserir dados de compras | Na seçãoOutros dados/dados de fabricante, efetue a seguinte entrada:Tempo de processamento da entrada de mercadorias: por exemplo, 1 |  |  |
| 7 | Salvar os dados | Na parte inferior da tela, clique em Salvar. | Os dados estão salvos. |  |

##### Criar dados MRP/planejamento

Objetivo

Este material só é relevante para edição na nuvem.

Pré-requisito

Você deve completar os procedimentos anteriores, antes de continuar com esta seção.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Escolha no app Criar material. | Exibe-se Criar material (primeira tela). |  |
| 2 | Inserir dados básicos de material | Na tela Criar material, efetue as seguintes entradas:Material: SRV_05Tipo de material: Produtos comercializáveisClique em Selecionar visões. | A tela Seleção de visões é aberta. |  |
| 3 | Clicar em Visões | Na janela Marcar visão(ões), selecione MRP1, MRP2, MRP3 e MRP4 e clique em Continuar. | Níveis organizacionais é exibida. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais, na seção Nível organizacional, efetue as seguintes entradas:Centro: 1710Depósito: 171ANota São exibidas informações na parte inferior da tela: O material já existe e será ampliado. | A tela Criar material SRV_05 (Produtos comercializáveis) é aberta. |  |
| 5 | Inserir dados MRP/de planejamento | Na tela Material SRV_05 (produtos comercializáveis), na guia MRP1, na seção Dados gerais, efetue as seguintes entradas:Tipo de MRP: NDPlanejador MRP: <001> |  |  |
| 6 | Inserir dados MRP/de planejamento | Na seçãoDados do tamanho do lote, efetue a seguinte entrada:Procedimento de dimensionamento de lotes: <EX>Selecione a guia seguinte, MRP 2 | A guia seguinte, MRP 2 é aberta. |  |
| 7 | Inserir dados MRP/de planejamento | Na tela Criar material SRV_05 (Produtos comercializáveis), na guia MRP 2, na seção Suprimento, efetue as seguintes entradas:Tipo de suprimento: XNa seção Programação, efetue as seguintes entradas:Prazo de entrega planejado: por exemplo, 3Tempo de processamento da entrada de mercadorias: por exemplo, 1Chave de prazos: por exemplo, 000Selecione a guia seguinte, MRP 3. | A guia seguinte, MRP 3 é aberta. |  |
| 8 | Inserir dados MRP/de planejamento | Na tela Criar material (produtos comercializáveis), na guia MRP 3, na seção Planejamento, efetue as seguintes entradas:Grupo de estratégias: por exemplo, 40 |  |  |
| 9 | Inserir dados MRP/de planejamento | Na seção Verificação de disponibilidade, efetue as seguintes entradas:Verificação de disponibilidade: NCTempo total reposição por exemplo, 3Selecione a guia seguinte, MRP 4 | A guia seguinte, MRP 4 é aberta. |  |
| 10 | Inserir dados MRP/de planejamento | Na tela Criar material SRV_05 (Produtos comercializáveis), na guia MRP 4, na seção Explosão lista técnica/necessidades secundárias, efetue as seguintes entradas:Indiv./colet.: <em branco> |  |  |
| 11 | Salvar os dados | Na parte inferior da tela, clique em Salvar. | Os dados estão salvos. |  |

##### Criar dados do depósito

Objetivo

Este material só é relevante para edição na nuvem.

Pré-requisito

Você deve completar os procedimentos anteriores, antes de continuar com esta seção.

|  |
| --- |
| Nota Primeiro, você cria uma visão para o depósito 171A, em seguida, cria a mesma para o depósito 171B. |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Clique no bloco do app Criar material. | Exibe-se Criar material (primeira tela). |  |
| 2 | Inserir dados básicos de material | Na tela Criar material, efetue as seguintes entradas:Material: SRV_05Tipo de material: Produtos comercializáveisClique em Selecionar visões. | Selecionar visões é aberta. |  |
| 3 | Clicar em Visões | Na janela Marcar visão(ões), selecione as seguintes visões:Dados gerais do centro/armazenamento 1Dados gerais do centro/armazenamento 2Clique em Continuar. | São exibidos Níveis organizacionais. |  |
| 4 | Inserir dados dos níveis organizacionais | Na seção Unidades organizacionais, na seção Nível organizacional, efetue as seguintes entradas:Centro: 1710Depósito:171ANota São exibidas informações na parte inferior da tela: O material já existe e será ampliado. | É aberto Criar material SRV_05 (Produtos comercializáveis). |  |
| 5 | Inserir dados do depósito | Na tela Criar material SRV_05 (Produtos comercializáveis), na guia Dados centro/depósito 1, na seção Dados gerais, efetue a seguinte entrada:Número de notas de EM: por exemplo, 1 | A guia seguinte Dados centro/depósito 2 é aberta. |  |
| 6 | Inserir dados do depósito | Na tela Criar material SRV_05 (Produtos comercializáveis), na guia Dados centro/depósito 2, na seção Dados gerais, efetue a seguinte entrada:Centro de lucro: YB700 |  |  |
| 7 | Salvar os dados | Na parte inferior do display, clique em Salvar. | Dados mestre-produto é exibido.Os dados estão salvos. |  |

##### Criar dados contábeis

Objetivo

Este material só é relevante para edição na nuvem.

Pré-requisito

Você deve completar os procedimentos anteriores, antes de continuar com esta seção.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Escolha no app Criar material. | É aberta uma nova janela exibindo Criar material (1ª tela). |  |
| 2 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: SRV_05Tipo de material: Produtos comercializáveis HAWAClique em Selecionar visões. | Selecionar visões é aberta. |  |
| 3 | Clicar em Visões | Em Selecionar visões, selecione as seguintes visões:Contabilidade 1Clique em Continuar. | A tela Níveis organizacionais é aberta. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais, na seção Nível organizacional, efetue as seguintes entradas:Centro: 1710Nota São exibidas informações na parte inferior da tela: O material já existe e será ampliado. | É aberto Criar material SRV_05 (Produtos comercializáveis). |  |
| 5 | Inserir dados contábeis | Na tela Criar material SRV_05 (produtos comercializáveis), na guia Contabilidade 1, na seção Dados de avaliação gerais, efetue a seguinte entrada:Classe de avaliação: 3100Determ.preço: 2 (baseada na transação) |  |  |
| 6 | Inserir dados contábeis | Na seçãoPreços e valores, efetue as seguintes entradas:Preço padrão: por exemplo, 13,50Controle de preço: S |  |  |
| 7 | Salvar os dados | Na parte inferior do display, clique em Salvar. | A janela produto de dados mestre é exibida.Os dados estão salvos. |  |

### Definir preços para materiais

#### Preço para SRV_01

Objetivo

Este material só é relevante para edição na nuvem.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | O launchpad do SAP Fiori é aberto. |  |
| 2 | Acessar o app SAP Fiori | Clique em Definir preços de material - Vendas. | A visão Modificar registros de condições é exibida. |  |
| 3 | Tipo de condição para determinação de preços | Na visão Modificar registros de condição, insira as seguintes informações:Tipo de condição: PPR0Em seguida, pressione Enter. | A visão Combinação de chaves é exibida. |  |
| 4 | Combinação de chaves | Na visão Combinação de chaves, selecione a opção Material com status de liberação.Em seguida, selecione Selecionar (ENTER). | A visão Modificar preço (PPR0): seleção é exibida. |  |
| 5 | Seleção | Na visão Modificar preço (PPR0): seleção, atualize as seguintes informações:Org. vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Material:SRV_01 (produto dos serviços)Válido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição para determinação de preços (PPR0): síntese é exibida. |  |
| 6 | Modificar condição de preço | Na tela Modificar condição de preço (PPR0): Síntese, atualize os seguintes dados para o material SRV_01:Material: por exemplo, SRV_01 (produto dos serviços)Montante : por exemplo, 35,00Unidade: USDVálido desde: <Data>, por exemplo, a data de hojePressione Enter. | As condições de preço para produtos dos serviços SRV_01 foram atualizadas. |  |
| 7 | Salvar | Clique em Salvar. | Os preços para os produtos dos serviços foram definidos. |  |

#### Preço para SRV_CONTRACT

Objetivo

Este material é relevante para edição na nuvem e edição local.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | O launchpad do SAP Fiori é aberto. |  |
| 2 | Acessar o app SAP Fiori | Clique em Definir preços de material - Vendas. | A visão Modificar registros de condições é exibida. |  |
| 3 | Tipo de condição para determinação de preços | Na visão Modificar registros de condição, insira as seguintes informações:Tipo de condição: PSI1Em seguida, pressione Enter. | A visão Combinação de chaves é exibida. |  |
| 4 | Combinação de chaves | Na visão Combinação de chaves, selecione Material.Em seguida, pressione Enter. | A visão Alterar preço (PSI1): seleção é exibida. |  |
| 5 | Seleção | Na visão Modificar preço (PSI1): seleção, atualize as seguintes informações:Org. vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Material:SRV_CONTRACT (Produto do contrato de serviços)Válido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição para determinação de preços (PPSI): síntese é exibida. |  |
| 6 | Modificar condição de preço | Na visão Modificar condição de preço (PSI1): Síntese, atualize os seguintes dados para o material SRV_CONTRACT:Material: por exemplo, SRV_CONTRACT (produto do contrato de serviços)Montante : por exemplo, 100,00Unidade: por exemplo, USDVálido desde: <Data>, por exemplo, a data de hojePressione Enter. | As condições de preço para o produto do contrato de serviços SRV_CONTRACT são atualizadas. |  |
| 7 | Salvar | Clique em Salvar. | O preço para o produto do contrato de serviços é salvo. |  |

#### Preço para SRV_CTR_RENEWAL

Objetivo

Este material é relevante para edição na nuvem e edição local.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | O launchpad do SAP Fiori é aberto. |  |
| 2 | Acessar o app SAP Fiori | Clique em Definir preços de material - Vendas. | A visão Modificar registros de condições é exibida. |  |
| 3 | Tipo de condição para determinação de preços | Na visão Modificar registros de condição, insira as seguintes informações:Tipo de condição: PSI1Em seguida, pressione Enter. | A visão Combinação de chaves é exibida. |  |
| 4 | Combinação de chaves | Na visão Combinação de chaves, selecione Material.Em seguida, pressione Enter. | A visão Alterar preço (PSI1): seleção é exibida. |  |
| 5 | Seleção | Na visão Modificar preço (PSI1): seleção, atualize as seguintes informações:Org. vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Material:SRV_CTR_RENEWAL (produto de prorrogação do contrato de serviços)Válido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição para determinação de preços (PPSI): síntese é exibida. |  |
| 6 | Modificar condição de preço | Na visão Modificar condição de preço (PSI1): síntese, atualize os seguintes dados para o material SRV_CTR_RENEWAL:Material: por exemplo, SRV_CTR_RENEWAL (produto de prorrogação do contrato de serviços)Montante : por exemplo, 90,00Unidade: por exemplo, USDVálido desde: <Data>, por exemplo, a data de hojePressione Enter. | As condições de preço para produtos do contrato de serviços SRV_CTR_RENEWAL são atualizadas. |  |
| 7 | Salvar | Clique em Salvar. | Os preços para os produtos do contrato de serviços foram definidos. |  |

#### Preço para SRV_02

Objetivo

Este material é relevante para edição na nuvem e edição local.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | O launchpad do SAP Fiori é aberto. |  |
| 2 | Acessar o app SAP Fiori | Clique em Definir preços de material - Vendas. | A visão Modificar registros de condições é exibida. |  |
| 3 | Tipo de condição para determinação de preços | Na visão Modificar registros de condição, insira as seguintes informações:Tipo de condição: PPR0Em seguida, pressione Enter. | A visão Combinação de chaves é exibida. |  |
| 4 | Combinação de chaves | Na visão Combinação de chaves, selecione Material com status de liberação.Em seguida, pressione Enter. | A visão Modificar preço (PPR0): seleção é exibida. |  |
| 5 | Seleção | Na visão Modificar preço (PPR0): seleção, atualize as seguintes informações:Org. vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Material:SRV_02 (despesas de serviço)Válido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição para determinação de preços (PPR0): síntese é exibida. |  |
| 6 | Modificar condição de preço | Na tela Modificar condição de preço (PPR0): síntese, atualize os seguintes dados para o material SRV_02:Material: por exemplo, SRV_02 (serviços)Montante : por exemplo, 15,00Unidade: por exemplo, USDVálido desde: <Data>, por exemplo, a data de hojePressione Enter. | As condições de preço para produtos dos serviços SRV_02 são atualizadas. |  |
| 7 | Salvar | Clique em Salvar. | Os preços para os produtos dos serviços foram definidos. |  |

#### Preço para SRV_04

Objetivo

Este material só é relevante para edição na nuvem.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | O launchpad do SAP Fiori é aberto. |  |
| 2 | Acessar o app SAP Fiori | Clique em Definir preços de material - Vendas. | A visão Modificar registros de condições é exibida. |  |
| 3 | Tipo de condição para determinação de preços | Na visão Modificar registros de condição, insira as seguintes informações:Tipo de condição: PPR0Em seguida, pressione Enter. | A visão Combinação de chaves é exibida. |  |
| 4 | Combinação de chaves | Na visão Combinação de chaves, selecione Material com status de liberação.Em seguida, pressione Enter. | A visão Modificar preço (PPR0): seleção é exibida. |  |
| 5 | Seleção | Na visão Modificar preço (PPR0): seleção, atualize as seguintes informações:Org. vendas: 1710 ( Org.vendas nac.EUA)Canal de Distribuição:: 10 (vendas diretas)Material:SRV_04 (Peça de reposição administrada (não estocável))Válido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição para determinação de preços (PPR0): síntese é exibida. |  |
| 6 | Modificar condição de preço | Na tela Modificar condição de preço (PPR0): síntese, atualize os seguintes dados para o material SRV_04:Material: SRV_04 (Peça de reposição administrada (não estocável))Montante : por exemplo, 15,00Unid: USDVálido desde: <Data>, por exemplo, a data de hojePressione Enter. | As condições de preço para produtos dos serviços SRV_04 são atualizadas. |  |
| 7 | Salvar | Clique em Salvar. | Os preços para os produtos dos serviços foram definidos. |  |

#### Preço para SRV_BUNDLE_01

Objetivo

Este material só é relevante para edição na nuvem.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | O launchpad do SAP Fiori é aberto. |  |
| 2 | Acessar o app SAP Fiori | Clique em Definir preços de material - Vendas. | A visão Modificar registros de condições é exibida. |  |
| 3 | Tipo de condição para determinação de preços | Na visão Modificar registros de condição, insira as seguintes informações:Tipo de condição: PPR0Em seguida, pressione Enter. | A visão Combinação de chaves é exibida. |  |
| 4 | Combinação de chaves | Na visão Combinação de chaves, selecione Material com status de liberação.Em seguida, pressione Enter. | A visão Modificar preço (PPR0): seleção é exibida. |  |
| 5 | Seleção | Na visão Modificar preço (PPR0): seleção, atualize as seguintes informações:Org. vendas: 1710 ( Org.vendas nac.EUA)Canal de Distribuição:: 10 (vendas diretas)Material:SRV_BUNDLE_01 (Pacote de serviços 01)Válido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição para determinação de preços (PPR0): síntese é exibida. |  |
| 6 | Modificar condição de preço | Na tela Modificar condição de preço (PPR0): Síntese, atualize os seguintes dados para o material SRV_01:Material: SRV_BUNDLE_01 (Pacote de serviços 01)Montante : por exemplo, 200,00Unid: USDVálido desde: <Data>, por exemplo, a data de hojePressione Enter. | As condições de preço para produtos dos serviços SRV_BUNDLE_01 são atualizadas. |  |
| 7 | Salvar | Clique em Salvar. | Os preços para os produtos dos serviços foram definidos. |  |

#### Preço para SRV_05

Objetivo

Este preço do material só é relevante para edição na nuvem.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | O launchpad do SAP Fiori é aberto. |  |
| 2 | Acessar o app SAP Fiori | Clique em Definir preços de material - Vendas. | A visão Modificar registros de condições é exibida. |  |
| 3 | Tipo de condição para determinação de preços | Na visão Modificar registros de condição, insira as seguintes informações:Tipo de condição: PPR0Em seguida, pressione Enter. | A visão Combinação de chaves é exibida. |  |
| 4 | Combinação de chaves | Na visão Combinação de chaves, selecione a opção Material com status de liberação.Em seguida, selecione Selecionar (ENTER). | A visão Modificar preço (PPR0): seleção é exibida. |  |
| 5 | Seleção | Na visão Modificar preço (PPR0): seleção, atualize as seguintes informações:Org. vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Material: SRV_05 (Peça de reposição de estoque)Válido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição para determinação de preços (PPR0): síntese é exibida. |  |
| 6 | Modificar condição de preço | Na tela Modificar condição de preço (PPR0): Síntese, atualize os seguintes dados para o material SRV_01:Material: SRV_05 (Peça de reposição de estoque)Montante: por exemplo, 14,50Unidade: USDVálido desde: <Data>, por exemplo, a data de hojePressione Enter. | A condição de correção de preço para produtos dos serviços SRV_01 foi atualizada. |  |
| 7 | Salvar | Clique em Salvar. | Os preços para os produtos dos serviços foram definidos. |  |

#### Preço para FSM - Despesa EXP_FSM_MILEAGE

Objetivo

Este material é relevante para edição na nuvem e edição local.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | O launchpad do SAP Fiori é aberto. |  |
| 2 | Acessar o app SAP Fiori | Abra Definir preços de material – Vendas | A visão Modificar registros de condições é exibida. |  |
| 3 | Tipo de condição para determinação de preços | Na visão Modificar registros de condição, insira as seguintes informações:Tipo de condição: PCO4Em seguida, pressione Enter. | A visão Combinação de chaves é exibida. |  |
| 4 | Combinação de chaves | Na visão Combinação de chaves, selecione Material com status de liberação.Em seguida, pressione Enter. | A visão Modificar preço (PCO4): seleção é exibida. |  |
| 5 | Seleção | Na visão Modificar preço (PCO4): seleção, atualize as seguintes informações:Org. vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Material:EXP_FSM_MILEAGEVálido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição para determinação de preços (PCO4): síntese é exibida. |  |
| 6 | Modificar condição de preço | Na visão Modificar condição de preço (PCO4): síntese, atualize os seguintes dados para o material EXP_FSM_MILEAGE:Material: por exemplo, EXP_FSM_MILEAGEMontante : por exemplo, 1.50 (preço por unidade)Unidade: por exemplo, USDVálido desde: <Data>, por exemplo, a data de hojePressione Enter. | As condições para determinação de preços para o produto dos serviços EXP_FSM_MILEAGE são atualizadas. |  |
| 7 | Salvar | Clique em Salvar. | Os preços para os produtos dos serviços foram definidos. |  |

### Definir preços para horas extras

Objetivo

Este procedimento descreve como definir preços para horas extras, Este capítulo só é relevante para 3D2 edição na nuvem).

|  |
| --- |
| Nota Antes de atualizar os preços para horas extras, você tem que criar primeiro as "Categorias de horas extras".Você encontrará a descrição no script de teste 3D2, capítulo "2.5.6 Atualizar categoria de horas extras". |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | O launchpad do SAP Fiori é aberto. |  |
| 2 | Acessar o app SAP Fiori | Clique em Definir preços de material de Vendas. | A visão Modificar registros de condições é exibida. |  |
| 3 | Tipo de condição para determinação de preços | Na visão Modificar registros de condição, insira as seguintes informações:Tipo de condição: SOV1 ou SOV2Em seguida, pressione Enter. | A tela Modificar horas extras (SOV1): seleção ou Modificar horas extras (SOV 2 ): seleção é aberta.Info:Se SOV1 tiver sido selecionado como registro de condição, você pode atualizar um valor absoluto como preço.Se SOV2 tiver sido selecionado como registro de condição, você pode atualizar um valor percentual para o cálculo do preço. |  |
| 4 | Seleção | Na visão Modificar horas extras (SOV1): seleção ou Modificar horas extras (SOV 2 ): seleção, atualize as seguintes informações:Org.vendas:1710 ( Org.vendas nac.EUA)Canais de distribuição:10 (vendas diretas)Válido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar horas extras (SOV1): Síntese ou Modificar horas extras (SOV 2): síntese é exibida. |  |
| 5 | Modificar condição de preço | Na visão Modificar horas extras (SOV1): seleção ou Modificar horas extras (SOV 2 ): Seleção,, atualize uma ou mais condições de preço para horas extras:Horas extras: por exemplo, OV01, OV02, OV03Montante: por exemplo, 30 ou 50Unid: por exemplo, USD ou %UM: por exemplo, HRVálido desde: <Data>, por exemplo, a data de hojePressione Enter. |  |  |
| 6 | Salvar | Clique em Salvar. | As condições de preço para o cálculo de horas extras foram criadas |  |

### Criar registro de condição para critério para cálculo

Objetivo

Nesta etapa, você define registros de condições para critérios para cálculo. Esta condição pode ser utilizado em ordens de serviço para diferenciar entre itens faturáveis, não faturáveis e parcialmente faturáveis para fins de determinação do preço e de controlling. Os serviços não faturáveis e parcialmente faturáveis são, por exemplo, os serviços fornecidos com garantia ou tolerância. O registro de condições para código de contabilidade é opcional e somente para a edição na nuvem.

Procedimento (usando o launchpad do SAP Fiori)

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Efetuar login | Efetue login no launchpad do SAP Fiori como especialista em preços. | O launchpad do SAP Fiori é aberto. |  |
| 2 | Acessar o app SAP Fiori | Selecione Definir preços de material - Vendas | A visão Modificar registros de condições é exibida. |  |
| 3 | Tipo de condição para determinação de preços | Na visão Modificar registros de condição, insira as seguintes informações:Tipo de condição: DAI2Em seguida, pressione Enter. | A visão Modificar critério para cálculo (DAI2): seleção é exibida. |  |
| 4 | Seleção | Na visão Modificar critério para cálculo (DAI2): seleção, atualize as seguintes informações:Organização de vendas: por exemplo, 1710 ( Org.vendas nac.EUA)Canal distr.: por exemplo, 10 (vendas diretas)Válido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição de critério para cálculo (%) (DAI2): síntese é exibida. |  |
| 5 | Criar registro de condição | Na visão Modificar condição de critério para cálculo (%) (DAI2): síntese, crie a seguinte condição para SRV_01:Organização de vendas: por exemplo, 1710 ( Org.vendas nac.EUA)Canal distrib.: por exemplo, <10> (vendas diretas)Material: por exemplo, <SRV_01>Crit.p/cálc.: S1Montante: por exemplo, <-100>Tipo cálc.: AVálido desde:<data> por exemplo, a data de hojeVálido até:<Data> por exemplo, a data de hoje.Selecione Enter. | A condição para determinação de preços foi atualizada. |  |
| 6 | Salvar | Clique em Salvar. | São criados registros de condição para critério para cálculo para o produto dos serviços. |  |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: SRV_06 is listed in the overview table but has no creation procedure in the document

> [!warning] Conflict
> Flagged while digesting this document, not verified: Some price steps for SRV_BUNDLE_01 and SRV_05 refer to material SRV_01 in instructions/results (copy-paste inconsistency)

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview says SRV_03/SRV_04 are 'only supplied' non-stock, while the SRV_03 outline label says undefined and SRV_04 defined spare part; SRV_05 item group given as 'SVST or NORM' alternatives

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-service-product-for-service-processes-mds-3k]]
- related-to :: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-3kv-349]]
- related-to :: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-mds-3kv-351]]
- related-to :: [[14-maintenance-service-and-projects/script-de-datos-maestros-creacion-de-producto-de-servicio-para-proceso]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KV_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 74,388 chars in the whole document
