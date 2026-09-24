import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="Niver Grátis - Uberlândia", layout="wide")

CADASTRO_SUGESTAO = (
    "Dica: a maioria dos brindes exige cadastro gratuito no app/programa de fidelidade com "
    "a data de nascimento correta. Cadastre-se com 1 a 2 meses de antecedência e ative as "
    "notificações."
)

LOCAIS = [
    {
        "nome": "Tinin's Bar",
        "categoria": "Bar / Restaurante",
        "tipo": "local",
        "brinde": "Combo de brindes: drink da casa, porção de batata, petit gateau e rodada de tequila (10 doses) de ter a qui; sex/sab ganha batata frita + rodada de tequila.",
        "como": "Comparecer com grupo de convidados e informar que é aniversariante (roupa de aniversariante ajuda).",
        "condicao": "A partir de 4 convidados no grupo. Ter a sab, das 18h as 01h.",
        "janela_antes": 0,
        "janela_depois": 0,
        "quando": "No dia (aniversariante da semana em alguns casos)",
        "local": "Av. Ana Godoy de Souza, 1640 - Santa Monica, Uberlandia/MG",
        "link": "Instagram: @tinins.bar",
        "nota": "Considerado o bar com mais brindes para aniversariantes de Uberlandia; parceiro do Folks e Pub Sertanejo.",
    },
    {
        "nome": "Bullteco",
        "categoria": "Bar / Restaurante",
        "tipo": "local",
        "brinde": "Entrada free, 5 cervejas por R$ 9 cada, 20% off em porcoes + 1 caipirinha de limao.",
        "como": "Fazer reserva para o grupo e avisar que e aniversariante.",
        "condicao": "Reserva minima de 10 pessoas.",
        "janela_antes": 0,
        "janela_depois": 0,
        "quando": "No dia",
        "local": "Uberlandia/MG (confira o endereco no Instagram)",
        "link": "Instagram: @bullteco",
        "nota": "",
    },
    {
        "nome": "D'Gusta Beer",
        "categoria": "Bar",
        "tipo": "local",
        "brinde": "R$ 100 no Pix na hora para o aniversariante.",
        "como": "Levando 10 convidados e apresentando documento com foto.",
        "condicao": "Reserva obrigatoria.",
        "janela_antes": 0,
        "janela_depois": 0,
        "quando": "No dia",
        "local": "Uberlandia/MG (confira no Instagram)",
        "link": "Instagram: @dgusttabeer",
        "nota": "",
    },
    {
        "nome": "Amaretto Gourmet (Fundinho)",
        "categoria": "Restaurante",
        "tipo": "local",
        "brinde": "Aniversariante nao paga o buffet.",
        "como": "Levar 15 convidados que consumam o buffet.",
        "condicao": "Reserva obrigatoria.",
        "janela_antes": 0,
        "janela_depois": 0,
        "quando": "No dia",
        "local": "Funcionario de Deus - Uberlandia/MG",
        "link": "Instagram: @amarettogourmet",
        "nota": "",
    },
    {
        "nome": "Todo Dia Garage",
        "categoria": "Bar / Restaurante",
        "tipo": "local",
        "brinde": "1 drink Garage Rainbow + cone de nuggets + rodada de tequila para a mesa.",
        "como": "Reservar mesa informando que e aniversariante.",
        "condicao": "Reserva a partir de 5 pessoas.",
        "janela_antes": 0,
        "janela_depois": 0,
        "quando": "No dia",
        "local": "Uberlandia/MG (confira no Instagram)",
        "link": "Instagram: @tododiagarage",
        "nota": "",
    },
    {
        "nome": "Neiva Bar",
        "categoria": "Bar",
        "tipo": "local",
        "brinde": "R$ 100 de consumacao para o aniversariante.",
        "como": "Levando 10 pagantes na Mesa de Boteco.",
        "condicao": "Valido seg a sab, das 19h as 23h.",
        "janela_antes": 0,
        "janela_depois": 0,
        "quando": "No dia",
        "local": "Uberlandia/MG (confira no Instagram)",
        "link": "Instagram: @neivabaroficial",
        "nota": "",
    },
    {
        "nome": "Santa Cana (Santacarne Udi)",
        "categoria": "Bar / Restaurante",
        "tipo": "local",
        "brinde": "Aniversariante e open de graca + 1 dose de Licor 43.",
        "como": "Levar 7 convidados pagantes.",
        "condicao": "Confirme as condicoes atuais com o estabelecimento.",
        "janela_antes": 0,
        "janela_depois": 0,
        "quando": "No dia",
        "local": "Uberlandia/MG (confira no Instagram)",
        "link": "Instagram: @santacarneudi",
        "nota": "",
    },
    {
        "nome": "Espeto Imperial",
        "categoria": "Bar / Restaurante",
        "tipo": "local",
        "brinde": "Condicao especial para aniversariante (confirme a regra atual).",
        "como": "Combinar com o estabelecimento ao reservar.",
        "condicao": "Confirme via Instagram.",
        "janela_antes": 0,
        "janela_depois": 0,
        "quando": "No dia",
        "local": "Uberlandia/MG",
        "link": "Instagram: @espetoimperialudia",
        "nota": "",
    },
    {
        "nome": "Mr. Dough",
        "categoria": "Hamburgueria / Pub",
        "tipo": "local",
        "brinde": "Aniversariante da semana gira a roleta premiada: drinks, sobremesa de aniversario ou desconto na conta.",
        "como": "Ir no local, sem entrada, durante a semana de aniversario.",
        "condicao": "Confirme as regras da semana com a casa.",
        "janela_antes": -3,
        "janela_depois": 3,
        "quando": "Aniversariante da semana",
        "local": "Av. Francisco Galassi, 790, Uberlandia/MG",
        "link": "Instagram: @mr.dough",
        "nota": "Nao cobram entrada e ha espaco para comemorar sem aluguel.",
    },
    {
        "nome": "Santa Cana Bar e Restaurante",
        "categoria": "Bar / Restaurante",
        "tipo": "local",
        "brinde": "Brindes para aniversariante curtir com os convidados + happy hour com chope e drinks em dobro.",
        "como": "Ir ao local informando que e aniversariante.",
        "condicao": "Happy hour seg a sab das 11h-14h e 18h-20h. Nao cobram 10%.",
        "janela_antes": 0,
        "janela_depois": 0,
        "quando": "Checar validade",
        "local": "Av. Belarmino Cotta Pacheco, 150, Uberlandia/MG",
        "link": "Instagram: @santacana.udi",
        "nota": "Espaco kids gratuito.",
    },
    {
        "nome": "Casarao Beer Pub",
        "categoria": "Bar / Pub",
        "tipo": "local",
        "brinde": "Brinde para aniversariante (confirme a regra atual).",
        "como": "Ir ao pub informando que e aniversariante.",
        "condicao": "Confirme condicoes atuais. Qua a sex 17h-00h; sab 11h-00h; dom 11h-23h.",
        "janela_antes": 0,
        "janela_depois": 0,
        "quando": "Checar validade",
        "local": "Av. Anselmo Alves dos Santos, 980 - Santa Monica, Uberlandia/MG",
        "link": "Instagram: @casaraobeerpub",
        "nota": "Tambem atende delivery.",
    },
]

