---
id: 13-quality-ehs-and-compliance/criar-registro-info-de-qualidade-mds-bf5-554
title: Criar registro info de qualidade – MDS (BF5) (BF5_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese master data test script (BF5) for creating quality info records, QM control keys and first-sample (PAPP) settings in SAP S/4HANA Cloud Public Edition 2608."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/quality-info-records]
aliases: [BF5_S4CLD2608_Master_Data_PT_XX]
keywords: [Quality Info Records in Procurement, quality info record, qm procurement control key, production part approval, first sample inspection, vendor release, business roles, master data scripts, goods receipt inspection, BF5]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-554
topic: 13-quality-ehs-and-compliance/quality-info-records
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar registro info de qualidade – MDS (BF5) (BF5_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Quality Info Records in Procurement** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar registro info de qualidade – MDS (BF5) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893948)

[2 Pré-requisitos 3](#_Toc233893949)

[2.1 Acesso ao sistema 3](#_Toc233893950)

[2.2 Funções 3](#_Toc233893951)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893952)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893953)

[3 Tabela de síntese 5](#_Toc233893954)

[4 Procedimentos de teste 6](#_Toc233893955)

[4.1 Criar registro info de qualidade no suprimento 6](#_Toc233893956)

[4.2 Criar registro info de qualidade para materiais sem registro info de qualidade (opcional) 7](#_Toc233893957)

[4.3 Atribuir chaves de controle QM para suprimento 8](#_Toc233893958)

[4.4 Criar configurações para PAPP 9](#_Toc233893959)

## Objetivo

Se for necessário um acordo de garantia de qualidade ou uma liberação de fornecedor para um material, um planejador da qualidade terá que criar um registro de informação de qualidade (registro info de qualidade). O registro info de qualidade define o modo como o material pode continuar sendo processado.

Se um pedido for criado, o sistema verifica se um registro info de qualidade é necessário e está disponível para a combinação de material e fornecedor.

O sistema também verifica se a combinação fornecedor e material-fornecedor está bloqueada ou foi liberada para cotações, pedidos e/ou entrada de mercadorias. A execução desta verificação depende das configurações de QM na chave de controle de suprimento no mestre de materiais.

Além disso, você pode atribuir sistemas QM e acionar um possível controle de forma correspondente. Ele também pode determinar se um controle de entrada de mercadorias e/ou um controle de recebimento é acionado. Você também pode indicar se um processo de aprovação de peças de produção (APP) é necessário; nesse caso, você pode planejar os controles da primeira amostra (CPA) no registro info de qualidade. Você pode administrar o APP aqui atualizando o Status APP e o Código de avaliação (com base na decisão de utilização tomada). Além disso, você pode atribuir vários pedidos/itens ao mesmo tempo ao APP para executar o controle da primeira amostra (CPA).

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
| Planejador da qualidade | SAP_BR_QUALITY_PLANNER | Planejamento de qualidade | SAP_BR_QUALITY_PLANNER |  |

Para mais informações sobre funções empresariais, consulte Atribuir funções empresariais a um usuário no Guia de administração para a implementação do SAP S/4HANA Cloud Public Edition.

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre de cliente são dependentes das unidades organizacionais da empresa. Os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Registro info de qualidade | Centro |  | Os dados do centro podem existir para cada ID do centro da sua estrutura empresarial para a qual é usado o registro mestre de cliente. | Centro: |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre da administração de qualidade podem fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem usados em um registro info de qualidade.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Mestre de materiais |  | Obrigatório | Com visão da administração de qualidade. Para mais informações, consulte o script de dados mestre Criar atributos de administração de qualidade para mestre de materiais/produtos – MDS (BNY). |
| Mestre de fornecedores |  | Obrigatório |  |

|  |
| --- |
| Nota Um registro info de qualidade é necessário se a chave de suprimento QM exigir uma liberação de fornecedor. Nesse caso, para cada combinação de fornecedor e material, é necessário criar um registro info de qualidade. |

## Tabela de síntese

Este item de escopo é composto por várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar registro info de qualidade no suprimento](#unique_8) [página ] 6 | Planejador da qualidade | Criar registro info de qualidade - Suprimento(QI01) | Foi criado um registro info de qualidade. |
| [Criar registro info de qualidade para materiais sem registro info de qualidade (opcional)](#unique_9) [página ] 7 | Planejador da qualidade | Administrar registros info qualidade(F2256A) | Foi criado um registro info de qualidade. |
| [Atribuir chaves de controle QM para suprimento](#unique_10) [página ] 8 | Planejador da qualidade | Atribuir chaves de controle QM para suprimento - Processar manualmente(QI05) | Foi criado um registro info de qualidade. |
| [Criar configurações para PAPP](#unique_11) [página ] 9 | Planejador da qualidade | Administrar registros info qualidade(F2256A) | Foi criado um registro info de qualidade. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar registro info de qualidade no suprimento

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador da qualidade. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar registro info de qualidade - Suprimento(QI01). | A visão Criar registro info de qualidade é exibida. |  |
| 3 | Inserir dados gerais | Efetue as seguintes entradas:Material: <número do material>Fornecedor: <código do fornecedor>Centro: <código do centro>Selecione Continuar. |  |  |
| 4 | Inserir dados de liberação | Na seção Liberar, insira os dados seguintes:Liberar até: data no futuro, por exemplo, daqui a um anoOpcional:Quantidade liberada está ativa: marcadoQuantidade liberada: por exemplo, 15 |  |  |
| 5 | Salvar os dados | Clique em Salvar. | Os dados são salvos. |  |

|  |
| --- |
| Nota No registro info de qualidade, você também pode decidir se quer desativar o controle de entrada de mercadorias ou executar um controle de entrada de mercadorias e/ou controle de recebimento. Para isso, selecione a guia Controle da verificação e insira os seguintes dados:Se você quiser executar um controle de recebimento além de um controle de entrada de mercadorias, insira um tipo de controle para o controle de recebimento e um tempo de processamento em dias.Se você não quiser executar um controle de entrada de mercadorias mesmo que as configurações no mestre de materiais indiquem um controle desse tipo, configure o indicador Nenhum controle.Se você quiser executar um controle de recebimento em vez de um controle de entrada de mercadorias, configure o indicador relevante.Se esse indicador estiver definido, o sistema não criará um lote de controle para uma entrada de mercadorias se for executado um controle de recebimento. Se não for executado nenhum controle de recebimento, será gerado um lote de controle para a entrada de mercadorias.Na guia Controle da verificação, você também pode inserir o seguinte:Sistema QM do fornecedorSe o fornecedor tiver um sistema QM, você poderá armazenar aqui a descrição do sistema QM para esse material específico.Aprovação da peça de produçãoVocê pode especificar que um processo de aprovação da peça de produção é necessário. Você deve fazer outras configurações para isso no app Administrar registros info qualidade(F2256A) (veja o capítulo [Atribuir chaves de controle QM para suprimento](#unique_10) [página ] 8). |

### Criar registro info de qualidade para materiais sem registro info de qualidade (opcional)

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador da qualidade. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar registros info qualidade(F2256A). |  |  |
| 3 | Criar registro info de qualidade (opcional) | Selecione Criar no canto superior direito da tabela de resultados e atualize os seguintes dados no nível do Cabeçalho:Material: número do materialFornecedor: código do fornecedorCentro: código do centroPara a seção Liberação, consulte o capítulo anterior, etapa 4. |  |  |
| 4 | Salvar os dados | Clique em Criar. | Os dados são salvos e um novo registro info de qualidade foi criado. |  |

### Atribuir chaves de controle QM para suprimento

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador da qualidade. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atribuir chaves de controle QM para suprimento - Processar manualmente(QI05). |  |  |
| 3 | Atribuir chave de controle QM | Você pode executar esta seleção no nível do centro e/ou do material. Selecione a chave de controle QM a ser atribuída.Material: número do materialCentro: código do centroChave de controle QM: Chave de controle QMExecutar modif.banco dados: ativo (se este código não estiver definido, só é executada uma execução de teste)Nota Somente os materiais em que o código QM em suprmto. ativo está definido nos dados mestre de materiais são selecionados. |  |  |

### Criar configurações para PAPP

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Pré-requisito

Um controle da primeira amostra é alcançado usando o plano de controle dedicado Controle da primeira amostra de EM, que é atribuído às seguintes Chaves de controle para QM no suprimento:

- 0001 Liberação de fornecedor
- 9001 Liberação de fornecedor (com mensagem de erro)

Em detalhe, as seguintes condições devem ser cumpridas para que um controle da primeira amostra seja executado:

- Existe um plano de controle com a utilização Controle da primeira amostra de EM (51) para o controle da primeira amostra.
- Uma das chaves de controle QM listadas acima está atribuída ao material.
- Para este material, existe um registro info de qualidade com as seguintes configurações em Aprovação de peça de produção:
    - A aprovação de peça de produção é ativada e o nível PAPP e o status PAPP são definidos.
    - Pelo menos um pedido de compra e um item do pedido de compra são inseridos.

Na entrada de mercadorias para o item do pedido de compra, é criado um lote de controle para o controle da primeira amostra. Para esse lote de controle, a utilização do plano FAI da chave de controle QM é usada e a utilização é atualizada para o tipo de controle.

Procedimento

Você ativa PAPP no app Administrar registros info qualidade(F2256A). Ali você pode indicar para um material que um controle da primeira amostra deve ocorrer na entrada de mercadorias para um ou vários itens do pedido de compra.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador da qualidade. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar registros info qualidade(F2256A). |  |  |
| 3 | Criar registro info de qualidade | Selecione Criar no canto superior direito da tabela de resultados e atualize os seguintes dados no nível do Cabeçalho:Material: número do materialFornecedor: código do fornecedorCentro: código do centroPara a seção Liberação, consulte a etapa 4 no capítulo anterior.Ou então, selecione um registro info de qualidade existente em que você pretende ativar o PAPP. |  |  |
| 4 | Inserir dados de aprovação da peça de produção | Vá para a seção Aprovação da peça de produção. Selecione Ativar.Atribua o nível PAPP correspondente no campo Nível PAPP. |  |  |
| 5 | Salvar os dados | Clique em Criar. | Os dados são salvos e um novo registro info de qualidade foi criado. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/crear-registro-info-de-calidad-mds-bf5-552]]
- related-to :: [[13-quality-ehs-and-compliance/create-quality-info-record-mds-bf5-551]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bf5-553]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bf5-555]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 18,225 chars in the whole document
