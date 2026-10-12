---
id: 09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-de-vendas-de-produto-de-assin
title: Script de dados mestre - Criar faturamento de vendas de produto de assinatura - MDS (5BD) (5BD_S4CLD2608_Master_Data_PT_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (PT, 5BD): create subscription products in SAP Subscription Billing and extend them in S/4HANA."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/subscription-product-master-data]
aliases: [5BD_S4CLD2608_Master_Data_PT_XX]
keywords: [Subscription Products and Rate Plans, subscription products, rate elements, rate plan templates, pricing schemes, lookup tables, product master data, sbpd products, sbre products, distribution chains]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_PT_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-428
topic: 09-subscription-billing-and-contract-accounting/subscription-product-master-data
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar faturamento de vendas de produto de assinatura - MDS (5BD) (5BD_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Subscription Products and Rate Plans** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar faturamento de vendas de produto de assinatura - MDS (5BD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893773)

[2 Pré-requisitos 3](#_Toc233893774)

[2.1 Acesso ao sistema 3](#_Toc233893775)

[2.2 Funções 3](#_Toc233893776)

[2.3 Unidades organizacionais necessárias (SAP S/4HANA) 3](#_Toc233893777)

[3 Tabela de síntese 4](#_Toc233893778)

[4 Procedimentos 5](#_Toc233893779)

[4.1 Criar produto de assinatura (SAP Subscription Billing) 5](#_Toc233893780)

[4.1.1 Criar elementos de tarifa 5](#_Toc233893781)

[4.1.2 Criar modelo de plano de tarifas 7](#_Toc233893782)

[4.1.3 Criar um produto 8](#_Toc233893783)

[4.1.4 Criar um produto com esquema de cálculo 9](#_Toc233893784)

[4.1.5 Carregar tabelas de pesquisa para determinação de preços 12](#_Toc233893785)

[4.2 Enriquecer produtos de assinatura (SAP S/4HANA) 17](#_Toc233893786)

[4.2.1 Ampliar produtos de faturamento de assinatura do tipo SBPD 17](#_Toc233893787)

[4.2.2 Ampliar produtos de faturamento de assinatura do tipo SBRE 19](#_Toc233893788)

## Objetivo

Neste documento, você pode encontrar uma descrição sobre como criar dados mestre de produto de assinatura. A descrição inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema "normal". O leitor aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo não são descritos neste documento, embora eles possam aparecer na interface do usuário.

Um registro mestre de assinatura criado da forma aqui descrita pode ser utilizado para o faturamento de assinatura.

| ID do produto de assinatura | Descrição | Utilização |
| --- | --- | --- |
| P-CLOUD_STORAGE | Produto de assinatura | Representa o produto de faturamento de assinatura |
| P-CLD_STORAGE_PCS | Produto de serviços de cálculo de preço | Representa o produto de cálculo de preços |

## Pré-requisitos

### Acesso ao sistema

| Sistema | Detalhes |
| --- | --- |
| Sistema SAP S/4HANA | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece o URL para acessar os vários apps atribuídos à sua função. |
| SAP Subscription Billing | Acessível via URL. Seu administrador do sistema fornece a você o URL para acessar o app. |
| Serviço de cálculo de preço | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece o URL para acessar os vários apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

SAP S/4HANA

| Nome | ID |
| --- | --- |
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST |

SAP Subscription Billing

Contate o seu administrador do sistema para a configuração da autorização.

### Unidades organizacionais necessárias (SAP S/4HANA)

Alguns segmentos dos dados mestre são dependentes das unidades organizacionais da empresa. Os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Unidade organizacional a ser usada | Unidade organizacional a ser usada |
| --- | --- | --- | --- |
| Criar registro de dados mestre | Organização de vendas | 1710 ( Org.vendas nac.EUA) | Para a Alemanha, use 1010 ( Org.vendas nacional DE) |
| Criar registro de dados mestre | Canal de distribuição | 10 (vendas diretas) | 10 (vendas diretas) |

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

| Segmento | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| Criar produto de assinatura (SAP Subscription Billing) | N/A | N/A | Os produtos de assinatura são criados. |
| Criar produtos de assinatura (SAP S/4HANA) | SAP_BR_PRODMASTER_SPECIALIST | Administrar dados mestre de produto | Os produtos de assinatura são criados. |

## Procedimentos

Esta seção descreve procedimentos para cada segmento ou etapa do processo que faz parte deste registro mestre.

### Criar produto de assinatura (SAP Subscription Billing)

#### Criar elementos de tarifa

Objetivo

Nesta atividade, você cria elementos de tarifa no SAP Subscription Billing. Os IDs da tarifa devem corresponder aos produtos S/4HANA relevantes do tipo SBRE:

| ID da tarifa | Tipo de tarifa | Descrição |
| --- | --- | --- |
| R-ONETIME | Única | Taxa de ativação única |
| R-SEATS | Periódico | Taxa mensal baseada no assento |
| R-TRAFFIC | Baseado na utilização | Taxa de utilização baseada no tráfego |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no SAP Subscription Billing. | A página Inicial é exibida. |  |
| 2 | Navegar para elementos de tarifa | Em Dados mestre e configuração, clique em Administrar configuração empresarial > Elementos de tarifa. | A visão Elementos de tarifa é exibida. |  |
| 3 | Criar elemento de tarifa: R-ONETIME | Clique em Criar > Ocasional e atualize os seguintes dados:ID: R-ONETIMEUnidade: Unidade (Unid.)Etiqueta: Taxa de ativação únicaFonte de dados: NenhumaTipo único: Taxa inicialTipo de faturamento: TaxaDescrição: Atualize uma descrição, por exemplo, Taxa de ativação únicaAtivo: SelecionadoSelecione Gravar. | O elemento de tarifa R-ONETIME é criado. |  |
| 4 | Criar elemento de tarifa: R-SEATS | Selecione Criar e, em seguida, atualize os seguintes dados:Tipo: PeriódicoID: R-SEATSUnidade: Unidade (Unid.)Etiqueta: Taxa mensal baseada no assentoFonte de dados: AssinaturaTipo de faturamento: TaxaDescrição: Atualize uma descrição, por exemplo, Taxa mensal baseada no assentoAtivo: SelecionadoSelecione Gravar. | O elemento de tarifa R-SEATS é criado. |  |
| 5 | Criar elemento de tarifa: R-TRAFFIC | Selecione Criar e, em seguida, atualize os seguintes dados:Tipo: Baseado na utilizaçãoID: R-TRAFFICUnidade: Unidade (Unid.)Etiqueta: Taxa de utilização baseada no tráfegoFonte de dados: UtilizaçãoTipo de faturamento: TaxaUsar subelementos de tarifa: Selecionado (só para produtos PCS)Variante de avaliação de utilização: AgregadoTipo de ID de recurso técnico: ID de espaço de memória na nuvemDescrição: Atualize uma descrição, por exemplo, Carregar/baixar tráfegoAtivo: SelecionadoSelecione Gravar. | O elemento de tarifa R-TRAFFIC é criado. |  |

|  |
| --- |
| Nota Os recursos técnicos identificam o assinante e o serviço assinado em um sistema técnico. Eles são necessários quando você fatura seus clientes com base na utilização do seu serviço. Por exemplo, medindo o consumo de eletricidade. Aqui, o Tipo de ID de recurso técnico: pode ser definido como o 'ID do medidor de eletricidade', que é o ID único (por exemplo, EM392734-A) em relação ao qual a utilização é lançada. Em um cenário em que a quilometragem está sendo medida, o Tipo de ID de recurso técnico: pode ser definido como o 'Número da placa do veículo'.Este é um campo de entrada do usuário e é definido de acordo com o serviço/cenário. |

#### Criar modelo de plano de tarifas

Objetivo

Nesta atividade, você cria um modelo de plano de tarifas no SAP Subscription Billing.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no SAP Subscription Billing. | É exibida a Página inicial. |  |
| 2 | Navegar para modelos de plano de tarifas | Em Determinação de preços, selecione o app Administrar modelos do plano de tarifas. | Os modelos de plano de tarifas disponíveis são exibidos. |  |
| 3 | Criar modelo de plano de tarifas: | Selecione Criar > Sem esquema de determinação de preço e atualize os seguintes dados nas Informações gerais:Descrição: Modelo do plano baseado no assentoCiclo de cálculo da fatura: mensalmente no primeiro dia do mêsMoeda: Valor – USD (para a versão de país US) | A tela Modelo do plano de tarifas é exibida. |  |
| 4 | Atualizar taxas/créditos para elementos de tarifa | Na seção Taxas/Créditos, clique em Taxas / Crédito, clique em Adicionar e escolha Ocasional.Em seguida, atualize os seguintes dados:Elemento de tarifa: R-ONETIMEValor do preço: 100 USDPara Taxas / Crédito, clique em Criar depois em Recorrente e escolha Taxa de determinação de preço de porcentagem.Em seguida, atualize os seguintes dados:Elemento de tarifa: R-SEATSAplicar modificações com próximo ciclo: selecionadoAdiantamento de faturamento: selecionadoDistribuir pro-rata primeiro ciclo: selecionadoPreço por unidade: 10 USDRelação: 100Para Taxas / Crédito, clique em Adicionar, depois em UtilizaçãoDeterminação de preços de bloqueio.Em seguida, atualize os seguintes dados:Elemento de tarifa: R-TRAFFICSubitem da tarifa: atualize Subitem da tarifase a opção Usar subitens da tarifa estiver ativada na etapa [Criar elementos de tarifa](#unique_7) [página ] 5.Nota Subitem da tarifaé um campo obrigatório se a opção Usar subitens da tarifa estiver ativada.Aplicar modificações com próximo ciclo: Não selecionadoQuantidade incluída: Valor – 1Tamanho do bloco: Valor – 1Preço por bloco: Valor - 1 USD (para a versão de país US)Selecione Criar.Em seguida, clique em Publicar. | As taxas/créditos são criados. |  |

#### Criar um produto

Objetivo

Nesta atividade, você cria um produto P-CLOUD_STORAGE em SAP Subscription Billing. O ID do produto em SAP Subscription Billing deve corresponder ao ID do produto relevante no SAP S/4HANA.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no SAP Subscription Billing. | É exibida a Página inicial. |  |
| 2 | Navegar para produtos | Em Dados mestre e configuração, abra o app Administrar produtos. | Os produtos disponíveis são exibidos. |  |
| 3 | Atualizar informações gerais sobre o produto | Clique em Criar e atualize os seguintes dados na área Informações gerais:Nome do produto: Armazenamento na nuvemID do produto: P-CLOUD_STORAGETipo de assinatura: ComercialCriar assinaturas como pendentes: desmarcadoPerfil de assinatura Integração S/4 | As informações gerais foram atualizadas. |  |
| 4 | Atualizar plano de tarifas para produto | Na guia Planos de tarifas, clique em Criar > Sem esquema de cálculoe atualize os seguintes dados:Nota Se você estiver usando produtos que necessitam de um esquema de cálculo, deve selecionar Com esquema de cálculo. Para uma síntese da determinação de preço com e sem esquemas de cálculo, consulte [Determinação de preço](https://help.sap.com/docs/subscription-billing/feature-overview/pricing) na documentação do SAP Subscription Billing.Mercado: Leste dos EUA (para versão de país US)Modelo do plano de tarifas: Modelo do plano baseado no assentoDescrição: Plano de tarifas periódicas (baseado no assento)Ciclo de faturamento: mensalmente no primeiro dia do mêsSelecione Criar. | O plano de tarifas foi atualizado para o produto. |  |
| 5 | Atualizar prazos de assinatura | Em Termos do contrato, atualize os seguintes detalhes:Período validade previsto: por exemplo, 12Prazo mínimo: 12Período de renovação: 12Período de revogação: 14 | Os termos de assinatura são atualizados. |  |
| 6 | Criar produto | Para todo o produto, selecione Criar.Em seguida, clique em Publicar. | O produto P-CLOUD_STORAGE é criado. |  |

#### Criar um produto com esquema de cálculo

Ao passar por um caso de uso de amostra, você pode usar os valores de amostra para criar dados do zero ou pode usar a configuração predefinida fornecida com cada novo locatário. Você deve executar as etapas a seguir em Serviço de cálculo de preço antes de criar um produto com um esquema de determinação de preços.

Você pode encontrar uma descrição detalhada sobre como configurar a determinação de preço com esquemas de cálculo (usando um exemplo) no [Guia de configuração de determinação de preço com esquemas de cálculo](https://help.sap.com/docs/subscription-billing/pricing-configuration/pricing-with-pricing-schemes-configuration-guide).

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

|  |
| --- |
| Nota Se as especificações do elemento de preço para os elementos acima não estiverem atualizadas, você deve atualizá-las no app Administrar especificações de elemento de preço selecionando os elementos individuais Campos substituíveis > Adicionar/Criar > Preço/Desconto > Salvar. |

4. Esquema de determinação de preços

No app Administrar esquemas de determinação de preços, você cria e atualiza esquemas de determinação de preços. Um esquema de determinação de preços é um procedimento que define a utilização e a relação das especificações do elemento de preço para um determinado documento com preço calculável. Ele também determina a sequência de execução dessas especificações para gerar um montante total em um documento precificado.

O esquema de determinação de preços 'Inicial' faz parte do conteúdo predefinido. Assim, você não precisa efetuar configurações adicionais nesta etapa.

5. Criar modelo de plano de tarifas

| Nº da etapa de teste | Nome da etapa de teste | Instruções | Resultados previstos | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no SAP Subscription Billing. | A página Inicial é exibida. |  |
| 2 | Navegue para o app Modelos de plano de tarifas | Vá paraDeterminação de preço > Administrar modelos de plano de tarifas | Os modelos de plano de tarifas são exibidos. |  |
| 3 | Selecione Criar | Clique em Criar > Com esquema de determinação de preços e atualize os seguintes dados em Informações gerais:Descrição: RPT para cálculo de preçoTags: PCS (opcional)Esquema de determinação de preços: InicialCiclo de faturamento: mensalmente no primeiro dia do mêsPerfil de faturamento: Configurações iniciaisMoeda: USD | As informações gerais foram atualizadas. |  |
| 4 | Atualizar Taxas/créditos para elementos de tarifa | Para únicas, selecione Taxas/créditos > Criar > Única e insira Elemento de tarifa = R-ONETIME.Clique em Detalhes de campos editáveis > Criar > Desconto 1 e insira Preço único = selecionar. Selecione Aceitar.Para recorrentes, selecione Taxas/créditos > Criar > Recorrente e insira Elemento de tarifa = R-SEATS.Clique em Detalhes de campos substituíveis > Criar > Desconto 1 e insira Preço recorrente = selecionar. Selecione Aceitar.Para uso, selecione Taxas/créditos > Criar > Determinação de preços de bloqueio de utilização e insira Elemento de tarifa = R-TRAFFICe Subitem da tarifa.Nota Subitem da tarifaé um campo obrigatório se a opção Usar subitens da tarifa estiver ativada na etapa [Criar elementos de tarifa](#unique_7) [página ] 5 .Clique em Detalhes de campos substituíveis > Criar > Desconto 1 e insira Preço baseado util. = selecionar. Selecione Aceitar.Clique em Criar e em Publicar. |  |  |

6. Criar produto

Você cria um produto P-CLOUD_STORAGE_PC no SAP Subscription Billing. O ID do produto em SAP Subscription Billing deve corresponder ao ID do produto relevante no SAP S/4HANA. Você pode usar os seguintes procedimentos:

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no SAP Subscription Billing. | A página Inicial é exibida. |  |
| 2 | Navegue para Produtos | Em Dados mestre e configuração, abra o app Administrar produtos. | Os produtos disponíveis são exibidos. |  |
| 3 | Atualizar informações gerais sobre o produto | Clique em Criar e atualize os seguintes dados na área Informações gerais:Nome do produto: Cálculo de preço de armazenamento em nuvemID do produto: P-CLOUD_STORAGE_PCTipo de assinatura: ComercialCriar assinaturas como pendentes: desmarcado | As informações gerais foram atualizadas. |  |
| 4 | Atualizar plano de tarifas para produto | Na guia Planos de tarifa, selecione Criar – > Com esquema de cálculo, navegue até Criar modelo e atualize os seguintes dados:Mercado: Leste dos EUA (para versão de país US)Modelo do plano de tarifas: RPT para cálculo de preçoDescrição: RPT para cálculo de preçoCiclo de faturamento: mensalmente no primeiro dia do mêsSelecione Criar. | O plano de tarifas foi atualizado para o produto. |  |
| 5 | Atualizar Termos do contrato | Em Parâmetro de assinatura, atualize os seguintes dados na área Termos do contrato:Temp.exec.esperado: por exemplo, 12Período de validade mínimo: 12Período de renovação: 12Período de revogação: 14 | Os termos de assinatura são atualizados. |  |
| 6 | Criar produto | Na visão Produto, clique em Criar.Clique em Publicar. | O produto P-CLOUD_STORAGE_PC é criado. |  |

7. Carregar tabelas de pesquisa para determinação de preços

Para mais informações sobre como carregar tabelas de pesquisa, consulte [Carregar tabelas de pesquisa para determinação de preços](#unique_11) [página ] 12.

#### Carregar tabelas de pesquisa para determinação de preços

Você pode carregar suas tabelas de pesquisa para taxas únicas, recorrentes e baseadas no uso e para desconto, usando o seguinte procedimento. Os dados na tabela resultante são usados para encontrar os preços relevantes durante a determinação de preços como parte do processo de classificação.

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
| 3 | Selecione UsagePrice | Selecione a tabela de pesquisa UsagePrice.Baixe a tabela vazia e armazene-a localmente como um arquivo CSV.Dica Se o formato do arquivo baixado não for separado por colunas, você deve alterar o formato da planilha eletrônica para um formato dos EUA. |  |  |
| 4 | Atualize o arquivo baixado | Insira os seguintes valores e salve o arquivo:productCode: P-CLOUD_STORAGE_PCmarketId: A1rateElement: R-TRAFFICprice: Volumeprice (Price Type): LinearOs seguintes valores específicos estão disponíveis para cada nível para um subelemento de taxa alta:rateSubElement: Altoprice (Range): 500price (Range Unit): EAprice (Value): 30price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAOs seguintes valores específicos estão disponíveis para cada nível:rateSubElement: Altoprice (Range): 1000price (Range Unit): EAprice (Value): 25price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAOs seguintes valores específicos estão disponíveis para cada nível:rateSubElement: Altoprice (Range):price (Range Unit): EAprice (Value): 20price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAOs seguintes valores específicos estão disponíveis para cada nível para um subelemento de taxa baixa:rateSubElement: Baixoprice (Range): 500price (Range Unit): EAprice (Value): 15price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAOs seguintes valores específicos estão disponíveis para cada nível para um subelemento de taxa baixa:rateSubElement: Baixoprice (Range): 1000price (Range Unit): EAprice (Value): 10price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAOs seguintes valores específicos estão disponíveis para cada nível para um subelemento de taxa baixa:rateSubElement: Baixoprice (Range):price (Range Unit): EAprice (Value): 5price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA |  |  |
| 5 | Carregue o arquivo CSV | Escolha a tabela de pesquisa UsagePrice e vá para Importar > Procurar para carregar o arquivo salvo do passo anterior.Nota Existem dois tipos de importações: Selecione Consolidar para manter os dados existentes intactos.Clique em Importar. | A tabela de pesquisa UsagePrice é atualizada. |  |

Tabela 4: Carregar tabela de descontos

| Nº da etapa de teste | Nome da etapa de teste | Instruções | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no SAP Price Calculation | A Página inicial é exibida. |  |
| 2 | Navegar para Modelos de plano de tarifas | Em Gerenciamento de dados mestre, abra o app Administrar dados da tabela de pesquisa. | As tabelas de pesquisa são exibidas. |  |
| 3 | Selecione Discount1 | Selecione a tabela de pesquisa Discount1.Baixe a tabela vazia e armazene-a localmente como um arquivo CSV.Dica Se o formato do arquivo baixado não for separado por colunas, você deve alterar o formato da planilha eletrônica para um formato dos EUA. |  |  |
| 4 | Atualize o arquivo baixado | Insira os seguintes valores e salve o arquivo:marketId: A1discount: Singlediscount (Price Type): Percentagediscount (value): 0,1 |  |  |
| 5 | Carregue o arquivo CSV | Escolha a tabela de pesquisa Discount1 e vá para Importar > Procurar para carregar o arquivo salvo do passo anterior.Nota Existem dois tipos de importações: Selecione Consolidar para manter os dados existentes intactos.Clique em Importar. | A tabela de pesquisa Discount1 é atualizada. |  |

### Enriquecer produtos de assinatura (SAP S/4HANA)

#### Ampliar produtos de faturamento de assinatura do tipo SBPD

Objetivo

Nesta atividade, você amplia o produto de faturamento de assinatura P-CLOUD_STORAGE no SAP S/4HANA. Este produto é criado no Faturamento de assinaturas, replicado para SAP S/4HANA e está disponível após a replicação de produtos ser configurada como parte do item de escopo 57Z. Para mais informações sobre a replicação de produtos, consulte [Configurar pacote de iFlow para replicação de produtos e itens da tarifa](https://help.sap.com/docs/CLOUD_TO_CASH_OD/a78a4be305be4dbc903bd826a1aba456/93e79ab9ec8e4dc49bc1710e396608ed.html).

|  |
| --- |
| Nota Os campos específicos do Brasil precisam de um cálculo de imposto adequado. Para mais informações sobre isto, consulte Dados do mestre de materiais > Definir campos específicos de BR para dados mestre > Criar dados mestre para o Brasil (JD0_BR). |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Selecione o bloco Administrar dados mestre de produto. | É exibido o app Administrar dados mestre do produto. |  |
| 3 | Localizar o produto | Na área de pesquisa na parte superior, insira o Produto: P-CLOUD_ STORAGE e P-CLOUD_ STORAGE_PC.Clique em Ir. | Seu produto é exibido na lista de relatórios. |  |
| 4 | Abrir produto e atualizar cadeias de distribuição: Informações gerais | Selecione o produto a partir da lista de relatórios.Número do produto:P-CLOUD_STORAGEUnidade básica: EATipo de produto:SBPD (produto faturamento de assinatura)Descrição: Armazenamento na nuvemEm seguida, clique em OK.Nota Em Descrição, forneça os detalhes de Idioma e Produto para uma região específica, por exemplo, Idioma: inglês e Produto: Produto de faturamento de assinatura. | O produto deve ser aberto e as informações gerais atualizadas. |  |
| 5 | Atualizar cadeias de distribuição: Informações gerais | Na visão Produto, na área Cadeias de distribuição, selecione Criar e atualize os seguintes dados:Organização de vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Nota A cadeia de distribuição não é necessária para o tipo de produto SBPD caso esteja usando MDI. Elas são necessárias apenas quando você usa o Cloud Integration. |  | Para a versão de país Alemanha, atualize o seguinte valor em vez de 1710:Organização de vendas: 1010 ( Org.vendas nacional DE)As outras entradas são as mesmas para os dois países |
| 6 | Atualizar cadeias de distribuição: Critérios de agrupamento | Navegue para a área Critérios de agrupamento e atualize os seguintes dados:Grupo de categorias de item: SBPD (produto faturamento de assinatura)Grupo de classificações contábeis: X9 (serviço periódico)Classificação fiscal: 1 (imposto total)Em seguida, clique em Aplicar > Criar.Nota O grupo de categorias de item não é necessário para o tipo de produto SBPD caso esteja usando MDI. Isso é necessário apenas quando você usa o Cloud Integration. | Os critérios de agrupamento são atualizados e o produto é salvo. | Para a versão de país Alemanha, atualize o seguinte valor em vez de 1 (Imposto total):Classificação fiscal: 6 (imposto total (serviços))As outras entradas são as mesmas para os dois países. |
| 7 | Atualizar centros | Navegue para Centros > Criar e atualize os seguintes dados:Centro: 1710 (Centro EUA)Clique em Aplicar > Salvar. | Os dados do centro são atualizados. |  |

#### Ampliar produtos de faturamento de assinatura do tipo SBRE

Objetivo

Nesta atividade, você amplia os seguintes produtos de assinatura no SAP S/4HANA que correspondem a elementos de tarifa no SAP Subscription Billing: Os produtos são criados no SAP Subscription Billing e replicados no SAP S/4HANA. Os elementos da tarifa estarão disponíveis assim que a replicação de produtos for configurada como mencionado no guia de configuração do item de escopo 57Z ou consulte [Replicação de produto e elemento de tarifa](https://help.sap.com/docs/CLOUD_TO_CASH_OD/a78a4be305be4dbc903bd826a1aba456/9dbec8b5ce1841a6a39f0af5571ed63b.html?version=latest).

|  |
| --- |
| Nota Os campos específicos do Brasil precisam de um cálculo de imposto adequado. Para mais informações sobre isto, consulte Dados do mestre de materiais > Definir campos específicos de BR para dados mestre > Verificar Criar dados mestre para o Brasil (JD0_BR). |

| ID do produto | Tipo de produto | Descrição |
| --- | --- | --- |
| R-ONETIME | SBRE | Taxa de ativação única |
| R-SEATS | SBRE | Taxa mensal baseada no assento |
| R-TRAFFIC | SBRE | Taxa de utilização baseada no tráfego |

Procedimento

Produto: R-ONETIME

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Selecione o bloco Administrar dados mestre de produto. | É exibido o app Administrar dados mestre do produto. |  |
| 3 | Procurar produto | Na área de pesquisa na parte superior, insira o Produto: R-ONETIME.Clique em Ir. | Seu produto é exibido na lista de relatórios. |  |
| 4 | Abrir produto e atualizar cadeias de distribuição: Informações gerais | Na visão Produto, na área Cadeias de distribuição, selecione Criar e atualize os seguintes dados:Organização de vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Nota Em Descrição, forneça os detalhes de Idioma e Produto para uma região específica, por exemplo, Idioma: inglês e Produto: Produto de faturamento de assinatura. | O produto deve ser aberto e as informações gerais atualizadas. | Para a versão de país Alemanha, atualize o seguinte valor em vez de 1710:Organização de vendas: 1010 ( Org.vendas nacional DE)As outras entradas são as mesmas para os dois países. |
| 5 | Atualizar cadeias de distribuição: Critérios de agrupamento | Navegue para a área Critérios de agrupamento e atualize os seguintes dados:Grupo de classificações contábeis: X9 (serviço periódico)Classificação fiscal: 1 (imposto total)Em seguida, clique em Aplicar e depois Criar.Nota O grupo de categorias de item não é necessário para o tipo de produto SBRE caso esteja usando MDI. | Os critérios de agrupamento são atualizados e o produto é salvo. | Para a versão de país Alemanha, atualize o seguinte valor em vez de 1 (Imposto total):Classificação fiscal: 6 (imposto total (serviços))As outras entradas são iguais para as duas versões. |
| 6 | Atualizar centros | Navegue para a área Centros, selecione Criar e atualize os seguintes dados:Centro: 1710 (centro EUA)Clique em Aplicar e em Salvar. | Os dados do centro são atualizados. | Para a versão de país Alemanha, atualize o seguinte valor:Centro: Centro 10101 (Centro ALE) |

Produto: R-SEATS

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Selecione o bloco Administrar dados mestre de produto. | É exibido o app Administrar dados mestre do produto. |  |
| 3 | Procurar produto | Na área de pesquisa na parte superior,insira o Produto: R-SEATSPressione o botão Ir. | Seu produto é exibido na lista de relatórios. |  |
| 4 | Abrir produto e atualizar cadeias de distribuição: Informações gerais | Na visão Produto, na área Cadeias de distribuição, selecione Criar e atualize os seguintes dados:Organização de vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Nota Em Descrição, forneça os detalhes de Idioma e Produto para uma região específica, por exemplo, Idioma: inglês e Produto: Produto de faturamento de assinatura. | O produto deve ser aberto e as informações gerais atualizadas. | Para a versão de país Alemanha, atualize o seguinte valor em vez de 1710:Organização de vendas: 1010 ( Org.vendas nacional DE)As outras entradas são as mesmas para os dois países |
| 5 | Atualizar cadeias de distribuição: Critérios de agrupamento | Navegue para a área Critérios de agrupamento e atualize os seguintes dados:Grupo de classificações contábeis: X9 (serviço periódico)Classificação fiscal: 1 (imposto total)Em seguida, selecione Aplicar. | Os critérios de agrupamento são atualizados e o produto é salvo. | Para a versão de país Alemanha, atualize o seguinte valor em vez de 1 (Imposto total):Classificação fiscal: 6 (imposto total (serviços))As outras entradas são iguais para as duas versões. |
| 6 | Atualizar centros | Navegue para a área Centros, selecione Criar e atualize os seguintes dados:Centro: 1710 (centro EUA)Clique em Aplicar e em Salvar. | Os dados do centro são atualizados. | Para a versão de país Alemanha, atualize o seguinte valor:Centro: Centro 1010 (Centro ALE) |

Produto: R-TRAFFIC

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Selecione o bloco Administrar dados mestre de produto. | É exibido o app Administrar dados mestre do produto. |  |
| 3 | Procurar produto | Na área de pesquisa na parte superior,insira o Produto: R-TrafficPressione o botão Ir. | Seu produto é exibido na lista de relatórios. |  |
| 4 | Abrir produto e atualizar cadeias de distribuição: Informações gerais | Na visão Produto, na área Cadeias de distribuição, selecione Criar e atualize os seguintes dados:Organização de vendas: 1710 ( Org.vendas nac.EUA)Canal de distribuição: 10 (vendas diretas)Nota Em Descrição, forneça os detalhes de Idioma e Produto para uma região específica, por exemplo, Idioma: inglês e Produto: Produto de faturamento de assinatura. | O produto deve ser aberto e as informações gerais atualizadas. | Para a versão de país Alemanha, atualize o seguinte valor em vez de 1710:Organização de vendas: 1010 ( Org.vendas nacional DE)As outras entradas são as mesmas para os dois países |
| 5 | Atualizar cadeias de distribuição: Critérios de agrupamento | Navegue para a área Critérios de agrupamento e atualize os seguintes dados:Grupo de categorias de item: SBRE (elemento de taxa de faturamento de assinatura)Grupo de classificações contábeis: X9 (serviço periódico)Classificação fiscal: 1 (imposto total)Clique em Aplicar e, em seguida, Salvar.Nota O grupo de categorias de item não é necessário para o produto SBRE caso esteja usando MDI. | O produto é salvo. | Para a versão local Alemanha, atualize o seguinte valor em vez de 1 (imposto total):Classificação fiscal: 6 (imposto total (serviços))As outras entradas são iguais para as duas versões. |
| 6 | Atualizar centros | Navegue para a área Centros, selecione Criar e atualize os seguintes dados:Centro: 1710 (centro EUA)Clique em Aplicar e, em seguida, Salvar. | Os dados do centro são atualizados. | Para a versão de país Alemanha, atualize o seguinte valor: Centro: Centro 10101 (Centro DE) |

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
> Flagged while digesting this document, not verified: German plant for SBRE products is inconsistent inside the document: 10101 for R-ONETIME and R-TRAFFIC versus 1010 for R-SEATS.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-sales-billing-mds-5bd-4]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-5bd-429]]
- related-to :: [[09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-mds-5bd-427]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-crear-facturacion-de-ventas-de-productos-de-s]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 39,411 chars in the whole document
