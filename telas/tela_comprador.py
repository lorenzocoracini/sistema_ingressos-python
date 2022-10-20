class TelaComprador:
    def mostra_tela_comprador(self):
        print('*'*20)
        print("POSSUI CADASTRO ? ")
        print('1 - LOGIN')
        print('2 - CADASTRE - SE ')
        opcao = int(input('ESCOLHA A OPÇÃO: '))

        return opcao

    def mostra_tela_cadastro_comprador(self):
        print("Digite seus dados:")
        self.__nome = input("Nome: ")
        self.__cpf = int(input("CPF (Coloque apenas números): "))
        self.__nascimento = input("Nascimento: ")
        self.__email = input("Email: ")
        self.__celular = int(input("Celular (Coloque apenas números): "))

        return {"nome_comprador": self.__nome, "cpf_comprador": self.__cpf, "nascimento_comprador": self.__nascimento,
                "email_comprador": self.__email, "celular_comprador": self.__celular}

    def mostra_tela_login_comprador(self):
        print('login produtor')
        self.__cpf_login = input("Digite seu CPF: ")
        self.__senha_login = input("Digite sua senha: ")
        dados_login = {"cpf_login_comprador": self.__cpf_login, "senha_login_comprador": self.__senha_login}
        return dados_login

    def mostrar_opcoes_comprador(self):
        print("Login efetuado com sucesso!")

    def listar_dados_comprador(self):
        pass