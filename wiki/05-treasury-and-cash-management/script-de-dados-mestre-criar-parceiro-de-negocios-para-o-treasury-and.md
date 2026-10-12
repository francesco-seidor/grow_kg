---
id: 05-treasury-and-cash-management/script-de-dados-mestre-criar-parceiro-de-negocios-para-o-treasury-and
title: Script de dados mestre - Criar parceiro de negócios para o Treasury and Risk Management – MDS (22G) (22G_S4CLD2608_Master_Data_PT_XX)
description: SAP S/4HANA Cloud Public Edition 2608 master data script (PT) with manual test steps to create and maintain business partners for Treasury and Risk Management (22G).
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/treasury-business-partners]
aliases: [22G_S4CLD2608_Master_Data_PT_XX]
keywords: [Business Partners for Treasury and Risk Management, business partner creation, treasury risk management, payment details, correspondence profiles, securities partner roles, business partner authorizations, derived flows, external recipients, internal recipients]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/22G_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-260
topic: 05-treasury-and-cash-management/treasury-business-partners
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar parceiro de negócios para o Treasury and Risk Management – MDS (22G) (22G_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/22G_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Business Partners for Treasury and Risk Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar parceiro de negócios para o Treasury and Risk Management – MDS (22G) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893569)

[2 Pré-requisitos 3](#_Toc233893570)

[2.1 Acesso ao sistema 3](#_Toc233893571)

[2.2 Funções 3](#_Toc233893572)

[2.3 Dados mestre, dados organizacionais e outros dados 4](#_Toc233893573)

[3 Tabela de síntese 5](#_Toc233893574)

[4 Procedimentos de teste 7](#_Toc233893575)

[4.1 Atualizar dados gerais para o parceiro de negócios 7](#_Toc233893576)

[4.2 Atualizar dados da empresa para o parceiro de negócios 9](#_Toc233893577)

[4.2.1 Atualizar detalhes de pagamento para o parceiro de negócios 9](#_Toc233893578)

[4.2.2 Atualizar autorizações para o parceiro de negócios 12](#_Toc233893579)

[4.2.3 Atualizar movimentos derivados para o parceiro de negócios (opcional) 13](#_Toc233893580)

[4.2.4 Atualizar dados contábeis na empresa para o parceiro de negócios 15](#_Toc233893581)

[4.3 Atualizar dados de correspondência para o parceiro de negócios 17](#_Toc233893582)

[4.3.1 Atualizar perfil e atribuições do grupo de PN ao destinatário externo 17](#_Toc233893583)

[4.3.2 Atualizar perfil e atribuições do grupo de PN ao destinatário interno 21](#_Toc233893584)

[4.4 Atualizar dados mestre do parceiro de negócios para títulos 24](#_Toc233893585)

[4.4.1 Criar função emitente para o parceiro de negócios 25](#_Toc233893586)

[4.4.2 Criar função banco de depósitos para o parceiro de negócios 26](#_Toc233893587)

[4.5 Atualizar dados mestre do parceiro para carta de crédito 27](#_Toc233893588)

[4.5.1 Criar Função Banco para Parceiro de Negócios 27](#_Toc233893589)

## Objetivo

Este módulo fornece as etapas manuais básicas para criar parceiros de negócios para Treasury and Risk Management.

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
| Especialista de tesouraria - back office | SAP_BR_TREASURY_SPECIALIST_BOE | Tesouraria back office | SAP_BR_TREASURY_SPECIALIST_BOE |  |
| Especialista em dados mestre - dados do parceiro de negócios | SAP_BR_BUPA_MASTER_SPECIALIST | Dados mestre - Parceiros de negócios / Governança do parceiro de negócios / Governança do parceiro de negócios / Governança do parceiro de negócios | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Especialista de configuração - configuração de processo empresarial | SAP_BR_BPC_EXPERT | Configuração de processo empresarial / Configuração de processo empresarial - Finanças / Configuração de processo empresarial - Suprimento / Administrar sua solução / Configuração de processo empresarial - Workflow / Configuração empresarial - Administração de funcionalidades / Configuração de processo empresarial - Extensibility Explorer / Configuração de gestão empresarial - Transporte | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Dados mestre, dados organizacionais e outros dados

A estrutura organizacional e os dados mestre da empresa foram criados no seu sistema durante a ativação. A estrutura organizacional reflete a estrutura da sua empresa. Os dados mestre representam materiais, clientes e fornecedores, por exemplo, dependendo do foco operacional da sua empresa.

Use seus próprios dados mestre para analisar o procedimento de teste. Se você tiver instalado um pacote SAP Best Practices Baseline, poderá usar os seguintes dados de amostra do pacote básico.

|  |
| --- |
| Atenção Os valores de amostra para valores de dados mestre são específicos do país/região e os valores fornecidos na tabela a seguir são para a Alemanha. Substitua os valores específicos de país/região fornecidos por SAP Best Practices para SAP S/4HANA Cloud Public Edition ou use os valores de dados mestre criados para esse fim. |

| Dados | Valor de amostra | Detalhes | Comentários |
| --- | --- | --- | --- |
| EMPRESA | por exemplo, 1010 |  |  |
| MOEDA | por exemplo, EUR |  |  |
| MOEDA ESTRANGEIRA 1 | Por exemplo, USD |  |  |
| BANCO DA EMPRESA | Por exemplo, DEBK1 |  |  |
| ID DA CONTA BANCÁRIA DA EMPRESA 1 | Por exemplo, DEAC1 |  |  |
| ID DA CONTA BANCÁRIA DA EMPRESA 2 | Por exemplo, USAC2 |  |  |
| PARCEIRO DE NEGÓCIOS | 10537001 |  |  |

## Tabela de síntese

Criar parceiro de negócios para o Treasury and Risk Management – MDS (22G) é composto por várias etapas de processo fornecidas nas seguintes tabelas:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

Tabela 1: Atualizar dados para parceiro de negócios padrão

| Etapa de processo, relatório ou item | Função empresarial | Transação / App | Resultados previstos |
| --- | --- | --- | --- |
| [Atualizar dados gerais para o parceiro de negócios](#unique_7) [página ] 7 | Especialista em dados mestre - dados do parceiro de negócios | Atualizar parceiro de negócios(BP) | Os dados gerais do parceiro de negócios são atualizados. |
| Atualizar dados da empresa para o parceiro de negócios |  |  |  |
| [Atualizar detalhes de pagamento para o parceiro de negócios](#unique_8) [página ] 9 | Especialista em dados mestre - dados do parceiro de negócios | Atualizar parceiro de negócios(BP) | Os dados dos detalhes de pagamento do parceiro de negócios são atualizados. |
| [Atualizar autorizações para o parceiro de negócios](#unique_9) [página ] 12 | Especialista em dados mestre - dados do parceiro de negócios | Atualizar parceiro de negócios(BP) | Os dados de autorização do parceiro de negócios são atualizados. |
| [Atualizar movimentos derivados para o parceiro de negócios (opcional)](#unique_10) [página ] 13 | Especialista em dados mestre - dados do parceiro de negócios | Atualizar parceiro de negócios(BP) | Os dados de movimentos derivados do parceiro de negócios são atualizados. |
| [Atualizar dados contábeis na empresa para o parceiro de negócios](#unique_11) [página ] 15 | Especialista em dados mestre - dados do parceiro de negócios | Atualizar parceiro de negócios(BP) | Os dados contábeis do parceiro de negócios são atualizados. |
| Atualizar dados de correspondência para parceiros de negócios |  |  |  |
| [Atualizar perfil e atribuições do grupo de PN ao destinatário externo](#unique_12) [página ] 17 | Especialista em dados mestre - dados do parceiro de negócios | Atribuir perfil e grupo de PNs - Destinatários externos(FTR_EXT_ASSIGN) | Os perfis do PN e os grupos do PN são atualizados para o destinatário externo. |
| [Atualizar perfil e atribuições do grupo de PN ao destinatário interno](#unique_13) [página ] 21 | Especialista em dados mestre - dados do parceiro de negócios | Atribuir perfil e grupo de PNs - Destinatários internos(FTR_INT_ASSIGN) | Os perfis e os grupos do PN e os IDs do usuário são atualizados para o destinatário interno. |
| Atualizar dados mestre do parceiro de negócios para títulos |  |  |  |
| [Criar função emitente para o parceiro de negócios](#unique_14) [página ] 25 | Especialista em dados mestre - dados do parceiro de negócios | Atualizar parceiro de negócios(BP) | A função emitente será criada. |
| [Criar função banco de depósitos para o parceiro de negócios](#unique_15) [página ] 26 | Especialista em dados mestre - dados do parceiro de negócios | Atualizar parceiro de negócios(BP) | A função banco de depósito será criada. |
| Atualizar dados mestre do parceiro para carta de crédito |  |  |  |
| [Criar Função Banco para Parceiro de Negócios](#unique_16) [página ] 27 | Especialista em dados mestre - dados do parceiro de negócios | Atualizar parceiro de negócios(BP) | A função Banco é criada. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Atualizar dados gerais para o parceiro de negócios

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Esta seção descreve o processo de atualização de dados gerais para o parceiro de negócios.

|  |
| --- |
| Lembrete Os valores de amostra para valores de dados mestre são específicos de país/região e os valores fornecidos na tabela a seguir são para a Alemanha. Substitua os valores específicos de país/região fornecidos por SAP Best Practices para SAP S/4HANA Cloud Public Edition ou use os valores de dados mestre criados para esse fim. |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar parceiro de negócios(BP). | O app é aberto. |  |
| 3 | Inserir dados na 1ª tela | Na tela Atualizar parceiro de negócios, selecione Organização. | A tela Criar organização é exibida. |  |
| 4 | Inserir dados de endereço | Na tela Criar organização, insira os seguintes dados:Parceiro de negócios: por exemplo, 10537001.Agrupamento: selecione TR02 Parceiro de tesouraria (externo).Criar na função PN: selecione 000000 Parceiro de negócios (geral).Título: selecione 0003 Empresa.Nome: por exemplo, Banco 1 - BANCO MODELO.Saudação: por exemplo, Banco 1.Critério de pesquisa 1/2: por exemplo, Banco 1.Rua/número: <Endereço>Código postal/Cidade: <código postal e cidade>País/região: Selecione o <código do país/região>.Idioma: Selecionar <código do idioma>.E-mail: <endereço de e-mail>Endereço válido desde: por exemplo, <a data atual no ano anterior>.Endereço válido até: Por exemplo, 31 de dez.do ano 9999.Clique em Salvar.Nota Permaneça na tela para etapas subsequentes.Nota Se você apenas visualiza Parceiro de negócios (geral) sem a chave 000000, talvez você tenha que ir para Menu > Configurações - Design de interação > Visualização > Lista dropdown > Mostrar listas dropdown com chaves e ativá-lo. | O parceiro de negócios é criado corretamente. |  |
| 5 | Comutar para modo de modificação | Na tela Exibir organização: 10537001, selecione Comutar entre exibição e modificação e insira os seguintes dados:Alterar em função PN: Selecione TR0151 Contraparte | São exibidas mais guias relacionadas à contraparte, como Dados legais, Classificação. |  |
| 6 | Inserir dados legais | Na tela Alterar organização: 10537001 , nova função Contraparte, selecione Menu de navegação.Nota O Menu de navegação encontra-se na parte direita da tela. É exibido como …, imediatamente ao lado do símbolo >.Na lista dropdown, selecione Dados legais e insira os seguintes dados:País/região: por exemplo, selecione DE.Clique em Salvar.Nota Permaneça na tela para etapas subsequentes. | Os dados legais são inseridos e salvos.A tela Modificar organização: 10537001, nova função Contraparte é exibida. |  |
| 7 | Inserir dados da transação de pagamento | Na tela Alterar organização: 10537001, função Contraparte, escolha Menu de navegação.Na lista dropdown, selecione Transações de pagamento e insira os seguintes dados em duas linhas:Linha 1:ID: código da moeda + 1, por exemplo, EUR1.P/R: <Código do país/região>Chave do banco: <chave do banco>Conta bancária: <conta bancária>IBAN: selecione o IBAN e depois Continuar na caixa de diálogo IBAN.Linha 2:ID: código da moeda estrangeira + 1, por exemplo, USD1.P/R: <Código do país/região>Chave do banco: <chave do banco>Conta bancária: <conta bancária>IBAN: selecione o IBAN e depois Continuar na caixa de diálogo IBAN.Clique em Salvar.Nota Se a caixa de diálogo Informações for exibida quando você selecionar IBAN, selecione ContinuarNota O IBAN é usado principalmente em países da UE. Para os EUA, ignore as etapas relacionadas ao IBAN. | Os dados da transação de pagamento são inseridos e o parceiro de negócios é salvo. |  |

### Atualizar dados da empresa para o parceiro de negócios

#### Atualizar detalhes de pagamento para o parceiro de negócios

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Esta seção descreve as etapas sobre como atualizar os dados de detalhes de pagamento para o parceiro de negócios.

|  |
| --- |
| Lembrete Os valores de amostra para valores de dados mestre são específicos do país/região e os valores fornecidos na tabela a seguir são para a Alemanha. Substitua os valores específicos de país/região fornecidos por SAP Best Practices para SAP S/4HANA Cloud Public Edition ou use os valores de dados mestre criados para esse fim. |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar parceiro de negócios(BP). | A tela Atualizar parceiro de negócios é exibida. |  |
| 3 | Comutar para modo de modificação | Na tela Atualizar parceiro de negócios, selecione Abrir PN. Na caixa de diálogo, insira os seguintes dados:Parceiro de negócios: 10537001Pressione Enter.Selecione Comutar entre Exibição e Modificação e insira os dados seguintes:Modificar em função PN: selecione TR0151 Contraparte | A tela Modificar organização: 10537001, função Contraparte é exibida. |  |
| 4 | Inserir SI: Dados de detalhes do pagamento | Em Modificar organização: 10537001, função Contraparte, selecione Empresa e insira os dados seguintes:Empresa: por exemplo, 1010Pressione ENTER e clique em SI: Detalhes do pagamento para inserir as quatro linhas de dados a seguir:Linha 1Moeda: por exemplo, EURID DetlhsPgto.: por exemplo, EURIBanco da empresa: Por exemplo, DEBK1.ID da conta: por exemplo, DEAC1Pagador/recebedor do pagamento: por exemplo, deixar em brancoBanco do parceiro: por exemplo, deixar em brancoSolicitação de pagamento: por exemplo, Anular seleçãoFormas de pagamento: por exemplo, deixar em brancoLinha 2Moeda: por exemplo, EURID DetlhsPgto.: por exemplo, EUROBanco da empresa: Por exemplo, DEBK1.ID da conta: por exemplo, DEAC1Pagador/recebedor do pagamento: por exemplo, 10537001Banco do parceiro: por exemplo, EUR1Solicitação de pagamento: por exemplo, selecionarFormas de pagamento: por exemplo, TLinha 3Moeda: por exemplo, USDID DetlhsPgto.: por exemplo, USDIBanco da empresa: Por exemplo, DEBK1.ID da conta: por exemplo, USDACPagador/recebedor do pagamento: por exemplo, deixar em brancoBanco do parceiro: por exemplo, deixar em brancoSolicitação de pagamento: por exemplo, Anular seleçãoFormas de pagamento: por exemplo, deixar em brancoLinha 4Moeda: por exemplo, USDID DetlhsPgto.: por exemplo, USDOBanco da empresa: Por exemplo, DEBK1.ID da conta: por exemplo, USDACPagador/recebedor do pagamento: por exemplo, 10537001Banco do parceiro: por exemplo, USD1Solicitação de pagamento: por exemplo, SelecionarFormas de pagamento: por exemplo, FNota Permaneça nesta tela para as etapas subsequentes.Nota Certifique-se de inserir a forma de pagamento no campo Formas de pagamento em vez de no campo Forma de pagamento.Nota Se for exibida uma janela de aviso com a mensagem seguinte: Parceiro de negócios proposto como pagador/recebedor do pagamento (veja texto descritivo)Novamente exibir esta mensagem para este parceiro de negócios?Selecione Não. | Os dados SI: detalhes do pagamento são inseridos. |  |
| 5 | Atribuir detalhes do pagamento | Na tela da etapa anterior, atribua detalhes do pagamento. Por exemplo, para EUR, selecione a linha EUR EURI.Selecione Atribuir na caixa de diálogo Modificação de contraparte: atribuição dos detalhes de pagamento.Selecione Selecionar todas as entradas. O resultado é a exibição de EURI em ID do pagamento de entrada.Clique em Continuar para fechar a caixa de diálogo.Selecione a linha EUR EURO.Selecione Atribuir na caixa de diálogo Modificação de contraparte: atribuição dos detalhes de pagamento.Selecione Selecionar todas as saídas. Como resultado, é exibido EURO em IDPgto.Saída.Clique em Continuar para fechar a caixa de diálogo.Repita a etapa para USD:USDI: IDPgto.Entr.USDO: IDPgto.SaídaNa tela Modificar organização: 10537001, função Contraparte, clique em Salvar. | Os detalhes do pagamento e as atribuições são salvos. |  |

#### Atualizar autorizações para o parceiro de negócios

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Esta seção descreve as etapas sobre como atualizar os dados de autorização para o parceiro de negócios para o SAP Treasury and Risk Management.

|  |
| --- |
| Lembrete Os valores de amostra para valores de dados mestre são específicos do país/região e os valores fornecidos na tabela a seguir são para a Alemanha. Substitua os valores específicos de país/região fornecidos por SAP Best Practices para SAP S/4HANA Cloud Public Edition ou use os valores de dados mestre criados para esse fim. |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar parceiro de negócios(BP). | A tela Atualizar parceiro de negócios é exibida. |  |
| 3 | Comutar para modo de modificação | Na tela Atualizar parceiro de negócios, selecione Abrir PN. Na caixa de diálogo, insira os seguintes dados:Parceiro de negócios: 10537001Pressione Enter.Clique em Mudar entre modo exibição e modificação e insira os seguintes dados:Modificar em função PN: selecione TR0151 Contraparte | A tela Modificar organização: 10537001, função Contraparte é exibida. |  |
| 4 | Inserir SI: Dados de autorizações | Na tela Modificar organização: 10537001, função Contraparte, clique em Empresa, SI: Autorizações.Marque o campo de seleção Autoriz. para todas as outras entradas e clique em Salvar.Nota Você também pode conceder autorização a um tipo de produto e transação específicos expandindo as pastas. Para fins de teste, são concedidas todas as autorizações a todos os tipos de produto e de transação. | Os dados de autorização são salvos. |  |

#### Atualizar movimentos derivados para o parceiro de negócios (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Esta seção descreve as etapas sobre como atualizar os dados de movimentos derivados para um parceiro de negócios. Alguns países o o imposto sobre o rendimento da taxa de juros é o que cria um tipo especial de imposto que você deve incluir para um parceiro de negócios. Neste procedimento você define um imposto sobre o rendimento de juros, específico do país/região, para tipo de produto e tipo de transação. Esta etapa é opcional.

|  |
| --- |
| Lembrete Os valores de amostra para valores de dados mestre são específicos de país/região e os valores fornecidos na tabela a seguir são para a Alemanha. Substitua os valores específicos de país/região fornecidos por SAP Best Practices para SAP S/4HANA Cloud Public Edition ou use os valores de dados mestre criados para esse fim. |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar parceiro de negócios(BP). | O app é aberto. |  |
| 3 | Comutar para modo de modificação | Na tela Atualizar parceiro de negócios, selecione Abrir PN. Na caixa de diálogo, insira os seguintes dados:Parceiro de negócios: 10537001Pressione Enter.Selecione Comutar entre exibição e modificação e insira os seguintes dados:Modificar em função PN: Selecione TR0151 Contraparte | A tela Modificar organização: 10537001, função Contraparte é exibida. |  |
| 4 | Inserir SI: Dados de movimentos derivados | Na tela Modificar organização: 10537001, função Contraparte, clique em Empresa, SI: Movimentos derivados e expanda: Mercado monetário > Instrumento de taxa de juros > 51A Depósito a prazo fixo/empréstimos > 100 InvestimentoSelecione Marcar/desm.linhas entradas.Na caixa de diálogo Procedimento para gerar movimentos derivados 1 Entrada, selecione INTDE.Clique em OK.Os resultados são o que o INTDE exibe na coluna Procedimento.Clique em Salvar. | Os dados dos movimentos derivados são inseridos e salvos. |  |
| 5 | Repetir para produto e tipos de transação adicionais | Repita a etapa anterior para cada um dos seguintes tipos de produto e de transação:Tipo de produto.…..Tipo de transação52B.…..10053A.…..10053A.…..10153A.…..10254A.…..10055A.…..10058A.…..300Dica As localizações dos tipos de produto são as seguintes:52B se encontra em Mercado monetário > Depósito a pré-aviso.53A se encontra em Mercado monetário > Papel comercial.54A se encontra em Mercado monetário > Transação de fluxo de caixa.55A se encontra em Mercado monetário > Instrumento de taxa de juros.58A se encontra em Mercado monetário > Instrumento no estilo de conta corrente. |  |  |

#### Atualizar dados contábeis na empresa para o parceiro de negócios

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Esta seção descreve as etapas para atualizar relações empresariais para um parceiro de negócios.

|  |
| --- |
| Lembrete Os valores de amostra para valores de dados mestre são específicos do país/região e os valores fornecidos na tabela a seguir são para a Alemanha. Substitua os valores específicos de país/região fornecidos por SAP Best Practices para SAP S/4HANA Cloud Public Edition ou use os valores de dados mestre criados para esse fim. |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar parceiro de negócios(BP). | A tela Atualizar parceiro de negócios é exibida. |  |
| 3 | Comutar para modo de modificação | Na tela Atualizar parceiro de negócios, selecione Abrir PN. Na caixa de diálogo, insira os seguintes dados:Parceiro de negócios: 10537001Pressione Enter.Selecione Comutar entre Exibição e Modificação e insira os dados seguintes:Modificar em função PN: clique em TR0151 Contraparte | A visão Alterar organização: 10537001, função Contraparte é exibida. |  |
| 4 | Inserir dados contábeis na empresa | Na tela Modificar organização: 10537001, função Contraparte, clique em Empresa e Dados contábeis na empresa,Nota Se você não encontrar os dados contábeis na empresa na tela, vá para o menu de navegação e selecione-os no menu drop-down.Insira os seguintes dados:Rel. empresa: por exemplo, 3 OutrosClique em Salvar.Nota Rels.empres. reflete sua relação com a contraparte:1 afiliada e consolidada2 afiliada, mas não consolidada3 não afiliada4 Não utilizarEstas são utilizadas para derivar as contas do Razão corretas. | Os dados contábeis são inseridos e salvos. |  |

### Atualizar dados de correspondência para o parceiro de negócios

SAP Treasury Risk Management fornece uma funcionalidade de correspondência padrão. Com esta funcionalidade de correspondência, sempre que uma transação de Treasury and Risk Management seja gravada, o sistema envia um e-mail ao parceiro de negócios ou imprime automaticamente um formulário na impressora designada.

Para utilizar esta funcionalidade de correspondência, é necessário atribuir os seguintes dados a um parceiro de negócios:

- Perfil do parceiro de negócios
- Grupo de parceiros de negócios

#### Atualizar perfil e atribuições do grupo de PN ao destinatário externo

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Este procedimento descreve a atribuição de perfis de parceiro de negócios e grupos de parceiros de negócios a um parceiro de negócios externo.

Os perfis do parceiro de negócios e os grupos de parceiros de negócios controlam as atividades de correspondência no SAP Treasury Risk Management.

Os perfis de parceiro de negócios predefinidos são os seguintes:

- PR_EMAIL
- PR_PRINT

Estes perfis de parceiro de negócios predefinidos podem ser atribuídos a seu parceiro de negócios. Por exemplo, se a comunicação com seu parceiro de negócios for feita por meio de e-mail, você atribui PR_EMAIL ao parceiro de negócios. Se a comunicação for feita por envio de um documento impresso, você atribui PR_PRINT ao parceiro de negócios.

O grupo de parceiros de negócios a seguir foi predefinido:

- BPG_DEFAULT

Você atribui este grupo de parceiros de negócios a seu parceiro de negócios ou usa as etapas de configuração Definir grupo de parceiros de negócios e Atribuir atributos a grupos de parceiros de negócios para adicionar seu próprio grupo de parceiros de negócios e depois designar atributos apropriados de acordo com seus requisitos específicos. É possível atribuir diferentes perfis de parceiro de negócios e grupos de parceiros de negócios ao mesmo parceiro de negócios.

|  |
| --- |
| Lembrete Os valores de amostra para valores de dados mestre são específicos do país/região e os valores fornecidos na tabela a seguir são para a Alemanha. Substitua os valores específicos de país/região fornecidos por SAP Best Practices para SAP S/4HANA Cloud Public Edition ou use os valores de dados mestre criados para esse fim. |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista de tesouraria - back office. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atribuir perfil e grupo de PNs - Destinatários externos(FTR_EXT_ASSIGN). | A tela Atribuir perfil e grupo PN a destinatários externos é exibida. |  |
| 3 | Inserir dados do parceiro de negócios | No lado esquerdo da tela Atribuir perfil e grupo PN a destinatários externos, selecione Inserir linha e insira os seguintes dados.PN: por exemplo, 10537001Empr.: por exemplo, 1010Tipo envio/dest.: por exemplo, selecione a linha CONTRAPARTEPressione Enter. | As informações do parceiro de negócios são inseridas. |  |
| 4 | Atribuir perfil empresarial e grupo PN ao parceiro de negócios | Na parte superior direita da tela Atribuição de perfis e grupos PN a destinatários externos, selecione Expandir nó para expandir:PN:0010537001 / Emp.: 1010 / Tipo emiss./dest.: CONTRAPARTE > Mercado monetário > Instrumento de taxa de juros > 51A Depósito prazo fixo/empréstimo > 100 Investimento.Selecione 10 Contratos.Na parte inferior direta da tela Atribuição de perfis e grupos PN a destinatários externos, selecione Inserir linha e adicione o e-mail ou o perfil de impressão:Nota Normalmente, você atribui somente um perfil a um tipo de produto/tipo de transação/categoria de atividade. Se for necessário atribuir ambos os perfis após concluir o primeiro perfil, selecione Inserir linha novamente para adicionar o outro perfil.Quando o perfil for e-mail:Perfil: por exemplo, PR_EMAILGrupo PN: por exemplo, BPG_DEFAULTClique em Salvar.Ou quando o perfil for impressão:Perfil: por exemplo, PR_PRINTGrupo PN: por exemplo, BPG_DEFAULTClique em Salvar. | Os perfis do parceiro de negócios e os grupos de parceiros de negócios são atribuídos para o tipo de produto/tipo de transação/categoria de atividade. |  |
| 5 | Repetir para tipo de produto/Tipo de transação/Categoria de atividade | Clique em Modificar linha na parte superior esquerda da tela e repita a etapa anterior para atribuir perfis e grupos de PN para os seguintes tipos de produto e transações:Tipo de produtoTipo de movimentoCtg. atividade51A1001051A2001052B1001052B1001153A1001053A1011053A1021053A2001053A2011053A2021054A1001054A2001055A1001055A2001055A1001155A2001156A1001056A2001058A3001058A3001160A1012060A1022060A1032060A1042060A1052060A1072060B1032060B1035560B1042060B1045560B1052060B1055560B1102060B1105562A3002062A3012062A3022062B3002062B3012062B3022076A1002076A20020 | Para todos os tipos de produto/tipos de transação/categorias da atividade listados são atribuídos perfis e grupos PN. |  |

#### Atualizar perfil e atribuições do grupo de PN ao destinatário interno

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O ID de destinatário interno é predefinido pela SAP. Pode estar ligado aos IDs de usuário da SAP. Se estiver ligado a um ID de usuário da SAP, sempre que um objeto de correspondência interno seja gerado, o SAP TRM tentará enviar informações de correspondência ao endereço do ID de usuário da SAP. Dependendo dos diferentes perfis (PR_EMAIL /PR_PRINT), o e-mail pode ser enviado ao endereço de e-mail do usuário ou um formulário é impresso.

Esta etapa descreve o modo como atribuir perfis do parceiro de negócios e grupos de parceiros de negócios a um parceiro de negócios interno.

|  |
| --- |
| Lembrete Os valores de amostra para valores de dados mestre são específicos do país/região e os valores fornecidos na tabela a seguir são para a Alemanha. Substitua os valores específicos de país/região fornecidos por SAP Best Practices para SAP S/4HANA Cloud Public Edition ou use os valores de dados mestre criados para esse fim. |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista de tesouraria - back office. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atribuir perfil e grupo de PNs - Destinatários internos(FTR_INT_ASSIGN). | A tela Atribuição de perfis e grupos PN a destinatários internos é exibida. |  |
| 3 | Inserir dados do parceiro de negócios | No lado esquerdo da tela Atribuição de perfis e grupos PN a destinatários internos, selecione Inserir linha e insira os seguintes dados:Lembrete Os valores de amostra para valores de dados mestre são específicos de país/região e os valores de exemplo a seguir são para Alemanha. Substitua os valores específicos de seu país/região fornecidos por SAP Best Practices para SAP S/4HANA Cloud Public Edition ou use os valores de dados mestre que você criou para esse fim.DesInt: por exemplo, DESTIN.INT.Empr.: por exemplo, 1010Tipo envio/dest.: por exemplo, marque o campo de seleção INTERNO.Pressione Enter. | As informações do parceiro de negócios são inseridas. |  |
| 4 | Atribuir perfil empresarial e grupo PN ao parceiro de negócios | Na parte superior direita da tela Atribuição de perfis e grupos PN a destinatários internos, expanda:PN:INT. INT./empr.: 1010/Tipo emiss./dest.: INTERNO > Mercado monetário > Instrumento de taxa de juros > 51A Depósito a prazo fixo/empréstimos > 100 InvestimentoSelecione 10 Contratos.Na parte inferior direita da tela Atribuição de perfis e grupos PN a destinatários internos, selecione Inserir linha.Insira as informações de perfil para o e-mail ou para a impressão:Perfil: por exemplo, para e-mail, PR_EMAILGrupo PN: por exemplo, BPG_DEFAULTNome de usuário: selecione um <ID do usuário>.Clique em Salvar.Selecione novamente Inserir linha e adicione uma outra entrada para a impressão:Perfil: por exemplo, para a opção de impressão, PR_PRINTGrupo PN: por exemplo, BPG_DEFAULTNome de usuário: selecione um <ID do usuário>.Nota O <ID do usuário> é um ID de usuário back-end.Clique em Salvar. | O perfil do parceiro de negócios e o grupo de parceiros de negócios, bem como o ID do usuário são atribuídos para o Tipo de produto/Tipo de transação/Categoria da atividade. |  |
| 5 | Repetir para tipo de produto/Tipo de transação/Categoria de atividade | Clique em Modificar linha na parte superior esquerda da tela e repita a etapa anterior para atribuir perfis e grupos de PN para os seguintes tipos de produto e transações:Tipo de produtoTipo de movimentoCtg. atividade51A1001051A2001052B1001052B1001153A1001053A1011053A1021053A2001053A2011053A2021054A1001054A2001055A1001055A2001055A1001155A2001156A1001056A2001058A3001058A3001160A1012060A1015560A1022060A1025560A1032060A1035560A1042060A1045560A1052060A1055560A1072060A1075560B1032060B1035560B1042060B1045560B1052060B1055560B1102060B1105562A3002062A3012062A3022062B3002062B3012062B3022076A1002076A20020 | Os perfis de PN, os grupos de PN e os IDs do usuário são atribuídos a todos os Tipos de produto/Tipos de transação/Categorias da atividade listados. |  |

### Atualizar dados mestre do parceiro de negócios para títulos

Objetivo

Para instrumentos financeiros relacionados com títulos, por exemplo, fundo do mercado financeiro, para registrar as informações básicas do emitente e banco de depósito, crie as seguintes funções de parceiro de negócios:

- TR0150 emitente
- TR0152 banco de depósitos

#### Criar função emitente para o parceiro de negócios

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Esta etapa descreve os processos para criar a função emitente para um parceiro de negócios.

|  |
| --- |
| Lembrete Os valores de amostra para valores de dados mestre são específicos de país/região. Substitua os valores específicos de país/região fornecidos por SAP Best Practices para SAP S/4HANA Cloud Public Edition ou use os valores de dados mestre criados para esse fim. |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app | Abra Atualizar parceiro de negócios(BP). | A tela Atualizar parceiro de negócios: é exibida. |  |
| 3 | Criar função de emissor | Selecione Abrir PN. Na caixa de diálogo, insira os seguintes dados:Parceiro de negócios: 10537001Pressione Enter.Selecione Comutar entre Exibição e Modificação e insira os dados seguintes:Modificar em função PN: selecione Emissor TR0150e clique em Salvar. | Na tela Modificar organização: 10537001, função Emissor, a seguinte notificação será exibida:As modificações foram salvas. |  |

#### Criar função banco de depósitos para o parceiro de negócios

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Esta etapa descreve os processos para criar a função banco de depósito para um parceiro de negócios.

|  |
| --- |
| Lembrete Os valores de amostra para valores de dados mestre são específicos de país/região e os exemplos de valores a seguir são para Alemanha. Substitua os valores específicos de país/região fornecidos por SAP Best Practices para SAP S/4HANA Cloud Public Edition ou use os valores de dados mestre criados para esse fim. |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar parceiro de negócios(BP). | A tela Atualizar parceiro de negócios é exibida. |  |
| 3 | Criar função Banco de depósitos | Selecione Abrir PN. Na caixa de diálogo, insira os seguintes dados:Parceiro de negócios: 10537001Pressione Enter.Selecione Comutar entre Exibição e Modificação e insira os dados seguintes:Modificar em função PN: selecione TR0152 Banco de depósitose clique em Salvar. | Na tela Modificar organização: 10537001, função Banco de depósitos, a seguinte notificação é exibida:As modificações foram salvas. |  |

### Atualizar dados mestre do parceiro para carta de crédito

#### Criar Função Banco para Parceiro de Negócios

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login no launchpad do SAP Fiori | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app | Abra Atualizar parceiro de negócios(BP). | A tela Atualizar parceiro de negócios é exibida. |  |
| 3 | Criar Função banco | Clique em Abrir PN. Na caixa de diálogo, insira os seguintes dados:Parceiro de negócios: 10537001Pressione Enter.Selecione Comutar entre Exibição e Modificação e insira os dados seguintes:Modificar em função PN: selecione Banco TR0703e clique em Salvar. | Na tela Modificar organização: 10537001 função Banco, a seguinte notificação será exibida:As modificações foram salvas. |  |

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
- related-to :: [[05-treasury-and-cash-management/create-business-partner-for-treasury-and-risk-management-mds-22g-257]]
- related-to :: [[05-treasury-and-cash-management/geschaftspartner-fur-treasury-and-risk-management-anlegen-mds-22g-256]]
- related-to :: [[05-treasury-and-cash-management/mds-22g-259]]
- related-to :: [[05-treasury-and-cash-management/mds-22g-261]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/22G_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 44,413 chars in the whole document
