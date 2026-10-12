---
id: 14-maintenance-service-and-projects/script-de-dados-mestre-criar-lista-tecnica-de-material-e-equipamento-p
title: "Script de dados mestre: Criar lista técnica de material e equipamento para serviço - MDS (63J) (63J_S4CLD2608_Master_Data_PT_XX)"
description: "Portuguese master data script (63J) for SAP S/4HANA Cloud Public Edition 2608: create service products, material BOM, equipment and equipment BOM."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-technical-objects-and-boms]
aliases: [63J_S4CLD2608_Master_Data_PT_XX]
keywords: [Technical Objects and BOMs for Service, material bom, service products, equipment master data, equipment bom, master data scripts, business roles, organizational units, profit center, service contracts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/63J_S4CLD2608_Master_Data_PT_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-494
topic: 14-maintenance-service-and-projects/service-technical-objects-and-boms
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre: Criar lista técnica de material e equipamento para serviço - MDS (63J) (63J_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/63J_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Technical Objects and BOMs for Service** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar lista técnica de material e equipamento para serviço – MDS (63J) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893903)

[2 Pré-requisitos 3](#_Toc233893904)

[2.1 Acesso ao sistema 3](#_Toc233893905)

[2.2 Funções 3](#_Toc233893906)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893907)

[2.4 Dados mestre obrigatórios e operacionais 4](#_Toc233893908)

[3 Tabela de síntese 5](#_Toc233893909)

[4 Procedimentos 6](#_Toc233893910)

[4.1 Criar lista técnica de material 6](#_Toc233893911)

[4.1.1 Criar produtos dos serviços 6](#_Toc233893912)

[4.1.1.1 Criar produto de serviços - SRV_BOM_01_01 6](#_Toc233893913)

[4.1.1.2 Criar produto de serviços - SRV_BOM_02_01 7](#_Toc233893914)

[4.1.1.3 Criar produto de serviços - SRV_BOM_02_02 9](#_Toc233893915)

[4.1.2 Criar nova lista técnica 10](#_Toc233893916)

[4.2 Criar lista técnica de equipamento 12](#_Toc233893917)

[4.2.1 Criar equipamento 12](#_Toc233893918)

[4.2.2 Criar lista técnica de equipamento 14](#_Toc233893919)

## Objetivo

Neste documento, você encontra uma descrição sobre como criar registros de dados mestre de produto de serviço e gerar a lista técnica com os produtos de serviços criados. A descrição inclui os segmentos de dados relevantes para os dados mestre para trabalhar em um ambiente de sistema "normal". O leitor aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo não são descritos neste documento, embora eles possam aparecer na interface do usuário.

Um registro mestre do produto de serviço criado como descrito aqui pode ser usado para os contratos de serviço.

| Tipo de produto | ID do produto de serviços | Descrição |
| --- | --- | --- |
| Mestre de materiais | SRV_BOM_01_01 | Produto do serviço com lista técnica 01_01 |
|  | SRV_BOM_02_01 | Produto do serviço com lista técnica 02_01 |
|  | SRV_BOM_02_02 | Produto do serviço com lista técnica 02_02 |
| LT do material | SRV_BOM_01_01 | Produto do serviço com lista técnica 01_01 |
| Equipamento | <ID do equipamento> | Criar equipamento |
| Lista de peças para equipamento | <Lista de peças para equipamento> | Lista de peças para equipamento |

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
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Dados mestre - Produto | SAP_CMD_SP_PR_MAINT |
| Responsável pela lista técnica | SAP_BR_BOM_ENGINEER | Listas técnicas | SAP_BR_BOM_ENGINEER |
| Planejador de manutenção | SAP_BR_MAINTENANCE_PLANNER | Planejamento de manutenção | SAP_BR_MAINTENANCE_PLANNER |

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre são dependentes das unidades organizacionais da empresa. Os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Unidade organizacional a ser utilizada para os EUA | Unidade organizacional a ser utilizada para DE |
| --- | --- | --- | --- |
| Criar material | Organização de vendas | 1710 ( Org.vendas nac.EUA) | 1010 ( Org.vendas nacional DE) |
| Criar material | Canal de distribuição | 10 (vendas diretas) | 10 (vendas diretas) |

### Dados mestre obrigatórios e operacionais

Os registros de dados mestre de materiais podem fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre de materiais.

|  |
| --- |
| Nota Os campos específicos do Brasil são necessários para obter um cálculo de imposto adequado.Verifique Nota Fiscal Brasil - JD0 no capítulo Definir campos específicos do BR para dados mestre para dados mestre de materiais. |

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Centro de lucro |  | Obrigatório | A atribuição de um centro de lucro a um mestre de materiais (produtos) é necessária para os processos de avaliação corretos. |

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

Se seu administrador do sistema tiver ativado espaços e páginas no launchpad do SAP Fiori, a página inicial só irá conter os apps essenciais para executar as tarefas típicas de uma função empresarial.

Você pode encontrar todos os outros apps não incluídos na página inicial usando a barra de pesquisa.

Para personalizar a página inicial e incluir os apps ocultos, navegue até seu perfil do usuário e clique em Configurações > App Finder.

| ID (modelo de função) | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| Criar lista técnica de material | SAP_BR_PRODMASTER_SPECIALIST | Criar material(MM01) | Os produtos dos serviços são criados. |
| SAP_BR_BOM_ENGINEER | Atualizar lista técnica - Criar, modificar e exibir LTs | A lista técnica do material é criada |  |
| Criar lista técnica de equipamento | SAP_BR_MAINTENANCE_PLANNER | Criar objeto técnico | O equipamento é criado |
| Criar lista técnica de equipamento | A lista técnica de produção é criada |  |  |

## Procedimentos

Esta seção descreve procedimentos para cada segmento ou etapa do processo que faz parte deste registro mestre.

### Criar lista técnica de material

#### Criar produtos dos serviços

##### Criar produto de serviços - SRV_BOM_01_01

Objetivo

Este material só é relevante para edição na nuvem.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como especialista em dados mestre – dados do produto (MDG). | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Selecione o bloco Criar material. | É exibido Criar material (1ª tela). |  |
| 3 | Atualizar dados básicos de material (para produto de serviços) | Em Criar material (primeira tela), efetue as seguintes entradas: caixa de diálogo, selecione oMaterial:SRV_BOM_01_01Tipo de material:produto de serviçosEm seguida, clique em Continuar (Enter). | Você atualizou as informações básicas para o novo produto dos serviços.É exibida a caixa de diálogo Selecionar visão(ões). |  |
| 4 | Clicar em visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Dados básicos 1Vendas: Dados da organização de vendas 1Vendas: Dados da organização de vendas 2Em seguida, clique em Continuar (Enter). | A caixa de diálogo Níveis organizacionais é exibida. |  |
| 5 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:Org.vendas:1710 ( Org.vendas nac.EUA)Canal de distribuição:10 (vendas diretas)Em seguida, clique em Continuar (Enter). | Os dados organizacionais foram selecionados.A visão Criar Material SRV_BOM_01_01 é exibida. |  |
| 6 | Atualizar dados básicos | Na visão Dados básicos 1, atualize os seguintes valores:Descr.:produto de serviços com lista técnica 01_01Unidade de medida básica:h (horas)Grupo de materiais:P001 (serviços)GrpCategItemGer:SRVP (produto de serviços)Em seguida, clique em Salvar. | Os dados básicos são atualizados e o produto dos serviços é salvo.Após a gravação, a visão Criar material (primeira tela) é exibida.Para cada idioma diferente utilizado na sua empresa, a descrição correspondente para o produto deve ser atualizada por código de idioma. |  |
| 7 | Atualizar dados da organização de vendas (1) | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados geraisDesconto:X <selecionado>Dados do impostoClassificação fiscal:1 (imposto total)Em seguida, pressione Enter. | Os dados organizacionais de vendas são atualizados. A guia Vendas: organização de vendas 2 é exibida. |  |
| 8 | Atualizar dados da organização de vendas (2) | Na guia Vendas: organização de vendas 2, atualize a seguinte entrada:Grupo de categorias de item:SRVP (produto de serviços)Em seguida, clique em Salvar. | Os dados organizacionais de vendas são atualizados. A guia Vendas: Geral/centro é exibida. |  |

##### Criar produto de serviços - SRV_BOM_02_01

Objetivo

Este material só é relevante para edição na nuvem.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como especialista em dados mestre – dados do produto (MDG). | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Selecione o bloco Criar material. | É exibido Criar material (1ª tela). |  |
| 3 | Atualizar dados básicos de material (para produto de serviços) | Em Criar material (primeira tela), efetue as seguintes entradas: caixa de diálogo, selecione oMaterial:SRV_BOM_02_01Tipo de material:produto de serviçosEm seguida, clique em Continuar (Enter). | Você atualizou as informações básicas para o novo produto dos serviços.É exibida a caixa de diálogo Selecionar visão(ões). |  |
| 4 | Clicar em visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Dados básicos 1Vendas: Dados da organização de vendas 1Vendas: Dados da organização de vendas 2Em seguida, clique em Continuar (Enter). | A caixa de diálogo Níveis organizacionais é exibida. |  |
| 5 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:Org.vendas:1710 ( Org.vendas nac.EUA)Canal de distribuição:10 (vendas diretas)Em seguida, clique em Continuar (Enter). | Os dados organizacionais foram selecionados.A visão Criar material SRV_BOM_ 02_01 é exibida. |  |
| 6 | Atualizar dados básicos | Na visão Dados básicos 1, atualize os seguintes valores:Descr.:produto de serviços com lista técnica 02_01Unidade de medida básica:h (horas)Grupo de materiais:P001 (serviços)GrpCategItemGer:SRVP (produto de serviços)Em seguida, pressione Enter. | Os dados básicos são atualizados e o produto dos serviços é salvo.Após a gravação, a visão Criar material (primeira tela) é exibida.Para cada idioma diferente utilizado na sua empresa, a descrição correspondente para o produto deve ser atualizada por código de idioma. |  |
| 7 | Atualizar dados da organização de vendas (1) | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados geraisDesconto:X <selecionado>Dados do impostoClassificação fiscal:1 (imposto total)Em seguida, pressione Enter. | Os dados organizacionais de vendas são atualizados. A guia Vendas: organização de vendas 2 é exibida. |  |
| 8 | Atualizar dados da organização de vendas (2) | Na guia Vendas: organização de vendas 2, atualize a seguinte entrada:Grupo de categorias de item:SRVP (produto de serviços)Em seguida, clique em Salvar. | Os dados organizacionais de vendas são atualizados. A guia Vendas: Geral/centro é exibida. |  |

##### Criar produto de serviços - SRV_BOM_02_02

Objetivo

Este material só é relevante para edição na nuvem.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como especialista em dados mestre – dados do produto (MDG). | A página inicial é exibida. |  |
| 2 | Acessar o app SAP Fiori | Selecione o bloco Criar material. | É exibido Criar material (1ª tela). |  |
| 3 | Atualizar dados básicos de material (para produto de serviços) | Em Criar material (primeira tela), efetue as seguintes entradas: caixa de diálogo, selecione oMaterial:SRV_BOM_02_02Tipo de material:produto de serviçosEm seguida, clique em Continuar (Enter). | Você atualizou as informações básicas para o novo produto dos serviços.É exibida a caixa de diálogo Selecionar visão(ões). |  |
| 4 | Clicar em visões | Na caixa de diálogo Selecionar visões, selecione as seguintes visões:Dados básicos 1Vendas: Dados da organização de vendas 1Vendas: Dados da organização de vendas 2Em seguida, clique em Continuar (Enter). | A caixa de diálogo Níveis organizacionais é exibida. |  |
| 5 | Selecionar níveis organizacionais | Na janela Níveis organizacionais, atualize os seguintes valores:Org.vendas:1710 ( Org.vendas nac.EUA)Canal de distribuição:10 (vendas diretas)Em seguida, clique em Continuar (Enter). | Os dados organizacionais foram selecionados.É exibida a visão Criar Material SRV_BOM_02_02 . |  |
| 6 | Atualizar dados básicos | Na visão Dados básicos 1, atualize os seguintes valores:Descr.:produto dos serviços com lista técnica 02_02Unidade de medida básica:h(horas)Grupo de materiais:P001 (serviços)GrpCategItemGer:SRVP (produto de serviços)Em seguida, pressione Enter. | Os dados básicos são atualizados e o produto dos serviços é salvo.Após a gravação, a visão Criar material (primeira tela) é exibida.Para cada idioma diferente utilizado na sua empresa, a descrição correspondente para o produto deve ser atualizada por código de idioma. |  |
| 7 | Atualizar dados da organização de vendas (1) | Na guia Vendas: organização de vendas 1, atualize os seguintes valores:Dados geraisDesconto:X <selecionado>Dados do impostoClassificação fiscal:1 (imposto total)Em seguida, pressione Enter. | Os dados organizacionais de vendas são atualizados. A guia Vendas: organização de vendas 2 é exibida. |  |
| 8 | Atualizar dados da organização de vendas (2) | Na guia Vendas: organização de vendas 2, atualize a seguinte entrada:Grupo de categorias de itens:SRVP (projeto)Em seguida, clique em Salvar. | Os dados organizacionais de vendas são atualizados. A guia Vendas: Geral/centro é exibida. |  |

#### Criar nova lista técnica

Objetivo

Este material só é relevante para edição na nuvem. Nesta etapa, você pode criar uma nova lista técnica.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como engenheiro de lista técnica. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra o app Atualizar lista técnica (versão 2) - Criar, modificar e exibir LTs(F1813A). |  |  |
| 3 | Selecionar Criar LT | Na tela Atualizar lista técnica, selecione Criar LT. | A caixa de diálogo Criar LT é exibida. |  |
| 4 | Atualizar dados de cabeçalho da LT | Na janela Criar LT, insira os dados de acordo com o seguinte exemplo e clique em OK:ExemploMaterial: SRV_BOM_01_01Utilização da lista técnica: S (administração de serviços)Válido desde: hoje | A tela Atualizar lista técnica é exibida e, por padrão, a guia Componentes será aberta. |  |
| 5 | Atualizar dados de componentes de LT | Na linha Nº do item de LT 0010, efetue as entradas semelhantes ao seguinte exemplo:ExemploComponente: SRV_BOM_02_01Quantidade do componente:10 h(Pressione Enter para ativar os campos Componente e Quantidade do componente)Nota O valor da categoria do item é N (item não estocado) | Nº do item de LT 0010, Componente, Descrição do componente e Quantidade do componente é exibido na primeira linha da tabela. |  |
| 6 | Atualizar dados de componentes LT adicionais | Repetir a etapa acima para o nº do item de LT 0020 com as seguintes entradas:Componente: SRV_BOM_02_02Quantidade do componente: 20 h(Pressione Enter para ativar os campos Componente e Quantidade do componente)Nota O valor da categoria do item é N (item não estocado) | Nº do item de LT 0020, Componente, Descrição do componente e Quantidade do componente é exibido nas linhas da tabela. |  |
| 8 | Navegar para detalhe do item | Na linha Nº de item LT 0010, clique na seta de detalhes no lado direito extremo da tabela.Na tela Atualizar lista técnica, efetue entradas semelhantes aos exemplos a seguir na guia Detalhes básicos:ExemploQuantidade do componente: 10UM do componente: h | A tela Atualizar lista técnica com a seção de detalhes do material inserido é exibida. |  |
| 9 | Navegar para detalhe do item | Na linha Nº de item LT 0020, clique na seta de detalhes no lado direito extremo da tabela.Na tela Atualizar lista técnica, efetue entradas semelhantes aos exemplos a seguir na guia Detalhes básicos:ExemploQuantidade do componente: 20UM do componente: h | A tela Atualizar lista técnica com a seção de detalhes do material inserido é exibida. |  |
| 10 | Clicar em Salvar | Na tela Atualizar lista técnica, clique em Criar. | A lista técnica está salva.Nota Após salvar, o status da LT será definido automaticamente como 1 (Ativo).Se o status da LT2 (inativo) for necessário para a LT, na tela Atualizar lista técnica, selecione Exibir detalhes de cabeçalho, escolha Dados administrativos e defina o status da LT de forma apropriada antes de salvar novamente.O número da modificação é inserido sob a guia Linha do tempo. |  |

### Criar lista técnica de equipamento

#### Criar equipamento

Objetivo

Nesta etapa de teste, você atualiza um registro para um equipamento que está montado em um local de instalação.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no Launchpad do SAP Fiori como um planejador de manutenção. | O launchpad do SAP Fiori é exibido. |  |
| 3 | Acessar o app SAP Fiori | Abra Criar objeto técnico | É aberta uma janela exibindo Criar objeto técnico: 1ª tela. |  |
| 4 | Criar equipamento | Na tela Criar objeto técnico, selecione o Tipo de objeto técnico: Equipamento.Na tela seguinte, insira o seguinte:Tipo de objeto técnico: EquipamentoObjeto técnico: deixar em brancoVálido desde: data de hojeCategoria de objeto técnico: M (Máquinas)Clique em Continuar (Enter). |  |  |
| 5 | Atualizar dados gerais | Na tela Criar objeto técnico: <ID do equipamento>, na seção Dados gerais, insira o seguinte:Descrição: Por exemplo, equipamento do cabeçalho da lista técnica para serviçoTipo de objeto: Por exemplo, 9400Data de início das atividades: Por exemplo, a data de hojePaís/região de produção: por exemplo, EUAMês/ano de construção: por exemplo, 04/2011Número da peça do fabricante: por exemplo, HZZ-TD B4>Nº de série do fabricante: por exemplo, HZZ-TD B4/66>Valor de aquisição/moeda: por exemplo, 10.000,00/ USD >Data de aquisição: por exemplo, 10/04/2011Nota Alternativamente, atualize outros dados gerais e, em seguida, navegue até a seção de dados do local. | A tela Criar objeto técnico: dados gerais é exibida. |  |
| 6 | Atualizar dados da unidade gerencial | Na seção Dados do local, insira o seguinte:Centro de manutenção: por exemplo, 1710 para os EUA>Local: por exemplo, YB_1701 para os EUAÁrea operacional: por exemplo, YOH para os EUA>Nota os objetos técnicos que pertencem à mesma estrutura devem ter o mesmo centro atribuído. Como alternativa, você pode deixar a informação sobre o centro em branco para todos os objetos técnicos.Opcionalmente, atualize outros detalhes, tais como informações de endereço. | A tela Criar objeto técnico: dados do local é exibida. |  |
| 8 | Atualizar dados organizacionais | Na seção Dados organizacionais, insira o seguinte:Grupo de planejamento: por exemplo, 920 para os EUA>Centro de planejamento: por exemplo, 1710 para os EUA>Centro de trabalho de manutenção: por exemplo, RES-0100 para os EUA>Centro de trabalho: por exemplo, 1710 para os EUA>Centro de custo: por exemplo, 17101701 para os EUA>Opcionalmente, você pode atualizar informações adicionais, por exemplo, informações do parceiro e outras, na seção Dados organizacionais. | A tela Criar objeto técnico: dados organizacionais é exibida. |  |
| 9 | Salvar equipamento | Opcionalmente, você pode atualizar informações adicionais para outras seções.Clique no botão Verificar entradas.Clique em Salvar. | O equipamento é criado.Anote o ID do equipamento criado. |  |

#### Criar lista técnica de equipamento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no Launchpad do SAP Fiori como um planejador de manutenção. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar ListTéc equipamento | É aberta uma nova janela, exibindo Criar ListTéc equipamento: 1ª tela. |  |
| 3 | Criar equipamento | Na tela Criar ListTéc equipamento: 1ª tela, insira os seguintes dados:Equipamento: ID de equipamento gerado no capítulo anteriorUtilização da LT: SClique em Continuar. |  |  |
| 4 | Atualizar dados de material | Na tela Criar ListTéc equipamento: síntese de itens gerais , na seção Material , insira o seguinte:Componente: ID do material, por exemplo, SRV_BOM_02_02Categoria do item: N (item não estocado)Quantidade: Por exemplo, 10Unidade de medida: por exemplo, HRPressione Enter | É exibida a tela Criar ListTéc equipamento: síntese de itens gerais. |  |
| 5 | Salvar equipamento | Clique em Salvar | A lista técnica de equipamento é criada. |  |

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
> Flagged while digesting this document, not verified: SRV_BOM_02_02 step 8 lists item category group SRVP as '(projeto)' whereas the other products label SRVP as 'produto de serviços'

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/bom-mds-63j-493]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-material-and-equipment-bom-for-service-mds-6]]
- related-to :: [[14-maintenance-service-and-projects/material-und-equipmentstuckliste-fur-service-anlegen-sds-63j-490]]
- related-to :: [[14-maintenance-service-and-projects/mds-63j-495]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/63J_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 24,644 chars in the whole document
