from async_stripe import stripe

stripe.api_key='pk_live_eBee6q6n88Q6DCAatTPCOycn00XBRXLwKV'

async def checker(cc):
    try:
        result = await stripe.PaymentMethod.create(
    type="card",
    card={
    "number": cc[0],
    "exp_month": cc[1],
    "exp_year": cc[2],
    "cvc": cc[3],
    },
    )
        text='<b>✅ Карта прошла проверку! СЛИТО В ТЕЛЕГРАМ КАНАЛЕ – @SMOKE_SOFTWARE\n\n🆗 Тип: <code>'+result['card']['brand']+'</code>\n🏳️ Страна: <code>'+result['card']['country']+'</code>\n🔑 Номер карты: <code>'+str(cc[0])+'</code>\n🎫 Срок действия: <code>до '+str(result['card']['exp_month'])+'/'+str(result['card']['exp_year'])+'</code>\n❗️ 3DS: <b>'+str(result['card']['three_d_secure_usage']['supported'])+'</b></b>'               
        return text
    except Exception as f:
        return '<b>❌ Карта '+str(cc[0])+' не прошла проверку</b>'

async def checker_two(cc):
    try:
        result = await stripe.PaymentMethod.create(
    type="card",
    card={
    "number": cc[0],
    "exp_month": cc[1],
    "exp_year": cc[2],
    "cvc": cc[3],
    },
    )
        text='<b>✅ Карта снова проверку\n\n🆗 Тип: <code>'+result['card']['brand']+'</code>\n🏳️ Страна: <code>'+result['card']['country']+'</code>\n🔑 Номер карты: <code>'+str(cc[0])+'</code>\n🎫 Срок действия: <code>до '+str(result['card']['exp_month'])+'/'+str(result['card']['exp_year'])+'</code>\n❗️ 3DS: <b>'+str(result['card']['three_d_secure_usage']['supported'])+'</b></b>'               
        return text
    except Exception as f:
        return '<b>❌ Карта '+str(cc[0])+' снова не прошла проверку BY @SMOKE_SOFTWARE</b>'