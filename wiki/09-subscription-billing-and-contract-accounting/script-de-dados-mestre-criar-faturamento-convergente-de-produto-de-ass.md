---
id: 09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-convergente-de-produto-de-ass
title: Script de dados mestre - Criar faturamento convergente de produto de assinatura - MDS (5LP) (5LP_S4CLD2608_Master_Data_PT_XX)
description: "Master data script (PT) for SAP S/4HANA Cloud Public Edition 2608: create subscription products, rate elements, price lookup tables and enrich SBPD/SBRE products (5LP)."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/subscription-product-master-data]
aliases: [5LP_S4CLD2608_Master_Data_PT_XX]
keywords: [Subscription Products and Rate Plans, subscription products, convergent billing, rate elements, rate plan templates, price calculation, lookup tables, product master enrichment, business partners, contract accounts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_PT_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-452
topic: 09-subscription-billing-and-contract-accounting/subscription-product-master-data
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar faturamento convergente de produto de assinatura - MDS (5LP) (5LP_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Subscription Products and Rate Plans** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar faturamento convergente de produto de assinatura - MDS (5LP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893783)

[2 Pré-requisitos 3](#_Toc233893784)

[2.1 Acesso ao sistema 3](#_Toc233893785)

[2.2 Funções 3](#_Toc233893786)

[2.3 Unidades organizacionais necessárias (SAP S/4HANA) 4](#_Toc233893787)

[3 Tabela de síntese 5](#_Toc233893788)

[4 Procedimentos 6](#_Toc233893789)

[4.1 Criar parceiro de negócios 6](#_Toc233893790)

[4.1.1 Criar dados mestre de cliente 7](#_Toc233893791)

[4.1.2 Criar uma conta de contrato 9](#_Toc233893792)

[4.2 Criar produto de assinatura (SAP Subscription Billing) 11](#_Toc233893793)

[4.2.1 Criar elementos de tarifa 11](#_Toc233893794)

[4.2.2 Criar modelo de plano de tarifas 12](#_Toc233893795)

[4.2.3 Criar produto (SAP Subscription Billing) 14](#_Toc233893796)

[4.2.4 Criar um produto para serviços de cálculo de preço 16](#_Toc233893797)

[4.2.5 Carregar tabelas de pesquisa para determinação de preços 18](#_Toc233893798)

[4.3 Enriquecer produtos de faturamento de assinatura 23](#_Toc233893799)

[4.3.1 Ampliar produto de assinatura do tipo SBPD 23](#_Toc233893800)

[4.3.2 Ampliar produtos de assinatura do tipo SBRE 26](#_Toc233893801)

[5 Anexo 30](#_Toc233893802)

## Objetivo

Neste documento, você pode encontrar uma descrição sobre como criar dados mestre de produto de assinatura. A descrição inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema "normal". Aqui, o leitor sabe principalmente quais segmentos de dados e campos precisam ser preenchidos com valores de entrada. Os campos que não são relevantes para o escopo não são descritos neste documento, embora eles possam aparecer na interface do usuário.

Um registro mestre de assinatura criado por este documento pode ser utilizado para o faturamento de assinatura.

| ID do produto de assinatura | Descrição | Utilização |
| --- | --- | --- |
| P-CLOUD_COMM | Produto de assinatura | Representa o produto de assinatura |
| P-CLOUD_SUPPORT | Produto de assinatura | Representa o produto de assinatura |

## Pré-requisitos

### Acesso ao sistema

A tabela a seguir discute os requisitos de acesso ao sistema.

| Sistema | Detalhes |
| --- | --- |
| Sistema SAP S/4HANA | Acessível via launchpad do SAP Fiori.O administrador do sistema fornece o URL para acessar os vários apps atribuídos à sua função. |
| SAP Subscription Billing | Acessível via URL.Seu administrador do sistema fornece a você o URL para acessar o app. |

### Funções

Você pode criar funções empresariais utilizando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

SAP S/4HANA

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) | Efetuar login |
| --- | --- | --- | --- | --- |
| Especialista em dados mestre – Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Especialista em dados mestre – Dados do produto | SAP_BR_PRODMASTER_SPECIALIST |  |
| Contador da contabilidade de fornecedores/clientes (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Contador da contabilidade de fornecedores/clientes (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA |  |

SAP Subscription Billing

Você deve contatar o administrador do sistema para configurar as autorizações necessárias.

### Unidades organizacionais necessárias (SAP S/4HANA)

Enquanto alguns segmentos dos dados mestre são dependentes das unidades organizacionais da empresa. Os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Unidade organizacional a ser usada | Comentários |
| --- | --- | --- | --- |
| Criar registro de dados mestre | Organização de vendas | 1710 ( Org.vendas nac.EUA) | Para a Alemanha, utilize 1010 ( Org.vendas nacional DE) |
| Criar registro de dados mestre | Canal de distribuição | 10 (vendas diretas) |  |

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

| Segmento | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| Criar produto de assinatura (SAP Subscription Billing) | N/A | N/A | Os produtos de assinatura são criados. |
| Enriquecer produtos de assinatura (SAP S/4HANA) | SAP_BR_PRODMASTER_SPECIALIST | Administrar dados mestre do produto | Os produtos de assinatura são criados. |

## Procedimentos

Esta seção descreve procedimentos para cada segmento ou etapa de processo que faz parte deste registro mestre.

### Criar parceiro de negócios

Contexto

Nesta atividade, você cria um parceiro de negócios para um novo cliente FI-CA no S/4HANA Cloud.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como contador da contabilidade de fornecedores e de clientes (FI-CA). | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar parceiro de negócios (BP). | A visão Atualizar parceiro de negócios é exibida. |  |
| 3 | Criar um parceiro de negócios | Selecione Pessoa ou Mais > Parceiro de negócios > Criar > Pessoa. | A visão Criar pessoa é exibida. |  |
| 4 | Selecione a função PN. | Efetue a seguinte entrada:Criar na função PN: Parceiro de contrato | A visão Modificar para outra função PN é exibida no modo de criação. |  |
| 5 | Criar | Selecione Criar | Selecione Função de parceiro de contrato na caixa de diálogo Criar pessoa.Parceiro do contrato (novo) é selecionado para Criar na função PN. |  |
| 6 | Inserir dados básicos | Efetue as seguintes entradas:Parceiro de negócios: <Insira um ID específico>, por exemplo, BP_US_97Agrupamento: numeração alfanumérica externa |  |  |
| 7 | Inserir dados de endereço | Efetue a seguinte entrada na guia Endereço:Primeiro nome/sobrenome: John/MillerRua/número: Avenida Hillview/3410Código postal/cidade: 94304/PALO ALTOPaís: EUARegião: CADomicílio fiscal: CA00000000Dica Se o Domicílio fiscal não estiver visível, clique em + para expandir as opções. |  |  |
| 8 | Atualizar dados de pagamento | Adicione dados bancários utilizando o app Administrar parceiro de negócios e registre o cartão de pagamento utilizando o app Administrar dados mestre do parceiro de negócios.Efetue a seguinte entrada na guia Transações de pagamento:Na seção Dados bancários, insira:ID: 01País: EUACódigo do banco: 011000390Cta.bancária: <conta bancária>Código SWIFT (SWIFT/BIC): CITIUS33XXXClique em Enviar. | Aparece a visão Verificando chave de reconciliação. |  |
| 9 | Salvar | Clique em Salvar. | Um novo parceiro de negócios é criado. |  |

#### Criar dados mestre de cliente

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Contexto

Nesta atividade, você amplia um parceiro de negócios FI-CA com a função de PN FLCU01 e MKK com os dados mestre da área de vendas.

Procedimentos

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori com as suas credenciais de usuário como SAP_BR_APR_ACCOUNTANT_FICA | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar parceiro de negócios(BP). | A tela Atualizar parceiro de negócios é exibida. |  |
| 3 | Selecionar parceiro de negócios | Insira o número do Parceiro de negócios |  |  |
| 4 | Abrir Parceiro de negócios | Selecione Enter |  |  |
| 5 | Comutar para modo de modificação | Clique em Comutar entre exibição e modificação. |  |  |
| 6 | Alterar em função PN | No campo Modificar em função PN, selecione o seguinte valor: ClienteA chave técnica desta função de PN é FLCU01. |  |  |
| 7 | Informação de entrada para endereço | Idioma correspondência: <EN> |  |  |
| 8 | Abrir Área de vendas | Selecione Vendas e distribuição na parte superior da visão. | A visão Área de vendas é exibida. |  |
| 9 | Inserir dados da área de vendas | Insira os seguintes dados:Organização de vendas: 1710Canal de distribuição: 10Setor de atividade: 00Pressione Enter e, em seguida, Salvar.Nota As três entradas acima formam a área de vendas. Em muitos casos, a área de vendas define o objetivo para o processamento de vendas, por exemplo, no âmbito da ordem do cliente ou da determinação do preço. | As alterações são salvas para o parceiro de negócios. |  |
| 10 | Inserir dados de expedição | Na guia Expedição, na seção Expedição, insira os seguintes dados:Centro fornecedor: 1710 |  |  |
| 11 | Inserir dados de imposto | Na guia Faturamento, na seção Imposto liquidado,insira os seguintes dados:Classificação fiscal: <1>Por exemplo, o valor <1> significa que este cliente é totalmente tributável. |  |  |
| 12 | Salvar os dados | Salve as suas entradas. |  |  |
| 13 | Alterar em função PN | No campo Modificar em função PN, selecione o seguinte valor: Parceiro de contratoA chave técnica desta função de PN é MKK. |  |  |
| 14 | Informação de entrada para endereço | Idioma correspondência: <EN> |  |  |
| 15 | Inserir dados de expedição | Na guia Expedição, na seção Expedição, insira os seguintes dados:Centro fornecedor: 1710 |  |  |
| 16 | Inserir dados de imposto | Na guia Faturamento, na seção Imposto liquidado,insira os seguintes dados:Classificação fiscal: <1>Por exemplo, o valor <1> significa que este cliente é totalmente tributável. |  |  |
| 17 | Salvar os dados | Salve as suas entradas. |  |  |

#### Criar uma conta de contrato

Contexto

Nesta atividade, você cria dados mestre de conta de contrato para um cliente FI-CA no SAP S/4HANA Cloud Public Edition.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori com suas credenciais de usuário usando a função empresarial Contador da contabilidade de fornecedores e de clientes (FI-CA). | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar conta de contrato(CAA3). | A tela Exibição de conta de contrato: 1ª tela é exibida. |  |
| 3 | Criar uma conta de contrato | Selecione Criar ou Mais > Conta do contrato > Criar. | A tela Criação de contas de contrato: 1ª tela é exibida. |  |
| 4 | Inserir dados básicos | Efetue a seguinte entrada:Conta de contrato: <insira um ID específico>, por exemplo, CA_US_97Parceiro de negócios: <Selecione o número do parceiro de negócios criado na etapa Criar um parceiro de negócios>Ctg. cta. cont.: Y1Válido desde: <data de hoje> |  |  |
| 5 | Atualizar detalhes da conta de contrato | Clique em Continuar. | A tela Criação de contas de contrato: dados gerais é exibida. |  |
| 6 | Inserir dados gerais | Na guia Informações gerais, efetue a seguinte entrada:Nome cta.contrato: <nome da conta de contrato>Relação conta: titular da contaGrupo de tolerância: Y001 Tolerância não permitidaGrupo de planejamento: Clientes nacionaisCondições de pagamento: YN01ID determ. cta.: Y1 |  |  |
| 7 | Inserir dados de pagamentos/impostos | Efetue a seguinte entrada na guia Pagamentos/impostos:Grupo de empresas: 1710Empresa padrão: 1710 |  |  |
| 8 | Inserir advertências/correspondência | Efetue a seguinte entrada na guia Advertências/correspondência:Variante de correspond.: <só impressão, imediata> |  |  |
| 9 | Salvar | Clique em Salvar. | Uma nova conta de contrato é criada. |  |

### Criar produto de assinatura (SAP Subscription Billing)

#### Criar elementos de tarifa

Objetivo

Nesta atividade, você cria elementos de tarifa no SAP Subscription Billing. Os IDs da tarifa devem corresponder aos produtos S/4HANA relevantes do tipo SBRE:

| ID da tarifa | Tipo de tarifa | Descrição |
| --- | --- | --- |
| R-ONETIME | Única | Taxa de ativação única |
| R-SEATS | Periódico | Taxa mensal baseada no assento |
| R-TICKETS | Baseado na utilização | Taxa de uso baseada em ticket |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no SAP Subscription Billing. | É exibida a Página inicial. |  |
| 2 | Navegar para elementos de tarifa | Em Dados mestre e configuração, selecione Configuração empresarial > Elementos de tarifa. | A visão Elementos de tarifa é exibida. |  |
| 3 | Criar elemento de tarifa: Única | Selecione Criar e, em seguida, atualize os seguintes dados:Tipo: ÚnicaID: R-ONETIMEUnidade: Unidade (Unid.)Etiqueta: Taxa de ativação únicaFonte de dados: NenhumaTipo único: Taxa inicialTipo de faturamento: TaxaDescrição: Atualize uma descrição, por exemplo, Taxa de ativação únicaAtivo: SelecionadoSelecione Gravar. | O elemento de tarifa R-One-Time é criado. |  |
| 4 | Criar elemento de tarifa: R-SEATS | Selecione Criar e, em seguida, atualize os seguintes dados:Tipo: PeriódicoID: R-SEATSUnidade: Unidade (Unid.)Etiqueta: Taxa mensal baseada no assentoFonte de dados: AssinaturaTipo de faturamento: TaxaDescrição: Atualize uma descrição, por exemplo, Taxa mensal baseada no assentoAtivo: SelecionadoSelecione Gravar. | O elemento de tarifa R-SEATS é criado. |  |
| 5 | Criar elemento de tarifa: R-TICKETS | Selecione Criar e, em seguida, atualize os seguintes dados:Tipo: Baseado na utilizaçãoID: R-TICKETSUnidade: Gigabyte (GB)/Unidade (Unid.)Etiqueta: Taxa de uso baseada em ticketFonte de dados: UtilizaçãoTipo de faturamento: TaxaVariante de avaliação de utilização: AgregadoTipo de ID de recurso técnico: ID de espaço de memória na nuvemDescrição: Atualize uma descrição, por exemplo, Carregar/baixar tráfego em GBAtivo: SelecionadoSelecione Gravar. | O elemento de tarifa R-TICKETS é criado. |  |

#### Criar modelo de plano de tarifas

Objetivo

Nesta atividade, você cria um modelo de plano de tarifas no SAP Subscription Billing.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no SAP Subscription Billing. | É exibida a Página inicial. |  |
| 2 | Navegar para modelos de plano de tarifas | Em Determinação do preço, abra o app Modelos do plano de tarifas. | Os modelos de plano de tarifas disponíveis são exibidos. |  |
| 3 | Criar modelo de plano de tarifas: SEATS | Selecione Criar > Sem esquema de determinação de preço e atualize os seguintes dados nas Informações gerais:Descrição: Modelo do plano baseado no assentoCiclo de cálculo da fatura: Valor - mensalmente no primeiro dia do mêsMoeda: Valor – USD (para a versão de país EUA)Clique em Adicionar | Os dados básicos para o modelo são definidos. |  |
| 4 | Atualizar taxas/créditos para SEATS | Crie uma cobrança única na seção Taxas/créditos ao selecionar Adicionar > uma vez. Atualize os seguintes dados:Elemento de tarifa: R-ONETIMEPreço: Valor - 9,99 USD (para a versão de país EUA)Crie uma cobrança recorrente na seção Taxas/créditos ao selecionar Adicionar > determinação > do preço de porcentagem recorrente. Atualize os seguintes dados:Elemento de tarifa: R-SEATSAplicar modificações com próximo ciclo: selecionadoAdiantamento de faturamento: selecionadoDistribuir pro-rata primeiro ciclo: selecionadoPreço por unidade: 1 USDRelação: 100Crie uma cobrança baseada na utilização na seção Taxas/créditos ao selecionar Adicionar > determinação de preço de bloco > baseada na utilização. Atualize os seguintes dados:Elemento de tarifa:R-TICKETSAplicar modificações com próximo ciclo: Não selecionadoQuantidade incluída: Valor – 1Tamanho do bloco: Valor – 1Preço por bloco: Valor - 1 USD (para a versão de país EUA)Clique em Salvar e Publicar. | As taxas/créditos são criados. |  |

#### Criar produto (SAP Subscription Billing)

Objetivo

Nesta atividade, você cria produtos P-CLOUD_COMM e P-CLOUD_SUPPORT no SAP Subscription Billing. O ID do produto no SAP Subscription Billing deve corresponder ao ID do produto relevante no SAP S/4HANA.

Procedimento

Produto: P-CLOUD_COMM

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no SAP Subscription Billing. | É exibida a Página inicial. |  |
| 2 | Navegar para produtos | No catálogo Dados mestre e configuração, selecione Configuração empresarial > Produtos. | Os produtos disponíveis são exibidos. |  |
| 3 | Atualizar informações gerais sobre o produto | Selecione Criar e, em seguida, atualize os seguintes dados na área Informações gerais:Nome do produto: Comunicação na nuvemID do produto: P-CLOUD_COMMTipo de assinatura: ComercialCriar assinaturas como pendentes: desmarcadoVendido eletronicamente: Selecionado | As informações gerais foram atualizadas. |  |
| 4 | Atualizar plano de tarifas para produto | Na área Planos de tarifas, selecione Criar plano de tarifas a partir do modelo.Na visão Criar plano de tarifas, atualize os seguintes dados:Mercado: Leste dos EUA (para versão de país US)Modelo do plano de tarifas: Modelo do plano baseado no assentoDescrição: Plano de tarifas periódicas (baseado no assento) | O plano de tarifas do produto foi atualizado. |  |
| 5 | Atualizar prazos de assinatura | Atualize os seguintes detalhes de parâmetros de assinatura:Prazo previsto: por exemplo,12Prazo mínimo: 12Período de renovação: 12Período de revogação: 14 | Os termos de assinatura são atualizados. |  |
| 6 | Criar produto | Na visão Criar plano de tarifas, clique em Criar.Na visão Produto, clique em Salvar.Em seguida, clique em Publicar. | O produto P-CLOUD_COMM é criado. |  |

Produto: P-CLOUD_SUPPORT

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no SAP Subscription Billing. | É exibida a Página inicial. |  |
| 2 | Navegar para produtos | Na área de navegação do lado esquerdo, selecione Produtos. | Os produtos disponíveis são exibidos. |  |
| 3 | Atualizar informações gerais sobre o produto | Selecione Criar e, em seguida, atualize os seguintes dados na área Informações gerais:Nome do produto: Suporte na nuvemID do produto: P-CLOUD_SUPPORTTipo de assinatura: ComercialCriar assinaturas como pendentes: desmarcadoVendido eletronicamente: Selecionado | As informações gerais foram atualizadas. |  |
| 4 | Atualizar plano de tarifas para produto | Na área Planos de tarifas, selecione Criar plano de tarifas a partir do modelo.Na visão Criar plano de tarifas, atualize os seguintes dados:Mercado: Leste dos EUA (para versão de país US)Modelo do plano de tarifas: Modelo do plano baseado no assentoDescrição: Plano de tarifas periódicas (baseado no assento) | O plano de tarifas do produto foi atualizado. |  |
| 5 | Atualizar prazos de assinatura | Atualize os detalhes de parâmetros de assinatura:Prazo previsto: por exemplo, 12Prazo mínimo: 12Período de renovação: 12Período de revogação: 14 | Os termos de assinatura são atualizados. |  |
| 6 | Criar produto | Na visão Criar plano de tarifas, clique em Criar.Na visão Produto, clique em Salvar.Em seguida, clique em Publicar. | O produto P-CLOUD_SUPPORT é criado. |  |

#### Criar um produto para serviços de cálculo de preço

Ao passar por um caso de uso de amostra, você pode usar os valores de amostra para criar dados do zero ou pode usar a configuração predefinida fornecida com cada novo locatário. Você deve executar as seguintes etapas no cálculo de preços antes de criar um produto para PCS.

Procedimento

1. Administrar catálogo de campos

Se você estiver usando os dados de amostra, um catálogo de campos predefinido é usado no app Administrar catálogo de campos. Assim, você não precisa efetuar configurações adicionais aqui. O app Administrar catálogo de campos permite a você criar campos que são usados posteriormente para definir as tabelas de pesquisa e características de entrada para especificações de elemento de preço.

2. Criar tabelas de pesquisa

No app Administrar tabelas de pesquisa, você pode criar tabelas de pesquisa mapeando um conjunto de campos de entrada para um conjunto de campos de saída. Em seguida, essas tabelas de pesquisa são usadas em uma etapa posterior para criar especificações de elemento de preço. O objetivo desta etapa é criar as seguintes tabelas de pesquisa para taxas únicas, recorrentes e de utilização:

- OneTimePrice
- RecurringPrice
- UsagePrice
- Discount1

Essas tabelas fazem parte do conteúdo predefinido. Assim, você não precisa efetuar configurações adicionais nesta etapa.

3. Especificações do elemento de preço

No app Administrar especificações do elemento de preço, você define sua configuração de determinação de preços criando especificações do item de preço. Isso inclui a configuração da lógica de determinação de preços e campos substituíveis:

- OneTimePrice
- RecurringPrice
- UsagePrice
- Discount1

Essas especificações de elemento de preço fazem parte do conteúdo predefinido. Assim, você não precisa efetuar configurações adicionais nesta etapa.

4. Esquema de determinação de preços

No app Administrar esquema de determinação de preços, você cria e atualiza esquemas de determinação de preços. Um esquema de determinação de preços é um procedimento que define a utilização e a relação das especificações do elemento de preço para um determinado documento com preço calculável. Ele também determina a sequência de execução dessas especificações para gerar um montante total em um documento precificado.

O esquema de determinação de preços 'Inicial' faz parte do conteúdo predefinido. Assim, você não precisa efetuar configurações adicionais nesta etapa.

5. Criar modelo de plano de tarifas

| Nº da etapa de teste | Nome da etapa de teste | Instruções | Resultados previstos | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no SAP Subscription Billing. | A página Inicial é exibida. |  |
| 2 | Navegue para o app Modelos de plano de tarifas | Vá para Determinação de preços > Modelos de plano de tarifas | Os modelos de plano de tarifas são exibidos. |  |
| 3 | Selecione Criar | Selecione Criar – Com esquema de determinação de preços e atualize os seguintes dados nas Informações gerais:Descrição: RPT para cálculo de preçoTags: PCS (opcional)Esquema de determinação de preços: InicialCiclo de faturamento: mensalmente no primeiro dia do mêsMoeda: USD | As informações gerais foram atualizadas. |  |
| 4 | Atualizar Taxas/créditos para elementos de tarifa | Para únicas, selecione Taxas/créditos > Adicionar > Única e insira Elemento de tarifa = R-ONETIME.Para recorrentes, selecione Taxas/créditos > Adicionar > Recorrente e insira Elemento de tarifa = R-SEATS.Para utilização, selecione Taxas/créditos > Adicionar > Utilização – Determinação de preços de bloco e insira Elemento de tarifa = R-TRAFFIC.Clique em Salvar e, em seguida, Publicar. |  |  |

6. Criar produto

Você cria um produto P-CLOUD_STORAGE_PC no SAP Subscription Billing. O ID do produto em SAP Subscription Billing deve corresponder ao ID do produto relevante no SAP S/4HANA. Você pode usar os seguintes procedimentos:

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no SAP Subscription Billing. | A página Inicial é exibida. |  |
| 2 | Navegue para Produtos | Em Dados mestre e configuração, abra o app Produtos. | Os produtos disponíveis são exibidos. |  |
| 3 | Atualizar informações gerais sobre o produto | Clique em Criar e atualize os seguintes dados na área Informações gerais:Nome do produto: Cálculo de preço de armazenamento em nuvemID do produto: P-CLOUD_STORAGE_PCTipo de assinatura: ComercialCriar assinaturas como pendentes: desmarcado | As informações gerais foram atualizadas. |  |
| 4 | Atualizar plano de tarifas para produto | Na guia Planos de tarifas, clique em Criar – Com esquema de determinação de preços.Nota Para mais informações sobre produtos de cálculo de preços, consulte [SAP Subscription Billing com esquemas de determinação de preços](https://help.sap.com/docs/CLOUD_TO_CASH_OD/3da4082dc5094e3489b7c98e9113cf6c/3542ae740bb046b9bf422e193f3e0526.html)Navegue para Criar plano de tarifas a partir do modelo > Criar plano de tarifas com esquema de determinação de preços e atualize os seguintes dados:Mercado: Leste dos EUA (para versão de país US)Modelo do plano de tarifas: RPT para cálculo de preçoDescrição: RPT para cálculo de preçoCiclo de faturamento: mensalmente no primeiro dia do mêsSelecione Criar. | O plano de tarifas foi atualizado para o produto. |  |
| 5 | Atualizar Prazos de assinatura | Atualize os seguintes dados na área Termos da assinatura:Prazo previsto: por exemplo, 12Período de validade mínimo: 12Período de renovação: 12Período de revogação: 14 | Os termos de assinatura são atualizados. |  |
| 6 | Criar produto | Na visão Criar plano de tarifas, clique em Criar.Na visão Produto, clique em Salvar.Clique em Publicar. | O produto P-CLOUD_STORAGE_PC é criado. |  |

7. Carregar tabelas de pesquisa para determinação de preços

Para obter maiores informações sobre o carregamento de tabelas de pesquisa, consulte Carregar tabelas de pesquisa para determinação de preços.

Para mais informações sobre produtos de cálculo de preços, consulte [SAP Subscription Billing com esquemas de determinação de preços](https://help.sap.com/docs/CLOUD_TO_CASH_OD/3da4082dc5094e3489b7c98e9113cf6c/3542ae740bb046b9bf422e193f3e0526.html)

#### Carregar tabelas de pesquisa para determinação de preços

Você pode carregar suas tabelas de pesquisa para taxas únicas, recorrentes e baseadas no uso e para desconto, usando o seguinte procedimento. Os dados na tabela a seguir são usados para encontrar os preços relevantes durante a determinação de preços como parte do processo de classificação.

Tabela 1: Carregar tabela única

| Nº da etapa de teste | Nome da etapa de teste | Instruções | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no SAP Price Calculation | A Página inicial é exibida. |  |
| 2 | Navegar para Modelos de plano de tarifas | Em Gerenciamento de dados mestre, abra o app Administrar dados da tabela de pesquisa. | As tabelas de pesquisa são exibidas. |  |
| 3 | Selecione OneTimePrice | Selecione a tabela de pesquisa OneTimePrice.Baixe a tabela vazia e armazene-a localmente como um arquivo CSV.Dica Se o formato do arquivo baixado não for separado por colunas, você deve alterar o formato da planilha eletrônica para um formato dos EUA. |  |  |
| 4 | Atualize o arquivo baixado | Insira os seguintes valores e salve o arquivo:productCode: P-CLOUD_STORAGE_PCmarketId: A1rateElement: R-ONETIMEprice: Singleprice (Price Type): Fixedprice (Value): 5000price (Value Currency): USD |  |  |
| 5 | Carregue o arquivo CSV | Escolha a tabela de pesquisa OneTimePrice e vá para Importar > Procurar para carregar o arquivo salvo do passo anterior.Nota Existem dois tipos de importações: Selecione Consolidar para manter os dados existentes intactos.Clique em Importar. | A tabela de pesquisa OneTimePrice é atualizada. |  |

Tabela 2: Carregar tabela recorrente

| Nº da etapa de teste | Nome da etapa de teste | Instruções | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no SAP Price Calculation | A Página inicial é exibida. |  |
| 2 | Navegar para Modelos de plano de tarifas | Em Gerenciamento de dados mestre, abra o app Administrar dados da tabela de pesquisa. | As tabelas de pesquisa são exibidas. |  |
| 3 | Selecione RecurringPrice | Selecione a tabela de pesquisa RecurringPrice.Baixe a tabela vazia e armazene-a localmente como um arquivo CSV.Dica Se o formato do arquivo baixado não for separado por colunas, você deve alterar o formato da planilha eletrônica para um formato dos EUA. |  |  |
| 4 | Atualize o arquivo baixado | Insira os seguintes valores e salve o arquivo:productCode: P-CLOUD_STORAGE_PCmarketId: A1rateElement: R-SEATSprice: Singleprice (Price Type): Linearprice (Value): 50price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA |  |  |
| 5 | Carregue o arquivo CSV | Escolha a tabela de pesquisa RecurringPrice e vá para Importar > Procurar para carregar o arquivo salvo do passo anterior.Nota Existem dois tipos de importações: Selecione Consolidar para manter os dados existentes intactos.Clique em Importar. | A tabela de pesquisa RecurringPrice é atualizada. |  |

Tabela 3: Carregar tabela de utilização

| Nº da etapa de teste | Nome da etapa de teste | Instruções | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no SAP Price Calculation | A Página inicial é exibida. |  |
| 2 | Navegar para Modelos de plano de tarifas | Em Gerenciamento de dados mestre, abra o app Administrar dados da tabela de pesquisa. | As tabelas de pesquisa são exibidas. |  |
| 3 | Selecione UsagePrice | Selecione a tabela de pesquisa OneTimePrice.Baixe a tabela vazia e armazene-a localmente como um arquivo CSV.Dica Se o formato do arquivo baixado não for separado por colunas, você deve alterar o formato da planilha eletrônica para um formato dos EUA. |  |  |
| 4 | Atualize o arquivo baixado | Insira os seguintes valores e salve o arquivo:productCode: P-CLOUD_STORAGE_PCmarketId: A1rateElement: R-TRAFFICprice: Volumeprice (Price Type): LinearOs seguintes valores específicos estão disponíveis para cada nível para um subelemento de taxa alta:rateSubElement: Altoprice (Range): 500price (Range Unit): EAprice (Value): 30price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAOs seguintes valores específicos estão disponíveis para cada nível:rateSubElement: Altoprice (Range): 1000price (Range Unit): EAprice (Value): 25price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAOs seguintes valores específicos estão disponíveis para cada nível:rateSubElement: Altoprice (Range):price (Range Unit): EAprice (Value): 20price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAOs seguintes valores específicos estão disponíveis para cada nível para um subelemento de taxa baixa:rateSubElement: Baixoprice (Range): 500price (Range Unit): EAprice (Value): 15price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAOs seguintes valores específicos estão disponíveis para cada nível para um subelemento de taxa baixa:rateSubElement: Baixoprice (Range): 1000price (Range Unit): EAprice (Value): 10price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAOs seguintes valores específicos estão disponíveis para cada nível para um subelemento de taxa baixa:rateSubElement: Baixoprice (Range):price (Range Unit): EAprice (Value): 5price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA |  |  |
| 5 | Carregue o arquivo CSV | Escolha a tabela de pesquisa OneTimePrice e vá para Importar > Procurar para carregar o arquivo salvo do passo anterior.Nota Existem dois tipos de importações: Selecione Consolidar para manter os dados existentes intactos.Clique em Importar.. | A tabela de pesquisa OneTimePrice é atualizada. |  |

Tabela 4: Carregar tabela de descontos

| Nº da etapa de teste | Nome da etapa de teste | Instruções | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no SAP Price Calculation | A Página inicial é exibida. |  |
| 2 | Navegar para Modelos de plano de tarifas | Em Gerenciamento de dados mestre, abra o app Administrar dados da tabela de pesquisa. | As tabelas de pesquisa são exibidas. |  |
| 3 | Selecione Discount1 | Selecione a tabela de pesquisa Discount1.Baixe a tabela vazia e armazene-a localmente como um arquivo CSV.Dica Se o formato do arquivo baixado não for separado por colunas, você deve alterar o formato da planilha eletrônica para um formato dos EUA. |  |  |
| 4 | Atualize o arquivo baixado | Insira os seguintes valores e salve o arquivo:marketId: A1discount: Singlediscount (Price Type): Percentagediscount (value): 0,1 |  |  |
| 5 | Carregue o arquivo CSV | Escolha a tabela de pesquisa Discount1 e vá para Importar > Procurar para carregar o arquivo salvo do passo anterior.Nota Existem dois tipos de importações: Selecione Consolidar para manter os dados existentes intactos.Clique em Importar.. | A tabela de pesquisa Discount1 é atualizada. |  |

### Enriquecer produtos de faturamento de assinatura

#### Ampliar produto de assinatura do tipo SBPD

Objetivo

Nesta atividade, você amplia os produtos de assinatura P-CLOUD_COMM e P-CLOUD_SUPPORT no SAP S/4HANA. Esses produtos são criados no SAP Subscription Billing e replicados no SAP S/4HANA.

Procedimento

Produto: P-CLOUD_COMM

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Selecione o bloco Administrar dados mestre de produto. | É exibido o app Administrar dados mestre do produto. |  |
| 3 | Procurar produto P-CLOUD_COMM | Na área de pesquisa na parte superior,insira o Produto:P-CLOUD_COMM.Pressione o botão Ir. | Seu produto é exibido na lista de relatórios. |  |
| 4 | Abrir produto e atualizar cadeias de distribuição: Informações gerais | Selecione o produto a partir da lista de relatórios.Número do produto:P-CLOUD_COMMUnidade básica: EATipo de produto:SBPD (produto faturamento de assinatura)Em seguida, clique em OK.Nota Em Descrição, forneça os detalhes de Idioma e Produto para uma região específica, por exemplo, Idioma: inglês e Produto: Produto de faturamento de assinatura. | O produto deve ser aberto e as informações gerais atualizadas. |  |
| 5 | Atualizar cadeias de distribuição: Informações gerais | Na visão Produto, na área Cadeias de distribuição, selecione Criar e atualize os seguintes dados:Organização de vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Nota A cadeia de distribuição não é necessária para o tipo de produto SBPD caso esteja usando MDI. Isso é necessário apenas quando você usa o Cloud Integration. | Os critérios de agrupamento são atualizados e o produto é salvo. | Para a versão de país Alemanha, atualize o seguinte valor em vez de 1 (Imposto total):Classificação fiscal: 6 (imposto total (serviços))As outras entradas são as mesmas para os dois países. |
| 6 | Atualizar cadeias de distribuição: Critérios de agrupamento | Navegue para a área Critérios de agrupamento e atualize os seguintes dados:Grupo de categorias de item: SBPD (produto faturamento de assinatura)Grupo de classificações contábeis: X9 (serviço periódico)Classificação fiscal: 1 (imposto total)Em seguida, selecione Aplicar e, em seguida, Criar.Nota O grupo de categorias de item só é necessário se você estiver usando o Cloud Integration e não o Master Data Integration para replicação |  |  |
| 7 | Atualizar centros | Navegue para a área Centros, selecione Criar e atualize os seguintes dados:Centro: 1710 (centro EUA)Em seguida, selecione Aplicar e depois Gravar | Os dados do centro são atualizados. |  |

Produto: P-CLOUD_SUPPORT

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Selecione o bloco Administrar dados mestre de produto. | É exibido o app Administrar dados mestre do produto. |  |
| 3 | Procurar produto P-CLOUD_SUPPORT | Na área de pesquisa na parte superior,insira o Produto: P-CLOUD_SUPPORTPressione o botão Ir. | Seu produto é exibido na lista de relatórios. |  |
| 4 | Abrir produto e atualizar cadeias de distribuição: Informações gerais | Selecione o produto a partir da lista de relatórios.Número do produto:P-CLOUD_COMMUnidade básica: EATipo de produto:SBPD (produto faturamento de assinatura)Em seguida, clique em OK.Nota Em Descrição, forneça os detalhes de Idioma e Produto para uma região específica, por exemplo, Idioma: inglês e Produto: Produto de faturamento de assinatura. | O produto deve ser aberto e as informações gerais atualizadas. |  |
| 5 | Atualizar cadeias de distribuição: Informações gerais | Na visão Produto, na área Cadeias de distribuição, selecione Criar e atualize os seguintes dados:Organização de vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Nota A cadeia de distribuição não é necessária para o tipo de produto SBPD se você estiver usando Master Data Integration. Isso é necessário apenas quando você usa o Cloud Integration. | Os critérios de agrupamento são atualizados e o produto é salvo. | Para a versão de país Alemanha, atualize o seguinte valor em vez de 1 (Imposto total):Classificação fiscal: 6 (imposto total (serviços))As outras entradas são as mesmas para os dois países. |
| 6 | Atualizar cadeias de distribuição: Critérios de agrupamento | Navegue para a área Critérios de agrupamento e atualize os seguintes dados:Grupo de categorias de item: SBPD (produto faturamento de assinatura)Grupo de classificações contábeis: X9 (serviço periódico)Classificação fiscal: 1 (imposto total)Em seguida, selecione Aplicar e, em seguida, Criar.Nota A cadeia de distribuição não é necessária para o tipo de produto SBPD se você estiver usando Master Data Integration e somente necessária se estiver usando Cloud Integration. |  |  |
| 7 | Atualizar centros | Navegue para a área Centros, selecione Criar e atualize os seguintes dados:Centro: 1710 (centro EUA)Em seguida, selecione Aplicar e depois Gravar | Os dados do centro são atualizados. |  |

#### Ampliar produtos de assinatura do tipo SBRE

Objetivo

Nesta atividade, você amplia os seguintes produtos de assinatura no SAP S/4HANA. Esses produtos são criados no SAP Subscription Billing e replicados no SAP S/4HANA.

| ID do produto | Tipo de produto | Descrição |
| --- | --- | --- |
| R-ONETIME | SBRE | Taxa de ativação única |
| R-SEATS | SBRE | Taxa mensal baseada no assento |
| R-TICKETS | SBRE | Taxa de uso baseada em ticket |

Procedimento

Produto: R_ONETIME

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Selecione o bloco Administrar dados mestre de produto. | É exibido o app Administrar dados mestre do produto. |  |
| 3 | Procurar produto R_ONETIME | Na área de pesquisa, insira o Produto:R-ONETIMEClique em Ir. | Seu produto é exibido na lista de relatórios. |  |
| 4 | Abrir produto e atualizar cadeias de distribuição: Informações gerais | Na visão Produto, na área Cadeias de distribuição, selecione Criar e atualize os seguintes dados:Organização de vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Desconto: SimNota Em Descrição, forneça os detalhes de Idioma e Produto para uma região específica, por exemplo, Idioma: inglês e Produto: Produto de faturamento de assinatura. | O produto deve ser aberto e as informações gerais atualizadas. | Para a versão de país Alemanha, atualize o seguinte valor em vez de 1710:Organização de vendas: 1010 ( Org.vendas nacional DE)As outras entradas são as mesmas para os dois países. |
| 5 | Atualizar cadeias de distribuição: Critérios de agrupamento | Navegue para a área Critérios de agrupamento e atualize os seguintes dados:Grupo de classificações contábeis: X9 (serviço periódico)Classificação fiscal: 1 (imposto total)Em seguida, clique em Aplicar. | Os critérios de agrupamento são atualizados e o produto é salvo. | Para a versão de país Alemanha, atualize o seguinte valor em vez de 1 (Imposto total):Classificação fiscal: 6 (imposto total (serviços))As outras entradas são as mesmas para os dois países. |
| 6 | Atualizar centros | Navegue para a área Centros, selecione Criar e atualize os seguintes dados:Centro:1710 (centro EUA)Em seguida, selecione Aplicar e, em seguida, Criar. | Os dados do centro são atualizados. |  |

Produto: R_SEATS

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Selecione o bloco Administrar dados mestre de produto. | É exibido o app Administrar dados mestre do produto. |  |
| 3 | Procurar produto R_SEATS | Na área de pesquisa, insira o Produto:R-SEATSClique em Ir. | Seu produto é exibido na lista de relatórios. |  |
| 4 | Abrir produto e atualizar cadeias de distribuição: Informações gerais | Selecione o produto a partir da lista de relatórios.Na visão Produto, clique em Editar.Na área Cadeias de distribuição, selecione Criar e atualize os seguintes dados:Organização de vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Nota Em Descrição, forneça os detalhes de Idioma e Produto para uma região específica, por exemplo, Idioma: inglês e Produto: Produto de faturamento de assinatura. | O produto deve ser aberto e as informações gerais atualizadas. | Para a versão de país Alemanha, atualize o seguinte valor em vez de 1710:Organização de vendas: 1010 ( Org.vendas nacional DE)As outras entradas são as mesmas para os dois países. |
| 5 | Atualizar cadeias de distribuição: Critérios de agrupamento | Navegue para a área Critérios de agrupamento e atualize os seguintes dados:Grupo de categorias de item: SBRE (elemento de taxa de faturamento de assinatura)Grupo de classificações contábeis: X9 (serviço periódico)Classificação fiscal: 1 (imposto total)Em seguida, selecione Aplicar. | Os critérios de agrupamento são atualizados e o produto é salvo. | Para a versão de país Alemanha, atualize o seguinte valor em vez de 1 (Imposto total):Classificação fiscal: 6 (imposto total (serviços))As outras entradas são as mesmas para os dois países. |
| 6 | Atualizar centros | Navegue para a área Centros, selecione Criar e atualize os seguintes dados:Centro:1710 (centro EUA)Em seguida, clique em Aplicar e Salvar. | Os dados do centro são atualizados. |  |

Produto: R_TICKETS

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Selecione o bloco Administrar dados mestre de produto. | É exibido o app Administrar dados mestre do produto. |  |
| 3 | Procurar produto R_TICKETS | Na área de pesquisa, insira o Produto:R-TICKETSClique em Ir. | Seu produto é exibido na lista de relatórios. |  |
| 4 | Abrir produto e atualizar cadeias de distribuição: Informações gerais | Selecione o produto a partir da lista de relatórios.Na visão Produto, clique em Editar.Na área Cadeias de distribuição, selecione Criar e atualize os seguintes dados:Organização de vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Nota Em Descrição, forneça os detalhes de Idioma e Produto para uma região específica, por exemplo, Idioma: inglês e Produto: Produto de faturamento de assinatura. | O produto deve ser aberto e as informações gerais atualizadas. | Para a versão de país Alemanha, atualize o seguinte valor em vez de 1710:Organização de vendas: 1010 ( Org.vendas nacional DE)As outras entradas são as mesmas para os dois países. |
| 5 | Atualizar cadeias de distribuição: Critérios de agrupamento | Navegue para a área Critérios de agrupamento e atualize os seguintes dados:Grupo de classificações contábeis: X9 (serviço periódico)Classificação fiscal: 1 (imposto total)Em seguida, selecione Aplicar. | Os critérios de agrupamento são atualizados e o produto é salvo. | Para a versão de país Alemanha, atualize o seguinte valor em vez de 1 (Imposto total):Classificação fiscal: 6 (imposto total (serviços))As outras entradas são as mesmas para os dois países. |
| 6 | Atualizar centros | Navegue para a área Centros, selecione Criar e atualize os seguintes dados:Centro:1710 (centro EUA)Em seguida, clique em Aplicar e Salvar. | Os dados do centro são atualizados. |  |

## Anexo

Tabela 5: Convenções tipográficas

| Tipo de estilo | Descrição |
| --- | --- |
| Exemplo | Palavras ou caracteres citados na tela.Incluem-se aqui nomes de campo, títulos de tela, textos de botões, nomes de menu, caminhos de menu e opções de menu.Referências cruzadas textuais a outros documentos. |
| Exemplo | Palavras ou expressões enfatizadas. |
| Example | Nomes técnicos de objetos de sistema.Incluem-se aqui nomes de relatórios, nomes de programas, códigos de transação, nomes de tabela e conceitos-chave de uma linguagem de programação quando rodeados por texto de corpo, por exemplo, SELECIONAR e INCLUIR. |
| Exemplo | Saída na tela.Isto inclui nomes de arquivos e diretórios e seus caminhos, mensagens, nomes de variáveis e parâmetros, texto fonte e nomes de ferramentas de instalação, upgrade e banco de dados. |
| Exemplo | Entrada exata do usuário.Estas são palavras ou caracteres que você insere no sistema, exatamente como aparecem na documentação. |
| <Exemplo> | Entrada variável do usuário.Colchetes indicam que você deve substituir estas palavras ou caracteres por entradas apropriadas ao realizar entradas no sistema. |
| Exemplo | Chaves no teclado, por exemplo, F2 ou ENTER. |

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
> Flagged while digesting this document, not verified: Rate element R-TICKETS is created, but the price-calculation rate plan template and UsagePrice table refer to R-TRAFFIC

> [!warning] Conflict
> Flagged while digesting this document, not verified: Product IDs written R_ONETIME/R_SEATS/R_TICKETS in headings but R-ONETIME/R-SEATS/R-TICKETS elsewhere

> [!warning] Conflict
> Flagged while digesting this document, not verified: P-CLOUD_SUPPORT enrichment step 4 gives product number P-CLOUD_COMM

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-convergent-invoicing-md]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-5lp-451]]
- related-to :: [[09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-convergent-invoicing-mds-5lp-453]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-creacion-de-facturacion-convergente-de-produc]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 49,022 chars in the whole document
