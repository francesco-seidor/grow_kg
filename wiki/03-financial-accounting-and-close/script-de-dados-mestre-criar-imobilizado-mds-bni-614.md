---
id: 03-financial-accounting-and-close/script-de-dados-mestre-criar-imobilizado-mds-bni-614
title: Script de dados mestre - Criar imobilizado – MDS (BNI) (BNI_S4CLD2608_Master_Data_PT_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (PT): prerequisites, asset classes/number ranges and test procedures to create, change, block and delete fixed assets."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/fixed-asset-master-data]
aliases: [BNI_S4CLD2608_Master_Data_PT_XX]
keywords: [Fixed Asset Master Records, fixed asset master data, asset classes, number ranges, asset creation, asset modification, asset blocking and deletion, legacy data transfer, asset subnumbers, balance carryforward]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNI_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-614
topic: 03-financial-accounting-and-close/fixed-asset-master-data
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar imobilizado – MDS (BNI) (BNI_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNI_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Fixed Asset Master Records** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar imobilizado – MDS (BNI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893995)

[2 Pré-requisitos 3](#_Toc233893996)

[2.1 Acesso ao sistema 3](#_Toc233893997)

[2.2 Funções 3](#_Toc233893998)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893999)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233894000)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233894001)

[2.5.1 Classes do imobilizado e intervalos de numeração 4](#_Toc233894002)

[2.6 Etapas preliminares 6](#_Toc233894003)

[2.6.1 Validar disponibilidade do sistema de contabilidade do imobilizado 6](#_Toc233894004)

[2.6.1.1 Confirmar informação da data de aceitação 6](#_Toc233894005)

[2.6.1.2 Confirmar execução do transporte de saldo inicial para o exercício fiscal atual 8](#_Toc233894006)

[3 Tabela de síntese 10](#_Toc233894007)

[4 Procedimentos de teste 11](#_Toc233894008)

[4.1 Criar imobilizado 11](#_Toc233894009)

[4.2 Modificar imobilizado 13](#_Toc233894010)

[4.3 Exibir imobilizado 14](#_Toc233894011)

[4.4 Bloquear imobilizados 15](#_Toc233894012)

[4.5 Eliminar imobilizado 16](#_Toc233894013)

[4.6 Criar subativo de ativo 17](#_Toc233894014)

[4.7 Documentos de modificação para registros mestre do imobilizado 18](#_Toc233894015)

[4.8 Chave de depreciação: Exibir detalhes 19](#_Toc233894016)

## Objetivo

Um imobilizado é um objeto, um direito ou um outro item de propriedade de uma empresa, previsto para uso a longo prazo e que pode ser identificado individualmente no balanço. A manutenção de imobilizados envolve a criação, a modificação e a exibição de registro mestre do imobilizado.

Os diversos itens de informação são estruturados de acordo com a área de uso e funções no sistema, para facilitar aos usuários a criação, atualização e avaliação de dados mestre.

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
| Contador de imobilizado | SAP_BR_AA_ACCOUNTANT | Imobilizado | SAP_BR_AA_ACCOUNTANT |  |
| Contador geral | SAP_BR_GL_ACCOUNTANT | Razão | SAP_BR_GL_ACCOUNTANT |  |

### Unidades organizacionais necessárias

Os dados mestre do imobilizado são dependentes da unidade organizacional da empresa.

A tabela a seguir fornece uma síntese desta unidade organizacional:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser utilizada |
| --- | --- | --- | --- | --- |
| Dados da empresa | Empresa | ID, Descrição, Centro de custo, etc. | Os dados da empresa podem existir para cada ID da empresa da sua estrutura empresarial para a qual é utilizado o registro mestre do imobilizado. | <sua empresa> |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre do imobilizado podem fazer referência a outros dados mestre. A tabela seguinte oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre do imobilizado.

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Centro de custo | No mestre do ativo você encontra a entrada do centro de custo na guia Dependente de tempo. | Obrigatório | Para inserir o centro de custo do imobilizado, você deve criar o centro de custo previamente. Você pode inserir depois o centro de custo real nos registros mestre do imobilizado. |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um registro de dados mestre do imobilizado:

#### Classes do imobilizado e intervalos de numeração

As classes do imobilizado determinam os intervalos de numeração para os IDs de registro mestre do imobilizado. Você não pode modificar a atribuição ou os IDs posteriormente, mas somente transferi-los para outros registro mestre do imobilizado criado para outra classe do imobilizado. Se uma classe do imobilizado estiver atribuída a um intervalo de numeração interno, você não pode inserir o ID do registro mestre do imobilizado manualmente. Nesse caso, deixe o campo em branco, uma vez que o sistema seleciona automaticamente um número a partir do intervalo de numeração numérico atribuído.

As seguintes classes do imobilizado e os intervalos de numeração correspondentes são definidos para imobilizados na empresa 1010:

| Classe do imobilizado | Intervalo de numeração/ID do registro mestre do imobilizado | Comentários |
| --- | --- | --- |
| 1000 | Intervalo de numeração numérico interno:10000000 – 19999999 | Bens imóveis e direitos afins |
| 1100 | Intervalo de numeração numérico interno:10000000 – 19999999 | Edifícios |
| 1200Não relevante para todos os países ou regiões | Intervalo de numeração numérico interno:10000000 – 19999999 | Melhorias do terreno |
| 1500Não relevante para todos os países ou regiões | Intervalo de numeração numérico interno:10000000 – 19999999 | Melhorias de locação |
| 2000 | Intervalo de numeração numérico interno:20000000 – 29999999 | Máquinas e equipamentos |
| 3000 | Intervalo de numeração numérico interno:30000000 – 39999999 | Instalações e equipamentos |
| 3100 | Intervalo de numeração numérico interno:50000000 – 59999999 | Frota de veículos |
| 3200 | Intervalo de numeração numérico interno:60000000 – 69999999 | Hardware de computador |
| 3210 | Intervalo de numeração numérico interno:60000000 – 69999999 | Software de computador |
| 3300 | Intervalo de numeração numérico interno:30000000 – 39999999 | Equipamento de escritório |
| 4000 | Intervalo de numeração numérico interno:40000000 – 49999999 | Ativo em andamento (tangível): |
| 4010 | Intervalo de numeração numérico interno:40000000 – 49999999 | Ativo em andamento (intangível): |
| 4001 | Intervalo de numeração numérico interno:40000000 – 49999999 | IeA como medida de investimento (tangível) |
| 4011 | Intervalo de numeração numérico interno:40000000 – 49999999 | IeA como medida de investimento (intangível) |
| 5000 | Intervalo de numeração numérico interno:80000000 – 89999999 | Bens de baixo valor |
| 8200 | Intervalo de numeração numérico interno:90000000 – 99999999 | Aviamento |
| 8300 | Intervalo de numeração numérico interno:80000000 – 89999999 | Outros bens intangíveis |
| 9000 | Intervalo de numeração numérico interno:90000000 – 99999999 | Imobilizados apenas de imposto |

### Etapas preliminares

#### Validar disponibilidade do sistema de contabilidade do imobilizado

##### Confirmar informação da data de aceitação

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta atividade você confirma os valores para a data de aceitação de dados, status e tipo de documento para a entrada de imobilizados antigos

|  |
| --- |
| Nota Após a conclusão da ativação de conteúdo inicial, você precisa definir uma data de aceitação. Isto define o exercício corrente e último exercício encerrado na contabilidade do imobilizado. A data de aceitação é crítica para o processamento do sistema, pois identifica o momento em que os valores de imobilizado antigos são carregados. Para sistemas SAP S/4HANA Cloud Public Edition, trata-se normalmente do dia anterior ao fim do ano. Por exemplo, quando o sistema está em FY-2020 e a empresa estiver em um Exercício fiscal de ano civil padrão, a DATA DE ACEITAÇÃO é 31/12/2020. |

|  |
| --- |
| Atenção Isso implica que o carregamento de imobilizados antigos será a partir do final do ano de 2020. |

Procedimento

| Nº da etapa de processo | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador de imobilizado. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Efetuar configurações da empresa - Específico da contabilidade do imobilizado(F7312). | A tela Exibir configurações p/empresa na contabilidade imobilizado é exibida.Para comutar entre o modo de exibição e de modificação, selecione Modificar / Exibir. |  |
| 3 | Selecionar empresa | Selecione a sua empresa no lado esquerdo da tela e, em seguida, clique em Selecionar empresa. |  |  |
| 4 | Configurações gerais | Selecione a guia Configurações gerais. |  |  |
| 5 | Verificar as configurações gerais | Verifique o status da sua empresa | A guia Informações gerais exibe as configurações de sua empresa. O status da empresa deverá ser A testar. |  |
| 6 | Atualizar parâmetros para a transferência de dados de sistema antigo | Na seção Transferência de dados de sistema antigo, verifique ou modifique as seguintes entradas:Nota Se necessário, crie primeiro um novo segmento de transferência de sistema antigo selecionando Criar segmento de transferência de sistema antigo.Data de transferência: para efeitos de teste, defina esta data para o ÚLTIMO DIA do FIM DO EXERCÍCIO FISCAL ANTERIORStatus da transferência de dados de sistema antigo: para fins de teste, defina este status para ATUAL(outros lançamentos permitidos)Tipo de documento: para fins de teste, defina como AANota Para o valor Data de transferência, trata-se geralmente uma data de encerramento de um exercício anterior. Se você tiver instruções para usar uma data durante o exercício, esta data irá consistir em um data de fim do mês. A data deve ser sempre adiada (nunca atrasa).Nota Para o valor Status da transferência de dados de sistema antigo, você possui quatro opções:Em preparação: O sistema permite configurações de customizing incompletas para a transferência de dados legados (nesta fase não são permitidos lançamentos de documento).Atual: são permitidos apenas lançamentos da transferência de dados de sistema antigo (por exemplo, outros tipos de lançamentos, aquisições, baixas não são permitidos).Atual (outros lançamentos permitidos): São permitidos ambos lançamentos de transferência de dados de sistema antigo e outros lançamentos. Este status faz sentido quando você executa transferências de dados de sistema antigo adicionais em uma empresa que já seja produtiva.Concluído: a transferência de dados de sistema antigo está concluída. Não são permitidos lançamentos de transferência de dados de sistema antigo e você não pode criar imobilizados antigos. |  |  |
| 7 | Salvar as alterações | Selecione Menu > Geral > Salvar. |  |  |

##### Confirmar execução do transporte de saldo inicial para o exercício fiscal atual

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta atividade você confirma que o transporte de saldo inicial foi executado para o exercício fiscal atual.

|  |
| --- |
| Nota Se sua implementação não usar um ledger específico, ignore-o. |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador geral. |  |  |
| 2 | Acessar o app SAP Fiori | Abra Escalonar jobs do Razão(F1927). |  |  |
| 3 | Criar | Clique em Criar. |  |  |
| 4 | Inserir detalhes | Efetue as seguintes entradas e clique em Etapa 2:Modelo de job: Transporte de saldo inicialNome do job: Transporte de saldo inicial |  |  |
| 5 | Inserir detalhes | Efetue as seguintes entradas e clique em Etapa 3:Iniciar imediatamente: selecionado |  |  |
| 6 | Inserir detalhes | Efetue as seguintes entradas e clique em Programar:Ledger: <ledger>,, por exemplo, 0LEmpresa: <empresa>Transferência para exercício fiscal: <exercício fiscal>Execução de teste: selecionado | Você programou a execução do job como execução de teste. |  |
| 7 | Revisar resultados | Para revisar os resultados da sua execução de teste, procure pela execução no painel Jobs e clique no botão de seta à direita da respectiva linha. |  |  |
| 8 | Detalhes da execução | Selecione a guia Detalhes da execução. Revise o status do log. |  |  |
| 9 | Execução efetiva | Para efetuar uma execução produtiva, repita este processo, mas desmarque a Execução de teste | Você programou a execução de job como uma execução produtiva. |  |

## Tabela de síntese

Este item de escopo consiste nas etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar imobilizado](#unique_12) [página ] 11 | Contador de imobilizado | Abra Administrar imobilizado(F3425A) | O mestre do ativo fixo é criado no nível da empresa (plano de avaliação). |
| [Modificar imobilizado](#unique_13) [página ] 13 | Contador de imobilizado | Abra Administrar imobilizado(F3425A) | O mestre do ativo fixo é atualizado. |
| [Exibir imobilizado](#unique_14) [página ] 14 | Contador de imobilizado | Abra Administrar imobilizado(F3425A) | O mestre do ativo fixo é atualizado. |
| [Bloquear imobilizados](#unique_15) [página ] 15 | Contador de imobilizado | Abra Administrar imobilizado(F3425A) | O ativo fixo é bloqueado. |
| [Eliminar imobilizado](#unique_16) [página ] 16 | Contador de imobilizado | Abra Administrar imobilizado(F3425A) | O ativo fixo do imobilizado é excluído. |
| [Criar subativo de ativo](#unique_17) [página ] 17 | Contador de imobilizado | Abra Administrar imobilizado(F3425A) | O subimobilizado é criado. |
| [Documentos de modificação para registros mestre do imobilizado](#unique_18) [página ] 18 | Contador de imobilizado | Abra Administrar imobilizado(F3425A) | Todas as alterações anteriores de um registro de dados mestre de ativo existente (principal ou subativo) são exibidas. |
| [Chave de depreciação: Exibir detalhes](#unique_19) [página ] 19 | Contador de imobilizado | Chave de depreciação: exibir detalhes(FAA_DEPRKEY_SHOW)Nota Se você tiver ativado o Feature Toggle para o novo design, o app Chave de depreciação: exibir detalhes(FAA_DEPRKEY_SHOW) não será aplicável. | Com este app, são fornecidas informações sobre configurações de chaves de depreciação entregues pelo conteúdo padrão. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar imobilizado

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta atividade você pode criar um novo registro de dados principal do imobilizado como parte das suas operações diárias.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador de imobilizado. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar imobilizado(F3425A). | A tela Administrar ativos fixos é exibida. |  |
| 3 | Inserir detalhes do mestre do imobilizado | Clique em Criar > Criar imobilizado principal.Efetue as seguintes entradas:Empresa: <sua empresa>Classe do imobilizado: <classe do imobilizado para a qual você deseja criar um novo imobilizado>Incorporação posterior: <só necessário, se você desejar usar este registro mestre para lançar uma incorporação posterior>Um modelo de dados mestre do imobilizado pode ser usado. Caso seja necessário, o imobilizado a ser usado como referência deve ser inserido no campo Número principal do imobilizado, na seção Referência.Clique em OK. | A tela Criar imobilizado principal é exibida. |  |
| 4 | Inserir descrição do imobilizado e unidade de medida básica | Efetue as seguintes entradas:Descrição: <sua descrição do imobilizado>Unidade de medida básica: <Insira a unidade de medida necessária> |  |  |
| 5 | Clicar na guia Dados dependentes de tempo | Clique na guia Dados dependentes de tempo. | A guia Dados dependentes de tempo é exibida. |  |
| 6 | Inserir centro de custo | Efetue as seguintes entradas:Centro de custo: <seu centro de custoWBS_Element: <seu WBS_Element>Nota O Centro de custo e/ou o WBS_Element podem ser inseridos como coletor de custos para depreciação. |  |  |
| 7 | Inserir data de incorporação | Você só precisa inserir a data Incorporado em, caso o imobilizado tenha sido criado com o código incorporação posterior.Incorporado em: <sua data de incorporação> |  |  |
| 8 | Verificar outras guias | Vá para as outras guias e faça as entradas ou alterações necessárias. |  |  |
| 9 | Inserir, verificar ou adaptar parâmetros de depreciação | Efetue as seguintes entradas para todas as áreas de depreciação disponíveis:ChvD: <sua chave de depreciação>Nota Se você tiver ativado o Feature Toggle para o novo design, use o perfil de depreciação em vez da chave de depreciação.VidaÚtil: <vida útil em anos>Per: <vida útil em períodos>: | Todos os parâmetros de depreciação necessários foram especificados corretamente. |  |
| 10 | Salvar novo mestre do imobilizado | Clique em Criar para salvar suas entradas. | O registro mestre do imobilizado é criado. A mensagem do sistema confirma a criação e exibe o novo número do imobilizado. |  |

### Modificar imobilizado

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta atividade você pode alterar um registro de dados mestre do imobilizado existente (principal ou subnúmero) como parte das suas operações diárias.

|  |
| --- |
| Nota A modificação da classe do imobilizado só é possível mediante uma transferência interna à empresa para um novo registro mestre do ativo imobilizado dentro da nova classe do imobilizado. |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador de imobilizado. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar imobilizado(F3425A). | A tela Administrar ativos fixos é exibida. |  |
| 3 | Inserir informação sobre o imobilizado | Efetue as seguintes entradas:Empresa: <sua empresa>Imobilizado: <seu número do imobilizado>Clique em Ir.Selecione o número do ativo na tabela usando o link com o número do seu imobilizado.Na tela seguinte, clique em Editar. | A tela Administrar imobilizado é exibida.Nota As funções de exibição, alteração e exclusão estão disponíveis selecionando o imobilizado, a ação a ser exibida na caixa de diálogo e, em seguida, selecionando novamente essa ação. |  |
| 4 | Alterar mestre do imobilizado | Faça qualquer alteração necessária nos dados mestre do imobilizado. | As alterações necessárias são efetuadas. |  |
| 5 | Salvar mestre do imobilizado alterado | Clique em Criar para salvar suas entradas.Nota O sistema exibe uma notificação de êxito. Você precisa verificar suas alterações. | As alterações do mestre do imobilizado são salvas.As alterações efetuadas serão exibidas na guia Alterar documento. |  |

### Exibir imobilizado

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta atividade você pode exibir um registro de dados mestre do imobilizado existente (principal ou subnúmero) como parte das suas operações diárias.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador de imobilizado. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar imobilizado(F3425A). | A tela Administrar ativos fixos é exibida. |  |
| 3 | Inserir informação sobre o imobilizado | Efetue as seguintes entradas:Empresa: <sua empresa>Imobilizado: <seu número do imobilizado>Subnúmero: <seu subnúmero do imobilizado no caso>Clique em Ir.Selecione seu número do imobilizado na tabela usando o link com seu número do imobilizado.Selecione cada página Guia para revisar o registro mestre do imobilizado. |  |  |

### Bloquear imobilizados

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta atividade você bloqueia um registro de dados mestre do imobilizado existente (principal ou subnúmero) para mais aquisições.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador de imobilizado. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar imobilizado(F3425A). | A tela Administrar ativos fixos é exibida. |  |
| 3 | Inserir informação sobre o imobilizado | Efetue as seguintes entradas e clique em Ir:Empresa: <sua empresa>Imobilizado: <seu número do imobilizado> | A tela Administrar ativos fixos é exibida. |  |
| 4 | Definir o código de bloqueio | Selecione o Nº do imobilizado na tabela.Na nova tela, selecione Bloquear.Nota A notificação Imobilizado <número do imobilizado> bloqueado é exibida. | O código de bloqueio está definido.O imobilizado está bloqueado para outras aquisições.As alterações efetuadas serão exibidas na guia Documento de alteração. |  |

### Eliminar imobilizado

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta atividade você pode excluir um registro de dados mestre do imobilizado (principal ou subnúmero).

|  |
| --- |
| Nota Só os ativos sem data de incorporação e sem valores podem ser excluídos diretamente. |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador de imobilizado. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar imobilizado(F3425A). | A tela Administrar ativos fixos é exibida. |  |
| 3 | Inserir informação sobre o imobilizado | Efetue as seguintes entradas e clique em Ir:Empresa: <sua empresa>Imobilizado: <seu número do imobilizado> |  |  |
| 4 | Definir o código de eliminação | Selecione o Nº do imobilizado e, na nova tela, clique em Excluir. | O código está definido. |  |
| 5 | Confirmar | Uma mensagem Excluir objeto? é exibida na tela. Clique em Excluir para confirmá-la. |  |  |

### Criar subativo de ativo

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta atividade você pode criar um novo registro de dados do subativo de ativo como parte das suas operações diárias.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador de imobilizado. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar imobilizado(F3425A). | A tela Administrar ativos fixos é exibida. |  |
| 3 | Inserir a referência do imobilizado principal | Na tela Administrar ativos, clique em Criar ativo > Criar subativo de ativo.Efetue as seguintes entradas e pressione Enter:Empresa: <sua empresa>Imobilizado: <número principal do ativo para o qual você deseja criar um subativo>Incorporação posterior: <só necessário, se você desejar usar este registro mestre para lançar uma incorporação posterior> | A tela Criar subimobilizado é exibida.A guia Geral é exibida. |  |
| 4 | Inserir dados gerais | Na guia Geral, efetue as seguintes entradas:Denominação do imobilizado: <sua descrição do imobilizado>Unidade de medida: <unidade de medida>:Incorporado em: <sua data> |  |  |
| 5 | Dados dependentes de tempo | Clique na guia Dados dependentes de tempo. |  |  |
| 6 | WBS_Element ou centro de custo | Efetue, verifique ou adapte as seguintes entradas:Centro de custos: <seu centro de custoOu WBS_Element: <seu WBS_Element> |  |  |
| 7 | Verificar outras guias | Vá para as outras guias e faça as entradas ou modificações necessárias. | Todos os campos mestre do imobilizado necessários estão preenchidos. |  |
| 8 | Inserir, verificar ou adaptar parâmetros de depreciação | Se necessário, efetue ou ajuste as seguintes entradas para todas as áreas de depreciação disponíveis:ChaveD: <sua chave de depreciação>Nota Se você tiver ativado o Feature Toggle para o novo design, use o perfil de depreciação em vez da chave de depreciação.VidaÚtil: <sua vida útil em anos>Per: <sua vida útil em períodos> | Todos os parâmetros de depreciação necessários são atualizados corretamente. |  |
| 9 | Salvar novo subativo de ativo | Salve as entradas. | O subativo mestre do ativo é criado.O subativo começa com 1, por exemplo, xxxxx-1. |  |

### Documentos de modificação para registros mestre do imobilizado

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta atividade, você pode exibir todas as alterações anteriores de um registro de dados mestre do imobilizado existente (principal ou subnúmero).

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador de imobilizado. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar imobilizado(F3425A). | A tela Administrar ativos fixos é exibida. |  |
| 3 | Inserir informação sobre o imobilizado | Efetue as seguintes entradas e clique em Ir:Empresa: <sua empresa>Número do imobilizado: <seu número do imobilizado>Subnúmero do imobilizado: <seu subnúmero do imobilizado> | A tela Modificações dos registros mestre do imobilizado é exibida. |  |

### Chave de depreciação: Exibir detalhes

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta atividade, você pode exibir todas as alterações anteriores de um registro de dados mestre do ativo existente (principal ou subativo).

|  |
| --- |
| Nota Se você tiver ativado o Feature Toggle para o novo design, o app Chave de depreciação: exibir detalhes(FAA_DEPRKEY_SHOW) não será aplicável. |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador de imobilizado. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Chave de depreciação: exibir detalhes(FAA_DEPRKEY_SHOW). | O app é aberto. |  |
| 3 | Inserir informação sobre o imobilizado | Efetue as seguintes entradas e clique em Executar:Plano de avaliação: <Plano de avaliação>Chave de depreciação: <Chave de depreciação> | A tela Chave de depreciação <XXXX> no plano de avaliação <XXXX> é exibida.As configurações por trás da chave de depreciação selecionada são exibidas. |  |

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
- related-to :: [[03-financial-accounting-and-close/master-data-script-create-asset-bni-sap-s-4hana-cloud-public-edition-6]]
- related-to :: [[03-financial-accounting-and-close/mds-bni-613]]
- related-to :: [[03-financial-accounting-and-close/sap-s-4hana-cloud-public-edition-mds-bni-615]]
- related-to :: [[03-financial-accounting-and-close/script-de-datos-maestros-crear-activo-fijo-mds-bni-612]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNI_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 34,187 chars in the whole document
