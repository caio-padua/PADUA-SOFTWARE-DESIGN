# DICIONÁRIO PADAXOR — Termos Técnicos com Número Permanente

> **Regra central:** o número é identidade permanente.
> `(*3)` significa *API* hoje e daqui a dois anos. Nunca se reordena, nunca se reaproveita.
> Termo novo entra sempre no final — recebe o próximo número livre.

## Como ler

| Coluna | O que contém |
| --- | --- |
| **Nº** | Número permanente. Aparece como `(*N)` nas mensagens do Slack e Telegram. |
| **Termo** | A palavra técnica exata, como aparece no código e nas mensagens. |
| **Tradução** | O que o termo significa formalmente, em português direto. (`oque_e` no JSON) |
| **Analogia Clínica** | A mesma ideia explicada com o mundo da clínica — para o CEO entender. (`leigo` no JSON) |

## Dicionário completo

| Nº | Termo | Tradução | Analogia Clínica |
| --- | --- | --- | --- |
| (1) | **AI Gateway** | Ponto unico por onde passa toda chamada de IA, contando o consumo. | E a caixa de energia na frente da casa: nada consome sem passar pelo medidor. |
| (2) | **Anthropic** | Empresa que faz o Claude, o modelo de IA usado para raciocinio. | E um dos laboratorios de onde vem a inteligencia que o sistema usa. |
| (3) | **API** | Interface de Programacao de Aplicacoes. O conjunto de portas por onde um programa pede coisas a outro. | E o balcao de atendimento de um laboratorio. Voce nao entra no laboratorio: chega no balcao, entrega o pedido, recebe o resultado. A API e o balcao, e cada guiche e uma rota. |
| (4) | **append-only** | Registro em que se acrescenta linha, nunca se apaga nem se corrige linha antiga. | E o prontuario do paciente. Voce nao apaga a evolucao de ontem: escreve a de hoje embaixo. Se errou ontem, escreve hoje que errou. O erro fica registrado, e e isso que da valor legal. |
| (5) | **backup** | Copia dos dados guardada separada do original, para restaurar se o original se perder. | E o seguro do carro. Custa todo mes e parece dinheiro jogado fora, ate o dia da batida. |
| (6) | **banco de dados** | Programa que guarda os dados de forma organizada e permite buscar rapido. | E o arquivo de fichas da clinica, mas que responde em um centesimo de segundo e nunca perde uma ficha por descuido. |
| (7) | **branch** | Copia paralela do codigo onde se trabalha sem mexer na versao que esta no ar. | E a via de um exame: voce faz o rascunho da conduta numa folha separada antes de escrever no prontuario oficial. Se der errado, joga a folha fora e o prontuario continua intacto. |
| (8) | **CI/CD** | Robo que roda os testes sozinho a cada mudanca e barra o que quebrou antes de publicar. | E a conferencia dupla da enfermagem antes de aplicar a medicacao. Ninguem confia so na memoria de quem preparou. |
| (9) | **circuit breaker** | Trava que interrompe antes de gastar, quando o cliente nao tem saldo. | E o disjuntor do quadro: corta antes de queimar. |
| (10) | **clone** | Copia do sistema entregue a uma clinica que licenciou. | E uma franquia: mesma placa, dono diferente, cozinha propria. |
| (11) | **CNAME** | Tipo de registro de endereco na internet que diz 'este nome aponta para aquele outro nome'. | E o encaminhamento de telefone: quem liga para o numero antigo cai automaticamente no novo, sem saber que foi encaminhado. |
| (12) | **commit** | Um pacote de mudancas no codigo, com autor, data e explicacao, gravado de forma permanente. | E uma entrada assinada no prontuario: quem escreveu, quando, e o que mudou. Nao se apaga. |
| (13) | **conector** | Ponte pronta entre o sistema e um servico de fora. | E a tomada: voce nao refaz a fiacao da rua, so pluga. |
| (14) | **CORS** | Regra que diz quais sites tem permissao de chamar o seu servidor. | E a lista da portaria do predio: so sobe quem esta na lista. Sem a lista certa, ate o morador fica na calcada. |
| (15) | **cron** | Programa que dispara uma acao em horario marcado, sozinho. | E o despertador do sistema: voce marca a hora, ele toca sem ninguem lembrar. |
| (16) | **deploy** | Levar o codigo do computador do programador para o servidor onde o cliente usa. | E a diferenca entre escrever a receita no bloco e entregar na mao do paciente. Enquanto nao entregou, nao existe para ele. |
| (17) | **DKIM** | Assinatura digital que prova que o e-mail saiu mesmo do dominio que diz ter saido. | E o carimbo e a assinatura no receituario. Sem eles, a farmacia trata como falsificacao. |
| (18) | **DNS** | Sistema que traduz um nome como padaxor.com.br no endereco numerico real do servidor. | E a lista telefonica: voce sabe o nome da pessoa, e ela devolve o numero. Ninguem decora o numero. |
| (19) | **dry-run** | Rodar mostrando o que ACONTECERIA, sem fazer. | E o ensaio da cirurgia: todo mundo faz os gestos, ninguem corta. |
| (20) | **empresa_id** | Coluna que amarra cada registro a uma clinica. | E o numero do prontuario: e o que diz de quem e aquela ficha. |
| (21) | **endpoint** | Um endereco especifico da API que faz uma coisa so. | E o guiche especifico dentro do balcao: um guiche para entregar exame, outro para retirar resultado. |
| (22) | **FK** | Coluna que amarra uma linha de uma tabela a uma linha de outra tabela. | E o numero do prontuario escrito no pedido de exame: e o que amarra aquele exame aquele paciente e nao a outro. |
| (23) | **Gemini** | Modelo de IA do Google, usado para ler documento e imagem. | Outro laboratorio, melhor em enxergar imagem e PDF. |
| (24) | **hash** | Numero unico calculado a partir de um conteudo. Mudou uma virgula no conteudo, o numero muda inteiro. | E a impressao digital de um documento. Duas pessoas nao tem a mesma, e a sua nao muda sozinha. Se o documento foi adulterado, a impressao digital nao bate mais. |
| (25) | **idempotente** | Operacao que pode ser repetida quantas vezes for e o resultado final e sempre o mesmo. | E apertar o botao do elevador. Apertar dez vezes nao chama dez elevadores: o andar continua marcado uma vez so. |
| (26) | **indice unico** | Regra do banco que impede dois registros de terem o mesmo valor num campo. | E o CPF: o cartorio nao deixa dois cadastros com o mesmo numero. A regra vive no cartorio, nao na boa vontade de quem preenche. |
| (27) | **ledger** | Registro permanente de cada evento cobravel. | E o livro-caixa: cada linha e uma coisa que aconteceu e vale dinheiro. |
| (28) | **login_username** | O campo pelo qual cada pessoa se identifica ao entrar. | E o seu nome na portaria: a senha prova que e voce, o usuario diz quem voce diz ser. |
| (29) | **main** | A ramificacao oficial do codigo, a que esta valendo de verdade. | E o prontuario oficial, nao o rascunho. O que nao esta nele, oficialmente nao aconteceu. |
| (30) | **merge** | Juntar o trabalho de duas ramificacoes num so. | E juntar as anotacoes de dois medicos sobre o mesmo paciente num prontuario unico. |
| (31) | **middleware** | Codigo que fica no meio do caminho de toda chamada e decide se ela passa. | E o porteiro do predio: toda visita passa por ele antes de chegar no apartamento, e ele decide quem sobe. |
| (32) | **migration** | Script que muda a estrutura do banco de dados de forma controlada e registrada. | E a reforma da clinica com planta aprovada e registrada, em vez de derrubar parede no impulso. |
| (33) | **mock** | Dado ou resposta falsa usada so para testar, no lugar do dado real. | E o manequim de treinamento. Serve para ensaiar, e e perigoso se alguem esquecer e tratar como paciente. |
| (34) | **multi-tenant** | Um mesmo sistema atendendo varios clientes com os dados separados entre si. | E um predio de consultorios: mesma estrutura, mesmo elevador, mas cada sala tem chave propria e ninguem entra na do outro. |
| (35) | **OpenAI** | Empresa do GPT e do Whisper, usada para texto e transcricao de voz. | Um terceiro laboratorio, forte em transcrever audio. |
| (36) | **PR** | Pedido formal para juntar um trabalho na versao oficial, com espaco para revisao antes. | E o pedido de parecer antes da cirurgia. Alguem olha, comenta, e so depois entra. |
| (37) | **PWA** | Site que se comporta como aplicativo de celular, com icone na tela inicial e uso sem internet. | E um aparelho que serve de dois jeitos: no consultorio parece bancada, na mao vira portatil. Mesmo aparelho. |
| (38) | **RBAC** | Regra que define o que cada tipo de usuario pode ver e fazer. | E a diferenca entre medico, enfermeiro e recepcao no sistema da clinica: cada um ve a tela do seu papel. |
| (39) | **repositorio** | O lugar onde o codigo mora, com todo o historico de quem mudou o que e quando. | E o arquivo morto da clinica, mas em que nada se perde e da para voltar a qualquer dia do passado. |
| (40) | **RLS** | Trava dentro do proprio banco que impede um cliente de ler a linha de outro, mesmo com erro do programador. | E a tranca da porta da sala, nao o aviso 'por favor nao entre'. O aviso depende da boa vontade; a tranca nao. |
| (41) | **scrypt** | Metodo de embaralhar a senha de um jeito que nao se desfaz, para guardar sem saber qual e. | E guardar a impressao digital do paciente em vez do dedo dele. Da para conferir se bate, mas ninguem reconstroi o dedo a partir dela. |
| (42) | **SPF** | Registro que diz quais servidores tem permissao de mandar e-mail em nome do seu dominio. | E a lista de quem pode assinar receita em nome da clinica. Sem ela, qualquer um assina. |
| (43) | **SSE** | Tecnica em que o servidor avisa a tela sozinho quando algo muda, sem a tela ficar perguntando. | E o monitor de sinais vitais: ele avisa quando muda, voce nao fica olhando de minuto em minuto. |
| (44) | **token** | Codigo temporario que prova quem voce e depois que voce ja fez o login. | E a pulseira do hospital. Voce se identifica uma vez na recepcao e depois so mostra a pulseira em cada setor. |
| (45) | **UPSERT** | Operacao que grava o registro se ele nao existe, e atualiza se ja existe. | E abrir ficha se o paciente e novo, ou atualizar a que ja existe se ele ja veio antes. Uma decisao so, automatica. |
| (46) | **webhook** | Chamada que um sistema faz no outro sozinho quando um evento acontece. | E o laboratorio que liga para voce quando o resultado critico sai, em vez de voce ligar de hora em hora perguntando. |
| (47) | **worker** | Processo que roda separado do servidor principal, sem atender ninguem diretamente. | E o funcionario dos fundos: nao atende no balcao, faz o servico que leva tempo. |
| (48) | **JWT** | JSON Web Token — credencial digital assinada que prova identidade sem consultar o banco a cada pedido. | É a pulseira com QR-code da festa VIP: você mostra na entrada e entra em qualquer área permitida sem fila. |
| (49) | **tenant** | Empresa ou clínica que opera o sistema de forma isolada dentro da mesma instalação. | É um apartamento no prédio: mesma estrutura física, porta separada, mobília própria, vizinho não acessa. |
| (50) | **cron job** | Tarefa agendada que o sistema executa sozinho em horário determinado, sem intervenção humana. | É o funcionário que toda sexta às 18h fecha o caixa automaticamente — não precisa ninguém mandar. |
| (51) | **schema** | Definição formal da estrutura do banco: quais tabelas existem, quais colunas cada uma tem e de que tipo. | É a planta baixa da clínica: define onde fica cada sala, quantas portas tem, o que cabe em cada cômodo. |
| (52) | **buffer** | Área de memória temporária que armazena dados em trânsito enquanto aguardam processamento. | É a sala de espera antes do consultório: o paciente chega, espera, e é chamado na ordem. |
| (53) | **pipeline** | Sequência de etapas encadeadas onde a saída de uma vira entrada da próxima. | É a linha de montagem da farmácia de manipulação: pesa, mistura, encapsula, rotula — em ordem fixa. |
| (54) | **royalty** | Percentual pago ao detentor da licença cada vez que o produto é vendido ou usado. | É a comissão do médico que assina o protocolo: toda vez que a clínica licenciada aplica, ele recebe. |
| (55) | **UUID** | Identificador Único Universal — número gerado de forma que a probabilidade de repetição é astronomicamente baixa. | É o CPF do registro: nunca se repete, não depende de nenhum contador central. |
| (56) | **seed** | Conjunto de dados iniciais inseridos no banco na primeira vez que o sistema sobe, para funcionar de imediato. | É o estoque inicial de uma farmácia recém-aberta: sem ele, o sistema existe mas não tem nada para vender. |
| (57) | **mimeType** | Identificador padronizado que diz ao computador que tipo de conteúdo um arquivo ou resposta contém. | É a etiqueta do frasco de medicamento: diz se é comprimido, líquido ou pomada antes de abrir. |
| (58) | **proxy** | Intermediário que recebe pedidos de um lado e os repassa ao outro, podendo filtrar, logar ou modificar. | É o corretor de imóveis: você fala com ele, ele fala com o proprietário — ninguém se fala diretamente. |
| (59) | **OAuth** | Protocolo que permite que um sistema acesse recursos de outro em nome do usuário, sem receber a senha. | É dar a chave do carro ao manobrista: ele move o carro, mas não tem acesso à sua casa nem ao cofre. |
| (60) | **env var** | Variável de ambiente — valor de configuração armazenado fora do código, injetado no momento da execução. | É o cofre da clínica: a senha fica lá, não escrita no protocolo público. |
| (61) | **pull** | Operação que baixa as mudanças do repositório remoto para a cópia local de trabalho. | É sincronizar a agenda do Google: você puxa as consultas novas que outra pessoa adicionou. |
| (62) | **repo** | Repositório — diretório versionado com todo o histórico de alterações do código. | É o prontuário completo do sistema: cada mudança está lá, assinada, datada e reversível. |
| (63) | **fail-safe** | Mecanismo que garante que uma falha parcial não provoque falha total ou perda de dados. | É o gerador de emergência da UTI: se a rede cair, o monitor de sinais vitais continua ligado. |
| (64) | **spec** | Documento de especificação escrito antes do código, que define o que deve ser construído e por quê. | É a prescrição antes da manipulação: o médico escreve o que quer antes de a farmácia produzir. |
| (65) | **tenant context** | Estrutura que carrega as informações da clínica ativa em uma requisição (ID, nome, configurações). | É o crachá do plantonista: diz em qual hospital ele está naquele turno, quais salas pode acessar. |
| (66) | **ai_usage_log** | Tabela do banco que registra cada chamada de IA: modelo, tokens enviados, tokens recebidos, custo. | É o livro-caixa de exames terceirizados: cada pedido ao laboratório externo fica registrado com o custo. |
| (67) | **logAiUsage** | Função que grava automaticamente no ai_usage_log após cada chamada de IA. | É o carimbo automático da balança: todo peso registrado ganha carimbo de data e hora sem ninguém pedir. |
| (68) | **requireCeoInstance** | Middleware que bloqueia a rota para qualquer requisição que não venha da instância do CEO. | É a catraca do andar executivo: não adianta ter crachá de funcionário, precisa do crachá de diretor. |
| (69) | **PADAXOR_AI_BYPASS** | Variável de ambiente que identifica a instância do CEO e libera acesso às rotas de plataforma. | É o crachá master do dono do prédio: abre qualquer porta, inclusive as que o gerente não alcança. |
| (70) | **tenantContext** | Objeto TypeScript injetado pelo middleware com empresa_id, nome e configurações da clínica ativa. | É a pasta do plantonista: ao entrar no turno, ele recebe a pasta da clínica — dados daquele dia, daquele lugar. |
| (71) | **Slack** | Plataforma de comunicação corporativa com canais por tema, integrações e histórico pesquisável. | É o WhatsApp do trabalho: cada assunto tem seu grupo, mas a empresa controla o que fica gravado. |
| (72) | **Drive** | Google Drive — serviço de armazenamento na nuvem com compartilhamento e controle de acesso. | É o arquivo físico da clínica, mas na nuvem: qualquer médico autorizado acessa de qualquer lugar. |
| (73) | **Sheets** | Google Planilhas — planilha online colaborativa com API programática. | É a ficha de controle do estoque que todos veem ao mesmo tempo, sem precisar mandar e-mail com anexo. |
| (74) | **Cloudflare** | Empresa de infraestrutura de internet que oferece CDN, proteção contra ataques e AI Gateway. | É a portaria do prédio com câmera, identificação e lista de visitantes: nenhum pacote entra sem ser conferido. |
| (75) | **Railway** | Plataforma de deploy que executa o servidor do PADAXOR 24 horas na internet com banco de dados integrado. | É o data center terceirizado: você coloca o servidor lá, eles garantem a luz, o ar-condicionado e o acesso. |
| (76) | **Replit** | Ambiente de desenvolvimento online onde o código é escrito, testado e iterado em tempo real. | É o consultório de desenvolvimento: onde o médico estuda o caso antes de escrever a prescrição final. |
| (77) | **token (IA)** | Unidade de texto usada pelas IAs para medir o tamanho do que leram e do que responderam. | É como a IA cobra por palavra: não exatamente por palavra, mas é a unidade de conta — ~0,75 palavra em português. |
| (78) | **input_tokens** | Quantidade de tokens no texto enviado para a IA processar (pergunta + contexto + histórico). | É o número de páginas do prontuário que você entregou para o consultor ler antes de dar o parecer. |
| (79) | **output_tokens** | Quantidade de tokens no texto que a IA gerou como resposta. | É o número de páginas do laudo que o consultor escreveu depois de ler o prontuário. |
| (80) | **P0** | Prioridade zero — item crítico que impede o sistema de funcionar. Bloqueia tudo até ser resolvido. | É o paciente que chega em PCR: vai direto para a ressuscitação, fila não existe. |
| (81) | **P1** | Prioridade 1 — item de alta urgência que impacta o uso diário mas não paralisa o sistema. | É o paciente com dor intensa: não está em risco imediato de vida, mas não pode esperar. |
| (82) | **P2** | Prioridade 2 — item importante, entra no próximo ciclo de trabalho sem urgência imediata. | É o exame de rotina com resultado alterado: importante resolver, mas não hoje de manhã. |
| (83) | **P3** | Prioridade 3 — melhoria desejável que não bloqueia nada. Entra no backlog. | É a pintura da sala de espera: fica melhor, mas o consultório funciona sem ela. |
| (84) | **cron horário** | Cron job configurado para disparar no início de cada hora, todos os dias. | É o residente que bate na porta a cada hora para checar o pós-operatório — pontual, sem precisar de chamado. |
| (85) | **planilha de produção** | Documento Google Sheets que lista todas as tarefas do projeto com número, descrição e estado. | É o quadro de cirurgias do centro cirúrgico: todo mundo vê o que está agendado, em andamento e concluído. |
| (86) | **What & Why** | Seção obrigatória do plano de tarefa que descreve o problema a resolver e a motivação — por que existe, qual dor resolve. | É a primeira linha do prontuário: "paciente de 55 anos, hipertenso, veio por dor torácica". Sem ela, ninguém sabe por que está tratando. |
| (87) | **Done looks like** | Seção do plano que define outcomes observáveis e concretos — o que o usuário vê quando a tarefa está concluída, não detalhes de código. | É o critério de alta: "paciente recebe alta quando saturação acima de 95% em ar ambiente por 24h". Sem critério claro, ninguém sabe quando parar. |
| (88) | **Out of scope** | Seção que delimita explicitamente o que NÃO está incluído na tarefa — evita escopo inflado e trabalho não pedido. | É a contra-indicação do protocolo: o que não vai ser feito nesta sessão, para ninguém esperar o que não foi prometido. |
| (89) | **Steps** | Seção do plano com passos numerados de implementação para o executor — o que construir, em que ordem, sem código inline. | É o protocolo de manipulação da farmácia: passo 1, pese o ativo; passo 2, dissolva; passo 3, filtre. Sem ordem, resulta em erro. |
| (90) | **Relevant files** | Seção final do plano com caminhos exatos dos arquivos do repositório que o executor deve ler antes de começar a modificar. | É o índice do prontuário que aponta exatamente onde está cada resultado de exame, sem precisar folhear tudo. |
| (91) | **TTS** | Text-to-Speech — síntese de voz que converte texto em áudio falado. No Guia Digital usa a Web Speech API nativa do navegador. | É a recepcionista que lê em voz alta o nome do paciente: você não precisa enxergar o painel para saber que chegou a sua vez. |
| (92) | **Web Speech API** | API nativa dos navegadores modernos para síntese de voz (TTS) e reconhecimento de fala (STT) — zero custo, zero API externa. | É o microfone e o alto-falante que o navegador já tem instalados — sem precisar instalar mais nada. |
| (93) | **onboarding digital** | Processo estruturado de cadastro, configuração e integração inicial do paciente na plataforma — instalar PWA, entrar na área, vincular Telegram. | É a consulta de boas-vindas onde você explica ao paciente como funciona a clínica, o app e como chegar na próxima vez. |
| (94) | **rate limiting** | Controle de taxa que impede múltiplas chamadas idênticas num intervalo curto — protege APIs de disparo duplo ou loop acidental. | É o intervalo mínimo entre aplicações: não importa quantas vezes o médico clicar, a segunda dose não sai antes do prazo. |
| (95) | **funil de onboarding** | Sequência de etapas mensuráveis de um processo com registro de onde o usuário avança ou abandona — identifica gargalos. | É o acompanhamento da triagem: sabe quantos pacientes vieram ao pronto-socorro, quantos foram avaliados e quantos internaram. |
| (96) | **QR Code** | Quick Response Code — matriz bidimensional de pontos que codifica uma URL ou dado, lida instantaneamente pela câmera sem app especial. | É o código de barras moderno que a câmera do celular lê em um segundo — como um atalho impresso no papel que leva direto ao site. |

*Total: **96** termos. Próximo número livre: **97***

---

_Gerado automaticamente por `dicionario/gerar_md.py`._
_Para adicionar termos: edite `dicionario/dicionario.json` e rode este script._
_Nunca edite este arquivo manualmente — as mudanças serão sobrescritas._
