dic1 = [
        {
            "id_produto": "5567",
            "imagem_produto": "https://s3-hd-b2c-imagens-email.s3.amazonaws.com/50x50/5567/360/Lv1/11_01.jpg",
            "nome_produto": "Kit de Reparo de Cilindro Mestre de Freio",
            "codigo_original": "41700087",
            "quantidade_clientes": 1,
            "leads": [
                {
                    "nome": "Denis Pereira",
                    "possui_cadastro": 0,
                    "email": "denis@outroemail.com.br",
                    "telefone": "(99) 99999-9999",
                    "data_pedido": 1595882185
                }
            ]
        },
        {
            "id_produto": "5567",
            "imagem_produto": "https://s3-hd-b2c-imagens-email.s3.amazonaws.com/50x50/5567/360/Lv1/11_01.jpg",
            "nome_produto": "Kit de Reparo de Cilindro Mestre de Freio",
            "codigo_original": "41700087",
            "quantidade_clientes": 1,
            "leads": [
                {
                    "nome": "Visitante",
                    "possui_cadastro": 0,
                    "email": "denis@visitante.com.br",
                    "telefone": "77777777777",
                    "data_pedido": 1595882214
                }
            ]
        },
        {
            "id_produto": "2645",
            "imagem_produto": "https://s3-hd-b2c-imagens-email.s3.amazonaws.com/50x50/2645/360/Lv1/98557-14VW%20002S_01.jpg",
            "nome_produto": "Jaqueta",
            "codigo_original": "98557-14VW",
            "quantidade_clientes": 1,
            "leads": [
                {
                    "nome": "Jonathan",
                    "possui_cadastro": 0,
                    "email": "jonathan@e-peca.com.br",
                    "telefone": "41999999999",
                    "data_pedido": 1596720865
                }
            ]
        },
        {
            "id_produto": "3932",
            "imagem_produto": "https://s3-hd-b2c-imagens-email.s3.amazonaws.com/50x50/3932/360/Lv1/99408-16VM_01.jpg",
            "nome_produto": "Boné",
            "codigo_original": "99408-16VM",
            "quantidade_clientes": 1,
            "leads": [
                {
                    "nome": "Jonathan",
                    "possui_cadastro": 1,
                    "email": "jonathan@e-peca.com.br",
                    "telefone": "41999999999",
                    "data_pedido": 1596720865
                }
            ]
        },
        {
            "id_produto": "2645",
            "imagem_produto": "https://s3-hd-b2c-imagens-email.s3.amazonaws.com/50x50/2645/360/Lv1/98557-14VW%20002S_01.jpg",
            "nome_produto": "Jaqueta",
            "codigo_original": "98557-14VW",
            "quantidade_clientes": 1,
            "leads": [
                {
                    "nome": "Jonathan",
                    "possui_cadastro": 1,
                    "email": "jonathan@e-peca.com.br",
                    "telefone": "41999999999",
                    "data_pedido": 1596720865
                }
            ]
        },
        {
            "id_produto": "2614",
            "imagem_produto": "https://s3-hd-b2c-imagens-email.s3.amazonaws.com/50x50/2614/360/Lv1/96406-15VM%20002L_01.jpg",
            "nome_produto": "Suéter",
            "codigo_original": "96406-15VM",
            "quantidade_clientes": 1,
            "leads": [
                {
                    "nome": "Jonathan",
                    "possui_cadastro": 1,
                    "email": "jonathan@e-peca.com.br",
                    "telefone": "41999999999",
                    "data_pedido": 1596720865
                }
            ]
        },
        {
            "id_produto": "2614",
            "imagem_produto": "https://s3-hd-b2c-imagens-email.s3.amazonaws.com/50x50/2614/360/Lv1/96406-15VM%20002L_01.jpg",
            "nome_produto": "Suéter",
            "codigo_original": "96406-15VM",
            "quantidade_clientes": 1,
            "leads": [
                {
                    "nome": "Jonny",
                    "possui_cadastro": 0,
                    "email": "hahahah@haha.com",
                    "telefone": "123456789",
                    "data_pedido": 1596763194
                }
            ]
        },
        {
            "id_produto": "5638",
            "imagem_produto": "https://s3-hd-b2c-imagens-email.s3.amazonaws.com/50x50/5638/360/Lv1/2_01.jpg",
            "nome_produto": "Boné",
            "codigo_original": "99467-19VM",
            "quantidade_clientes": 1,
            "leads": [
                {
                    "nome": "jonny",
                    "possui_cadastro": 0,
                    "email": "hahaha@haha.com",
                    "telefone": "12545454545",
                    "data_pedido": 1596763286
                }
            ]
        }
    ]


from collections import Counter

def remove_duplicit(lista_produtos):
    lista_final = []
    produtos_duplicados = Counter(lista['id_produto'] for lista in lista_produtos)
    for key, value in produtos_duplicados.items():
        lista_temp = []
        for l in lista_produtos:
            if key in l["id_produto"]:
                lista_temp.append(l)
        if len(lista_temp) > 1:
            primeiro_valor = lista_temp[0]
            for i in lista_temp[1:]:
                primeiro_valor["leads"].extend(i["leads"])
            lista_final.append(primeiro_valor)
        else:
            lista_final.extend(lista_temp)
    for valor in lista_final:
        numero_leads = len(valor["leads"])
        valor["quantidade_clientes"] = numero_leads
    print(produtos_duplicados)
    print(lista_final)
    return lista_final


remove_duplicit(dic1)