REDES = [
    {
        "nome": "Cacau Show (Cacau Lovers)",
        "categoria": "Chocolateria / Sorveteria",
        "tipo": "rede",
        "brinde": "Chocolate gratis conforme o nivel: Crush (trufa 13,5g), Paquera (tablete 20g), Paixao (Bytes 100g), Amor (tablete 100g).",
        "como": "Cadastro gratis no app/site Cacau Lovers. No periodo do aniversario, resgate o voucher na aba Beneficios e va a loja com CPF p/ retirar.",
        "condicao": "Resgate disponivel 2 dias antes ate 4 dias depois do aniversario. Apos resgatar, valido por 7 dias para retirada.",
        "janela_antes": -2,
        "janela_depois": 4,
        "quando": "2 dias antes ate 4 dias depois",
        "local": "Lojas Cacau Show em Uberlandia (shopping e ruas)",
        "link": "App Cacau Show / cacaushow.com.br",
        "nota": "",
    },
    {
        "nome": "O Boticario (Clube Viva / Beautybox)",
        "categoria": "Beleza",
        "tipo": "rede",
        "brinde": "Presente de aniversario (produto em tamanho real conforme categoria do programa).",
        "como": "Resgate o voucher no app Clube Viva no mes do aniversario e apresente na loja.",
        "condicao": "Cadastro ativo com data de nascimento correta. Resgate durante o mes do aniversario.",
        "janela_antes": -15,
        "janela_depois": 15,
        "quando": "Durante o mes do aniversario",
        "local": "Lojas O Boticario em Uberlandia",
        "link": "App Clube Viva O Boticario",
        "nota": "Tambem funciona online em compras/e-commerce em alguns casos.",
    },
    {
        "nome": "Quem Disse, Berenice? (Beautybox)",
        "categoria": "Beleza",
        "tipo": "rede",
        "brinde": "Produto de maquiagem completo (batom, gloss, mascara ou skincare).",
        "como": "Cadastro no Beautybox pelo app; voucher aparece no mes do aniversario para resgate em loja.",
        "condicao": "Cadastro com pelo menos 30 dias de antecedencia.",
        "janela_antes": -15,
        "janela_depois": 15,
        "quando": "Durante o mes do aniversario",
        "local": "Lojas QDB em Uberlandia (confirme)",
        "link": "App O Boticario / Beautybox",
        "nota": "",
    },
    {
        "nome": "Sephora (Beauty Club)",
        "categoria": "Beleza",
        "tipo": "rede",
        "brinde": "Kit exclusivo com 3 a 5 produtos miniatura (melhor nas categorias Gold/Black).",
        "como": "Cadastro gratis no Beauty Club pelo app; resgate no mes do aniversario.",
        "condicao": "Resgate em loja (sem compra minima) ou online (com compra minima).",
        "janela_antes": -15,
        "janela_depois": 15,
        "quando": "Durante o mes do aniversario",
        "local": "Lojas Sephora (Center Shopping Uberlandia - confirme)",
        "link": "App Sephora",
        "nota": "",
    },
    {
        "nome": "MAC (MAC Lover)",
        "categoria": "Beleza",
        "tipo": "rede",
        "brinde": "Batom MAC em tamanho padrao (R$ 120 a R$ 170).",
        "como": "Cadastro gratis no MAC Lover; voucher por e-mail no mes do aniversario.",
        "condicao": "Necessario ter feito pelo menos 1 compra nos ultimos 12 meses. Resgate presencial.",
        "janela_antes": -15,
        "janela_depois": 15,
        "quando": "Durante o mes do aniversario",
        "local": "Lojas MAC em Uberlandia (confirme)",
        "link": "Site/app MAC Lover",
        "nota": "",
    },
    {
        "nome": "Starbucks (Starbucks Rewards)",
        "categoria": "Cafeteria",
        "tipo": "rede",
        "brinde": "Uma bebida gratuita em qualquer tamanho/sabor.",
        "como": "Programa Starbucks Rewards no app; reward aparece no dia do aniversario e fica disponivel por ate 30 dias.",
        "condicao": "Membro ha pelo menos 30 dias + 1 transacao desde o cadastro. Vale apenas o reward gerado no dia.",
        "janela_antes": 0,
        "janela_depois": 0,
        "quando": "No dia do aniversario",
        "local": "Unidades Starbucks em Uberlandia (confirme)",
        "link": "App Starbucks Brasil",
        "nota": "",
    },
    {
        "nome": "Subway (Subway Rewards)",
        "categoria": "Fast food",
        "tipo": "rede",
        "brinde": "Cookie gratis ou benficio em sub (em algumas unidades, sub 15cm gratis na compra de outro).",
        "como": "Programa Subway Rewards pelo app com data de nascimento cadastrada.",
        "condicao": "Cadastro com pelo menos 7 dias de antecedencia. Unidades participantes.",
        "janela_antes": -3,
        "janela_depois": 3,
        "quando": "Perto do aniversario",
        "local": "Lojas Subway em Uberlandia (confirme)",
        "link": "App Subway",
        "nota": "",
    },
    {
        "nome": "Burger King (Clube BK)",
        "categoria": "Fast food",
        "tipo": "rede",
        "brinde": "Cupom de produto gratis ou pontos em dobro no mes do aniversario.",
        "como": "App do Burger King com cadastro no Clube BK e data de nascimento correta.",
        "condicao": "Ofertas aparecem no app durante o mes do aniversario. Unidades participantes.",
        "janela_antes": -15,
        "janela_depois": 15,
        "quando": "Durante o mes do aniversario",
        "local": "Lojas BK em Uberlandia",
        "link": "App Burger King",
        "nota": "",
    },
    {
        "nome": "McDonald's (app Mequi)",
        "categoria": "Fast food",
        "tipo": "rede",
        "brinde": "Cupom de produto gratis no app (McFlurry, McNuggets ou McShake, conforme campanha).",
        "como": "App Mequi com cadastro, data de nascimento e notificacoes ativas.",
        "condicao": "Cupom aparece na semana do aniversario. Resgate em restaurante participante.",
        "janela_antes": -3,
        "janela_depois": 3,
        "quando": "Na semana do aniversario",
        "local": "Lojas McDonald's em Uberlandia",
        "link": "App Mequi",
        "nota": "",
    },
    {
        "nome": "Outback (Meu Outback)",
        "categoria": "Restaurante",
        "tipo": "rede",
        "brinde": "Sobremesa gratis (Ex.: Thunder ou Chocolate Thunder) ao jantar.",
        "como": "Cadastro no app/site Meu Outback; avisar o atendente e mostrar documento.",
        "condicao": "Consumo presencial (nao vale delivery). Recomenda-se reserva. Valido na semana do aniversario.",
        "janela_antes": -3,
        "janela_depois": 3,
        "quando": "Na semana do aniversario",
        "local": "Verificar unidade mais proxima (rede nacional)",
        "link": "App/site Meu Outback",
        "nota": "Uberlandia nao possui loja confirmada - verifique a unidade mais proxima.",
    },
    {
        "nome": "Renner (Meu Estilo)",
        "categoria": "Moda",
        "tipo": "rede",
        "brinde": "Desconto de ate 20% no mes do aniversario + pontos em dobro.",
        "como": "Programa Meu Estilo Renner pelo app com data de nascimento cadastrada.",
        "condicao": "Cadastro ativo. Pode ter restricoes em algumas categorias. Vale para loja e online.",
        "janela_antes": -15,
        "janela_depois": 15,
        "quando": "Durante o mes do aniversario",
        "local": "Loja Renner em Uberlandia + e-commerce",
        "link": "App Renner",
        "nota": "",
    },
    {
        "nome": "Riachuelo",
        "categoria": "Moda",
        "tipo": "rede",
        "brinde": "Desconto de 10% a 20% + pontos extras no mes do aniversario.",
        "como": "App da Riachuelo ou cadastro em loja; cupom enviado por e-mail/app.",
        "condicao": "Necessario cartao Riachuelo ou cadastro no programa. Vale para loja e online.",
        "janela_antes": -15,
        "janela_depois": 15,
        "quando": "Durante o mes do aniversario",
        "local": "Loja Riachuelo em Uberlandia + e-commerce",
        "link": "App Riachuelo",
        "nota": "",
    },
    {
        "nome": "Arezzo (Arezzo&Co)",
        "categoria": "Moda",
        "tipo": "rede",
        "brinde": "Desconto de ate 20% + possiveis brindes (necessaire, porta-cartoes).",
        "como": "Programa Arezzo&Co pelo app; beneficio automatico no mes do aniversario.",
        "condicao": "Cadastro ativo no programa.",
        "janela_antes": -15,
        "janela_depois": 15,
        "quando": "Durante o mes do aniversario",
        "local": "Lojas Arezzo em Uberlandia + e-commerce",
        "link": "App Arezzo",
        "nota": "",
    },
    {
        "nome": "Drogasil / Droga Raia",
        "categoria": "Farmacia",
        "tipo": "rede",
        "brinde": "Descontos de ate 30% em perfumaria, higiene e dermocosmeticos + pontos extras no mes do aniversario.",
        "como": "App Drogasil ou Droga Raia com CPF e data de nascimento cadastrados.",
        "condicao": "Produtos participantes. Oferecimentos personalizados no app.",
        "janela_antes": -15,
        "janela_depois": 15,
        "quando": "Durante o mes do aniversario",
        "local": "Drogarias em Uberlandia + app",
        "link": "App Drogasil / Droga Raia",
        "nota": "",
    },
    {
        "nome": "Cinemark Club",
        "categoria": "Cinema",
        "tipo": "rede",
        "brinde": "Combo de aniversario (pipoca + refrigerante) no mes do aniversario.",
        "como": "Sendo assinante ativo do Cinemark Club (90 dias de assinatura) e resgatando no app.",
        "condicao": "Resgate no mes do aniversario pelo app.",
        "janela_antes": -15,
        "janela_depois": 15,
        "quando": "Durante o mes do aniversario",
        "local": "Cinemark Center Shopping Uberlandia",
        "link": "App Cinemark",
        "nota": "",
    },
    {
        "nome": "Petz (Clubz Petz)",
        "categoria": "Pet",
        "tipo": "rede",
        "brinde": "Petisco ou brinquedo gratis no aniversario do seu pet.",
        "como": "Programa Clubz Petz pelo app, cadastrando data do tutor e do pet.",
        "condicao": "Brinde do pet resgatado em loja fisica.",
        "janela_antes": -15,
        "janela_depois": 15,
        "quando": "No mes de aniversario do pet",
        "local": "Lojas Petz em Uberlandia (confirme)",
        "link": "App Clubz Petz",
        "nota": "",
    },
]

