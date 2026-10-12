---
id: 08-sales-order-management/script-de-dados-mestre-criar-script-de-dados-mestre-de-hierarquia-de-c
title: Script de dados mestre - Criar script de dados mestre de hierarquia de clientes (6N3) (6N3_S4CLD2608_Master_Data_PT_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 test script (PT) for creating customer master data (general, company, sales area) and customer hierarchies via Fiori apps."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-hierarchies]
aliases: [6N3_S4CLD2608_Master_Data_PT_XX]
keywords: [Customer Hierarchies, customer master data, company code data, sales area data, business partner roles, business roles, organizational units, partner functions, tax identification numbers, country-specific requirements]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/6N3_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-518
topic: 08-sales-order-management/customer-hierarchies
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar script de dados mestre de hierarquia de clientes (6N3) (6N3_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/6N3_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Customer Hierarchies** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar script de dados mestre de hierarquia de clientes (6N3) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893901)

[2 Pré-requisitos 3](#_Toc233893902)

[2.1 Acesso ao sistema 3](#_Toc233893903)

[2.2 Funções 3](#_Toc233893904)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893905)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893906)

[3 Tabela de síntese 5](#_Toc233893907)

[4 Procedimentos de teste 6](#_Toc233893908)

[4.1 Criar dados mestre do cliente – Dados gerais 6](#_Toc233893909)

[4.2 Criar dados mestre do cliente – Dados da empresa 13](#_Toc233893910)

[4.3 Criar dados mestre do cliente – Dados da área de vendas 18](#_Toc233893911)

[4.4 Criar hierarquias de clientes 23](#_Toc233893912)

## Objetivo

O app Administrar hierarquias de clientes ajuda você a criar, copiar, editar e excluir hierarquias de clientes e atribuir vários níveis de nós de hierarquia. Você também pode administrar os períodos de validade das hierarquias e uma hierarquia será considerada somente para processos durante este período indicado.

Hierarquia de clientes – Análise: Você usa este tipo de hierarquia na análise de vendas para projetar dados transacionais e obter informações esclarecedoras.

Hierarquia de clientes – Vendas: Você usa este tipo de hierarquia para a determinação de preços em documentos de vendas e documentos de faturamento. Esta hierarquia contém informações do cliente relacionadas à mesma área de vendas. O sistema permite que você adicione nós de texto que podem indicar qualquer tipo de informação, como estado, distrito, etc. e que ajudam você a organizar melhor a hierarquia. Além disso, esses nós de texto podem ser atualizados como relevantes para a determinação de preços. A hierarquia também contém nós de parceiro de negócios que devem ter uma área de vendas do cliente associada.

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
| Especialista em dados mestre - dados do parceiro de negócios | SAP_BR_BUPA_MASTER_SPECIALIST | Dados mestre - Parceiros de negócios / Governança do parceiro de negócios / Governança do parceiro de negócios / Governança do parceiro de negócios | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Unidades organizacionais necessárias

As unidades organizacionais necessárias estão listadas abaixo:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Dados básicos | Independente de unidades organizacionais | Descrição do parceiro de negócios, Número do cliente, Relevante para determinação de preços, etc. | Dados básicos só existem uma vez para um registro de dados mestre de parceiro de negócios. | N/A |
| Dados de vendas | Organização de vendas, canal de distribuição e setor de atividade | Dados do imposto, relevante para determinação de preços, etc. | Dados de venda podem existir para todas as organizações de vendas de sua estrutura empresarial para a qual o registro de dados mestre do parceiro de negócios é usado. | Organização de vendasCanal de distribuiçãoSetor de atividade |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre do parceiro de negócios podem fazer referência a outros dados mestre. A tabela a seguir oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem usados em um registro de dados mestre do parceiro de negócios.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Áreas de vendas |  | Obrigatório | A atribuição de uma área de vendas aos dados mestre do parceiro de negócios é obrigatória para hierarquia de clientes. |

## Tabela de síntese

Este item de escopo consiste de várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar dados mestre do cliente – Dados gerais](#unique_8) [página ] 6 | Especialista em dados mestre - dados do parceiro de negócios | Atualizar parceiro de negócios(BP) ou Administrar dados mestre do cliente(F0850A) | Mestre de clientes – Dados gerais é criado. |
| [Criar dados mestre do cliente – Dados da empresa](#unique_9) [página ] 13 | Especialista em dados mestre - dados do parceiro de negócios | Atualizar parceiro de negócios(BP) ou Administrar dados mestre do cliente(F0850A) | Mestre de clientes – Dados da empresa é criado. |
| [Criar dados mestre do cliente – Dados da área de vendas](#unique_10) [página ] 18 | Especialista em dados mestre - dados do parceiro de negócios | Atualizar parceiro de negócios(BP) ou Administrar dados mestre do cliente(F0850A) | Mestre de clientes – Dados da área de vendas é criado. |
| [Criar hierarquias de clientes](#unique_11) [página ] 23 | Especialista em dados mestre - dados do parceiro de negócios | Administrar hierarquias de clientes(F5794) | As hierarquias de clientes são criadas. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar dados mestre do cliente – Dados gerais

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do cliente. Os apps disponíveis dependem de sua função atribuída. Por isso, são fornecidas duas opções.

A nota a seguir é somente para a Arábia Saudita.

|  |
| --- |
| Nota Para cumprir as regulamentações de fatura eletrônica da ZATCA, certifique-se de que todos os campos obrigatórios, como Rua 2, Rua 3, Distrito, etc., sejam inseridos corretamente nos formulários do parceiro de negócios antes de gerar documentos eletrônicos. Isso é necessário para a validação bem-sucedida de faturas eletrônicas antes de enviá-las ao portal da autoridade fiscal.Estas informações são usadas para preencher as tags XML adequadas, conforme exigido pela ZATCA, dependendo do tipo de documento eletrônico. Para obter mais informações sobre as diretrizes da ZATCA, consulte as Diretrizes Padrão de Implementação XML de Fatura Eletrônica. |

Procedimento: opção 1 - Atualizar parceiro de negócios

Siga este procedimento quando seu acesso de usuário oferece a você o app Atualizar parceiro de negócios(BP).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar parceiro de negócios(BP). | O app é aberto. |  |
| 3 | Criar uma organização do parceiro de negócios | Clique em Organização. | A tela Criar organização é exibida. |  |
| 4 | Inserir dados gerais | Efetue as seguintes entradas:Parceiro de negócios: <insira um ID do parceiro de negócios que comece com uma letra>Agrupamento: Selecione, por exemplo, Numeração alfanumérica externa.O campo Criar em função de PN é preenchido pelo sistema com a função Parceiro de negócios (geral). Mantenha esta configuração.Pressione Enter.Nota Para obter mais informações sobre os detalhes de dados gerais, consulte a seção [Pré-requisitos](#unique_2) [página ] 3. |  |  |
| 5 | Inserir dados de endereço | Na guia Endereço, na seção Nome, insira os seguintes dados:Título: <selecione um título>Nome: <nome> |  |  |
| 6 | Inserir dados de endereço | Na seção Endereço padrão, insira o endereço. |  |  |
| 7 | Inserir fuso horário e zona de transporte | Na seção Endereço, escolha Mais campos. Insira os seguintes dados:Fuso horário: <fuso horário>Zona de transporte: <zona de transporte> |  |  |
| Somente para a Tailândia | Inserir dados de endereço adicionais (só para a Tailândia) | Na seção Endereço, selecione Mais e insira os seguintes dados:Código do edifício: <edifício>Sala: <nº da sala>Andar: <nº do andar>Rua 2: <Moo>Rua 3: <Soi/Travessa>Rua: <estrada>Número: <não>Cidade diferente: <subdistrito>Bairro: <bairro/zona>Cidade: <província>Código postal: <Código postal>Telefone: <Número de telefone> |  |  |
| 8 | Inserir critérios de pesquisa | Na guia Endereço, na seção Critério de pesquisa, insira um ou dois critérios de pesquisa para o parceiro de negócios. |  |  |
| 9 | Inserir dados de comunicação | Na seção Comunicação, no campo Idioma, insira o idioma preferido do parceiro de negócios. |  |  |
| Só para o Japão | Inserir os dados do setor (somente Japão) | Na guia Identificação da seção Setores industriais, clique no botão Todos os sistemas setoriais. Insira os seguintes dados:Sistema de setor industrial: Selecione Banco do Japão.Setor industrial: <selecione um número de setor>Setor industr.padrão: <não selecionado> |  |  |
| 10 | Inserir números de identificação fiscal | Na guia Identificação, na seção Números de identificação fiscal, insira os seguintes dados:Categoria: <Category>Número de identificação fiscal: <número de identificação fiscal>Nota Selecione a categoria correta aplicável ao país/região do parceiro de negócios. Por exemplo, para um parceiro de negócios alemão, você atualiza um valor para a categoria DE1, que representa o número de identificação fiscal de IVA usado habitualmente. |  |  |
| 11 | Inserir contas bancárias | Na guia Transações de pagamento, na seção Dados bancários, insira os seguintes dados:Chave do banco: <chave do banco>Conta bancária: <conta bancária>Atenção As chaves do banco devem ser definidas previamente. Use as entradas possíveis para obter mais informações sobre as entradas permitidas neste campo. |  |  |
| 12 | Salvar os dados | Salve as entradas. | Seus dados estão salvos. |  |

Procedimento: opção 2 - Administrar dados mestre de cliente

Siga este procedimento quando seu acesso de usuário oferece a você o app Administrar dados mestre do cliente(F0850A).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do cliente(F0850A). | O app é aberto. |  |
| 3 | Criar nova organização | Na tela Mestre de clientes, clique em Criar > Organização. | A tela Criar organização é exibida no modo de edição. |  |
| 4 | Inserir dados básicos | Na tela Criar organização, efetue as seguintes entradas:Informações geraisParceiro de negócios: Por exemplo, Z … (ou seja, qualquer ID alfanumérico externo, pois tem de começar com uma letra).Agrupamento: Por exemplo, BPAB.Atribua cada parceiro de negócios a um agrupamento quando você cria o registro de parceiro de negócios. O agrupamento determina o intervalo de numeração. Você não pode modificar a atribuição posteriormente.Função de parceiro de negócios: Selecione uma função, por exemplo, FLCU01 - Cliente.Nota Um cliente deve ser criado com a função de parceiro de negócios FLCU00 – Cliente (contabilidade financeira) ou com a função de parceiro de negócios FLCU01 – Cliente, ou ambas. A função de parceiro de negócios FLCU00 – Cliente (contabilidade financeira) é usada na contabilidade financeira e a função de parceiro de negócios FLCU01 – Cliente é usada em vendas.Título da organização: Por exemplo, Empresa (0003).Nome 1: <insira um nome>Endereço padrãoPaís/Região: Por exemplo, US.Idioma: Por exemplo, EN |  |  |
| 5 | Fechar a tela Criar organização | Na tela Criar organização, clique em OK. | A tela Criar organização é fechada. A tela Novo cliente é exibida. |  |
| 6 | Selecionar funções | Na tela Novo cliente, clique em Funções. | Você navega para a seção Funções. |  |
| 7 | Clicar em Criar | Na seção Funções, clique em Criar. |  |  |
| 8 | Inserir dados de funções adicionais | Na seção Funções, clique em Criar e efetue a seguinte entrada:Função de parceiro de negócios: Selecione a função adicional, por exemplo, FLCU00 - Cliente (contabilidade financeira)Nota Um cliente deve ser criado com a função de parceiro de negócios FLCU00 – Cliente (contabilidade financeira) ou com a função de parceiro de negócios FLCU01 – Cliente, ou ambas. A função de parceiro de negócios FLCU00 – Cliente (contabilidade financeira) é usada na contabilidade financeira e a função de parceiro de negócios FLCU01 – Cliente é usada em vendas. | Depois de você ter concluído a atualização de todas as funções de parceiro de negócios, elas são exibidas na seção Funções na tela Novo cliente. |  |
| 9 | Selecionar dados básicos | Na tela Novo cliente, selecione Dados básicos e vá para a seção Informações do cliente. | Você navega para a seção Informações do cliente |  |
| 10 | Inserir informação sobre cliente | Na seção Informações do cliente, efetue as seguintes entradas:Classificação de cliente: Por exemplo, A – Cliente.Grupo de contas do cliente: <Grupo de contas do cliente>Nota Se o agrupamento de parceiros de negócios permitir uma atribuição flexível de grupo de contas, você pode selecionar o grupo de contas a ser usado e diferenciar do valor proposto. Consulte os detalhes sobre agrupamentos de parceiros de negócio e como eles se relacionam com a numeração de ID na seção Agrupamento de parceiros de negócios e intervalos de numeração neste documento. |  |  |
| 11 | Selecionar Informações adicionais | Na tela Novo cliente, selecione Dados básicos e vá para a seção Informações adicionais. | Você navega para a seção Informações adicionais. |  |
| 12 | Inserir informações adicionais | Na seção Informações adicionais, efetue as seguintes entradas:EstFrrExpExpr.: <nome da estação expressa>Centro: <selecione um centro>Código de setor 1: <selecione um código de setor>Grupo de condições 1: <selecione um grupo de condições> |  |  |
| 13 | Selecionar endereço | Na tela Novo cliente, clique em Endereço e vá para a seção Endereço padrão. | Você navega para a seção Endereço padrão. |  |
| 14 | Inserir dados de endereço | Na seção Endereço padrão, efetue as seguintes entradas:Rua: Por exemplo, Augusta Ave SESelecione o país/região se ainda não o tiver feito na etapa 4.Número: por exemplo, 200.Código postal: Por exemplo, 30315-1402.Cidade: Por exemplo, Atlanta.Região: Por exemplo, GA.Nota Quando você cria um Parceiro de negócios localizado nos Estados Unidos, o código do Domicílio fiscal é determinado automaticamente. No entanto, você tem que inserir o endereço correto e completo, uma vez que o domicílio é derivado com base nas entradas de Região e Código postal.Comunicação padrãoSelecione o idioma se não o tiver feito na etapa 4.Celular: <Celular>E-mail: Adicione o endereço de e-mail, por exemplo, contact@Z.com |  |  |
| 15 | Selecionar contas bancárias | Na tela Novo cliente, selecione Contas bancárias. | Você navega para a seção Contas bancárias. |  |
| 16 | Clicar em Criar | Na seção Contas bancárias, clique em Criar. | Uma entrada para a conta bancária é exibida no modo de edição. |  |
| 17 | Inserir dados do banco | Na tela Nova conta bancária, efetue as seguintes entradas e clique em Aplicar:ID: Por exemplo, BNK1.País do banco: Por exemplo, US.Chave do banco: Por exemplo, 011000390 - Banco 1 BANCO MODELONúmero da conta: por exemplo, 102030.Faça entradas em todos os outros campos para os dados do banco com base em seus requisitos. | Você navega de volta à tela Novo cliente. |  |
| 18 | Selecionar números de identificação | Na tela Novo cliente, selecione Números de identificação e vá para a seção Números de identificação fiscal. | Você navega para a seção Números de identificação fiscal. |  |
| 19 | Clicar em Criar | Na seção Números de identificação fiscal, clique em Criar. |  |  |
| 20 | Inserir dados do número de identificação fiscal | Na seção Números de identificação fiscal, efetue as seguintes entradas:Categoria de imposto: <Selecionar uma categoria principal>Número de identificação fiscal: <número de identificação fiscal>Os números de identificação fiscal inseridos dependem de requisitos de país/região específicos.Nota Selecione a categoria correta aplicável ao país/região do cliente. Por exemplo, para um parceiro de negócios alemão, você atualiza um valor para a categoria DE1, que representa o número de identificação fiscal de IVA usado habitualmente (Umsatzsteuer-Identifikationsnummer).Efetue entradas apenas para os campos necessários, caso contrário, clique em Excluir para remover o conjunto de dados (vazio). |  |  |
| 21 | Selecionar categorias de imposto | Na tela Novo cliente, selecione Categorias de imposto. | Você navega para a seção Categorias de imposto. |  |
| 22 | Clicar em Criar | Na seção Categorias de imposto, clique em Criar. |  |  |
| 23 | Inserir dados de categorias de imposto (opcional) | Na seção Categorias de impsoto, efetue as seguintes entradas:Código de imposto: Por exemplo, Câmara de comércio de COCNº do certificado de isenção: <Nº do certificado de isenção>Taxa de certificado de isenção: por exemplo, 800.Data de início da isenção: <Data de início da isenção>.Data final da isenção: <Data final da isenção> |  |  |
| 24 | Selecionar Textos | Na tela Novo cliente, selecione Textos. | Você navega para a seção Textos |  |
| 25 | Criar textos | Na seção Textos, clique em Criar e efetue as seguintes entradas:Idioma: Por exemplo, ENID: por exemplo, 01.Texto descritivo: <Insira um texto descritivo> |  |  |
| 26 | Selecionar dados básicos | Selecione Dados básicos > Clientes adicionais. | Você navega para a seção Clientes adicionais. |  |
| 27 | Adicionar dados do cliente adicional | Na seção Clientes adicionais, clique em Criar.Adicione os dados necessários como descrito nas etapas acima.Nota Este cenário destina-se a atribuições múltiplas de clientes aos mesmos parceiros de negócios e, por isso, são aplicáveis os mesmos dados mestre descritos nas etapas acima referidas.Se forem necessários dados adicionais, tais como dados de venda e dados da empresa, consulte as seções anteriores que descrevem como adicionar dados da empresa e dados de vendas, por exemplo. |  |  |
| 28 | Salvar os dados | Clique em Criar. | Uma mensagem do sistema indica que o objeto foi salvo. |  |

### Criar dados mestre do cliente – Dados da empresa

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do cliente. Os apps disponíveis dependem de sua função atribuída. Por isso, são fornecidas duas opções.

Pré-requisito

Você deve concluir o capítulo anterior, [Criar dados mestre do cliente – Dados gerais](#unique_8) [página ] 6, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos dados gerais, tal como descrito no capítulo anterior.

Procedimento: opção 1 - Atualizar parceiro de negócios

Siga este procedimento quando seu acesso de usuário oferece a você o app Atualizar parceiro de negócios(BP).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar parceiro de negócios(BP). | O app é aberto. |  |
| 3 | Procurar e abrir | Procure e abra o parceiro de negócios (cliente) que você criou no capítulo anterior: [Criar dados mestre do cliente – Dados gerais](#unique_8) [página ] 6. | O parceiro de negócios é exibido na lista de pesquisa. |  |
| 4 | Comutar para modo de modificação | Selecione Comutar entre exibição e modificação para ativar o modo de modificação. |  |  |
| 5 | Modificar função de parceiro de negócios | No campo Modificar em função de PN, selecione o seguinte valor:Cliente (contabilidade financeira)Nota A chave técnica para esta função de parceiro de negócios é FLCU00 |  |  |
| 6 | Abrir dados da empresa | Selecione Empresa. | A tela Empresa é exibida. |  |
| 7 | Inserir empresa | Insira a Empresa. |  |  |
| 8 | Inserir dados contábeis do cliente | Na guia Cliente: Administração de contas, na seção Administração de contas, efetue as seguintes entradas:Conta de reconciliação: 140000 (clientes – Contas a receber nacionais)Chave de ordenação: <Chave de ordenação> |  |  |
| 9 | Inserir dados de pagamento do cliente | Na guia Cliente: Transações de pagamento, na seção Dados de pagamento, efetue uma entrada para o seguinte campo:Condições de pagamento: <condições de pagamento> |  |  |
| 10 | Inserir dados de pagamento do cliente | Na guia Cliente: Transações de pagamento, na seção Transações de pagamento automáticas, efetue entradas para os seguintes campos:Formas de pagamento: <Formas de pagamento>Banco da empresa: <Banco da empresa>Nota Pressione F4 para abrir a seleção no campo Formas de pagamento. |  |  |
| 11 | Inserir dados de correspondência do cliente | Na guia Cliente: Correspondência, na seção Correspondência, efetue as seguintes entradas:Responsável: <Responsável>Conta no cliente: <Conta no cliente> |  |  |
| Somente para a Tailândia | Código de filial (só para a Tailândia) | Para abrir dados gerais, na guia Ampliação específica do país, atualize os dados de código da filial junto com o endereço e o código de filial padrão para este parceiro de negócios.Para o endereço do código da filial, clique em Endereço e insira os seguintes dados:Nome (primeiras duas linhas): <Nome do contribuinte>País: THCódigo do edifício: <nome edif./Localidade>Sala: <nº da sala>Andar: <andar>Rua 2: <Moo>Rua 3: <Trok/Soi>Rua: <estrada>Número: <não>Outra cidade: <Tumbol/Sub-zona>Bairro: <bairro/zona>Cidade: <província>Código postal: <Código postal>Telefone: <Número de telefone>Nota Caso haja mais de um código de filial para um parceiro de negócios, você deverá atualizar cada código de filial junto com o endereço para cada código de filial. Você também deve definir um código de filial que é normalmente usado pelo parceiro de negócios como padrão. |  |  |
| Só para o Japão | Resumo de faturas (só para o Japão) | Na guia Ampliação específica de país, se este cliente for relevante para o resumo de faturas, efetue as entradas a seguir de acordo com os requisitos.Na seção Japão: Resumo de faturas – FunçãoFunção IS: <Função IS>Se Função IS for P: Pagador do resumo de faturas, na seção Japão: Resumo de faturas – Fatura:Intervalo de numeração: MI: <Intervalo de numeração: MI>Cálculo do imposto em MI <Cálculo do imposto em MI>Deslocar data de vencimento: <Deslocar data de vencimento>Regra condição de pagamento <Regra condição de pagamento>Válido desde: <Início da validade>Condição de pagamento: <Condição de pagamento>Na seção Japão: Resumo de faturas – Pagamento:Intervalo de numeração: PI: <Intervalo de numeração: PI>Tarifa bancária – recebedor do pagamento: <Tarifa bancária – recebedor do pagamento>ID de modelo tarifa bancária: <ID de modelo tarifa bancária>Relevante para casos especiais: <NÃO selecionar>País do banco: <País do banco>Chave do banco: <Código do banco>Nº de conta virtual: <Nº de conta virtual>Número sequencial: <Número sequencial>Nome do recebedor alternativo do pagamento <Nome do recebedor alternativo do pagamento>Nome do banco do contador: <Nome do banco do contador>Nome da agência bancária do contador <Nome da agência bancária do contador>Se Função IS for M: recebedores da fatura mensal na seção Japão: Resumo de faturas – FunçãoPagador resumo de faturas: <Pagador do resumo de faturas>Na seção Japão: Resumo de faturas – Fatura:Intervalo de numeração: MI: <Intervalo de numeração: MI>Cálculo do imposto em MI <Cálculo do imposto em MI>Se Função IS for C: (resumo da fatura) cliente na seção Japão: Resumo de faturas – FunçãoDestinatário do resumo de faturas: <Destinatário do resumo de faturas>: |  |  |
| 12 | Salvar os dados | Salve as entradas. | A entrada no campo Modificação em função PN muda de Cliente FI (novo) para Cliente FI (definido). |  |

Procedimento: opção 2 - Administrar dados mestre de cliente

Siga este procedimento quando seu acesso de usuário oferece a você o app Administrar dados mestre do cliente(F0850A).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do cliente(F0850A). | O app é aberto. |  |
| 3 | Procurar e abrir | Procure e abra o parceiro de negócios (cliente) que você criou no capítulo anterior: [Criar dados mestre do cliente – Dados gerais](#unique_8) [página ] 6. |  |  |
| 4 | Clicar em Editar | Clique em Editar. | A tela Mestre de clientes é exibida no modo de edição (os campos estão prontos para suas entradas). |  |
| 5 | Selecionar Empresa | Na tela Mestre de clientes, clique na guia Empresas. | Você navega para a seção Empresas |  |
| 6 | Clicar em Criar | Na seção Empresas, clique em Criar. | A tela Nova empresa é exibida no modo de edição. |  |
| 7 | Inserir dados da empresa | Na tela Nova empresa, efetue as seguintes entradas:Empresa: insira a empresa, por exemplo, 1710.Na guia Correspondência:Responsável: Por exemplo: 01 Sra. Smith.Na guia Finanças:Finanças – ContabilidadeConta de reconciliação: Por exemplo, 12100000 – Contas a receber estrangeirasChave de ordenação: Por exemplo, 009 número de documento externo.Finanças – Dados de pagamentoCondições de pagamento: por exemplo, 0001.Finanças – Transações de pagamento automáticasFormas de pagamento: Por exemplo, C (cheque, por exemplo, para EUA)Na guia Dados de advertência:Área de advertência: Unidade organizacional que você usa para processar o programa de advertência, por exemplo, por divisão ou organização de vendas.Procedimento de advertência, Bloqueio de advertências, Destinatário da advertência, Responsável pela advertência: Selecione nas entradas possíveis.Nível de advertência: por exemplo, 0.Última advertência: Por exemplo, 10.02.2020Procedimento judicial de advertência de: por exemplo, 11.02.2020.Na guia Textos:Na seção Textos , clique em Criar e efetue as seguintes entradas:Idioma: Por exemplo, ENID: por exemplo, 01.Texto descritivo: <Insira um texto descritivo> |  |  |
| 8 | Retornar à tela principal | Clique em Aplicar. |  |  |
| 9 | Salvar os dados | Clique em Salvar. | Uma mensagem do sistema indica que o objeto foi salvo. |  |

### Criar dados mestre do cliente – Dados da área de vendas

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do cliente. Os apps disponíveis dependem de sua função atribuída. Por isso, são fornecidas duas opções.

Pré-requisito

Você deve concluir o capítulo anterior, [Criar dados mestre do cliente – Dados gerais](#unique_8) [página ] 6, para prosseguir com este capítulo.

Siga o procedimento depois de ter salvo as entradas dos dados gerais, tal como descrito no capítulo anterior, na tela Exibir organização: nome do cliente.

Procedimento: opção 1 - Atualizar parceiro de negócios

Siga este procedimento quando seu acesso de usuário oferece a você o app Atualizar parceiro de negócios(BP).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar parceiro de negócios(BP). | O app é aberto. |  |
| 3 | Comutar para modo de modificação | Selecione Comutar entre exibição e modificação para ativar o modo de modificação. |  |  |
| 4 | Modificar função de parceiro de negócios | No campo Modificar em função de PN, selecione o seguinte valor:ClienteNota A chave técnica para esta função de parceiro de negócios é FLCU01. |  |  |
| 5 | Abrir Área de vendas | Selecione Vendas e distribuição na tela. | A tela Área de vendas é exibida. |  |
| 6 | Inserir dados da área de vendas | Efetue as seguintes entradas:Organização de vendas: <organização de vendas>Canal de Distribuição:: <canal de distribuição>Setor: <setor de atividade>Nota Estas três entradas (organização de vendas, canal de distribuição e setor de atividade) formam a área de vendas. Em muitos casos, a área de vendas define o objetivo para o processamento de vendas, por exemplo, no âmbito da ordem do cliente ou da determinação do preço. |  |  |
| 7 | Inserir dados de ordens do cliente | Na guia Ordens, na seção Ordem, efetue as entradas seguintes:Moeda: <moeda> |  |  |
| 8 | Inserir dados de expedição | Na guia Expedição, na seção Expedição, efetue as entradas seguintes:Prioridade de remessa: <Prioridade de remessa>Centro fornecedor: <Centro fornecedor>Condições de expedição: <Condições de expedição> |  |  |
| 9 | Inserir dados de faturamento | Na guia Faturamento, na seção Condições de remessa e de pagamento, efetue as seguintes entradas:Incoterms: EXW (Na origem)Você pode atualizar o valor de incoterm e fornecer a respectiva descrição.Nota Os campos para incoterms são interdependentes. Por exemplo, ao atualizar o valor do campo Incoterms, você precisa fornecer as informações de ID local incoterm 1 e Local incoterm 1.Condições de pagamento: <selecione as condições de pagamento>Nota As condições de pagamento aqui definidas são copiadas para uma ordem do cliente e usadas em vez das condições de pagamento definidas no nível da empresa. |  |  |
| 10 | Inserir dados contábeis | Na seção Contabilidade, efetue a seguinte entrada:Grpo.ClassCont.clnt.: <selecione o grupo de classificações contábeis para o cliente>Por exemplo, os clientes nacionais poderão ser atribuídos ao grupo de classificações contábeis 01 e os clientes estrangeiros poderão ser atribuídos ao grupo de classificações contábeis 02. Vá para as entradas possíveis para ver mais opções. |  |  |
| 11 | Inserir dados de imposto | Na seção Imposto liquidado, selecione o valor seguinte para a entrada existente na tabela:Classif.fiscal: <1>Por exemplo, o valor <1> significa que este cliente é totalmente tributável. |  |  |
| 12 | Modificar dados de funções de parceiro | Na guia Funções do parceiro, as 4 funções padrão a seguir estão disponíveis para o cliente. Você pode criar as 4 funções de parceiro:EO – Emissor da ordemRF – Recebedor da faturaPgr – PagadorRM – Recebedor da mercadoriaNota As quatro funções de parceiro mencionadas acima são o conjunto mínimo de funções para a atribuição a um registro de dados mestre de cliente, para trabalhar em um processo padrão de vendas e distribuição. |  |  |
| 13 | Inserir texto descritivo | No campo Texto do cliente, insira os detalhes de dados de venda. Observe que este é um campo somente leitura. Use a opção Editar texto para modificar o texto descritivo. |  |  |
| 14 | Abrir Dados gerais | Selecione Dados gerais na tela. |  |  |
| 15 | Inserir dados organizacionais | Na guia Cliente: Dados gerais, na seção Marketing, efetue a seguinte entrada:Classificação cliente: <Selecionar uma classificação de cliente> |  |  |
| 16 | Salvar os dados | Salve as entradas. |  |  |

Procedimento: opção 2 - Administrar dados mestre de cliente

Siga este procedimento quando seu acesso de usuário oferece a você o app Administrar dados mestre do cliente(F0850A).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do cliente(F0850A). | O app é aberto. |  |
| 3 | Procurar e abrir | Procure e abra o parceiro de negócios (cliente) que você criou no capítulo anterior: [Criar dados mestre do cliente – Dados gerais](#unique_8) [página ] 6. |  |  |
| 4 | Clicar em Editar | Clique em Editar. | A tela Mestre de clientes é exibida no modo de edição (os campos estão prontos para suas entradas). |  |
| 5 | Selecionar Área de vendas | Na tela Mestre de clientes, selecione Áreas de vendas.Nota A guia Áreas de vendas só está disponível se o parceiro de negócios tiver a função FLCU01 (cliente). | A seção Áreas de vendas é exibida. |  |
| 6 | Clicar em Criar | Na seção Áreas de vendas, selecione Criar. | A tela Nova área de vendas é exibida no modo de edição. |  |
| 7 | Inserir dados da área de vendas | Na tela Nova área de vendas, efetue as seguintes entradas:Dados geraisOrganização de vendas: por exemplo, 1710.Nota Se você selecionar a organização de vendas a partir das entradas possíveis, os campos a seguir (Canal de distribuição e Setor de atividade) serão inseridos automaticamente.Canal de distribuição: por exemplo, 10.Setor: por exemplo, 00.Detalhes da área de vendasDetalhes da área de vendas - Ordens do cliente:Conta no cliente: <insira sua conta no cliente>Moeda: Por exemplo, USD.Detalhes da área de vendas – Faturamento:Incoterms: Por exemplo, EXW.Local incoterms 1: Por exemplo, Palo Alto.Condições de pagamento: por exemplo, 0001.Detalhes da área de vendas – Expedição:Prioridade de remessa: Por exemplo, Normal.Centro fornecedor: por exemplo, 1710.Condições de expedição: Por exemplo, Imediatamente.Detalhes da área de vendas – Contabilidade:Grupo de classificações contábeis: Por exemplo, Receitas nacionais.Detalhes da área de vendas – Determinação do preço e estatísticas:Esquema do cliente: Por exemplo, Procedimento 01. |  |  |
| 8 | Selecionar Textos | Na tela Nova área de vendas, clique em Textos. |  |  |
| 9 | Clicar em Criar | Na seção Textos, clique em Criar e efetue as seguintes entradas:Idioma: Por exemplo, ENID: Selecione um número de ID ou insira um número de ID manualmente, por exemplo, 01.Texto descritivo: <insira um texto descritivo> |  |  |
| 10 | Selecionar Impostos | Na tela Nova área de vendas, clique em Impostos. | A seção Impostos é exibida. |  |
| 11 | Selecionar país/região e categoria de imposto | Na seção Impostos, selecione a entrada para um país/região, por exemplo, EUA (US).Nota A entrada Categoria de imposto depende da localização do cliente. Por exemplo, UTXJ é a categoria de imposto para criar um cliente americano, e TTXJ é a categoria de imposto para criar um cliente alemão. | A tela Impostos da área de vendas é exibida no modo de edição. |  |
| 12 | Inserir Classificação fiscal | Na guia Imposto, efetue a seguinte entrada:Classificação fiscal: Selecione, por exemplo, Sujeito a impostos (1). |  |  |
| 13 | Selecionar Aplicar | Clique em Aplicar. | Você volta para a visão principal. |  |
| 14 | Selecionar Funções do parceiro | Na tela Nova área de vendas, selecione Funções do parceiro. | A seção Funções do parceiro é exibida. |  |
| 15 | Clicar em Criar | Na seção Funções do parceiro, selecione Criar. | A seção Funções do parceiro é exibida no modo de edição. |  |
| 16 | Inserir dados de função de parceiro | Selecione uma função do parceiro, por exemplo, Emissor da ordem (SP).Selecione a entrada para a função do parceiro e, na tela Dados gerais, selecione um número de parceiro e insira uma descrição do parceiro. |  |  |
| 17 | Retornar à visão principal | Clique em Aplicar. | A função do parceiro adicionada é exibida na visão principal. |  |
| 18 | Inserir dados de função de parceiro | Repita as etapas 15 a 17 (para adicionar uma função do parceiro) para incluir dados adicionais da função do parceiro. Adicione as seguintes funções do parceiro:Nota As chaves de Função de parceiro de dois caracteres são dependentes do idioma. As chaves aqui documentadas são válidas para o idioma de login "português".Em outros idiomas, essas chaves podem ser diferentes. Por exemplo, as chaves de função de parceiro de dois caracteres em alemão são:AG para emissor da ordem (Auftraggeber)WE para recebedor da mercadoria (Warenempfänger)RE para recebedor da fatura (Rechnungsempfänger)RG para pagador (Regulierer)Função de parceiro: Recebedor da mercadoria:Função do parceiro: RM – Recebedor da mercadoriaFunção de parceiro: Recebedor da fatura:Função do parceiro: RF – Recebedor da faturaFunção de parceiro: Pgr – PagadorFunção do parceiro: Pgr – Pagador |  |  |
| 19 | Retornar à visão principal | Clique em Aplicar.Nota Certifique-se de que a mensagem do sistema Esboço atualizado é exibida na parte inferior da visão, antes de você retornar à visão principal. |  |  |
| 20 | Salvar os dados | Clique em Salvar. | Uma mensagem do sistema indica que o objeto foi salvo. |  |

### Criar hierarquias de clientes

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento fornece instruções para a hierarquia de clientes do tipo vendas e análise, usando o app Administrar hierarquias de clientes(F5794).

Pré-requisito

Você deve concluir o capítulo anterior, [Criar dados mestre do cliente – Dados gerais](#unique_8) [página ] 6, para prosseguir com este capítulo.

Siga o procedimento depois de salvar as entradas dos dados gerais, tal como descrito no capítulo anterior.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar hierarquias de clientes(F5794). | O app é aberto. |  |
| 3 | Criar nova hierarquia | Na tela Administrar hierarquias de clientes selecione Criar. |  |  |
| 4 | Selecionar Tipo de hierarquia | Selecione o tipo de hierarquia com base nas seguintes opções:Hierarquia de clientes – VendasHierarquia de clientes – Análise |  |  |
| 5 | Inserir dados relacionados à hierarquia | Na caixa de diálogo Criar novas hierarquias, forneça o ID da hierarquia e insira os outros dados necessários. |  |  |
| 6 | Editar subnó | Assim que o nó superior com o ID da hierarquia fornecido na etapa anterior for criado, adicione subnós a esse nó superior. Você poderá executar as seguintes ações:Modificar o nome da hierarquia.Alterar validades e outros detalhes, como vendas, distribuição, setor de atividade, etc.Simular opção como on/off.Excluir os subnós mapeados para a hierarquia. |  |  |
| 7 | Opções de subnó | Selecione o nó superior definido na etapa anterior.Selecione a opção para definir o subnó. Abaixo estão os três tipos de subnós que podem ser adicionados:Subnó: Este é um nó de texto que pode ser personalizado com base nas suas necessidades empresariais. Ele pode conter vários subnós.Subnó – Parceiro de negócios: Este é um nó de parceiro de negócios que pode conter vários subnós. O sistema verifica automaticamente se o parceiro de negócios adicionado à hierarquia pertence à mesma área de vendas.Parceiro de negócios: Este é um nó de parceiro de negócios; no entanto, é um nó final e não pode conter mais nós. O sistema verifica automaticamente se o parceiro de negócios adicionado à hierarquia pertence à mesma área de vendas. | É exibida a tela Dados mestre - produto.Os dados estão salvos. |  |
| 8 | Criar subnó | Selecione o nó pai.Selecione Editar. Clique em + para adicionar um subnó.Selecione registros mestre de cliente relevantes que já existem no sistemaSe o tipo de hierarquia for Vendas, selecione se um subnó é relevante para a determinação de preços.Nota Os subnós também podem ser criados no modo de entrada rápida, o que ajuda a criar vários subnós de uma só vez. | Certifique-se de que o subnó foi criado e é exibido sob o nó raiz.Nota Se os valores da área de vendas/setor de atividade/distribuição não corresponderem ao cliente relevante adicionado anteriormente, o subnó não poderá ser adicionado e uma mensagem de erro O cliente não tem vendas/setor de atividade/distribuição relevante é exibida. |  |
| 9 | Ativar hierarquia | Clique em Ativar. | A hierarquia do cliente é ativada. |  |
| 10 | Excluir hierarquia | Clique em OK, se desejar excluir uma hierarquia. |  |  |
| 11 | Exportar/Importar | Selecione Exportar/Importar se quiser exportar ou importar uma hierarquia. | Você pode exportar ou importar uma estrutura hierárquica. |  |

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
- related-to :: [[08-sales-order-management/6n3-517]]
- related-to :: [[08-sales-order-management/6n3-519]]
- related-to :: [[08-sales-order-management/create-customer-hierarchy-master-data-script-6n3-515]]
- related-to :: [[08-sales-order-management/script-de-datos-maestros-crear-script-de-datos-maestros-de-jerarquia-d]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/6N3_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 46,091 chars in the whole document
