---
id: 06-management-accounting/script-de-dados-mestre-criar-mestre-de-materiais-para-realizacao-de-re
title: Script de dados mestre - Criar mestre de materiais para realização de receita universal (7R8) (7R8_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP S/4HANA Cloud Public Edition 2608 script for creating URR test material master data and condition prices for SFS, fixed-price project and service contract scenarios."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/event-based-revenue-recognition-sell-from-stock]
aliases: [7R8_S4CLD2608_Master_Data_PT_XX]
keywords: [Event-Based Revenue Recognition for Sell from Stock, material master data, universal revenue recognition, stock-based sales scenario, fixed-price customer project, service contract, material pricing, business roles, organizational units, price condition types]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7R8_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-536
topic: 06-management-accounting/event-based-revenue-recognition-sell-from-stock
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar mestre de materiais para realização de receita universal (7R8) (7R8_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7R8_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Event-Based Revenue Recognition for Sell from Stock** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar mestre de materiais para realização de receita universal (7R8) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893926)

[2 Pré-requisitos 3](#_Toc233893927)

[2.1 Acesso ao sistema 3](#_Toc233893928)

[2.2 Funções 3](#_Toc233893929)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893930)

[3 Tabela de síntese 5](#_Toc233893931)

[4 Criar dados mestre de materiais para cenário de integração de venda do depósito (SFS) 6](#_Toc233893932)

[4.1 Produtos comercializáveis: URR_MAT1_NORM 6](#_Toc233893933)

[4.2 Produtos de serviços para serviços únicos URR_MAT1_SERV 8](#_Toc233893934)

[5 Criar dados mestre de materiais para cenário de integração de projeto de cliente de preço fixo 11](#_Toc233893935)

[5.1 URR_FPPRJ_1 11](#_Toc233893936)

[6 Criar dados mestre de materiais para cenário de integração de contrato de prestação de serviços 14](#_Toc233893937)

[6.1 URR_SRVCONT1 14](#_Toc233893938)

[7 Definir preços para materiais 16](#_Toc233893939)

[7.1 Preço para produtos comercializáveis para SFS: URR_MAT1_NORM 16](#_Toc233893940)

[7.2 Preço para produto de serviços para serviço único: URR_MAT1_SERV 18](#_Toc233893941)

[7.3 Preço para material de contrato de serviços: URR_SRVCONT1 20](#_Toc233893942)

## Objetivo

Este documento fornece um guia sobre como criar registros de dados mestre de materiais, incluindo preços para diferentes cenários de integração de realização de receita universal (URR): URR integrado com venda do depósito, URR integrado com projetos de serviço ao cliente e URR integrado com contrato de prestação de serviços.

O guia inclui a descrição de segmentos de dados relevantes para que os dados mestre trabalhem em um processo URR e campos que precisam ser preenchidos com valores de entrada nos segmentos de dados. Os segmentos de dados e campos que não são relevantes para o escopo não são descritos neste documento, embora eles possam aparecer na IU.

Dados mestre de materiais criados como descrito aqui podem ser usados para os processos de URR:

| ID do mestre de materiais | Descrição | Utilização |
| --- | --- | --- |
| URR_MAT1_NORM | URR material de teste 1 NORM | Este material é usado no cenário de integração de venda do depósito URR |
| URR_MAT2_NORM | URR material de teste 2 NORM | Este material é usado no cenário de integração de venda do depósito URR |
| URR_MAT1_SERV | URR material de teste 1 TAD | Este material é usado no cenário de integração de venda do depósito URR |
| URR_FPPRJ_1 | URR material de teste preço fixo projeto do cliente | Este material é usado no cenário de integração de projeto de cliente URR |
| URR_SRVCONT1 | URR contrato de serviço de material de teste | Este material é usado no cenário de integração de contrato de serviço URR |

## Pré-requisitos

### Acesso ao sistema

| sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via SAP Fiori Launchpad. O administrador do sistema fornece o URL para acessar os diversos apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) | Efetuar login |
| --- | --- | --- | --- | --- |
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Dados mestre - produtos / Governança de produto | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Especialista em preços | SAP_BR_PRICING_SPECIALIST | Gestão de preços | SAP_BR_PRICING_SPECIALIST |  |

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre são dependentes das unidades organizacionais da empresa. Os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Unidade organizacional a ser utilizada para DE | Unidade organizacional a ser utilizada para EUA |
| --- | --- | --- | --- |
| Criar material | Centro | 1010 (centro 1 DE) | 1710 (centro 1 EUA) |
| Criar material | Organização de vendas | 1010 ( Org.vendas nacional DE) | 1710 ( Org.vendas nac.EUA) |
| Criar material | Canal de distribuição | 10 (vendas diretas) | 10 (vendas diretas) |

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

Tabela 1: Criar dados mestre de materiais para cenário de integração de venda do depósito (SFS)

| Etapa do processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Produtos comercializáveis: URR_MAT1_NORM](#unique_6) [página ] 6 | Especialista em dados mestre - Dados do produto | Criar material |  |
| [Produtos de serviços para serviços únicos URR_MAT1_SERV](#unique_7) [página ] 8 | Especialista em dados mestre - Dados do produto | Criar material |  |

Tabela 2: Criar dados mestre de materiais para cenário de integração de projeto de cliente de preço fixo

| Etapa do processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [URR_FPPRJ_1](#unique_8) [página ] 11 | Especialista em dados mestre - Dados do produto | Criar material |  |

Tabela 3: Criar dados mestre de materiais para cenário de integração de contrato de prestação de serviços

| Etapa do processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [URR_SRVCONT1](#unique_9) [página ] 14 | Especialista em dados mestre - Dados do produto | Criar material |  |

Tabela 4: Criar dados mestre de materiais para cenário de integração de contrato de prestação de serviços

| Etapa do processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Preço para produtos comercializáveis para SFS: URR_MAT1_NORM](#unique_10) [página ] 16 | Especialista em preços | Definir preços de material |  |
| [Preço para produto de serviços para serviço único: URR_MAT1_SERV](#unique_11) [página ] 18 | Especialista em preços | Definir preços de material |  |
| [Preço para material de contrato de serviços: URR_SRVCONT1](#unique_12) [página ] 20 | Especialista em preços | Definir preços de material |  |

## Criar dados mestre de materiais para cenário de integração de venda do depósito (SFS)

### Produtos comercializáveis: URR_MAT1_NORM

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | A página Inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Selecione o app Criar material (se o app não estiver disponível na tela, você pode tentar procurar o app Criar material). | É exibido Criar material (1ª tela). |  |
| 3 | Inserir número do material e tipo de material | Em Criar material (1ª tela), efetue as seguintes entradas:Número do produto: URR_MAT1_NORMTipo de material: Produtos comercializáveisEm seguida, selecione Continuar (ENTER). | Você inseriu o número e o tipo de material para os novos dados mestre de materiais.É exibida a caixa de diálogo Selecionar visões. |  |
| 4 | Selecionar visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Dados básicos 1Vendas: Dados da organização de vendas 1Vendas: Dados da organização de vendas 2Vendas: Dados gerais/dados do centroContabilidade1Em seguida, selecione Continuar (ENTER). | A caixa de diálogo Níveis organizacionais é exibida. |  |
| 5 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:Centro: 1010 (centro 1 DE)Organização de vendas: 1010 ( Org.vendas nacional DE)Canal de distribuição: 10 (vendas diretas)Em seguida, selecione Continuar (ENTER). | Os dados organizacionais foram selecionados.A visão Dados básicos 1 de é exibida. |  |
| 6 | Atualizar visão: Dados básicos 1 | Na visão Dados básicos 1, atualize os seguintes valores:Descr.: URR material de teste 1 NORMUM básica: UN (unidade)Grupo de materiais: L001 (materiais comercializáveis)GenItemGroup: NORM (item padrão)Peso bruto: 1Peso líquido: 1Unidade de peso: KGVolume: 1Unidade de volume: M3Em seguida, pressione Enter. | Os dados básicos são atualizados.Depois de pressionar Enter, a visão Vendas: organização de vendas 1 é exibida. |  |
| 7 | Atualizar visão: Vendas: organização de vendas 1 | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados geraisDesconto: X <selecionado>Dados do impostoClassificação fiscal: 0Em seguida, selecione Enter. | Os dados organizacionais de vendas 1 são atualizados. A visão Vendas: organização de vendas 2 é exibida. |  |
| 8 | Atualizar visão: Vendas: organização de vendas 2 | Na visão Vendas: organização de vendas 2, atualize a seguinte entrada:Grp.ctg.item Grp: NORM (item padrão)Grupo de categorias de item: NORM (item padrão)Em seguida, selecione Enter. | Os dados organizacionais de vendas 2 são atualizados. A visão Vendas: geral/centro é exibida. |  |
| 9 | Atualizar visão: Vendas: Geral/Centro | Na visão Vendas: geral/centro, atualize os seguintes valores:UM básica: UN (unidade)Peso bruto: 1KGPeso líquido: 1Verificação de disponibilidade: NCGr. transporte: 0001Grp.carregamento: 0001Centro de lucro: Y1041Em seguida, selecione Enter. | Os dados gerais de venda são atualizados. A visão Contabilidade 1 é exibida. |  |
| 10 | Atualizar visão: Contabilidade 1 | Na visão Contabilidade 1, na seção Período atual, efetue a seguinte entrada:UM básica: UNClasse de avaliação: 3100Preço padrão: 16Preço unitário: 16Unidade de preço: 1Controle de preço: VPreço futuro: em brancoEm seguida, selecione Salvar. | Os dados contábeis são atualizados.Os dados mestre de materiais são salvos. |  |
| 11 | Criar mais dados mestre de materiais para teste, se necessário | Crie mais mestre de materiais seguindo a convenção de nomes URR_MAT*_NORM (por exemplo: URR_MAT2_NORM, URR_MAT3_NORM, etc.) com um preço padrão diferente. | Mais dados mestre de material de teste são criados. | Para CE 2502, URR_MAT1_NORM e URR_MAT2_NORM são fornecidos como dados de demonstração, de modo que o usuário não precisa criá-los manualmente.Se forem necessários mais dados mestre de materiais para o teste de cenário de integração de venda do depósito, siga as etapas desta seção para criar mais materiais. |

### Produtos de serviços para serviços únicos URR_MAT1_SERV

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | A página Inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Selecione o app Criar material (se o app não estiver disponível na tela, você pode tentar procurar o app Criar material). | É exibido Criar material (1ª tela). |  |
| 3 | Inserir número do material e tipo de material | Em Criar material (1ª tela), efetue as seguintes entradas:Número do produto: URR_MAT1_SERVTipo de material: Produto de serviçosEm seguida, clique em Continuar (Enter). | Você inseriu o número e o tipo de material para os novos dados mestre de materiais.É exibida a caixa de diálogo Selecionar visões. |  |
| 4 | Selecionar visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Dados básicos 1Vendas: Dados da organização de vendas 1Vendas: Dados da organização de vendas 2Vendas: Dados gerais/dados do centroContabilidade1Em seguida, selecione Continuar (ENTER). | A caixa de diálogo Níveis organizacionais é exibida. |  |
| 5 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:Centro: 1010 (centro 1 DE)Organização de vendas: 1010 ( Org.vendas nacional DE)Canal de distribuição: 10 (vendas diretas)Em seguida, clique em Continuar (Enter). | Os dados organizacionais foram selecionados.A visão Dados básicos 1 de é exibida. |  |
| 6 | Atualizar visão: Dados básicos 1 | Na visão Dados básicos 1, atualize os seguintes valores:Descr.: URR material de teste 1 TADUM básica: H (horas)Grupo de materiais: YBMM01 (material não estocável com ID)GenItemGroup: SERV (serviços)Em seguida, pressione Enter. | Os dados básicos são atualizadosDepois de pressionar Enter, a visão Vendas: organização de vendas 1 é exibida. |  |
| 7 | Atualizar visão: Vendas: organização de vendas 1 | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados geraisCentro fornecedor: 1010Desconto: X <selecionado>Dados do impostoClassificação fiscal: 0Em seguida, selecione Enter. | Os dados organizacionais de vendas 1 são atualizados. A visão Vendas: organização de vendas 2 é exibida. |  |
| 8 | Atualizar visão: Vendas: organização de vendas 2 | Na visão Vendas: organização de vendas 2, atualize a seguinte entrada:Grp.ctg.item Grp: SERV (serviço)Grupo de categorias de item: SERV (serviço)Em seguida, selecione Enter. | Os dados organizacionais de vendas 2 são atualizados. A visão Vendas: geral/centro é exibida. |  |
| 9 | Atualizar visão: Vendas: Geral/Centro | Na visão Vendas: geral/centro, atualize os seguintes valores:Centro de lucro: YB600Em seguida, selecione Enter. | Os dados gerais de venda são atualizados. A visão Contabilidade 1 é exibida. |  |
| 10 | Atualizar visão: Contabilidade 1 | Na visão Contabilidade 1, na seção Período atual, efetue a seguinte entrada:Classe de avaliação: 3300Preço padrão: 20Unidade de preço: 1Em seguida, selecione Salvar. | Os dados contábeis são atualizados.Os dados mestre de materiais são salvos. |  |

## Criar dados mestre de materiais para cenário de integração de projeto de cliente de preço fixo

### URR_FPPRJ_1

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Selecione o app Criar material (se o app não estiver disponível na tela, você pode tentar procurar o app Criar material). | É exibido Criar material (1ª tela). |  |
| 3 | Inserir número do material e tipo de material | Em Criar material (1ª tela), efetue as seguintes entradas:Número do produto: URR_FPPRJ_1Tipo de material: Produto de serviçosEm seguida, clique em Continuar (Enter). | Você inseriu o número e o tipo de material para os novos dados mestre de materiais.É exibida a caixa de diálogo Selecionar visões. |  |
| 4 | Selecionar visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Dados básicos 1Vendas: Dados da organização de vendas 1Vendas: Dados da organização de vendas 2Vendas: Dados gerais/dados do centroContabilidade1Em seguida, selecione Continuar (ENTER). | A caixa de diálogo Níveis organizacionais é exibida. |  |
| 5 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:Centro: 1010 (centro 1 DE)Organização de vendas: 1010 ( Org.vendas nacional DE)Canal de distribuição: 10 (vendas diretas)Em seguida, clique em Continuar (Enter). | Os dados organizacionais foram selecionados.A visão Dados básicos 1 é exibida. |  |
| 6 | Atualizar visão: Dados básicos 1 | Na visão Dados básicos 1, atualize os seguintes valores:Descr.: URR material de teste 1 TADUM básica: US (unidade de serviço)Grupo de materiais: P000 (tipo de contrato)GenItemGroup: PSFP (Item de preço fixo)Em seguida, pressione Enter. | Os dados básicos são atualizados.Depois de pressionar Enter, a visão Vendas: organização de vendas 1 é exibida. |  |
| 7 | Atualizar visão: Vendas: organização de vendas 1 | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados geraisCentro fornecedor: 1010Desconto: X <selecionado>Dados do impostoClassificação fiscal: 0Em seguida, pressione Enter. | Os dados organizacionais de vendas 1 são atualizados. A visão Vendas: organização de vendas 2 é exibida. |  |
| 8 | Atualizar visão: Vendas: organização de vendas 2 | Na visão Vendas: organização de vendas 2, atualize a seguinte entrada:Grp.ctg.item Grp: PSFP (Item de preço fixo)Acct Assmt Grp Mat: Y1 (preço fixo)Grupo de categorias de item: PSFP (Item de preço fixo)Em seguida, pressione Enter. | Os dados organizacionais de vendas 2 são atualizados. A visão Vendas: geral/centro é exibida. |  |
| 9 | Atualizar visão: Vendas: Geral/Centro | Na visão Vendas: geral/centro, atualize os seguintes valores:Centro de lucro: YB101Em seguida, pressione Enter. | Os dados gerais de venda são atualizados. A visão Contabilidade 1 é exibida. |  |
| 10 | Atualizar visão: Contabilidade 1 | Na visão Contabilidade 1, na seção Período atual, efetue a seguinte entrada:Classe de avaliação: 3300Preço padrão: 30Unidade de preço: 1Em seguida, selecione Salvar. | Os dados contábeis são atualizados.Os dados mestre de materiais são salvos. |  |
| 11 | Criar mais dados mestre de materiais para teste, se necessário | Crie mais mestres de materiais com a convenção de nomes URR_FPPRJ* (por exemplo: URR_FPPRJ3, URR_FPPRJ4, etc.) com um preço padrão diferente, se necessário. | Mais dados mestre de material de teste são criados. |  |

## Criar dados mestre de materiais para cenário de integração de contrato de prestação de serviços

### URR_SRVCONT1

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | A página Inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Selecione o app Criar material (se o app não estiver disponível na tela, você pode tentar procurar o app Criar material). | É exibido Criar material (1ª tela). |  |
| 3 | Inserir número do material e tipo de material | Em Criar material (1ª tela), efetue as seguintes entradas:Número do produto: URR_SRVCON1Tipo de material: Produto de serviçosEm seguida, selecione Continuar (ENTER). | Você inseriu o número e o tipo de material para os novos dados mestre de materiais.É exibida a caixa de diálogo Selecionar visões. |  |
| 4 | Selecionar visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Dados básicos 1Vendas: Dados da organização de vendas 1Vendas: Dados da organização de vendas 2Vendas: Dados gerais/dados do centroComprasEm seguida, selecione Continuar (ENTER). | A caixa de diálogo Níveis organizacionais é exibida. |  |
| 5 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:Centro: 1010 (centro 1 DE)Organização de vendas: 1010 ( Org.vendas nacional DE)Canal de distribuição: 10 (vendas diretas)Em seguida, selecione Continuar (ENTER). | Os dados organizacionais foram selecionados.A visão Dados básicos 1 de é exibida. |  |
| 6 | Atualizar visão: Dados básicos 1 | Na visão Dados básicos 1, atualize os seguintes valores:Descr.: URR contrato de serviço de material de teste 1UM básica: US (unidade de serviço)Grupo de materiais: P001 (Serviços)GenItemGroup: (Prod.contrato serviços) SCNPEm seguida, pressione Enter. | Os dados básicos são atualizados.Depois de pressionar Enter, a visão Vendas: organização de vendas 1 é exibida. |  |
| 7 | Atualizar visão: Vendas: organização de vendas 1 | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados geraisUM básica: US (unidade de serviço)Grupo de materiais: P001 (ServiçosEm seguida, selecione Enter. | Os dados organizacionais de vendas 1 são atualizados. A visão Vendas: organização de vendas 2 é exibida. |  |
| 8 | Atualizar visão: Vendas: organização de vendas 2 | Na visão Vendas: organização de vendas 2, atualize a seguinte entrada:Grp.ctg.item Grp.SCNP (prod. contrato serviços) SCNPEm seguida, selecione Enter. | Os dados organizacionais de vendas 2 são atualizados. A visão Vendas: geral/centro é exibida. |  |
| 9 | Atualizar visão: Vendas: Geral/Centro | Na visão Vendas: geral/centro, atualize os seguintes valores:UM básica: US (unidade de serviço)Em seguida, selecione Enter. | Os dados gerais de venda são atualizados. A visão Contabilidade 1 é exibida. |  |
| 10 | Atualizar visão: Compras | Na visão Compras, efetue a seguinte entrada:UM básica: US (unidade de serviço)Grupo de materiais: P001 (Serviços)Em seguida, selecione Salvar. | Os dados contábeis são atualizados.Os dados mestre de materiais são salvos. |  |

## Definir preços para materiais

### Preço para produtos comercializáveis para SFS: URR_MAT1_NORM

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | O launchpad do SAP Fiori é aberto. |  |
| 2 | Acessar o app SAP Fiori | Clique em Definir preços de material - Vendas(VK12). | A visão Modificar registros de condição é exibida. |  |
| 3 | Tipo de condição para a determinação de preços | Na visão Modificar registros de condição, insira as seguintes informações:Tipo de condição: PPR0Em seguida, clique em Enter. | A visão Combinação de chaves é exibida. |  |
| 4 | Combinação de chaves | Na visão Combinação de chaves, selecione a opção Material com status de liberação.Em seguida, clique em Selecionar. | A visão Modificar preço (PPR0): seleção é exibida. |  |
| 5 | Seleção | Na visão Modificar preço (PPR0): seleção, atualize as seguintes informações:Organização de vendas: 1010 ( Org.vendas nacional DE)Canal de distribuição: 10 (vendas diretas)Material: URR_MAT1_NORMVálido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição para modificação de preço (PPR0): síntese é exibida. |  |
| 6 | Modificar condição de preço | Na tela Modificar condição de preço (PPR0): síntese, atualize os seguintes dados para o material:Material: URR_MAT1_NORMMontante: por exemplo, 25,00Unidade: EURVálido desde: <Data> por exemplo, a data de hojeClique em Enter. | A condição do preço foi atualizada. |  |
| 7 | Salvar | Clique em Salvar. | Os preços foram definidos. |  |
| 8 | Voltar e acessar o app novamente | Na visão Modificar registros de condição, insira as seguintes informações:Tipo de condição: PSAMEm seguida, pressione Enter. | A visão Combinação de chaves é exibida. |  |
| 9 | Combinação de chaves | Na visão Combinação de chaves, selecione a opção Material com status de liberação.Em seguida, pressione Enter. | A visão Modificar preço (PSAM): seleção é exibida. |  |
| 10 | Seleção | Na visão Modificar preço (PSAM): seleção, atualize as seguintes informações:Organização de vendas: 1010 ( Org.vendas nacional DE)Canal de distribuição: 10 (vendas diretas)Material: URR_MAT1_NORMVálido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição de preço (PSAM): síntese é exibida. |  |
| 11 | Modificar condição de preço | Na visão Modificar condição de preço (PSAM): síntese, atualize os seguintes dados para o material:Material: URR_MAT1_NORMMontante: por exemplo, 35,00Unidade: EURVálido desde: <Data> por exemplo, a data de hojePressione Enter. | A condição do preço foi atualizada. |  |
| 12 | Salvar | Clique em Salvar. | O preço foi definido. |  |

### Preço para produto de serviços para serviço único: URR_MAT1_SERV

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | O launchpad do SAP Fiori é aberto. |  |
| 2 | Acessar o app SAP Fiori | Clique em Definir preços de material - Vendas(VK12). | A visão Modificar registros de condição é exibida. |  |
| 3 | Tipo de condição para a determinação de preços | Na visão Modificar registros de condição, insira as seguintes informações:Tipo de condição: PPR0Em seguida, pressione Enter. | A visão Combinação de chaves é exibida. |  |
| 4 | Combinação de chaves | Na visão Combinação de chaves, selecione a opção Material com status de liberação.Em seguida, selecione Selecionar (ENTER). | A visão Modificar preço (PPR0): seleção é exibida. |  |
| 5 | Seleção | Na visão Modificar preço (PPR0): seleção, atualize as seguintes informações:Organização de vendas: 1010 ( Org.vendas nacional DE)Canal de distribuição: 10 (vendas diretas)Material: URR_MAT1_SERVVálido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição para modificação de preço (PPR0): síntese é exibida. |  |
| 6 | Modificar condição de preço | Na tela Modificar condição de preço (PPR0): síntese, atualize os seguintes dados para o material:Material: URR_MAT1_SERVMontante: por exemplo, 25,00Unidade: EURVálido desde: <Data> por exemplo, a data de hojePressione Enter. | As condições de preço para produtos dos serviços SRV_01 foram atualizadas. |  |
| 7 | Salvar | Clique em Salvar. | Os preços para os produtos dos serviços foram definidos. |  |
| 8 | Voltar e acessar o app novamente | Na visão Modificar registros de condição, insira as seguintes informações:Tipo de condição: PSAMEm seguida, pressione Enter. |  |  |
| 9 | Combinação de chaves | Na visão Combinação de chaves, selecione a opção Material com status de liberação.Em seguida, pressione Enter. | A visão Modificar preço (PSAM): seleção é exibida. |  |
| 10 | Seleção | Na visão Modificar preço (PSAM): seleção, atualize as seguintes informações:Organização de vendas: 1010 ( Org.vendas nacional DE)Canal de distribuição: 10 (vendas diretas)Material: URR_MAT1_SERVVálido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição de preço (PSAM): síntese é exibida. |  |
| 11 | Modificar condição de preço | Na visão Modificar condição de preço (PSAM): síntese, atualize os seguintes dados para o material:Material: URR_MAT1_SERVMontante: por exemplo, 35,00Unidade: EURVálido desde: <Data> por exemplo, a data de hojePressione Enter. | As condições de preço para produtos dos serviços SRV_01 foram atualizadas. |  |
| 12 | Salvar | Clique em Salvar. | O preço foi definido. |  |

### Preço para material de contrato de serviços: URR_SRVCONT1

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em preços. | O launchpad do SAP Fiori é aberto. |  |
| 2 | Acessar o app SAP Fiori | Clique em Definir preços de material - Vendas(VK12). | A visão Modificar registros de condição é exibida. |  |
| 3 | Tipo de condição para determinação de preços | Na visão Modificar registros de condição, insira as seguintes informações:Tipo de condição: PSI1Em seguida, pressione Enter. | A visão Combinação de chaves é exibida. |  |
| 4 | Combinação de chaves | Na visão Combinação de chaves, selecione Material.Em seguida, pressione Enter. | A visão Modificar preço (PSI1): seleção é exibida. |  |
| 5 | Seleção | Na visão Modificar preço (PSI1): seleção, atualize as seguintes informações:Organização de vendas: 1010 ( Org.vendas nacional DE)Canal de distribuição: 10 (vendas diretas)Material: URR_SRVCONT1Válido em: <Data> por exemplo, a data de hojeEm seguida, clique em Executar. | A visão Modificar condição de preço (PSI1): síntese é exibida. |  |
| 6 | Modificar condição de preço | Na visão Modificar condição de preço (PSI1): síntese, atualize os seguintes dados:embalagem: URR_SRVCONT1Montante: por exemplo, 90,00Unidade: por exemplo, EURVálido desde: <Data> por exemplo, a data de hojePressione Enter. | As condições de preço são atualizadas. |  |
| 7 | Salvar | Clique em Salvar. | O preço foi definido. |  |

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
- related-to :: [[06-management-accounting/7r8-537]]
- related-to :: [[06-management-accounting/master-data-script-create-material-master-for-universal-revenue-recogn]]
- related-to :: [[06-management-accounting/master-data-script-item-master-for-universal-revenue-recognition-7r8-j]]
- related-to :: [[06-management-accounting/script-de-datos-maestros-crear-maestro-de-materiales-para-el-reconocim]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7R8_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 34,259 chars in the whole document