ONLINE = [
    {
        "nome": "Aniversario Vai de Visa",
        "categoria": "Premiacao / Cartao",
        "tipo": "online",
        "brinde": "Participacao em sorteios de cartoes pre-pagos (R$ 500 a R$ 50.000) durante o mes do aniversario.",
        "como": "Cadastrar no hotsite Vai de Visa, aceitar os termos e fazer transacoes com cartao Visa (compra minima R$ 20).",
        "condicao": "Pessoa fisica 18+, CPF ativo, cartao Visa elegivel. Transacoes processadas pelo sistema da promocao.",
        "janela_antes": -15,
        "janela_depois": 15,
        "quando": "Durante o mes do aniversario",
        "local": "100% online (vaidevisa.com.br)",
        "link": "vaidevisa.com.br/aniversariovdv",
        "nota": "Promocao com autorizacao SPA/MF. Confira o regulamento completo no site.",
    },
    {
        "nome": "Nespresso & You",
        "categoria": "Cafe / Varejo",
        "tipo": "online",
        "brinde": "Capsulas gratis, acessorios ou descontos especiais para membros.",
        "como": "Cadastro gratuito no programa; brinde enviado por e-mail ou app.",
        "condicao": "Cadastro ativo no programa de fidelidade.",
        "janela_antes": -15,
        "janela_depois": 15,
        "quando": "Durante o mes do aniversario",
        "local": "Online (site/app) + boutiques da rede",
        "link": "Site/app Nespresso Brasil",
        "nota": "",
    },
    {
        "nome": "Cacau Show online",
        "categoria": "Chocolateria",
        "tipo": "online",
        "brinde": "Resgate do voucher de aniversario no site/app e retirada em loja; pontos de compras online contam para o nivel.",
        "como": "Acessar cacaushow.com.br ou o app com CPF e data de nascimento cadastrados.",
        "condicao": "Mesmas regras do Cacau Lovers (2 dias antes a 4 dias depois).",
        "janela_antes": -2,
        "janela_depois": 4,
        "quando": "Perto do aniversario",
        "local": "Online (site/app) ou retirada em loja",
        "link": "cacaushow.com.br",
        "nota": "",
    },
    {
        "nome": "O Boticario online",
        "categoria": "Beleza",
        "tipo": "online",
        "brinde": "Mimo/brinde de aniversario apos cadastro no Clube Viva; compras online contam pontos e frete gratis em condicoes especiais.",
        "como": "App O Boticario com data de nascimento correta; cupons de boas-vindas somam ao brinde.",
        "condicao": "Confira regras do programa no app.",
        "janela_antes": -15,
        "janela_depois": 15,
        "quando": "Durante o mes do aniversario",
        "local": "Online (app/site) com entrega ou retirada",
        "link": "App O Boticario",
        "nota": "",
    },
    {
        "nome": "Subway via app (pedido)",
        "categoria": "Fast food",
        "tipo": "online",
        "brinde": "Beneficio do Subway Rewards aplicado no pedido feito pelo app (retirada ou delivery).",
        "como": "Pedir pelo app com a conta Rewards cadastrada e o voucher ativo.",
        "condicao": "Confirme se a unidade escolhida aceita o resgate no canal digital.",
        "janela_antes": -3,
        "janela_depois": 3,
        "quando": "Perto do aniversario",
        "local": "Via app (online)",
        "link": "App Subway",
        "nota": "",
    },
    {
        "nome": "McDonald's / Burger King via app (pedido)",
        "categoria": "Fast food",
        "tipo": "online",
        "brinde": "Cupons de aniversario resgatados no app e usados em pedidos de retirada ou delivery.",
        "como": "App Mequi ou Clube BK com data de nascimento; adicionar cupom no pedido.",
        "condicao": "Restaurantes participantes e disponibilidade do cupom na unidade.",
        "janela_antes": -3,
        "janela_depois": 3,
        "quando": "Perto do aniversario",
        "local": "Via app (online)",
        "link": "App Mequi / App Burger King",
        "nota": "",
    },
    {
        "nome": "E-commerce de moda e farmacia",
        "categoria": "Moda / Farmacia",
        "tipo": "online",
        "brinde": "Descontos de aniversario de Renner, Riachuelo, Arezzo, Drogasil e Droga Raia utilizaveis no e-commerce e apps.",
        "como": "Logar no app/site com CPF e data de nascimento; o cupom de aniversario aparece na conta.",
        "condicao": "Restricoes de categoria podem se aplicar em produtos promocionais.",
        "janela_antes": -15,
        "janela_depois": 15,
        "quando": "Durante o mes do aniversario",
        "local": "100% online",
        "link": "Apps: Renner, Riachuelo, Arezzo, Drogasil, Raia",
        "nota": "",
    },
    {
        "nome": "Sephora online",
        "categoria": "Beleza",
        "tipo": "online",
        "brinde": "Brinde de aniversario do Beauty Club no pedido online (com compra minima).",
        "como": "Resgatar no app/site com conta Beauty Club ativa no mes do aniversario.",
        "condicao": "Compra minima para envio online.",
        "janela_antes": -15,
        "janela_depois": 15,
        "quando": "Durante o mes do aniversario",
        "local": "100% online",
        "link": "Site/app Sephora",
        "nota": "",
    },
]

