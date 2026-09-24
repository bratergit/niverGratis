import json
import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="Niver Grátis", layout="wide")

ARQUIVO_DADOS = "dados.json"

CADASTRO_SUGESTAO = (
    "Dica: a maioria dos brindes exige cadastro gratuito no app/programa de fidelidade com "
    "a data de nascimento correta. Cadastre-se com 1 a 2 meses de antecedência e ative as "
    "notificações."
)


def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, encoding="utf-8") as f:
            dados = json.load(f)
    except FileNotFoundError:
        st.error(
            f"Não encontrei o arquivo '{ARQUIVO_DADOS}'. Verifique se ele está na mesma "
            "pasta do app.py."
        )
        return {"atualizado_em": "", "ofertas": []}
    except json.JSONDecodeError as exc:
        st.error(f"Erro ao ler '{ARQUIVO_DADOS}': {exc}")
        return {"atualizado_em": "", "ofertas": []}
    return dados


def _ocorrencias(aniversario: date, hoje: date):
    b1 = aniversario.replace(year=hoje.year)
    b0 = aniversario.replace(year=hoje.year - 1)
    b2 = aniversario.replace(year=hoje.year + 1)
    return b0, b1, b2


def ativo(offer, aniversario: date, hoje: date):
    b0, b1, b2 = _ocorrencias(aniversario, hoje)
    antes, depois = offer["janela_antes"], offer["janela_depois"]
    for b in (b0, b1, b2):
        if b + timedelta(days=antes) <= hoje <= b + timedelta(days=depois):
            return True
    return False


def campos_atuais(offer, aniversario: date, hoje: date):
    b0, b1, b2 = _ocorrencias(aniversario, hoje)
    antes, depois = offer["janela_antes"], offer["janela_depois"]
    janelas = sorted(
        [(b + timedelta(days=antes), b + timedelta(days=depois)) for b in (b0, b1, b2)],
        key=lambda p: p[0],
    )
    for s, e in janelas:
        if s <= hoje <= e:
            return "Período de resgate ATIVO", s, e
    for s, e in janelas:
        if hoje < s:
            return "Ainda não começou", s, e
    return "Fora do período", None, None


def dias_ate(date1: date, date2: date):
    return (date2 - date1).days


def render(offer, aniversario: date, hoje: date, incluir_ativo):
    status, ini, fim = campos_atuais(offer, aniversario, hoje)
    is_ativo = status == "Período de resgate ATIVO"
    if incluir_ativo and not is_ativo:
        return
    if is_ativo:
        badge = ":green[**RESGATE ATIVO AGORA**]"
    elif status == "Ainda não começou":
        badge = f":orange[**{status}**]"
    else:
        badge = f":gray[**{status}**]"

    per = ""
    if ini and fim:
        per = f"Período: {ini.strftime('%d/%m/%Y')} a {fim.strftime('%d/%m/%Y')}"

    cidade = offer.get("cidade", "")
    cidade_txt = f" | Cidade: {cidade}" if cidade else ""

    with st.expander(f"{offer['nome']}  -  {badge}", expanded=is_ativo):
        st.markdown(f"**O que ganha:** {offer['brinde']}")
        st.markdown(f"**Como resgatar:** {offer['como']}")
        st.markdown(f"**Condições:** {offer['condicao']}")
        st.markdown(f"**Quando vale:** {offer['quando']}")
        st.markdown(f"**Local:** {offer['local']}")
        st.markdown(f"**Canal:** {offer['link']}")
        st.caption(cidade_txt)
        if per:
            st.markdown(f"{per}")
        if offer.get("nota"):
            st.caption(offer["nota"])


