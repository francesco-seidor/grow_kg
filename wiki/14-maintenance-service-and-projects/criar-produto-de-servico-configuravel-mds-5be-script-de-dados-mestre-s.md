---
id: 14-maintenance-service-and-projects/criar-produto-de-servico-configuravel-mds-5be-script-de-dados-mestre-s
title: Criar produto de serviço configurável - MDS (5BE) - Script de dados mestre SAP S/4HANA Cloud Public Edition 2608 (5BE_S4CLD2608_Master_Data_PT_XX)
description: "SAP Best Practices master data script (PT, 5BE): step-by-step creation of configurable service products, classes, characteristics, config profiles and variant prices in S/4HANA Cloud 2608."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/configurable-service-products]
aliases: [5BE_S4CLD2608_Master_Data_PT_XX]
keywords: [Configurable Service Products and Advanced Variant…, configurable service products, service contract products, service order products, characteristics, classes, configuration profile, variant pricing, material variants, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BE_S4CLD2608_Master_Data_PT_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-434
topic: 14-maintenance-service-and-projects/configurable-service-products
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar produto de serviço configurável - MDS (5BE) - Script de dados mestre SAP S/4HANA Cloud Public Edition 2608 (5BE_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BE_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Configurable Service Products and Advanced Variant Configuration** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar produto de serviço configurável - MDS (5BE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 3](#_Toc233893755)

[2 Pré-requisitos 4](#_Toc233893756)

[2.1 Acesso ao sistema 4](#_Toc233893757)

[2.2 Funções 4](#_Toc233893758)

[2.3 Unidades organizacionais necessárias 4](#_Toc233893759)

[2.4 Dados mestre obrigatórios e operacionais 5](#_Toc233893760)

[2.5 Etapas preliminares (obrigatórias) 5](#_Toc233893761)

[3 Tabela de síntese 7](#_Toc233893762)

[4 Procedimentos 8](#_Toc233893763)

[4.1 Criar produto dos serviços configurável para contratos de prestação de serviços 8](#_Toc233893764)

[4.1.1 Criar características 8](#_Toc233893765)

[4.1.2 Criar classe 10](#_Toc233893766)

[4.1.3 Criar produto dos serviços configurável para contratos 11](#_Toc233893767)

[4.1.4 Criar perfil de configuração 14](#_Toc233893768)

[4.1.5 Definir preços 15](#_Toc233893769)

[4.2 Criar produto dos serviços configurável para ordens de serviço 17](#_Toc233893770)

[4.2.1 Criar características 17](#_Toc233893771)

[4.2.2 Criar classe 21](#_Toc233893772)

[4.2.3 Criar produto dos serviços configurável para ordem de serviço 22](#_Toc233893773)

[4.2.4 Criar perfil de configuração 24](#_Toc233893774)

[4.2.5 Definir preços 25](#_Toc233893775)

[4.3 Criar variante de material para um produto de serviços 28](#_Toc233893776)

[4.3.1 Definir preços para variante do material 30](#_Toc233893777)

## Objetivo

Neste documento, você encontra uma descrição sobre como criar produtos de serviços configuráveis para contratos de prestação de serviços e ordens de serviço, bem como os preços relacionados. A descrição inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema "normal". O leitor aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo do fornecimento de conteúdo do S/4HANA, por SAP Best Practices, não são descritos neste documento, apesar de eles poderem aparecer na IU.

Os produtos de serviços configuráveis criados como descrito aqui podem ser utilizados para processamento de contrato de prestação de serviços e processamento de ordens de serviço. Para utilizar o produto dos serviços configurável, consulte o item de escopo Administração de serviços com configuração de variante avançada (6GS) ou Gerenciamento contrato prestação serviços c/configuração variante avançada (6GU).

A funcionalidade da configuração do produto que pode ser utilizada em contratos de prestação de serviços e ordens de serviço é a mesma que está descrita no item de escopo 22T - Definição de modelo configurável utilizando configuração de variantes.

## Pré-requisitos

### Acesso ao sistema

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece o URL para acessar os vários apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

| Nome | ID |
| --- | --- |
| Modelador de configuração de produto | SAP_BR_PRODUCT_CONFIG_MODELER |
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST |
| Especialista em preços | SAP_BR_PRICING_SPECIALIST |

Além disso, a seguinte função é relevante para o usuário de configuração que cuida das Etapas preliminares obrigatórias descritas abaixo:

| Nome | ID |
| --- | --- |
| Especialista de configuração - configuração de processo empresarial | SAP_BR_BPC_EXPERT |

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre são dependentes das unidades organizacionais da empresa. Os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Unidade organizacional a ser usada | Comentários |
| --- | --- | --- | --- |
| Criar material | Centro | 1710 (centro 1 EUA) | Para a Alemanha, use 1010 (centro 1 DE) |
| Criar material | Organização de vendas | 1710 ( Org.vendas nac.EUA) | Para a Alemanha, use 1010 ( Org.vendas nacional DE) |
| Criar material | Canal de distribuição | 10 (vendas diretas) | Para a Alemanha, use 10 (vendas diretas) |

### Dados mestre obrigatórios e operacionais

Os registros de dados mestre de materiais podem fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre de materiais.

|  |
| --- |
| Nota Os campos específicos do Brasil são necessários para obter um cálculo de imposto adequado.Verifique Nota Fiscal Brasil - JD0 no capítulo Definir campos específicos do BR para dados mestre para dados mestre de materiais. |

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Centro de lucro |  | Obrigatório | A atribuição de um centro de lucro a um mestre de materiais (produtos) é necessária para os processos de avaliação corretos. |

### Etapas preliminares (obrigatórias)

Utilização

Antes de criar o produto dos serviços configurável como descrito no procedimento seguinte, você deve ativar primeiro o tipo de material existente SERV (Serviços) para utilizar dados de classificação.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista de configuração - configuração de processo empresarial. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app | Abra o app Administrar sua solução. | O app Administrar sua solução é exibido. |  |
| 3 | Configurar sua solução | Na tela Administrar sua solução, selecione Configurar sua solução. | A tela Configurar sua solução: fase de realização é exibida. |  |
| 4 | Abrir o item do produto para configuração | Nos filtros de pesquisa, efetue as seguintes entradas:Área de aplicação: <Banco de dados e gerenciamento de dadosÁrea de subaplicação: ProdutoEscolha o registro Produto nos resultados da pesquisa. | É exibida a tela Configurar sua solução. |  |
| 5 | Configurar sua solução – Produto | Na seção Etapas de configuração em Definir atributos de tipos de material, clique em Configurar. | A tela Definir atributos de tipos de material: Alterar é exibida. |  |
| 6 | Abrir atributos do tipo de material SERV | Clique duas vezes na entrada SERV – Produto do serviço. | A tela Definir atributos de tipos de material: Modificar: detalhes é exibida. |  |
| 7 | Ativar classificação | Na lista Departamentos do usuário, selecione Classificação.Atenção Antes de salvar as alterações na configuração, verifique se as seleções preexistentes na lista Departamentos do usuário também estão selecionadas. |  |  |
| 8 | Salvar os dados | Clique em Salvar. |  |  |

Resultado

Ao criar produtos do tipo SERV – Produto dos serviços, a guia Classificação é ativada.

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

| Segmento | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar características](#unique_8) [página ] 8 | SAP_BR_PRODUCT_CONFIG_MODELER | Administrar características | São criadas características para a classe de contrato de prestação de serviços. |
| [Criar classe](#unique_9) [página ] 10 | SAP_BR_PRODUCT_CONFIG_MODELER | Administrar classes | A classe é criada. |
| [Criar produto dos serviços configurável para contratos](#unique_10) [página ] 11 | SAP_BR_PRODMASTER_SPECIALIST | Criar material | O produto dos serviços para contratos de prestação de serviços é criado. |
| [Criar perfil de configuração](#unique_11) [página ] 14 | SAP_BR_PRODUCT_CONFIG_MODELER | Ambiente de modelagem de configuração de variantes | O perfil de configuração é criado. |
| [Definir preços](#unique_12) [página ] 15 | SAP_BR_PRICING_SPECIALIST | Definir preços de material | Os preços são definidos. |
| [Criar características](#unique_13) [página ] 17 | SAP_BR_PRODUCT_CONFIG_MODELER | Administrar características | São criadas características para a classe de contrato de prestação de serviços. |
| [Criar classe](#unique_14) [página ] 21 | SAP_BR_PRODUCT_CONFIG_MODELER | Administrar classes | A classe é criada. |
| [Criar produto dos serviços configurável para ordem de serviço](#unique_15) [página ] 22 | SAP_BR_PRODMASTER_SPECIALIST | Criar material | O produto de serviços para a ordem de serviço é criado. |
| [Criar perfil de configuração](#unique_16) [página ] 24 | SAP_BR_PRODUCT_CONFIG_MODELER | Ambiente de modelagem de configuração de variantes | O perfil de configuração é criado. |
| [Definir preços](#unique_17) [página ] 25 | SAP_BR_PRICING_SPECIALIST | Definir preços de material | Os preços para produtos dos serviços estão definidos. |
| [Criar variante de material para um produto de serviços](#unique_18) [página ] 28 | SAP_BR_PRODMASTER_SPECIALIST | Criar material | Uma variante do material para um produto de serviços configurável é criada. |
| [Definir preços para variante do material](#unique_19) [página ] 30 | SAP_BR_PRICING_SPECIALIST | Definir preços de material | O preço para uma variante do material é definido. |

## Procedimentos

Esta seção descreve procedimentos para cada segmento ou etapa do processo que faz parte deste registro mestre.

### Criar produto dos serviços configurável para contratos de prestação de serviços

#### Criar características

Objetivo

Nesta atividade, você cria características que estarão disponíveis para seleção no produto dos serviços configurável e para as quais você pode atualizar preços de variante individuais.

Procedimento

Característica VARKOND (chave de condições de variantes)

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Modelador de configuração de produto. | A página inicial é exibida. |  |
| 2 | Acessar o app | Abra Administrar características.Na tela Características, atualize Característica: VARKONDEm seguida, clique em Criar. | São exibidas áreas de tela adicionais. |  |
| 3 | Inserir dados básicos | Na área Dados básicos, atualize os seguintes dados:Descrição: Chave de condição de varianteStatus: LiberadoTipo de data: Formato de caracteresNúmero de características: 26Considerar maiúsculas/minúsculas: SelecionadoVários valores: Selecionado |  |  |
| 4 | Inserir descrições | Opcionalmente, atualize idiomas adicionais na guia Atualizar descrições. |  |  |
| 5 | Inserir dados adicionais | Navegue para a guia Dados adicionais e atualize os seguintes dados:Nome da tabela: SDCOMNome do campo: VKONDNão disponível para entrada: SelecionadoNenhuma exibição: Selecionado |  |  |
| 6 | Salvar característica | Selecione Gravar. | A nova característica é criada. |  |

Característica SERVICE_CHANNEL (canal de serviço)

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Modelador de configuração de produto. | A página inicial é exibida. |  |
| 2 | Acessar o app | Abra Administrar características.Na tela Características , atualize Característica: SERVICE_CHANNELEm seguida, clique em Criar. | São exibidas áreas de tela adicionais. |  |
| 3 | Inserir dados básicos | Na área Dados básicos, atualize os seguintes dados:Descrição: Canal de serviçoStatus: LiberadoTipo de data: Formato de caracteresNúmero de características: 20Vários valores: SelecionadoEntrada obrigatória: Selecionado |  |  |
| 4 | Inserir descrições | Opcionalmente, atualize idiomas adicionais na guia Atualizar descrições. |  |  |
| 5 | Inserir valores | Vá para a guia Valores e atualize os seguintes dados:Caract. de característica: E-MAIL/suporte de e-mailCaract. de característica: TELEFONE/suporte por telefone |  |  |
| 6 | Salvar característica | Selecione Gravar. | A nova característica é criada. |  |

Característica PREVENTIVE_MAINTENANCE (manutenção preventiva)

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Modelador de configuração de produto. | A página inicial é exibida. |  |
| 2 | Acessar o app | Abra Administrar características.Na tela Características , atualize Característica: PREVENTIVE_MAINTENANCEEm seguida, clique em Criar. | São exibidas áreas de tela adicionais. |  |
| 3 | Inserir dados básicos | Na área Dados básicos, atualize os seguintes dados:Descrição: Manutenção preventivaStatus: LiberadoTipo de data: Formato de caracteresNúmero de características: 20Vários valores: SelecionadoEntrada obrigatória: Selecionado |  |  |
| 4 | Inserir descrições | Opcionalmente, atualize idiomas adicionais na guia Atualizar descrições. |  |  |
| 5 | Inserir valores | Vá para a guia Valores e atualize os seguintes dados:Caract. de característica: ANUAL/anualCaract. de característica: SEMESTRAL/SemestralCaract. de característica: TRIMESTRAL/Trimestral |  |  |
| 6 | Salvar característica | Selecione Gravar. | A nova característica é criada. |  |

#### Criar classe

Objetivo

Nesta atividade, você cria uma classe à qual atribui as características do capítulo anterior.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Modelador de configuração de produto. | A página Inicial é exibida. |  |
| 2 | Acessar o app | Abra Administrar classes.Na tela Classe, atualize as seguintes entradas:Classe: SERVICE_CONTRACT_CTipo de classe: 300 (variantes)Em seguida, clique em Criar. | São exibidas áreas de tela adicionais. |  |
| 3 | Inserir dados básicos | Na área Dados básicos, atualize os seguintes dados:Descrição: Classe de contrato de prestação de serviçosStatus: LiberadoNão verificar: selecionado |  |  |
| 4 | Inserir características | Vá para a guia Caract. e atualize os seguintes dados:VARKONDSERVICE_CHANNELPREVENTIVE_MAINTENANCE | As características relevantes são atribuídas à classe. |  |
| 5 | Salvar classe | Clique em Salvar. | A nova classe é criada. |  |

#### Criar produto dos serviços configurável para contratos

Objetivo

Nesta atividade, você atualiza um produto dos serviços configurável que pode utilizar em contratos de prestação de serviços.

|  |
| --- |
| Nota Os campos específicos do Brasil são necessários para obter um cálculo de imposto adequado. Verifique Criar dados mestre para o Brasil (JD0_BR) no capítulo Definir campos específicos de BR para dados mestre para dados mestre de materiais. |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | A página inicial é exibida. |  |
| 2 | Acessar o app | Selecione o link Criar materialembaixo do bloco Administrar dados mestre de produto. | É exibido Criar material (primeira tela). |  |
| 3 | Inserir ID e tipo de material | Em Criar material (primeira tela), atualize as seguintes entradas:Material: SRV_CONTR_CONFIGSetor industrial: MSe o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária.Tipo de material: Produto de serviçosEm seguida, clique em Continuar (Enter). |  |  |
| 4 | Selecionar visão de dados básicos | Na caixa de diálogo Selecionar visões, selecione a visão Dados básicos 1, em seguida, clique em Continuar (Enter).Na caixa de diálogo Níveis organizacionais, insira o seguinte:Centro: 1710Organização de vendas: 1710Canal de distribuição: 10Nota Para DE, insira Centro/Organização de vendas/Canal de distribuição como 1010/1010/10 | A visão Criar material SRV_CONTR _CONFIG é exibida. |  |
| 5 | Inserir dados básicos | Na visão Dados básicos 1, atualize os seguintes valores:Descr.: Contrato de prestação de serviços configurávelUnidade de medida básica: US (unidade de serviço)Grupo de mercadorias: P001 (Serviços)GenItemGroup: (Prod.contrato serviços) SCNPMaterial configurável:selecionadoNavegue para Dados adicionais e atualize os seguintes dados:Idioma: DEDescrição do material: Contrato de prestação de serviços configurávelEm seguida, clique em Salvar. | O produto é criado e a visão Criar material (primeira tela) é exibida. |  |
| 6 | Selecionar visões de vendas | Na visão Criar material (primeira tela), atualize o material SRV_CONTR_CONFIG e, em seguida, selecione Continuar (Enter).Na caixa de diálogo Selecionar visões, selecione a seguinte visão:Vendas: Dados da organização de vendas 1Vendas: Dados da organização de vendas 2Vendas: Dados gerais/dados do centroEm seguida, selecione Continuar (Enter). | A caixa de diálogo Níveis organizacionais é exibida. |  |
| 7 | Selecionar níveis organizacionais | Na caixa de diálogo Níveis organizacionais, atualize os seguintes valores:Centro: 1710 (Centro 1 EUA)Org.vendas: 1710 ( Org.vendas nac.EUA)Canal de distrib.: 10 (vendas diretas)Nota Nota: Para DE, atualize 1010/1010/10 respectivamente.Em seguida, clique em Continuar (Enter). | A visão Vendas: organização de vendas 1 é exibida. |  |
| 8 | Inserir dados da organização de vendas (1) | Na visão Vendas: organização de vendas 1, atualize os seguintes valores:Dados gerais• Desconto: X <selecionado>Dados do imposto• Classificação fiscal: 1 (imposto total)Em seguida, pressione Enter. | A guia Vendas: organização de vendas 2 é exibida. |  |
| 9 | Inserir dados da organização de vendas (2) | Na visão Vendas: organização de vendas 2, atualize a seguinte entrada:Grupo de categorias de item (Prod.contrato serviços) SCNPEm seguida, pressione Enter. | A guia Vendas: geral/centro é exibida. |  |
| 10 | Inserir dados de informações gerais | Na guia Vendas: Geral/centro, atualize os seguintes valores:Unidade de medida básica: US (unidade de serviço)Duração de trabalho: 1 HREm seguida, clique em Salvar.Só para a Polônia: pressione Enter em vez de Salvar. | A visão Criar material (primeira tela) é exibida. |  |
| Só para a Polônia | Inserir dados de vendas | Na seção Comércio internacional: exportação, insira os seguintes dados:Código de controle: por exemplo, 41.00.30.0Em seguida, clique em Salvar. | A visão Criar material (primeira tela) é exibida. |  |
| 11 | Selecionar visão de classificação | Na visão Criar material (primeira tela), atualize o material SRV_CONTR_CONFIG e, em seguida, selecione Continuar (Enter).Na caixa de diálogo Selecionar visões, selecione a seguinte visão:ClassificaçãoEm seguida, selecione Continuar (Enter). | A visão Classificação é exibida. |  |
| 12 | Inserir classificação | Na caixa de diálogo Tipo de classe, selecione a entrada Variantes (300) e, em seguida, selecione Copiar.Na visão Classificação, atualize os seguintes valores:Classe: SERVICE_CONTRACT_CPressione Enter para exibir as características atribuídas à classe.Na área da tela Valores para classe SERVICE_CONTRACT_C, para cada característica, abra as entradas possíveis e selecione todos os valores disponíveis.Em seguida, clique em Salvar. | A visão Criar material (primeira tela) é exibida. |  |

#### Criar perfil de configuração

Objetivo

Nesta atividade, você cria um perfil de configuração no modelador de configuração de variantes.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Modelador de configuração de produto. | A página inicial é exibida. |  |
| 2 | Acessar o app | Abra Ambiente de modelagem de configuração de variantes.Na tela Primeira tela de ambiente de modelagem de configuração de variantes, atualize os seguintes dados:Material: SRV_CONTR_CONFIGTipo de classe: 300 (variantes)Em seguida, selecione Inserir modelo. | A tela Configuração para SRV_CONTR_CONFIG é exibida. |  |
| 3 | Criar perfil de configuração | Na coluna Objeto, clique com o botão direito na entrada SRV_CONTR_CONF e selecione Criar perfil de configuração.Na caixa de diálogo Criar perfil de configuração, atualize os seguintes dados.Perfil de configuração: SRV_CONTR_CONFSem número de modificação: SelecionadoEm seguida, selecione Continuar (ENTER).No painel Objeto, clique duas vezes no material SRV_CONTR_CONFIG.Abra a guia DetermPrçsVars., clique em Alterare, em seguida, Expandir lista.Atualize todas as características atribuídas ao seu produto configurável, exceto a característica VARKOND. Certifique-se também de que atualiza uma condição de variante e uma descrição para todas elas. A condição de variante é utilizada na atualização de condições de preço.Por exemplo, para Característica/Caract. Valor/cond.variante /cond.variante Descrição, atualize:SERVICE_CHANNEL/E-MAIL/E-MAIL/Suporte de e-mailSERVICE_CHANNEL/TELEFONE/TELEFONE/Suporte por telefonePREVENTIVE_MAINTENANCE/ANUAL/ANUAL/AnualPREVENTIVE_MAINTENANCE/SEMESTRAL/SEMESTRAL/SemestralPREVENTIVE_MAINTENANCE/TRIMESTRAL/TRIMESTRAL/TrimestralEm seguida, clique em Salvar. | A tela Configuração para SRV_CONTR_CONFIG é exibida. |  |

#### Definir preços

Objetivo

Nesta atividade, você atualiza um registro de condição de preço padrão para o produto de serviços configurável, bem como registros de preço de variante para as variantes configuráveis.

Procedimento

Tipo de condição: PSI1 (preço para item do contrato de serviços)

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | A página inicial é exibida. |  |
| 2 | Acessar o app | Abra Definir preços de material. | A visão Modificar registros de condições é exibida. |  |
| 3 | Inserir o tipo de condição | Na visão Alterar registros de condições, atualize Tipo de condição: PSI1 (Preço p/contr.prest.serviços) e, em seguida, selecione Enter. | A visão Combinação de chaves é exibida. |  |
| 4 | Selecionar combinação de chaves | Na visão Combinação de chaves, selecione Material.Em seguida, pressione Enter. | A visão Alterar preço (PSI1): seleção é exibida. |  |
| 5 | Seleção | Na visão Modificar preço (PSI1): seleção, atualize as seguintes informações:Organização de vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Material:SRV_CONTRACT (Produto do contrato de serviços)Válido em: <Data>, por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição para determinação de preços (PPSI): síntese é exibida. |  |
| 6 | Inserir condição de preço | Na visão Modificar condição de preço (PSI1): síntese, atualize os seguintes dados:Material: SRV_CONTR_CONFIG (contrato de prestação de serviços configurável)Montante: por exemplo, 200,00Unidade: por exemplo, USDVálido desde: <Data>, por exemplo, a data de hojeSelecione Enter.Em seguida, clique em Salvar. | Um preço padrão para o produto dos serviços SRV_CONTR_CONFIG foi atualizado. |  |

Tipo de condição: VASE (preço de variante)

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | A página inicial é exibida. |  |
| 2 | Acessar o app | Abra Definir preços de material. | A visão Modificar registros de condições é exibida. |  |
| 3 | Inserir o tipo de condição | Na visão Alterar registros de condições, atualize Tipo de condição: VASE (preço de variante) e, em seguida, selecione Enter. | A visão Modificar preço de variante é exibida. |  |
| 4 | Inserir dados de vendas | Na visão Modificar preço de variante ( VASE ): seleção, atualize as seguintes informações:Organização de vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Material: SRV_CONTR_CONFIG (contrato de prestação de serviços configurável)Válido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição de preço de variante ( VASE ): síntese é exibida. |  |
| 5 | Inserir condições de variante | Na visão Modificar condição de preço de variante ( VASE ): síntese, atualize preços para todas as condições de variante que você atualizou no capítulo anterior, por exemplo:Variante/montante/unidade:E-MAIL/30 USDTELEFONE/50 USDANUAL/250 USDSEMESTRAL/135 USDTRIMESTRAL/90 USDPressione Enter e verifique as suas entradas.Em seguida, clique em Salvar. | As condições de preço de variante foram atualizadas. |  |

### Criar produto dos serviços configurável para ordens de serviço

#### Criar características

Objetivo

Nesta atividade, você cria características que estarão disponíveis para seleção no produto dos serviços configurável e para as quais você pode atualizar preços de variante individuais.

Procedimento

Característica VARKOND (chave de condições de variantes)

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Modelador de configuração de produto. | A página inicial é exibida. |  |
| 2 | Acessar o app | Abra Administrar características.Na tela Características, no campo Característica: insira VARKONDEm seguida, clique em Criar. | São exibidas áreas de tela adicionais. |  |
| 3 | Inserir dados básicos | Na área Dados básicos, insira os seguintes dados:Descrição: Chave de condição de varianteStatus: LiberadoTipo de data: Formato de caracteresNúmero de características: 26Considerar maiúsculas/minúsculas: SelecionadoVários valores: Selecionado |  |  |
| 4 | Inserir descrições | Opcionalmente, você pode inserir idiomas adicionais na guia Atualizar descrições. |  |  |
| 5 | Inserir dados adicionais | Navegue para a guia Dados adicionais e insira os seguintes dados:Nome da tabela: SDCOMNome do campo: VKONDNão disponível para entrada: SelecionadoNenhuma exibição: Selecionado |  |  |
| 6 | Gravar característica | Selecione Gravar. | A nova chave de condições de variantes é criada. |  |

Característica CAR_WASH_TYPE (tipo de posto de lavagem)

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Modelador de configuração de produto. | A página inicial é exibida. |  |
| 2 | Acessar o app | Abra Administrar características.Na tela Características , no campo Característica: insira CAR_WASH_TYPEEm seguida, clique em Criar. | São exibidas áreas de tela adicionais. |  |
| 3 | Inserir dados básicos | Na área Dados básicos, insira os seguintes dados:Descrição: tipo de posto de lavagemStatus: LiberadoTipo de data: Formato de caracteresNúmero de características: 20Valores individuais SelecionadoEntrada obrigatória: Selecionado |  |  |
| 4 | Inserir descrições | Opcionalmente, você pode inserir idiomas adicionais na guia Atualizar descrições. |  |  |
| 5 | Inserir valores | Navegue para a guia Valores e insira os seguintes dados:Valor/descrição de característica: BÁSICO/lavagem básicaValor/descrição de característica: PADRÃO/lavagem padrãoValor/descrição de característica: PREMIUM/lavagem premium |  |  |
| 6 | Gravar característica | Selecione Gravar. | A nova característica é criada. |  |

Característica CAR_SIZE (tamanho do carro)

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Modelador de configuração de produto. | A página inicial é exibida. |  |
| 2 | Acessar o app | Abra Administrar características.Na tela Características , no campo Característica: insira CAR_SIZEEm seguida, clique em Criar. | São exibidas áreas de tela adicionais. |  |
| 3 | Inserir dados básicos | Na área Dados básicos, insira os seguintes dados:Descrição: tamanho do veículoStatus: LiberadoTipo de data: Formato de caracteresNúmero de características: 20Valores individuais SelecionadoEntrada obrigatória: Selecionado |  |  |
| 4 | Inserir descrições | Opcionalmente, você pode inserir idiomas adicionais na guia Atualizar descrições. |  |  |
| 5 | Inserir valores | Navegue para a guia Valores e insira os seguintes dados:Valor/descrição de característica: P/pequenoValor/descrição de característica: M/médioValor/descrição de característica: G/grande |  |  |
| 6 | Gravar característica | Selecione Gravar. | A nova característica é criada. |  |

Característica EXTRA_POLISH (polimento adicional)

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Modelador de configuração de produto. | A página inicial é exibida. |  |
| 2 | Acessar o app | Abra Administrar características.Na tela Características , no campo Característica: insira EXTRA_POLISHEm seguida, clique em Criar. | São exibidas áreas de tela adicionais. |  |
| 3 | Inserir dados básicos | Na área Dados básicos, insira os seguintes dados:Descrição: polimento extraStatus: LiberadoTipo de data: Formato de caracteresNúmero de características: 10Valor individual: SelecionadoEntrada obrigatória: Selecionado |  |  |
| 4 | Inserir descrições | Opcionalmente, você pode inserir idiomas adicionais na guia Atualizar descrições. |  |  |
| 5 | Inserir valores | Navegue para a guia Valores e insira os seguintes dados:Valor/descrição de característica: SIM/SimValor/descrição de característica: NO/Não |  |  |
| 6 | Gravar característica | Selecione Gravar. | A nova característica é criada. |  |

#### Criar classe

Objetivo

Nesta atividade, você cria uma classe à qual atribui as características do capítulo anterior.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Modelador de configuração de produto. | A página Inicial é exibida. |  |
| 2 | Acessar o app | Abra Administrar classes.Na tela Classe, insira os seguintes dados:Classe: CAR_WASHTipo de classe: 300 (variantes)Em seguida, clique em Criar. | São exibidas áreas de tela adicionais. |  |
| 3 | Inserir nome da classe | Na tela Classe, insira os seguintes dados:Classe: CAR_WASHTipo de classe: 300 (variantes)Em seguida, selecione Criar. |  |  |
| 4 | Inserir dados básicos | Na área Dados básicos, insira os seguintes dados:Descrição: Posto de lavagemStatus: LiberadoNão verificar: selecionado |  |  |
| 5 | Inserir características | Vá para a ficha de registro Caract. e atualize os seguintes dados:VARKONDCAR_WASH_TYPECAR_SIZEEXTRA_POLISH | As características relevantes são atribuídas à classe. |  |
| 6 | Gravar classe | Clique em Salvar. | A nova classe é criada. |  |

#### Criar produto dos serviços configurável para ordem de serviço

Objetivo

Nesta atividade, você atualiza um produto dos serviços configurável que pode usar em ordens de serviço.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto | É exibida a Página inicial. |  |
| 2 | Acessar o app | Escolha no app Criar material. | É exibido Criar material (1ª tela). |  |
| 3 | Inserir ID e tipo de material | Em Criar material (1ª tela), insira os seguintes dados:Material: CAR-WASH_CONFSe o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária.Tipo de material: SERV produto do serviçoEm seguida, selecione Continuar (ENTER). |  |  |
| 4 | Selecionar visão de dados básicos | Na caixa de diálogo Níveis organizacionais, insira os dados seguintes:Centro: 1710 (Centro 1 EUA)Org.vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Nota: Para DE, insira 1010/1010/10 respectivamente.Em seguida, selecione Continuar (ENTER). | A visão Criar material CAR-WASH _CONF é exibida. |  |
| 5 | Inserir dados básicos | Na guia Dados básicos 1, insira os seguintes dados:Descr.: Posto de lavagem configurávelUnidade de medida básica: US (unidade de serviço)Grupo de mercadorias: P001 (Serviços)GrpCtgsItemGer.: SRVP (Produto dos serviços)Material configurável:selecionadoNavegue para Dados adicionais e atualize os seguintes dados:Idioma: DEDescrição do material: Posto de lavagem configurávelEm seguida, clique em Salvar. | O produto é criado e a visão Criar material (primeira tela) é exibida. |  |
| 6 | Selecionar visões de vendas | Na visão Criar material (primeira tela), no campo Material, insira CAR-WASH_CONF e em seguida selecione Continuar (Enter).Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Vendas: Dados da organização de vendas 1Vendas: Dados da organização de vendas 2Vendas: Dados gerais/dados do centroEm seguida, selecione Continuar (Enter). | A caixa de diálogo Níveis organizacionais é exibida. |  |
| 7 | Selecionar níveis organizacionais | Na caixa de diálogo Níveis organizacionais, insira os dados seguintes:Centro: 1710 (Centro 1 EUA)Org.vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Nota: Para DE, insira 1010/1010/10 respectivamente.Em seguida, selecione Continuar (ENTER). | A visão Vendas: organização de vendas 1 é exibida. |  |
| 8 | Inserir dados da organização de vendas (1) | Na guia Vendas: organização de vendas 1, insira os dados seguintes:Dados gerais• Desconto: X <selecionado>Dados do imposto• Classificação fiscal: 1 (imposto total)Em seguida, pressione Enter. | A visão Vendas: organização de vendas 2 é exibida. |  |
| 9 | Inserir dados da organização de vendas (2) | Na guia Vendas: organização de vendas 2, insira os dados seguintes:Grupo de categorias de item: SRVP (Produto dos serviços)Em seguida, pressione Enter. | A visão Vendas: geral/centro é exibida. |  |
| 10 | Inserir dados de informações gerais | Na guia Vendas: geral/centro, insira os dados seguintes:Unidade de medida básica: US (unidade de serviço)Duração de trabalho: 1 HREm seguida, clique em Salvar.Só para a Polônia: pressione Enter em vez de Salvar. | A visão Criar material (primeira tela) é exibida. |  |
| Só para a Polônia | Inserir dados de vendas | Na guia Comércio internacional: exportação, na área Data do comércio exterior, insira os seguintes dados:Código de controle: por exemplo, 41,00.30,0Em seguida, clique em Salvar. |  |  |
| 11 | Selecionar visão de classificação | Na visão Criar material (primeira tela), no campo Material, insira CAR-WASH_CONF e em seguida selecione Continuar (Enter).Na caixa de diálogo Selecionar visões, selecione a seguinte visão:ClassificaçãoEm seguida, selecione Continuar (Enter). | A visão Classificação é exibida. |  |
| 12 | Inserir classificação | Na caixa de diálogo Tipo de classe, selecione a entrada Variantes (300) e, em seguida, selecione Copiar.Na visão Classificação, insira os dados seguintes:Classe: CAR_WASHPressione Enter para exibir as características atribuídas à classe.Na área da tela Valores para classe CAR_WASH, para cada característica, abra as entradas possíveis e selecione todos os valores disponíveis.Em seguida, clique em Salvar. | As características atribuídas ao material. |  |

#### Criar perfil de configuração

Objetivo

Nesta atividade, você cria um perfil de configuração no modelador de configuração de variantes.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Modelador de configuração de produto. | A página inicial é exibida. |  |
| 2 | Acessar o app | Abra Ambiente de modelagem de configuração de variantes.Na tela Primeira tela de ambiente de modelagem de configuração de variantes, insira os seguintes dados:Material: CAR-WASH_CONFTipo de classe: 300 (variantes)Em seguida, selecione Inserir modelo. | A tela Configuração para CAR_WASH_CONF é exibida. |  |
| 3 | Criar perfil de configuração | Na coluna Objeto, clique com o botão direito na entrada CAR-WASH_CONF e clique em Criar perfil de configuração.Na caixa de diálogo Criar perfil de configuração, insira os seguintes dados.Perfil de configuração: CAR-WASH_CONFSem número de modificação: selecionadoEm seguida, selecione Continuar (ENTER).Na coluna Objeto, clique duas vezes na entrada CAR-WASH_CONF. Abra a guia Determinação do preço de variante e clique em Alterar. Em seguida, clique em Expandir lista.Insira todas as características atribuídas ao seu produto configurável, exceto a característica VARKOND. Certifique-se também de que insere uma Condição variante e uma Descrição para todas elas. A condição de variante é utilizada na atualização de condições de preço.Por exemplo, para Característica/Caract. Valor/cond.variante /cond.variante Descrição, insira:CAR_WASH_TYPE / BASIC / C_W_T_B / BasicCAR_WASH_TYPE / STANDARD / C_W_T_S / StandardCAR_WASH_TYPE / PREMIUM / C_W_T_P / PrêmioCAR_SIZE / S / C_S_S / PequenoCAR_SIZE / M / C_S_M / MédioCAR_SIZE / L / C_S_L / GrandeEXTRA_POLISH / SIM / E_P_Y / SimEXTRA_POLISH / NO / E_P_N / NãoEm seguida, clique em Salvar. | As condições de variante são criadas para todas as características. |  |

#### Definir preços

Objetivo

Nesta atividade, você atualiza um registro de condição de preço padrão para o produto de serviços configurável, bem como registros de preço de variante para as variantes configuráveis.

Procedimento

Tipo de condição: PPR0 (preço)

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | A página inicial é exibida. |  |
| 2 | Acessar o app | Abra Definir preços de material. | A visão Modificar registros de condições é exibida. |  |
| 3 | Inserir o tipo de condição | Na visão Modificar registros de condições, no campo Tipo de condição: insira PPR0 (preço) e, em seguida, selecione Enter. | A visão Combinação de chaves é exibida. |  |
| 4 | Selecionar combinação de chaves | Na visão Combinação de chaves, selecione Material.Em seguida, pressione Enter. | A visão Alterar preço (PPR0): seleção é exibida. |  |
| 5 | Seleção | Na visão Modificar preço (PPR0): seleção, insira os seguintes dados:Organização de vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Material: CAR-WASH_CONF (posto de lavagem configurável)Válido em: <Data>, por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição para determinação de preços (PPR0): síntese é exibida. |  |
| 6 | Inserir condição de preço | Na visão Alterar condição de preço (PPR0): síntese, insira os seguintes dados:Material: CAR-WASH_CONF (posto de lavagem configurável)Montante: por exemplo, 10,00Unidade: por exemplo, USDVálido desde: <Data>, por exemplo, a data de hojeSelecione Enter.Em seguida, clique em Salvar. | É criado um preço padrão para o produto dos serviços. |  |

Tipo de condição: PVA0 (preço de variante)

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | A página inicial é exibida. |  |
| 2 | Acessar o app | Abra Definir preços de material. | A visão Modificar registros de condições é exibida. |  |
| 3 | Inserir o tipo de condição | Na visão Alterar registros de condições, atualize Tipo de condição: PVA0 (preço de variante) e, em seguida, pressione Enter. | A visão Modificar preço de variante é exibida. |  |
| 4 | Inserir dados de vendas | Na visão Modificar preço de variante (PVA0): seleção, atualize as seguintes informações:Organização de vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Material: CAR-WASH_CONF (contrato de prestação de serviços configurável)Válido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição de preço de variante (PVA0): síntese é exibida. |  |
| 5 | Inserir condições de variante | Na visão Criar condição de preço de variante (PVA0): síntese, insira preços para todas as condições de variante que você criou no capítulo anterior, por exemplo:Variante/montante/unidade:C_W_T_B/5 USDC_W_T_S/USDC_W_T_P/12 USDC_S_S/2 USDC_S_M/4 USDC_S_L/10 USDPressione Enter e verifique as suas entradas.Em seguida, clique em Salvar. | As condições de preço de variante são criadas. |  |

PVA1 (% de preço de variante)

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | A página inicial é exibida. |  |
| 2 | Acessar o app | Abra Definir preços de material. | A visão Modificar registros de condições é exibida. |  |
| 3 | Inserir o tipo de condição | Na visão Modificar registros de condições, no campo Tipo de condição: insira PVA1 preço de variante (%), e em seguida selecione Enter. | A visão Modificar preço de variante (% PVA1) é exibida. |  |
| 4 | Inserir dados de vendas | Na visão Modificar preço de variante (% PVA1): seleção, insira os seguintes dados:Organização de vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Material: CAR-WASH_CONFVálido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição de preço de variante (%) (PVA1): síntese é exibida. |  |
| 5 | Inserir condições de variante | Na visão Criar condição de preço de variante (%) (PVA1): síntese, insira registros de condições para todas as condições de variante relevantes, por exemplo:Variante/montante/unidade:E_P_Y/20%E_P_N/-10%Pressione Enter e verifique as suas entradas.Em seguida, clique em Salvar. | As condições de preço de variante são criadas. |  |

### Criar variante de material para um produto de serviços

Objetivo

Nesta atividade, você cria uma variante do material com uma configuração predefinida que pode ser usada em uma ordem de serviço. O registro mestre da variante está ligado a um produto configurável que usa suas características.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto | A página inicial é exibida. |  |
| 2 | Acessar o app | Selecione o link Criar material abaixo do bloco Administrar dados mestre de produto. | É exibido Criar material (1ª tela). |  |
| 3 | Inserir ID e tipo de material | Em Criar material (primeira tela), insira os seguintes dados:Material: CAR-WASH-VARSetor industrial: engenharia mecânicaSe o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária.Tipo de material: SERV produto do serviçoEm seguida, selecione Continuar (ENTER).Na caixa de diálogo Selecionar visões, selecione Dados básicos 1Selecione Níveis organizacionais |  |  |
| 4 | Selecionar níveis organizacionais | Na caixa de diálogo Níveis organizacionais, insira os dados seguintes:Centro: 1710 (Centro 1 EUA)Organização de vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Nota Para DE, insira 1010/1010/10 respectivamente.Em seguida, selecione Continuar (ENTER). | A visão Criar material CAR-WASH-VAR é exibida. |  |
| 5 | Inserir dados básicos | Na guia Dados básicos 1, insira os seguintes dados:Descr.: Variante para lavagem de veículosUnidade de medida básica: US (unidade de serviço)Grupo de mercadorias: P001 (Serviços)GenItemGroup: SRVP (Produto dos serviços)Material configurável:desmarcadoCM válido para vários centros:CAR-WASH_CONFSelecione Configurar varianteNa visão Configuração de variantesSelecione as seguintes características:Tamanho do veículo: PequenoPolimento extra SimTipo de posto de lavagem Lavagem padrãoselecione ConcluídoEm seguida, clique em Salvar. | O produto é criado e a visão Criar material (primeira tela) é exibida. |  |
| 6 | Selecionar visões de vendas | Na visão Criar material (primeira tela), no campo Material, insira CAR-WASH-VAR e em seguida selecione Continuar (Enter).Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Vendas: Dados da organização de vendas 1Vendas: Dados da organização de vendas 2Vendas: Dados gerais/dados do centroEm seguida, selecione Continuar (ENTER). | A caixa de diálogo Níveis organizacionais é exibida. |  |
| 7 | Selecionar níveis organizacionais | Na caixa de diálogo Níveis organizacionais, insira os dados seguintes:Centro: 1710 (Centro 1 EUA)Org.vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Nota Para DE, insira 1010/1010/10 respectivamente.Em seguida, selecione Continuar (ENTER). | A guia Vendas: organização de vendas 1 é exibida. |  |
| 8 | Inserir dados da organização de vendas (1) | Na visão Vendas: organização de vendas 1, insira os dados seguintes:Dados gerais• Desconto: X <selecionado>Dados do impostoClassificação fiscal: 1 (imposto total)Em seguida, pressione Enter. | A guia Vendas: organização de vendas 2 é exibida. |  |
| 9 | Inserir dados da organização de vendas (2) | Na visão Vendas: organização de vendas 2, insira os dados seguintes:Grupo de categorias de item SRVP (Produto dos serviços)Em seguida, pressione Enter. | A guia Vendas: geral/centro é exibida. |  |
| 10 | Inserir dados de informações gerais | Na guia Vendas: geral/centro, insira os dados seguintes:Unidade de medida básica: US (unidade de serviço)Duração de trabalho: 1 HREm seguida, clique em Salvar. | A visão Criar material (primeira tela) é exibida. |  |

#### Definir preços para variante do material

Objetivo

Nesta atividade, você atualiza um registro de condição de preço padrão para a variante.

Procedimento

Tipo de condição: PPR0 (preço)

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | A página inicial é exibida. |  |
| 2 | Acessar o app | Abra Definir preços de material. | A visão Modificar registros de condições é exibida. |  |
| 3 | Inserir o tipo de condição | Na visão Modificar registros de condições, no campo Tipo de condição: insira PPR0 (preço) e, em seguida, pressione Enter. | A visão Combinação de chaves é exibida. |  |
| 4 | Selecionar combinação de chaves | Na visão Combinação de chaves, selecione Material com status de liberaçãoEm seguida, pressione Enter. | A visão Modificar preço (PPR0): seleção é exibida. |  |
| 5 | Seleção | Na visão Modificar preço (PPR0): seleção, insira os seguintes dados:Organização de vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Material: CAR-WASH-VAR (variante para lavagem de veículos)Válido em: <Data>, por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição para determinação de preços (PPR0): síntese é exibida. |  |
| 6 | Inserir condição de preço | Na visão Modificar condição de preço (PPR0): síntese, insira os seguintes dados:Material: CAR-WASH-VAR (VAR de lavagem de veículos)Montante: por exemplo, 20,00Unidade: por exemplo, USDVálido desde: <Data>, por exemplo, a data de hojePressione Enter.Em seguida, clique em Salvar. | É criado um preço padrão para a variante. |  |

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
> Flagged while digesting this document, not verified: Contract PSI1 price step uses material SRV_CONTRACT while the product is created as SRV_CONTR_CONFIG, likely a typo within the document

> [!warning] Conflict
> Flagged while digesting this document, not verified: PVA0 example list omits an amount for C_W_T_S (standard wash)

> [!warning] Conflict
> Flagged while digesting this document, not verified: Contract product step lists material type as 'Produto de serviços' while order product uses SERV; PVA0 step for CAR-WASH_CONF labels it 'contrato de prestação de serviços configurável'

> [!warning] Conflict
> Flagged while digesting this document, not verified: Order class creation repeats the create-class step twice (steps 2 and 3); control code format differs (41.00.30.0 vs 41,00.30,0)

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-configurable-service-product-mds-5be-431]]
- related-to :: [[14-maintenance-service-and-projects/mds-5be-master-data-script-create-configurable-service-products-435]]
- related-to :: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-mds-5be-433]]
- related-to :: [[14-maintenance-service-and-projects/script-de-datos-maestros-creacion-de-producto-de-servicio-configurable]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BE_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 50,660 chars in the whole document
