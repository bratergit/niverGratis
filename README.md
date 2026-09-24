# Niver Grátis 🎁

App **open source** feito com [Streamlit](https://streamlit.io) que lista estabelecimentos que oferecem **cortesias, brindes e descontos para aniversariantes** — em várias cidades, redes nacionais e opções 100% online.

Com base na sua data de nascimento, o app calcula automaticamente **quais benefícios estão no período de resgate agora** (por exemplo, "2 dias antes até 4 dias depois do aniversário").

## O que você pode encontrar

- 🍻 Bares e restaurantes que dão drink, rodada de tequila, sobremesa ou até **R$ 100 no Pix** para o aniversariante.
- 🍿 Cinemas (Cinemark, Cinépolis, Cinesystem) com **combo ou ingresso de graça** no mês do aniversário.
- 🍫 Redes como Cacau Show, Outback, Starbucks, McDonald's, Burger King e muitas outras.
- 💄 Beleza (Sephora, Boticário, MAC), moda (Renner, Riachuelo, Arezzo) e farmácias.
- 🌐 Programas 100% online (Vai de Visa, Nespresso, e-commerce).

> ℹ️ **Outback já está na lista!** Procurou e não achou? Ele fica na aba **"Redes nacionais"**.
> Se um local da sua cidade ainda não estiver lá, **contribua** — veja como abaixo. 👇

## Como rodar

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/niverGratis.git
cd niverGratis
```

### 2. Instalar as dependências

Recomendado usar um ambiente virtual:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

### 3. Rodar o app

```bash
streamlit run app.py
```

O app será aberto no seu navegador em `http://localhost:8501`.

### Deploy grátis na nuvem

Você pode publicar o app gratuitamente no [Streamlit Community Cloud](https://streamlit.io/cloud) conectando este repositório — sem custo e sem precisar de servidor.

## Como funciona

- 🗂️ Todos os dados ficam em **`dados.json`** (um arquivo simples e legível, pronto para Pull Requests).
- 🐍 O `app.py` apenas lê esse arquivo e exibe os dados. **Para adicionar um local, você não precisa tocar no código.**
- 📍 Cada oferta tem uma **`cidade`**, permitindo que pessoas de várias localidades contribuam e filtrem pelo seu município.

## Como contribuir (Pull Request) 🚀

Quer ajuda? É muito simples. O projeto é aberto justamente para que a comunidade adicione cortesias das suas cidades.

### Passo a passo

1. **Fork** este repositório (botão *Fork* no GitHub).
2. **Edite o arquivo `dados.json`** adicionando (ou corrigindo) o item do estabelecimento.
3. **Valide o JSON** (veja abaixo).
4. **Abra um Pull Request** descrevendo o que você adicionou. Assim que aprovado, o app passa a exibir sua contribuição.

### Estrutura do arquivo `dados.json`

O arquivo tem um resumo no topo e uma lista `ofertas`, onde cada elemento é um estabelecimento/benefício. Os campos são:

| Campo | Obrigatório | Descrição |
|---|---|---|
| `nome` | ✅ | Nome do estabelecimento / oferta. |
| `categoria` | ✅ | Ex.: `Bar / Restaurante`, `Cinema`, `Beleza`, `Fast food`. |
| `tipo` | ✅ | `local` (um endereço específico), `rede` (franquia/rédea nacional) ou `online` (100% remoto). |
| `cidade` | ✅ | Cidade da oferta (`Uberlândia`, `São Paulo`, `Belo Horizonte`...). Para `rede` use `Nacional`; para `online` use `Online / Todo o Brasil`. |
| `uf` | ✅ | Sigla do estado (`MG`, `SP`...) ou `BR` para rede/online. |
| `brinde` | ✅ | O que o aniversariante ganha. |
| `como` | ✅ | Como resgatar (passo a passo). |
| `condicao` | ✅ | Condições (mínimo de pessoas, cadastro prévio, horário...). |
| `janela_antes` | ✅ | Quantos **dias antes** do aniversário a oferta começa a valer. `0` = só no dia. `-3` = 3 dias antes. |
| `janela_depois` | ✅ | Quantos **dias depois** do aniversário a oferta ainda vale. `0` = só no dia. `+4` = até 4 dias depois. |
| `quando` | ✅ | Descrição em texto do período (ex.: "No mês do aniversário"). |
| `local` | ✅ | Endereço/abrangência (ex.: "Av. Central, 100 - Centro" ou "Unidades da rede pelo Brasil"). |
| `link` | ✅ | Link/app/Instagram para conferir ou resgatar. |
| `nota` | ❌ | Observações extras (opcional). Pode deixar `""`. |

#### Exemplo de entrada (`tipo: local`)

```json
{
  "nome": "Exemplo Bar",
  "categoria": "Bar / Restaurante",
  "tipo": "local",
  "cidade": "Belo Horizonte",
  "uf": "MG",
  "brinde": "1 drink da casa + porção de batata grátis.",
  "como": "Ir ao local informando que é aniversariante.",
  "condicao": "A partir de 4 convidados pagantes, de terça a sábado.",
  "janela_antes": 0,
  "janela_depois": 0,
  "quando": "No dia",
  "local": "Rua das Flores, 123 - Savassi, Belo Horizonte/MG",
  "link": "Instagram: @exemplobar",
  "nota": ""
}
```

#### Exemplo de entrada (`tipo: rede` e `tipo: online`)

```json
{
  "nome": "Rede Exemplo (Clube Fidelidade)",
  "categoria": "Restaurante",
  "tipo": "rede",
  "cidade": "Nacional",
  "uf": "BR",
  "brinde": "Sobremesa grátis na semana do aniversário.",
  "como": "Cadastro gratuito no app; resgatar o voucher e apresentar documento na loja.",
  "condicao": "Membro ativo e consumo presencial.",
  "janela_antes": -3,
  "janela_depois": 3,
  "quando": "Na semana do aniversário",
  "local": "Unidades da rede pelo Brasil",
  "link": "App da rede",
  "nota": ""
}
```

> Para `tipo: online`, use `"cidade": "Online / Todo o Brasil"` e `"uf": "BR"`.

### Regras de ouro antes de abrir o PR

1. **Confirme a promoção** — de preferência com o próprio estabelecimento (Instagram/WhatsApp) ou em fonte oficial. Nada de boa informação errada. ✅
2. **Seja específico nas condições** — mínimo de pessoas, horário, necessidade de reserva, cadastro prévio.
3. **Use os campos `janela_antes` e `janela_depois`** corretamente — eles controlam o destaque **"RESGATE ATIVO AGORA"** do app.
4. **Valide o JSON** antes de enviar. Pode fazer com Python:

```bash
python -c "import json; json.load(open('dados.json', encoding='utf-8')); print('JSON válido ✔')"
```

5. Descreva no PR **o que** adicionou e **como verificou** a informação.

### Ideias de contribuição

- Adicionar mais cidades (bares, pizzarias e restaurantes locais).
- Corrigir endereços, horários ou condições desatualizadas.
- Adicionar novas redes nacionais que faltam.
- Reportar promoções encerradas em uma Issue.

## Licença

Distribuído sob a licença **MIT** — use, modifique, compartilhe e faça o que quiser, por qualquer pessoa, incluindo uso comercial. Veja o arquivo [`LICENSE`](LICENSE) para os detalhes.