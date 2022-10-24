from entidades.comprador import Comprador
from telas.tela_comprador import TelaComprador


class ControladorComprador:
    def __init__(self):
        self.__tela_comprador = TelaComprador()
        self.__compradores = []
        self.__tela_aberta = False

    def inclui_comprador(self, nome, cpf, nascimento, email, celular, senha):
        comprador = Comprador(nome, cpf, nascimento, email, celular, senha)
        try:
            for i in self.__compradores:
                if comprador.cpf == i.cpf:
                    raise SystemError
            else:
                self.__compradores.append(comprador)
                #fazer metodo acao realizada com sucesso
        except SystemError:
            self.__tela_comprador.usuario_ja_existe()

    def retorna_comprador_e_senha_pelo_cpf(self, cpf):
        for comprador in self.__compradores:
            if comprador.cpf == cpf:
                return [comprador, comprador.senha]

    def escolher_acao(self):
        self.__tela_aberta = True
        opcoes = {1:self.ver_meus_ingressos, 2: self.ver_eventos_disponiveis, 3: self.favoritar_evento,
                  4: self.transferir_ingresso, 5: self.alterar_dados_comprador, 6: self.excluir_conta,
                  7: self.sair_da_conta}
        while self.__tela_aberta:
            opcao = self.__tela_comprador.mostrar_opcoes_comprador()
            opcoes[opcao]()

    def alterar_dados_comprador(self, dado_a_ser_alterado):
        pass

    def excluir_comprador(self):
        pass

    def listar_compradores(self):
        pass

    def ver_meus_ingressos(self):
        pass

    def ver_eventos_disponiveis(self):
        pass

    def favoritar_evento(self):
        pass

    def transferir_ingresso(self, cpf_para_transferir):
        pass

    def sair_da_conta(self):
        self.__tela_aberta = False

    def excluir_conta(self):
        pass