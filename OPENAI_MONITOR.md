# Monitor de Astra e novos modelos da OpenAI

Este monitor executa **a cada hora** e só abre uma issue quando encontra uma
novidade relevante sobre Astra ou outro novo modelo para ChatGPT, Codex ou API.

## Ordem de prioridade

1. OpenAI News, notas de lançamento, documentação e perfis oficiais no X.
2. Sam Altman, Greg Brockman, Mark Chen e Alexander Embiricos.
3. Imprensa com histórico verificável e posts recentes de r/OpenAI, r/ChatGPT e
   r/singularity que apresentem evidência.

A primeira execução cria uma linha de base silenciosa. O estado persistido em
`.openai-monitor-state.json` evita alertas repetidos. Falhas transitórias de uma
fonte não geram notificação. Quando houver confirmação oficial, o título começa
com `🚨 LANÇAMENTO/ANÚNCIO DO NOVO MODELO DETECTADO`.

Os alertas são issues atribuídas a `andradergabriel`, portanto aparecem nas
notificações do GitHub. Não há necessidade de cadastrar chaves adicionais.