def main():
    dados = carregar_dados()
    TODOS = dados.get("ofertas", [])
    LOCAIS = [o for o in TODOS if o["tipo"] == "local"]
    REDES = [o for o in TODOS if o["tipo"] == "rede"]
    ONLINE = [o for o in TODOS if o["tipo"] == "online"]
    CATEGORIAS = sorted({o["categoria"] for o in TODOS})
    CIDADES = sorted({o.get("cidade") for o in LOCAIS if o.get("cidade")})

    st.title("Niver Grátis 🎁")
    st.markdown(
        "Escolha sua data de nascimento e descubra os locais que presenteiam aniversariantes "
        "na **sua cidade**, em **redes nacionais** e em opções **100% online/remotas**."
    )

    with st.sidebar:
        st.header("Seu aniversário")
        nasc = st.date_input("Data de nascimento", value=date(1990, date.today().month, date.today().day))
        st.caption(CADASTRO_SUGESTAO)

        st.header("Filtros")
        cidades_sel = st.multiselect(
            "Cidades (locais)",
            CIDADES,
            default=CIDADES,
            help="Selecione as cidades dos locais presenciais. Redes nacionais e opções online sempre aparecem.",
        )
        tipo_map = {
            "Todos": "todos",
            "Locais (presencial)": "local",
            "Redes nacionais": "rede",
            "Online / Remoto": "online",
        }
        escolha = st.radio("Tipo", list(tipo_map.keys()))
        categoria = st.multiselect("Categoria", CATEGORIAS, default=[])
        so_ativos = st.checkbox("Mostrar apenas benefícios ativos agora", value=False)

    locais_filtrados = [o for o in LOCAIS if o.get("cidade") in cidades_sel]
    grupos = {"local": locais_filtrados, "rede": REDES, "online": ONLINE}
    lista = grupos[tipo_map[escolha]] if escolha != "Todos" else locais_filtrados + REDES + ONLINE
    if categoria:
        lista = [o for o in lista if o["categoria"] in categoria]

    hoje = date.today()
    b0, b1, b2 = _ocorrencias(nasc, hoje)
    proximo = b1 if b1 >= hoje else b2
    dias = dias_ate(hoje, proximo)
    faz = proximo.year - nasc.year
    ultimo = min([b for b in (b0, b1, b2) if b <= hoje], key=lambda b: hoje - b)

    st.info(
        f"Hoje: {hoje.strftime('%d/%m/%Y')}  |  Próximo aniversário: {proximo.strftime('%d/%m/%Y')} "
        f"({dias} dia(s) - você fará {faz} anos)  |  Último aniversário: {ultimo.strftime('%d/%m/%Y')}"
    )

    ativos = [o for o in lista if ativo(o, nasc, hoje)]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Benefícios ativos agora", len(ativos))
    c2.metric("Total na seleção", len(lista))
    c3.metric("Locais (presencial)", len(locais_filtrados))
    c4.metric("Redes nacionais", len(REDES))

    st.write("")

    tab1, tab2, tab3 = st.tabs(
        [
            "Locais (presencial)",
            "Redes nacionais",
            "Online / Remoto",
        ]
    )

    with tab1:
        sel = [o for o in locais_filtrados if o in lista]
        if not sel:
            st.write("Nenhuma oferta neste filtro. Ajuste os filtros de cidade ou tipo.")
        for o in sel:
            render(o, nasc, hoje, so_ativos)

    with tab2:
        sel = [o for o in REDES if o in lista]
        if not sel:
            st.write("Nenhuma oferta neste filtro.")
        for o in sel:
            render(o, nasc, hoje, so_ativos)

    with tab3:
        sel = [o for o in ONLINE if o in lista]
        if not sel:
            st.write("Nenhuma oferta neste filtro.")
        for o in sel:
            render(o, nasc, hoje, so_ativos)

    st.divider()
    st.subheader("Plano de caça aos brindes")
    st.markdown(
        "1. **Cadastre-se com antecedência** (1 a 2 meses) nos apps/programas abaixo com CPF e data de nascimento corretos.\n"
        "2. **Ative as notificações** para receber o voucher/cupom no momento certo.\n"
        "3. **Resgate no período indicado** de cada oferta - muitos são válidos só por alguns dias.\n"
        "4. **Confirme com o estabelecimento** antes de sair de casa, pois regras mudam com frequência.\n"
        "5. Combine benefícios: você pode resgatar diversos presentes no mesmo mês."
    )

    st.divider()
    st.subheader("Quer contribuir? 🚀")
    st.markdown(
        "Este projeto é **colaborativo e open source**. Se você conhece um local que dá cortesia "
        "para aniversariantes, basta editar o arquivo **`dados.json`** e abrir um **Pull Request**.\n"
        "O app carrega tudo a partir desse arquivo - não precisa mexer no código!\n"
        f"Base de dados atualizada em: **{dados.get('atualizado_em', 'não informado')}**.\n"
        "Veja o **`README.md`** para o passo a passo completo de como contribuir."
    )

    st.divider()
    st.caption(
        "Aviso: as promoções são informativas e podem mudar ou ser encerradas a qualquer momento pelas marcas. "
        "Confirme sempre as condições atualizadas no app/site oficial e com o estabelecimento. "
        "Informações compiladas com base em fontes públicas (2025-2026)."
    )


if __name__ == "__main__":
    main()