TODOS = LOCAIS + REDES + ONLINE

CATEGORIAS = sorted({o["categoria"] for o in TODOS})


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
            return "Periodo de resgate ATIVO", s, e
    for s, e in janelas:
        if hoje < s:
            return "Ainda nao comecou", s, e
    return "Fora do periodo", None, None


def dias_ate(date1: date, date2: date):
    return (date2 - date1).days


def render(offer, aniversario: date, hoje: date, incluir_ativo):
    status, ini, fim = campos_atuais(offer, aniversario, hoje)
    is_ativo = status == "Periodo de resgate ATIVO"
    if incluir_ativo and not is_ativo:
        return
    if is_ativo:
        badge = ":green[**RESGATE ATIVO AGORA**]"
    elif status == "Ainda nao comecou":
        badge = f":orange[**{status}**]"
    else:
        badge = f":gray[**{status}**]"

    per = ""
    if ini and fim:
        per = f"Periodo: {ini.strftime('%d/%m/%Y')} a {fim.strftime('%d/%m/%Y')}"

    with st.expander(f"{offer['nome']}  -  {badge}", expanded=is_ativo):
        st.markdown(f"**O que ganha:** {offer['brinde']}")
        st.markdown(f"**Como resgatar:** {offer['como']}")
        st.markdown(f"**Condicoes:** {offer['condicao']}")
        st.markdown(f"**Quando vale:** {offer['quando']}")
        st.markdown(f"**Local:** {offer['local']}")
        st.markdown(f"**Canal:** {offer['link']}")
        if per:
            st.markdown(f"{per}")
        if offer.get("nota"):
            st.caption(offer["nota"])


def main():
    st.title("Niver Gratis - Uberlandia e Online")
    st.markdown(
        "Escolha sua data de nascimento e descubra os locais que presenteiam aniversariantes "
        "em **Uberlandia/MG**, em redes presentes na cidade e tambem em opcoes **100% online/remotas**."
    )

    with st.sidebar:
        st.header("Seu aniversario")
        nasc = st.date_input("Data de nascimento", value=date(1990, date.today().month, date.today().day))
        st.caption(CADASTRO_SUGESTAO)

        st.header("Filtros")
        tipo_map = {
            "Todos": "todos",
            "Presencial em Uberlandia": "local",
            "Redes em Uberlandia": "rede",
            "Online / Remoto": "online",
        }
        escolha = st.radio("Tipo", list(tipo_map.keys()))
        categoria = st.multiselect("Categoria", CATEGORIAS, default=[])
        so_ativos = st.checkbox("Mostrar apenas beneficios ativos agora", value=False)

    hoje = date.today()
    b0, b1, b2 = _ocorrencias(nasc, hoje)
    proximo = b1 if b1 >= hoje else b2
    dias = dias_ate(hoje, proximo)
    faz = proximo.year - nasc.year
    ultimo = min([b for b in (b0, b1, b2) if b <= hoje], key=lambda b: hoje - b)

    st.info(
        f"Hoje: {hoje.strftime('%d/%m/%Y')}  |  Proximo aniversario: {proximo.strftime('%d/%m/%Y')} "
        f"({dias} dia(s) - voce fara {faz} anos)  |  Ultimo aniversario: {ultimo.strftime('%d/%m/%Y')}"
    )

    grupos = {"local": LOCAIS, "rede": REDES, "online": ONLINE}
    lista = grupos[tipo_map[escolha]] if escolha != "Todos" else TODOS
    if categoria:
        lista = [o for o in lista if o["categoria"] in categoria]

    ativos = [o for o in lista if ativo(o, nasc, hoje)]

    c1, c2, c3 = st.columns(3)
    c1.metric("Beneficios ativos agora", len(ativos))
    c2.metric("Total de ofertas na selecao", len(lista))
    c3.metric("Ofertas Uberlandia (presencial)", len([o for o in lista if o["tipo"] in ("local", "rede")]))

    st.write("")

    tab1, tab2, tab3 = st.tabs(
        [
            "Presencial em Uberlandia",
            "Redes em Uberlandia",
            "Online / Remoto",
        ]
    )

    with tab1:
        sel = [o for o in LOCAIS if o in lista]
        if not sel:
            st.write("Nenhuma oferta neste filtro.")
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
    st.subheader("Plano de caca aos brindes")
    st.markdown(
        "1. **Cadastre-se com antecedencia** (1 a 2 meses) nos apps/programas abaixo com CPF e data de nascimento corretos.\n"
        "2. **Ative as notificacoes** para receber o voucher/cupom no momento certo.\n"
        "3. **Resgate no periodo indicado** de cada oferta - muitos sao validos so por alguns dias.\n"
        "4. **Confirme com o estabelecimento** antes de sair de casa, pois regras mudam com frequencia.\n"
        "5. Combine benefcios: voce pode resgatar diversos presentes no mesmo mês."
    )

    st.divider()
    st.caption(
        "Aviso: as promocoes sao informativas e podem mudar ou ser encerradas a qualquer momento pelas marcas. "
        "Confirme sempre as condicoes atualizadas no app/site oficial e com o estabelecimento. "
        "Informacoes compiladas com base em fontes publicas (2025-2026)."
    )


if __name__ == "__main__":
    main()